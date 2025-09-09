import os
import streamlit as st
from google.api_core.exceptions import ResourceExhausted
from dotenv import load_dotenv
from langchain_core.prompts.chat import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Load .env variables
load_dotenv()

# Initialize the Google Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_token=None,
    timeout=None,
    max_retries=2,
)

# Define the chat prompt
promt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("You are a chatbot"),
    HumanMessagePromptTemplate.from_template("Question: {question}")
])

output_parser = StrOutputParser()

# Streamlit app UI
st.title('Clario - your friendly chatbot')

input_text = st.text_input("What can I do for you today?")

if input_text:
    try:
        # Format the prompt
        formatted_prompt = promt.format_prompt(question=input_text)
        
        # Generate response
        response = llm(formatted_prompt.to_messages())
        
        st.write("🤖 Clario:", response)
    except ResourceExhausted:
        st.error("⚠️ API quota exceeded. Please check your billing or wait until quota resets.")
