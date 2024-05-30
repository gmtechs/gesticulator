import streamlit as st

# Установка конфигурации страницы
st.set_page_config(
    page_title="GestureGuru",
    page_icon=":sparkles:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Добавление стилей
st.markdown("""
    <style>
    /* Основной фон */
    .main {
        background: linear-gradient(135deg, #e0f7fa, #ffccbc);
    }
    
    /* Стиль боковой панели */
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #ffccbc, #ffc107);
        padding: 1rem;
        border-radius: 10px;
        color: #4CAF50;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    
    /* Обертка для блока контента */
    .reportview-container .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    
    /* Стиль заголовка */
    .css-1h3lh1b {
        font-size: 2.5rem;
        color: #ff7043;
    }
    
    /* Стиль подзаголовка */
    .css-1siy2j7 {
        font-size: 1.5rem;
        color: #8d6e63;
    }
    
    /* Стиль кнопок */
    .stButton>button {
        background-color: #ff7043;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        margin: 10px;
    }
    
    .stButton>button:hover {
        background-color: #f4511e;
    }
    
    /* Карточки */
    .card {
        background-color: #ffffff;
        padding: 20px;
        margin: 10px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    
    /* Разделитель */
    .divider {
        height: 2px;
        background-color: #ff7043;
        margin: 20px 0;
    }
    
    /* Анимация */
    .fade-in {
        animation: fadeIn 2s;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

# Установка параметров URL
# Установка параметров запроса
st.experimental_set_query_params(page="main")
  # Используйте переменную page после определения

# Основной контент страницы
st.title("GestureGuru")
st.subheader("Russian Sign Language Recognition")
st.markdown("""
    <div class="card fade-in">
        <p>This application is designed to recognize sign language using a webcam feed. The model has been trained to recognize various sign language gestures and display the corresponding text in real-time.</p>
    </div>
    <div class="divider"></div>
    <div class="card fade-in">
        <h3>Features:</h3>
        <ul>
            <li>Real-time sign language recognition</li>
            <li>Supports multiple gestures</li>
            <li>Easy to use interface</li>
        </ul>
    </div>
    <div class="divider"></div>
    <div class="card fade-in">
        <h3>How it works:</h3>
        <ol>
            <li>Upload a video or use the camera for live recognition.</li>
            <li>The model processes the video and identifies the gestures.</li>
            <li>The recognized gestures are displayed as text.</li>
        </ol>
    </div>
    <div class="divider"></div>
    <div class="card fade-in">
        <h3>Why use this app:</h3>
        <ul>
            <li>Helps bridge the communication gap between sign language users and others.</li>
            <li>Useful for educational purposes and learning sign language.</li>
            <li>Enhances accessibility for people with hearing impairments.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)
st.image("image.webp", caption="Sign Language Recognition", use_column_width=True)





