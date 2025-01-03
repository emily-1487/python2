import streamlit as st


def menu():
    st.sidebar.title("選單")
    st.sidebar.markdown("---")
    st.sidebar.title("課程")
    st.sidebar.page_link(page="python2/pages/class16.py", label="課程16", icon="📚")
    st.sidebar.page_link(page="python2/pages/class17.py", label="課程17", icon="📚")
    st.sidebar.page_link(page="python2/pages/class17-2.py", label="課程17-2", icon="📚")
    st.sidebar.markdown("---")
