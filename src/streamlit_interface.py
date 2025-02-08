import streamlit as st
from sidebar import render_sidebar
from questions import render_questions
from chat import render_chat


st.set_page_config(layout="wide")
# Initialize session state
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# ============= HEADER SECTION =============
def render_header():
    st.title("LeanMedic - aplikacja testowa")
    st.write("Wywiad medyczny ze wsparciem sztucznej inteligencji")

# ============= BODY SECTION =============
def render_body():
    # Create two columns with adjusted ratio (3:2 instead of 2:1)
    col1, col2 = st.columns([3, 2])
    
    with col1:
        # Chat interface
        render_chat()
    
    with col2:
        # Questions section
        render_questions()

    # Render sidebar (outside columns)
    render_sidebar()

# Render the app
render_header()
render_body()

    
