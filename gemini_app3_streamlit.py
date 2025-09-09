import os
import time
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

# Load environment variables from .env
load_dotenv()

# Initialize the Google Gemini model with limits
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_output_tokens=300,   # Limit response length
    timeout=10,              # Prevent hanging
    max_retries=2,
)

# Define the chat prompt
promt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("You are a helpful chatbot."),
    HumanMessagePromptTemplate.from_template("Question: {question}")
])

output_parser = StrOutputParser()

# Streamlit UI
st.title('Clario - Your Friendly Chatbot')

input_text = st.text_input("What can I do for you today?")

if input_text:
    try:
        # Prepare prompt
        formatted_prompt = promt.format_prompt(question=input_text)

        # Start timer
        start_time = time.time()

        # Generate response
        response = llm(formatted_prompt.to_messages())

        # Calculate elapsed time
        elapsed = time.time() - start_time

        st.write("🤖 Clario:", response)
        st.info(f"⏱️ Response generated in {elapsed:.2f} seconds.")

    except ResourceExhausted:
        st.error("⚠️ API quota exceeded. Please check your billing or wait until quota resets.")
    except Exception as e:
        st.error(f"⚠️ An unexpected error occurred: {e}")

