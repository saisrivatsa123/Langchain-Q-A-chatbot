from langchain_community.llms import Ollama
from langchain_openai import OpenAI, ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


def get_openai_response(auth_token, question):
    # llm = Ollama(model= 'llama3-chatqa')
    print("auth", auth_token)
    llm = ChatOpenAI(openai_api_key = auth_token, model='gpt-3.5-turbo-instruct')
    return llm.predict(question)

#initialize streamlit app
st.set_page_config(page_title="Q&A Demo")
st.title("Langchain application1")

key = st.text_input("Auth-token", key='password', type='password')
input1 = st.text_input("Input:",key='input')


submit=st.button("Ask question")

if submit and input1 and key:
    st.subheader("The response is:")
    st.write(get_openai_response(key, input))