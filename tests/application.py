import streamlit as st
import persistlit as pt

st.title("Application Entry Point")

x = pt.text_input("my_text_input", persistent=True)
y = pt.text_input("my_text_input_2", persistent=True, key="y")

r = pt.radio("my_radio", options=["Option 1", "Option 2"], persistent=True)

p = pt.pills("my_pills", options=["Pill 1", "Pill 2", "Pill 3"], persistent=True)
mp = pt.pills("my_pills_multi", options=["Pill 1", "Pill 2", "Pill 3"], persistent=True, selection_mode="multi")