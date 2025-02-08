import streamlit as st

def get_diagnostic_questions():
    """Return a list of diagnostic questions"""
    return [
        "Jakie są główne dolegliwości?",
        "Kiedy zaczęły się objawy?",
        "Czy występuje ból? Jeśli tak, to gdzie?",
        "Czy przyjmujesz jakieś leki?",
        "Czy masz jakieś choroby przewlekłe?",
        "Czy w rodzinie występowały podobne problemy?",
        "Czy zauważyłeś/aś czynniki, które nasilają objawy?",
        "Jak oceniasz swój ogólny stan zdrowia?"
    ]

def get_examinations():
    """Return a list of common medical examinations"""
    return [
        "Podstawowe badania krwi (morfologia)",
        "Badanie moczu",
        "Pomiar ciśnienia krwi",
        "EKG",
        "RTG klatki piersiowej",
        "USG jamy brzusznej",
        "Poziom glukozy we krwi",
        "Profil lipidowy"
    ]

def render_questions():
    """Render the diagnostic questions section"""
    st.subheader("Pytania diagnostyczne")
    
    with st.expander("Zobacz listę pytań diagnostycznych", expanded=True):
        questions = get_diagnostic_questions()
        for i, question in enumerate(questions, 1):
            st.write(f"{i}. {question}")
    
    # Add examinations section below questions
    st.subheader("Zalecane badania")
    with st.expander("Zobacz listę zalecanych badań", expanded=True):
        examinations = get_examinations()
        for i, exam in enumerate(examinations, 1):
            st.write(f"{i}. {exam}") 