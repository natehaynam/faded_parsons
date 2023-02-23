# run command: streamlit run imageCaption.py
from openai_backend import ml_backend
import streamlit as st

st.title("Faded Parsons")
st.markdown("# Generate Image Caption")

with st.form(key="form", clear_on_submit=False):
    if type != '':
        text = st.text_input("What problem would you like faded?", placeholder="")

        submit_button = st.form_submit_button(label='Generate')

        if submit_button:
            with st.spinner("Generating ..."):
                caption = ml_backend().generate_caption(text)

            st.markdown("# Faded Parson's Problem ")
            st.text(caption)