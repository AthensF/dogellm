import streamlit as st
import os
from openai import OpenAI

# Initialize the client with environment variable
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])  # For Streamlit Cloud
MODEL = st.secrets["MODEL"]

st.title("Respond to Doge leadership team")
user_input = st.text_input("You: E.g. I ate sausage for breakfast this morning", "")
system_input = "You are a snarky federal employee responding to Elon Musks email that had asked you to report on how much work you have done."


if user_input:
    response = client.chat.completions.create(
        model= MODEL,
        messages=[
            {"role": "system", "content": system_input},
            {"role": "user", "content": user_input}]
    )
    st.write("", response.choices[0].message.content)