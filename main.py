import openai
import os
from dotenv import load_dotenv
import streamlit as st;
load_dotenv()
st.header("GPT-3 Chatbot")
st.write("This is a simple chatbot that uses GPT-3 to answer questions. It is trained on a dataset of questions and answers from the internet. It is not perfect, but it is a good demonstration of the capabilities of GPT-3.")
with st.form("my_form"):
    title = st.text_input("Enter your question here:")
    submitted = st.form_submit_button("Submit")
    if submitted:
        openai.api_key = os.getenv("OPENAI_KEY")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": title}
            ]
        )
        st.write("The answer to your question is:")
        st.write(response["choices"][0]["message"]["content"])