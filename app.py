import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st
load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def build_prompt(user_input):
    predefined_prompt = """
    You are a highly knowledgeable assistant specializing in data science and coding. 
    Your task is to assist with the following query related to data science concepts, interview questions, or coding doubts:
    
    "Query: {user_input}"
    
    1. Provide a detailed and accurate explanation or solution to the query.
    2. If it's a coding-related question, include well-commented code examples to clarify your response.
    3. Keep the response concise and focused on the query, avoiding unrelated topics.
    """
    return predefined_prompt.format(user_input=user_input)

def response(prompt):
    model=genai.GenerativeModel("gemini-1.5-pro")
    response=model.generate_content(prompt)
    return response

st.title("Im Your Data Science Assistant")
st.write("This is a chatbot that uses the Gemini AI model to generate responses to user input")
user_input=st.text_input("Enter Your Query")
if st.button("Ask") and user_input:
    query=build_prompt(user_input)
    model_response=response(query)
    st.markdown(model_response.text)

 