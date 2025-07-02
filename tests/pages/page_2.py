import streamlit as st
import persistlit as pt

st.title("Page 2")

st.write(st.session_state['my_text_input'])
st.write(st.session_state['y'])