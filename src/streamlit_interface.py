import streamlit as st
from chatbot import send_prompt, establish_api

# Establish sessions state variable to save conversation history
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

message_history = st.session_state['message_history']

# Titles
st.title("Hello, Streamlit!")
st.write("This is my first attempt at creating a simple chatbot using gemini API and streamlit :D")

with st.sidebar:
    st.title("Insert API Key to get started!")
    key = st.text_input("")
    if key:
        st.write(establish_api(key))


# Send, recieve and preserve conversation history
prompt = st.chat_input("Enter a prompt here")

messages = st.container()
if prompt:
    message_history.append({"user":prompt})
    response = send_prompt(prompt)
    message_history.append({"assistant":response})

for message in message_history:
    key, value = next(iter(message.items())) 
    messages.chat_message(key).write(value)

    
