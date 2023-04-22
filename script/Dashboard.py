import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

with open('./README.md') as f:
    lines = f.readlines()[0:42]
 
readme = '\n'.join(lines)

st.sidebar.success("Select one of the pages above to see our findings.")

st.markdown(readme)
