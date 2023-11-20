import streamlit as st
import langchain_helper as lch
import textwrap
import sys


st.set_page_config(page_icon="🌈",page_title="Youtube Assistant",layout="centered")

st.header("Youtube Assistant 🔥")

with st.form(key='my_form'):
    video_url = st.text_input(label='Enter a Youtube video URL', max_chars=50)
    query = st.text_input(label='Ask a question about the video', max_chars=50)
    submitted = st.form_submit_button(label='Submit')

if query and video_url:
    db = lch.create_db_from_youtube_video_url(video_url, api_key=st.secrets["OPENAI_API_KEY"])
    response, docs = lch.get_response_from_query(db=db, query=query)
    st.header("Answer:")
    st.text(textwrap.fill(response, width=45))




