import streamlit as st
from utils import init_page

init_page()
st.title("聊天室示範")
demo_messages = [
    {"role": "user", "content": "你好，請問怎麼學Python?"},
    {
        "role": "assistant",
        "content": "學習Python的基本步驟:\n1. 了解基礎語法\n2. 練習寫簡單程式\n3. 解決實際問題",
    },
    {"role": "user", "content": "看起來不難耶"},
    {
        "role": "assistant",
        "content": "沒錯!循序漸進的學習最重要。要不要試試看寫個簡單的程式?",
    },
]
for message in demo_messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
if message := st.chat_input("請輸入訊息"):
    with st.chat_message("user"):
        st.write(message)
    with st.chat_message("assistant"):
        st.write(f"這是示範回復:我收到你的訊息「{message}」")
