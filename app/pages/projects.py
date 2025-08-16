"""
Página projetos
"""
import streamlit as st

def show():
    """Exibe a página de projetos"""
    st.title("🚀 Meus Projetos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Projeto 1")
        st.write("Descrição do projeto 1")
        st.button("Ver mais", key="proj1")
    
    with col2:
        st.subheader("Projeto 2")
        st.write("Descrição do projeto 2")
        st.button("Ver mais", key="proj2")
