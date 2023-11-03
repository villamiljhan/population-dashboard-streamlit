import streamlit as st

st.set_page_config(
    page_title="Snowboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")
  
col = st.columns(5)

with col[0]:
    st.write(1)
with col[1]:
    st.write(2)
with col[2]:
    st.write(3)
with col[3]:
    st.write(4)
with col[4]:
    st.write(5)
