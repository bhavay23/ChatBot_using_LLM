from langchain.llms import OpenAI
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

## loading OpenAI model and Response

def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.environ["OPEN_API_KEY"],model_name='text-davinci-003',temperature=0.6)
    response = llm(question)
    return response

##initialising streamlit application

st.set_page_config(page_title = "Q&A Demo")

st.header("Ask me anything")

##getting the input from user
input = st.text_input("Input :",key="input")
response = get_openai_response(input)

submit = st.button("Ask the question")
get_openai_response(input)

##If ask button is clicked

if submit:
    st.subheader("The Answer is :")
    st.write(response)

