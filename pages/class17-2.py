import streamlit as st
import os

image_folder = "image"
image_files = os.listdir(image_folder)
st.write(image_files)
image_width = st.number_input("請輸入圖片寬度", value=300, step=10)
fruit = st.selectbox("請選擇水果", ["蘋果", "香蕉", "橘子"])
st.write(f"你選擇的水果是:{fruit}")
if fruit == "蘋果":
    st.image("image/1.png", width=image_width)
elif fruit == "香蕉":
    st.image("image/0.png", width=image_width)
else:
    st.image("image/2.png", width=image_width)
