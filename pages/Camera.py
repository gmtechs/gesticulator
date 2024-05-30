import logging
import queue
from collections import deque
import json
import tempfile

import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer, RTCConfiguration

from utils import SLInference


logger = logging.getLogger(__name__)

RTC_CONFIGURATION = RTCConfiguration({
    "iceServers": [
        {"urls": ["stun:stun.l.google.com:19302"]},
        {"urls": ["turn:TURN_SERVER_URL"], "username": "USERNAME", "credential": "CREDENTIAL"}
    ]
})

def main():
    """
    Main function of the app.
    """
    config = {
        "path_to_model": "S3D.onnx",
        "threshold": 0.3,
        "topk": 5,
        "path_to_class_list": "RSL_class_list.txt",
        "window_size": 32,
        "provider": "OpenVINOExecutionProvider"
    }

    # Сохранение конфигурации во временный файл
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json') as config_file:
        json.dump(config, config_file)
        config_file_path = config_file.name

    inference_thread = SLInference(config_file_path)
    inference_thread.start()

    webrtc_ctx = webrtc_streamer(
        key="video-sendonly",
        mode=WebRtcMode.SENDONLY,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={"video": True, "audio": False},
    )

    gestures_deque = deque(maxlen=5)

    # Set up Streamlit interface
    st.title("Sign Language Recognition Demo")
    image_place = st.empty()
    text_output = st.empty()
    last_5_gestures = st.empty()
    st.markdown(
        """
        This application is designed to recognize sign language using a webcam feed.
        The model has been trained to recognize various sign language gestures and display the corresponding text in real-time.

        
        The project is open for collaboration. If you have any suggestions or want to contribute, please feel free to reach out.
        """
    )

    while True:
        if webrtc_ctx.video_receiver:
            try:
                video_frame = webrtc_ctx.video_receiver.get_frame(timeout=1)
            except queue.Empty:
                logger.warning("Queue is empty")
                continue

            img_rgb = video_frame.to_ndarray(format="rgb24")
            image_place.image(img_rgb)
            inference_thread.input_queue.append(video_frame.reformat(224, 224).to_ndarray(format="rgb24"))

            gesture = inference_thread.pred
            if gesture not in ['no', '']:
                if not gestures_deque:
                    gestures_deque.append(gesture)
                elif gesture != gestures_deque[-1]:
                    gestures_deque.append(gesture)

            text_output.markdown(f'<p style="font-size:20px"> Current gesture: {gesture}</p>',
                                 unsafe_allow_html=True)
            last_5_gestures.markdown(f'<p style="font-size:20px"> Last 5 gestures: {" ".join(gestures_deque)}</p>',
                                 unsafe_allow_html=True)
            print(gestures_deque)

if __name__ == "__main__":
    main()

