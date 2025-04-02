import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Page setup
st.set_page_config(page_title="HR Chatbot")
st.title("🤖 HR Chatbot Assistant")

# Get user input
user_input = st.text_input("Ask your question:")

# When the user submits a question
if user_input:
    system_prompt = """
    You are an internal HR assistant chatbot for a company.
    You answer frequently asked questions (FAQs) from employees, such as leave policies, reimbursement procedures, and more.
    If a question is unrelated to HR topics, politely respond with: "Please consult a member of the HR department regarding that."
    Keep responses concise, professional, and accurate.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    answer = response.choices[0].message.content
    st.markdown(f"💬 **HR Chatbot:** {answer}")
