"""
Página contato
"""
import streamlit as st

def show():
    """Exibe a página de contato"""
    st.title("📞 Contato")
    
    with st.form("contact_form"):
        nome = st.text_input("Nome")
        email = st.text_input("Email")
        mensagem = st.text_area("Mensagem")
        submitted = st.form_submit_button("Enviar")
        
        if submitted:
            st.success("Mensagem enviada com sucesso!")
