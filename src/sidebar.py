import streamlit as st
from chatbot import establish_api

def render_sidebar():
    """Render the sidebar with API key handling"""
    with st.sidebar:
        if "api_key" not in st.session_state:
            st.title("Insert API Key!")
            api_key = st.text_input('');
            if api_key:
                st.session_state["api_key"] = api_key
                st.write(establish_api(api_key))
            st.write("**To get started, you'll need a Gemini API key:**")

            instructions = """
            1. **Go to Google AI Studio:** Login and access the platform.
            2. **Click "Get API Key":** Locate the option to obtain an API key.
            3. **Choose Project:** Select a new or existing project for the API key.
            4. **Copy the Key:** Once generated, copy the API key here and have fun!
            """

            st.markdown(instructions)
        else:
            st.write("API Key already entered. Enjoy :D") 