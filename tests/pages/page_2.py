import streamlit as st
import persistlit as pt

st.title("Page 2")

st.write(st.session_state['my_text_input'])
st.write(st.session_state['y'])

st.write(st.session_state['my_radio'])

st.write(st.session_state['my_pills'])
st.write(st.session_state['my_pills_multi'])