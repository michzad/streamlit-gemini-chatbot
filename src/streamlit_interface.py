import streamlit as st
from sidebar import render_sidebar
from questions import render_questions
from chat import render_chat


st.set_page_config(layout="wide")
# Initialize session state
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'last_message' not in st.session_state:
    st.session_state['last_message'] = {
        'followUpQuestions': [],
        'diagnosticProcedures': [],
        'summary': 'Pusto',
        'severity_index': ''
    }

# ============= HEADER SECTION =============
def render_header():
    st.title("LeanMedic - aplikacja testowa")
    # st.write("Wywiad medyczny ze wsparciem sztucznej inteligencji !")

# ============= BODY SECTION =============
def render_body():
    # Create two columns with adjusted ratio (3:2 instead of 2:1)

    render_chat()
    render_questions()
    


    # Render sidebar (outside columns)
    render_sidebar()

# Render the app
render_header()
render_body()

    
