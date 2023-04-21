import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

with open('./README.md') as f:
    lines = f.readlines()
 
readme = '\n'.join(lines)

st.sidebar.success("Select a demo above.")

st.markdown(readme)