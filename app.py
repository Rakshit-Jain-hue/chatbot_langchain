from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
os.environ['OPENAI_API_KEY'] = 'sk-proj-40Ge4y6UxEaiUYBqvvLZT3BlbkFJMK001xpnrUQOwUwgSZ1Q'
os.environ['LANGCHAIN_API_KEY'] = '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'
os.environ['LANGCHAIN_TRACING_V2'] = 'true'

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question:{question}")
    ]
)

llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser
import streamlit as st

st.title("LangChain with OpenAI")
input_text = st.text_input("Search the topic you want")

if input_text:
  response = chain.invoke({'question': input_text})
  st.write(response)