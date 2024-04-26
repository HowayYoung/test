import streamlit as st
import requests
import json

# API配置
API_KEY = 'AIzaSyAvl_NYfpWfKyE286UaTmULCxH_xotXpYE'
API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent'

# Streamlit页面设置
st.title('小杨的第一个LLM部署')

# 用户输入
user_input = st.text_area("Enter text to generate content:", "Write a story about a magic backpack")

# 发送请求到Google API
def query_gemma(text):
    headers = {'Content-Type': 'application/json'}
    payload = {
        'contents': [{
            'parts': [{
                'text': text
            }]
        }]
    }
    response = requests.post(f"{API_URL}?key={API_KEY}", headers=headers, json=payload)
    return response.json()

# 当用户点击按钮时
if st.button('Generate'):
    if user_input:
        result = query_gemma(user_input)
        # 仅提取文本内容部分
        if 'candidates' in result and result['candidates']:
            text_output = result['candidates'][0]['content']['parts'][0]['text']
            st.write(text_output)
        else:
            st.write("No response or invalid format received.")
    else:
        st.write("Please enter some text to generate content.")
