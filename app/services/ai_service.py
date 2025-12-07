import streamlit as st
from google import genai
from google.genai import types

GEMINI_KEY = "AIzaSyBS2TKSf0jCCEYiSxtBMjoRNF2u9cCOzco"

#initialize the Gemini Client
try:
    client = genai.Client(api_key=GEMINI_KEY)

except Exception as e:
    #Handles potential errors during client initialization
    st.error(f"Failed to initialize Gemini Client; {e}")
    st.stop()


def generate_ai_response(user_prompt: str, user_role: str):
    """
    Sends a user's text prompt to the Gemini model for a response,
    using systems instructions to maintain expertise in three domains.
    """

    #System instruction
    system_instruction = (
        f"You are a specialized AI Assistant for a Multi-Domain Intelligence Platform. "
        f"Your expertise covers three core areas: **Cybersecurity Incident Analysis**, "
        f"**Data Science/Dataset Metadata**, and **IT Service Management (ITSM)/IT Ticket Operations**. "
        f"The current user is logged in as a **{user_role}**. "
        f"Respond professionally and concisely. If the user asks about an area outside "
        f"of these three domains (e.g., cooking or poetry), you must politely decline and redirect them "
        f"to focus on platform-relevant intelligence queries. Provide expert-level insight "
        f"relevant to their specific domain query."
    )
    #Configure the Model and Call the API
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.7 #Allows for more flexible, helpful answers
    )

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_prompt,
            config=config
        )
        return response.text
    except Exception as e:
        return f"AI Analysis failed due to an API error. Please check your API key and network connection: {e}"