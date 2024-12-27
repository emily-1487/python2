import streamlit as st
import os

image_folder = "image"
image_files = os.listdir(image_folder)
st.write(image_files)
st.title("圖片元件")
st.image("image/0.png", width=300)
fruit = st.selectbox("請選擇水果", ["蘋果", "香蕉", "橘子"])
st.write(f"你選擇的水果是:{fruit}")
if fruit == "蘋果":
    st.image("image/1.png", width=300)
elif fruit == "香蕉":
    st.image("image/0.png", width=300)
else:
    st.image("image/2.png", width=300)


if st.button("按下去ans加1", key="ans2"):
    st.session_state.ans = st.session_state.ans + 1
col_num = st.number_input("圖片大小")
cols = st.columns(4)
for i in range(len(cols)):
    with cols[i]:
        st.button(f"按鈕{i+1}", key=f"btn{i+10}")
