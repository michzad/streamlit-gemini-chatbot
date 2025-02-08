import streamlit as st

def get_diagnostic_questions():
    # """Return a list of diagnostic questions"""
    return st.session_state['last_message']['followUpQuestions']

def get_examinations():
    # """Return a list of common medical examinations"""
    return st.session_state['last_message']['diagnosticProcedures']
    

def render_questions():
    """Render the diagnostic questions section"""
    st.subheader("Pytania diagnostyczne")
    
    with st.expander("Zobacz listę pytań diagnostycznych", expanded=True):
        questions = get_diagnostic_questions()
        for i, question in enumerate(questions, 1):
            st.write(f"{i}. {question['question']}")
    
    # Add examinations section below questions
    st.subheader("Zalecane badania")
    with st.expander("Zobacz listę zalecanych badań", expanded=True):
        examinations = get_examinations()
        for i, exam in enumerate(examinations, 1):
            st.write(f"{i}. {exam['procedure']}") 

    with st.expander("Podsumowanie", expanded=False):
        st.write(f"{st.session_state['last_message']['summary']}")

    with st.expander("ESI", expanded=False):
        st.write(f"{st.session_state['last_message']['severity_index']}")