import streamlit as st
from google import genai
from google.genai import types

#Secure key initialization
try:
    GEMINI_KEY = st.secrets['GEMINI_API_KEY']
    client = genai.Client(api_key=GEMINI_KEY)
         
except Exception as e:
    st.error(f"failed to initialize Gemini Client: {e}")
    st.stop()

#Base system instruction
SYSTEM_INSTRUCTION_PROMPT = (
    "You are a specialized AI Assistant for a Multi-Domain Intelligence Platform. "
    "Your expertise covers three core areas: **Cybersecurity Incident Analysis**, "
    "**Data Science/Dataset Metadata**, and **IT Service Management (ITSM)/IT Ticket Operations**. "
    "Respond professionally and concisely. If the user asks about an area outside "
    "of these three domains (e.g., cooking or poetry), you must politely decline and redirect them "
    "to focus on platform-relevant intelligence queries. Provide expert-level insight."
)


def generate_ai_response(user_prompt: str, user_role: str):
    """
    Sends a user's text prompt to the Gemini model for a response.
    """
    
    #construct the final system instruction with the user's role
    final_system_instruction = f"{SYSTEM_INSTRUCTION_PROMPT} The current user is logged in as a **{user_role}**."
    
    #Configure the Model and Call the API
    config = types.GenerateContentConfig(
        system_instruction=final_system_instruction,
        temperature=0.7, 
    )
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_prompt,
            config=config
        )
        return response.text
    except Exception as e:
        return f"AI Analysis failed to an API error: {e}"