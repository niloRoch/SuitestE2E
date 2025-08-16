# 🚀 1. Aplicação Principal (app/main.py)
import streamlit as st
from pathlib import Path

# Configuração da página
st.set_page_config(
    page_title="Meu Portfólio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    """Carrega CSS personalizado"""
    st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
    }
    .project-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .contact-form {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    load_css()
    
    # Sidebar para navegação
    st.sidebar.title("Navegação")
    page = st.sidebar.selectbox(
        "Selecione uma página:",
        ["🏠 Home", "👤 Sobre", "💼 Projetos", "📧 Contato"],
        key="navigation_select"
    )
    
    # Roteamento de páginas
    if page == "🏠 Home":
        show_home()
    elif page == "👤 Sobre":
        show_about()
    elif page == "💼 Projetos":
        show_projects()
    elif page == "📧 Contato":
        show_contact()

def show_home():
    """Página inicial"""
    st.markdown('<h1 class="main-header" data-testid="home-title">Bem-vindo ao Meu Portfólio</h1>', 
                unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Projetos Concluídos", 
            value="15", 
            delta="3 este mês",
            help="Número total de projetos finalizados"
        )
    
    with col2:
        st.metric(
            label="Tecnologias", 
            value="12", 
            delta="2 novas",
            help="Tecnologias que domino"
        )
    
    with col3:
        st.metric(
            label="Anos de Experiência", 
            value="5", 
            delta="Crescendo",
            help="Anos trabalhando com desenvolvimento"
        )
    
    st.markdown("---")
    st.markdown("### 🎯 Especialidades")
    
    skills = ["Python", "Streamlit", "Data Science", "Machine Learning", "Web Development"]
    cols = st.columns(len(skills))
    
    for i, skill in enumerate(skills):
        with cols[i]:
            st.button(skill, key=f"skill_{skill.lower()}")

def show_about():
    """Página sobre"""
    st.markdown('<h1 class="main-header" data-testid="about-title">Sobre Mim</h1>', 
                unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://via.placeholder.com/300x300", caption="Minha Foto")
    
    with col2:
        st.markdown("""
        ### 👋 Olá! Eu sou [Seu Nome]
        
        Sou um desenvolvedor apaixonado por tecnologia e inovação. Com experiência em:
        
        - 🐍 **Python Development**
        - 📊 **Data Science & Analytics**
        - 🤖 **Machine Learning**
        - 🌐 **Web Development**
        - ☁️ **Cloud Computing**
        
        Adoro resolver problemas complexos e criar soluções elegantes.
        """)
        
        if st.button("📄 Download CV", key="download_cv"):
            st.success("CV baixado com sucesso!")

def show_projects():
    """Página de projetos"""
    st.markdown('<h1 class="main-header" data-testid="projects-title">Meus Projetos</h1>', 
                unsafe_allow_html=True)
    
    # Filtros
    col1, col2 = st.columns([1, 1])
    with col1:
        tech_filter = st.multiselect(
            "Filtrar por tecnologia:",
            ["Python", "Streamlit", "Machine Learning", "Web Development"],
            key="tech_filter"
        )
    
    with col2:
        year_filter = st.selectbox(
            "Filtrar por ano:",
            ["Todos", "2024", "2023", "2022"],
            key="year_filter"
        )
    
    # Projetos
    projects = [
        {
            "title": "Dashboard Analytics",
            "description": "Dashboard interativo para análise de dados de vendas",
            "tech": ["Python", "Streamlit"],
            "year": "2024",
            "github": "https://github.com/user/dashboard"
        },
        {
            "title": "ML Predictor",
            "description": "Modelo de machine learning para previsão de preços",
            "tech": ["Python", "Machine Learning"],
            "year": "2023",
            "github": "https://github.com/user/ml-predictor"
        },
        {
            "title": "Web Scraper",
            "description": "Sistema de web scraping para coleta de dados",
            "tech": ["Python", "Web Development"],
            "year": "2023",
            "github": "https://github.com/user/scraper"
        }
    ]
    
    for project in projects:
        with st.container():
            st.markdown(f"""
            <div class="project-card" data-testid="project-{project['title'].lower().replace(' ', '-')}">
                <h3>{project['title']}</h3>
                <p>{project['description']}</p>
                <p><strong>Tecnologias:</strong> {', '.join(project['tech'])}</p>
                <p><strong>Ano:</strong> {project['year']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 4])
            with col1:
                st.link_button("GitHub", project['github'], key=f"github_{project['title']}")

def show_contact():
    """Página de contato"""
    st.markdown('<h1 class="main-header" data-testid="contact-title">Entre em Contato</h1>', 
                unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="contact-form">', unsafe_allow_html=True)
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Nome *", key="contact_name")
            email = st.text_input("Email *", key="contact_email")
            subject = st.selectbox(
                "Assunto *", 
                ["Proposta de Trabalho", "Colaboração", "Dúvidas", "Outro"],
                key="contact_subject"
            )
            message = st.text_area("Mensagem *", height=150, key="contact_message")
            
            submitted = st.form_submit_button("📤 Enviar Mensagem", type="primary")
            
            if submitted:
                if name and email and message:
                    st.success("✅ Mensagem enviada com sucesso! Responderei em breve.")
                else:
                    st.error("⚠️ Por favor, preencha todos os campos obrigatórios.")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        ### 📧 Informações de Contato
        
        **Email:** seuemail@exemplo.com
        
        **LinkedIn:** [linkedin.com/in/seuperfil](https://linkedin.com)
        
        **GitHub:** [github.com/seuusuario](https://github.com)
        
        **Localização:** Sua Cidade, Estado
        
        ---
        
        ### 🕒 Disponibilidade
        
        Segunda a Sexta: 9h - 18h
        
        Resposta em até 24h
        """)

if __name__ == "__main__":
    main()
