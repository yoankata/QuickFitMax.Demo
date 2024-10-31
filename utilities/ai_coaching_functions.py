import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import streamlit as st

# Utility function to set up Gemini AI API
def setup_gemini_api():
    # Gemini AI API setup
    api_key = st.secrets.general.GEMINI_API_KEY
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    
    safety_settings = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    }
    
    return chat, safety_settings

# Initialize chat and safety settings
chat, safety_settings = setup_gemini_api()

# Ensure setup is called before making AI-related calls
def ensure_setup():
    global chat, safety_settings
    if chat is None or safety_settings is None:
        chat, safety_settings = setup_gemini_api()

def get_ai_coaching(stage, heart_rate, max_hr):
    ensure_setup()

    prompt = f"You are an AI fitness coach for a REHIT workout. The user is currently in the {stage} stage with a heart rate of {heart_rate} bpm (max HR: {max_hr}). Provide a short, motivational coaching message (max 15 words) appropriate for this stage and heart rate."
    
    response = chat.send_message(prompt, safety_settings=safety_settings)
    return response.text

