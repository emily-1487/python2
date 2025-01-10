import streamlit as st
from utils import init_page

init_page()
st.title("聊天室示範")
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
if message := st.chat_input("請輸入訊息"):
    with st.chat_message("user"):
        st.write(message)
    st.session_state.messages.append({"role": "user", "content": message})
    assistant_response = f"你剛才說了:{message}"
    with st.chat_message("assistant"):
        st.write(assistant_response)
    st.session_state.messages.append({"role": "user", "content": assistant_response})
