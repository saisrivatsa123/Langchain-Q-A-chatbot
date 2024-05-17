from langchain_community.llms import Ollama
from langchain_openai import OpenAI, ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')


def get_openai_response(question):
    llm = Ollama(model= 'llama3-chatqa')
    return llm(question)

#initialize streamlit app
st.set_page_config(page_title="Q&A Demo")
st.title("Langchain application")

input = st.text_input("Input:",key='input')
response=get_openai_response(input)

submit=st.button("Ask question")

if submit:
    st.subheader("The response is:")
    st.write(response)