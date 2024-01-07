import streamlit as st

import model

# Создаем текстовое поле для ввода
input_text = st.text_input('Введите текст')

# Создаем поле для вывода
output_text = st.empty()


def process_text(input_text):
    return str(model.analyse(input_text)[0])

# Обрабатываем введенный текст и выводим результат
if st.button('Показать результат'):
    result = process_text(input_text)
    output_text.text(result)
