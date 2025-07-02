import streamlit as st
import persistlit as pt

st.title("Application Entry Point")

x = pt.text_input("my_text_input", persistent=True)
y = pt.text_input("my_text_input_2", persistent=True, key="y")