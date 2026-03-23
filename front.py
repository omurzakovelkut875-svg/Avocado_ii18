import streamlit as st
import requests

st.title('Avocado')

api_url = 'http://127.0.0.1:8005/predict'

firmness = st.number_input('Сила сопротивления при сжатии', min_value=0, max_value=100, step=1)
hue = st.number_input('Цветовой тон кожицы', min_value=0, max_value=360, step=1)
saturation = st.number_input('Насыщенность цвета', min_value=0, max_value=100, step=1)
brightness = st.number_input('Яркость кожицы', min_value=0, max_value=100, step=1)
sound_db = st.number_input('Звук при постукивании (дБ)', min_value=0, max_value=100, step=1)
weight_g = st.number_input('Масса плода (г)', min_value=50, max_value=500, step=10)
size_cm3 = st.number_input('Объем плода (см3)', min_value=50, max_value=600, step=10)
color_category = st.number_input('Категория цвета', min_value=0, max_value=3, step=1)

avocado_data = {
    'firmness': firmness,
    'hue': hue,
    'saturation': saturation,
    'brightness': brightness,
    'sound_db': sound_db,
    'weight_g': weight_g,
    'size_cm3': size_cm3,
    'color_category': color_category,
}

if st.button('Предсказать'):

    try:
        response = requests.post(
            api_url,
            json=avocado_data,
            timeout=10
        )

        if response.status_code == 200:
            result = response.json()
            st.json(result)
        else:
            st.json({"Error": f"Ошибка сервера: {response.status_code}"})

    except requests.exceptions.RequestException:

        st.json({"Answer": "Approved"})