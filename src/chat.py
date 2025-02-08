import streamlit as st
from chatbot import send_prompt

def render_chat():
    """Render the chat interface"""
    prompt = st.chat_input("Enter a prompt here")
    
    messages = st.container()
    if prompt:
        st.session_state['message_history'].append({"user": prompt})
        response = send_prompt(prompt)
        st.session_state['message_history'].append({"assistant": response})

    for message in st.session_state['message_history']:
        key, value = next(iter(message.items())) 
        messages.chat_message(key).write(value) 