"""
🚀 Portfolio E2E - Aplicação Streamlit Moderna
Frontend completo com design responsivo e funcionalidades avançadas
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import base64
from pathlib import Path
import json
import time

# ================================
# CONFIGURAÇÃO DA PÁGINA
# ================================

st.set_page_config(
    page_title="SuiteE2E",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/niloRoch/SuiteE2E',
        'Report a bug': "https://github.com/niloRoch/portfolio/issues",
        'About': "Portfolio E2E com testes automatizados"
    }
)

# ================================
# CSS CUSTOMIZADO
# ================================

def load_custom_css():
    """Carrega CSS customizado para um design moderno"""
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Reset e Base Styles */
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    /* Header customizado */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .main-header p {
        font-size: 1.2rem;
        opacity: 0.9;
        margin: 0;
    }
    
    /* Cards modernos */
    .skill-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        border-left: 4px solid #667eea;
        margin-bottom: 1rem;
        transition: transform 0.2s;
    }
    
    .skill-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
    }
    
    .project-card {
        background: linear-gradient(145deg, #f8fafc 0%, #e2e8f0 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        transform: scale(1.02);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    }
    
    /* Badges */
    .tech-badge {
        display: inline-block;
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
        margin: 0.25rem;
    }
    
    /* Sidebar customizada */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Métricas */
    .metric-container {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #667eea;
        margin-bottom: 0.5rem;
    }
    
    .metric-label {
        color: #64748b;
        font-weight: 500;
    }
    
    /* Formulário */
    .contact-form {
        background: #f8fafc;
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
    }
    
    /* Animações */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.6s ease-out;
    }
    
    /* Timeline */
    .timeline-item {
        border-left: 3px solid #667eea;
        padding-left: 1.5rem;
        margin-bottom: 2rem;
        position: relative;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -8px;
        top: 0;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: #667eea;
    }
    
    /* Responsividade */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 2rem;
        }
        
        .main-header p {
            font-size: 1rem;
        }
        
        .project-card {
            padding: 1rem;
        }
    }
    
    /* Dark mode support */
    .stApp[data-theme="dark"] .skill-card {
        background: #1e293b;
        border-left-color: #667eea;
    }
    
    .stApp[data-theme="dark"] .project-card {
        background: linear-gradient(145deg, #1e293b 0%, #334155 100%);
    }
    </style>
    """, unsafe_allow_html=True)

# ================================
# DADOS DO PORTFOLIO
# ================================

class PortfolioData:
    """Classe para gerenciar dados do portfolio"""
    
    @staticmethod
    def get_personal_info():
        return {
            "nome": "Seu Nome Aqui",
            "titulo": "Desenvolvedor Full Stack & Data Scientist",
            "descricao": "Especialista em Python, Machine Learning e desenvolvimento web com foco em soluções inovadoras e testes automatizados.",
            "email": "seu.email@exemplo.com",
            "linkedin": "https://linkedin.com/in/seu-perfil",
            "github": "https://github.com/seu-usuario",
            "telefone": "+55 11 99999-9999",
            "localizacao": "São Paulo, Brasil"
        }
    
    @staticmethod
    def get_skills():
        return {
            "Linguagens de Programação": {
                "skills": ["Python", "JavaScript", "TypeScript", "SQL", "R"],
                "icon": "💻"
            },
            "Frameworks & Bibliotecas": {
                "skills": ["Streamlit", "Flask", "FastAPI", "React", "Pandas", "Scikit-learn"],
                "icon": "🚀"
            },
            "Banco de Dados": {
                "skills": ["PostgreSQL", "MongoDB", "Redis", "SQLite"],
                "icon": "🗄️"
            },
            "Cloud & DevOps": {
                "skills": ["AWS", "Docker", "GitHub Actions", "Heroku"],
                "icon": "☁️"
            },
            "Testes & Qualidade": {
                "skills": ["Pytest", "Selenium", "Jest", "CI/CD"],
                "icon": "🧪"
            }
        }
    
    @staticmethod
    def get_projects():
        return [
            {
                "nome": "Portfolio E2E Testing",
                "descricao": "Sistema completo de portfolio com testes automatizados end-to-end usando Selenium e Pytest.",
                "tecnologias": ["Python", "Streamlit", "Selenium", "Pytest", "GitHub Actions"],
                "github": "https://github.com/usuario/portfolio-e2e",
                "demo": "https://portfolio-demo.streamlit.app",
                "status": "Em produção",
                "categoria": "Web Application"
            },
            {
                "nome": "Dashboard Analytics",
                "descricao": "Dashboard interativo para análise de dados de vendas com visualizações dinâmicas e relatórios automatizados.",
                "tecnologias": ["Python", "Plotly", "Pandas", "Streamlit"],
                "github": "https://github.com/usuario/dashboard-analytics",
                "demo": "https://analytics-demo.streamlit.app",
                "status": "Concluído",
                "categoria": "Data Science"
            },
            {
                "nome": "API REST Completa",
                "descricao": "API RESTful robusta com autenticação JWT, documentação Swagger e testes automatizados.",
                "tecnologias": ["FastAPI", "PostgreSQL", "Docker", "Pytest"],
                "github": "https://github.com/usuario/api-rest",
                "demo": "https://api-demo.herokuapp.com/docs",
                "status": "Concluído",
                "categoria": "Backend"
            },
            {
                "nome": "ML Pipeline Automation",
                "descricao": "Pipeline automatizado de Machine Learning para previsão de churn com deploy em produção.",
                "tecnologias": ["Python", "Scikit-learn", "MLflow", "AWS"],
                "github": "https://github.com/usuario/ml-pipeline",
                "demo": None,
                "status": "Em desenvolvimento",
                "categoria": "Machine Learning"
            }
        ]
    
    @staticmethod
    def get_experience():
        return [
            {
                "cargo": "Senior Full Stack Developer",
                "empresa": "Tech Solutions Inc.",
                "periodo": "Jan 2022 - Presente",
                "descricao": "Desenvolvimento de aplicações web escaláveis e liderança técnica de equipe.",
                "conquistas": [
                    "Implementou arquitetura de microserviços reduzindo latência em 40%",
                    "Liderou equipe de 5 desenvolvedores",
                    "Implementou CI/CD aumentando velocidade de deploy em 60%"
                ]
            },
            {
                "cargo": "Python Developer",
                "empresa": "DataCorp Analytics",
                "periodo": "Mar 2020 - Dez 2021",
                "descricao": "Desenvolvimento de soluções de análise de dados e automação de processos.",
                "conquistas": [
                    "Desenvolveu 15+ dashboards interativos",
                    "Automatizou relatórios reduzindo tempo manual em 80%",
                    "Implementou testes automatizados aumentando cobertura para 95%"
                ]
            },
            {
                "cargo": "Junior Developer",
                "empresa": "StartupXYZ",
                "periodo": "Jun 2019 - Fev 2020",
                "descricao": "Desenvolvimento web e mobile com foco em experiência do usuário.",
                "conquistas": [
                    "Contribuiu para 3 produtos que atingiram 10k+ usuários",
                    "Implementou features que aumentaram retenção em 25%",
                    "Participou de code reviews e mentoria técnica"
                ]
            }
        ]

# ================================
# COMPONENTES REUTILIZÁVEIS
# ================================

def create_metric_card(title, value, icon="📊"):
    """Cria um card de métrica personalizado"""
    st.markdown(f"""
    <div class="metric-container">
        <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-label">{title}</div>
    </div>
    """, unsafe_allow_html=True)

def create_skill_badge(skill):
    """Cria badge para habilidades"""
    return f'<span class="tech-badge">{skill}</span>'

def create_timeline_item(item):
    """Cria item de timeline para experiência"""
    return f"""
    <div class="timeline-item fade-in">
        <h4 style="color: #667eea; margin-bottom: 0.5rem;">{item['cargo']}</h4>
        <h5 style="color: #64748b; margin-bottom: 0.5rem;">{item['empresa']} • {item['periodo']}</h5>
        <p style="margin-bottom: 1rem;">{item['descricao']}</p>
        <ul style="margin: 0;">
        {"".join([f"<li>{conquista}</li>" for conquista in item['conquistas']])}
        </ul>
    </div>
    """

# ================================
# PÁGINAS DO PORTFOLIO
# ================================

def show_home_page():
    """Página inicial com overview"""
    info = PortfolioData.get_personal_info()
    
    # Header principal
    st.markdown(f"""
    <div class="main-header fade-in">
        <h1>👋 Olá, eu sou {info['nome']}</h1>
        <p>{info['titulo']}</p>
        <p>{info['descricao']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        create_metric_card("Projetos", "15+", "🚀")
    
    with col2:
        create_metric_card("Anos Exp.", "5+", "💼")
    
    with col3:
        create_metric_card("Tecnologias", "20+", "💻")
    
    with col4:
        create_metric_card("Clientes", "50+", "🤝")
    
    st.markdown("---")
    
    # Overview de habilidades
    st.markdown("### 🎯 Principais Competências")
    
    skills = PortfolioData.get_skills()
    
    for category, data in skills.items():
        with st.expander(f"{data['icon']} {category}", expanded=True):
            st.markdown("".join([create_skill_badge(skill) for skill in data['skills']]), 
                       unsafe_allow_html=True)
    
    # Gráfico de experiência
    st.markdown("### 📊 Distribuição de Experiência")
    
    # Dados para o gráfico
    exp_data = {
        'Tecnologia': ['Python', 'JavaScript', 'SQL', 'React', 'AWS', 'Docker'],
        'Anos': [5, 3, 4, 2, 2, 3],
        'Projetos': [25, 15, 20, 10, 8, 12]
    }
    
    df = pd.DataFrame(exp_data)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.bar(df, x='Tecnologia', y='Anos', 
                     title='Anos de Experiência por Tecnologia',
                     color='Anos',
                     color_continuous_scale='viridis')
        fig.update_layout(showlegend=False, height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.pie(df, values='Projetos', names='Tecnologia', 
                     title='Distribuição de Projetos por Tecnologia')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

def show_about_page():
    """Página sobre com informações detalhadas"""
    info = PortfolioData.get_personal_info()
    
    st.markdown("# 👨‍💻 Sobre Mim")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div class="fade-in">
        <h3>Olá! Eu sou {info['nome']}</h3>
        <p style="font-size: 1.1rem; line-height: 1.6;">
        Sou um desenvolvedor apaixonado por tecnologia com mais de 5 anos de experiência 
        em desenvolvimento web, análise de dados e automação. Especializo-me em criar 
        soluções robustas e escaláveis usando as melhores práticas de desenvolvimento.
        </p>
        
        <h4>🎯 Minha Missão</h4>
        <p>
        Transformar ideias complexas em soluções tecnológicas simples e eficientes, 
        sempre focando na qualidade, performance e experiência do usuário.
        </p>
        
        <h4>💡 Valores</h4>
        <ul>
            <li><strong>Qualidade:</strong> Código limpo e bem testado</li>
            <li><strong>Inovação:</strong> Sempre buscando novas tecnologias</li>
            <li><strong>Colaboração:</strong> Trabalho em equipe e mentoria</li>
            <li><strong>Aprendizado:</strong> Crescimento contínuo</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="contact-form">
            <h4>📞 Contato</h4>
            <p><strong>Email:</strong><br>{info['email']}</p>
            <p><strong>Telefone:</strong><br>{info['telefone']}</p>
            <p><strong>Localização:</strong><br>{info['localizacao']}</p>
            
            <div style="margin-top: 1rem;">
                <a href="{info['linkedin']}" target="_blank" style="margin-right: 1rem;">
                    <button style="background: #0077b5; color: white; border: none; padding: 0.5rem 1rem; border-radius: 5px;">
                        LinkedIn
                    </button>
                </a>
                <a href="{info['github']}" target="_blank">
                    <button style="background: #333; color: white; border: none; padding: 0.5rem 1rem; border-radius: 5px;">
                        GitHub
                    </button>
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Experiência profissional
    st.markdown("---")
    st.markdown("## 💼 Experiência Profissional")
    
    experience = PortfolioData.get_experience()
    
    for exp in experience:
        st.markdown(create_timeline_item(exp), unsafe_allow_html=True)
    
    # Educação e certificações
    st.markdown("---")
    st.markdown("## 🎓 Educação & Certificações")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🎓 Formação Acadêmica**
        - Bacharelado em Ciência da Computação - USP (2019)
        - MBA em Gestão de Projetos - FGV (2021)
        """)
    
    with col2:
        st.markdown("""
        **🏆 Certificações**
        - AWS Certified Solutions Architect
        - Google Cloud Professional
        - Scrum Master Certified
        """)

def show_projects_page():
    """Página de projetos com filtros e detalhes"""
    st.markdown("# 🚀 Meus Projetos")
    
    projects = PortfolioData.get_projects()
    
    # Filtros
    col1, col2, col3 = st.columns(3)
    
    with col1:
        categories = list(set([p['categoria'] for p in projects]))
        selected_category = st.selectbox("Categoria", ["Todas"] + categories)
    
    with col2:
        statuses = list(set([p['status'] for p in projects]))
        selected_status = st.selectbox("Status", ["Todos"] + statuses)
    
    with col3:
        # Tecnologias únicas
        all_techs = []
        for p in projects:
            all_techs.extend(p['tecnologias'])
        unique_techs = list(set(all_techs))
        selected_tech = st.selectbox("Tecnologia", ["Todas"] + unique_techs)
    
    # Filtrar projetos
    filtered_projects = projects
    
    if selected_category != "Todas":
        filtered_projects = [p for p in filtered_projects if p['categoria'] == selected_category]
    
    if selected_status != "Todos":
        filtered_projects = [p for p in filtered_projects if p['status'] == selected_status]
    
    if selected_tech != "Todas":
        filtered_projects = [p for p in filtered_projects if selected_tech in p['tecnologias']]
    
    st.markdown(f"**Mostrando {len(filtered_projects)} projeto(s)**")
    
    # Grid de projetos
    for i, project in enumerate(filtered_projects):
        if i % 2 == 0:
            col1, col2 = st.columns(2)
            current_col = col1
        else:
            current_col = col2
        
        with current_col:
            # Status badge
            status_color = {
                "Concluído": "🟢",
                "Em produção": "🔵", 
                "Em desenvolvimento": "🟡"
            }
            
            st.markdown(f"""
            <div class="project-card fade-in">
                <div style="display: flex; justify-content: between; align-items: center; margin-bottom: 1rem;">
                    <h4 style="margin: 0; color: #667eea;">{project['nome']}</h4>
                    <span style="font-size: 0.9rem;">{status_color.get(project['status'], '⚪')} {project['status']}</span>
                </div>
                
                <p style="margin-bottom: 1rem; line-height: 1.5;">{project['descricao']}</p>
                
                <div style="margin-bottom: 1rem;">
                    <strong>Tecnologias:</strong><br>
                    {"".join([create_skill_badge(tech) for tech in project['tecnologias']])}
                </div>
                
                <div style="margin-bottom: 1rem;">
                    <strong>Categoria:</strong> {project['categoria']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Botões de ação
            col_gh, col_demo = st.columns(2)
            
            with col_gh:
                st.markdown(f"[📂 GitHub]({project['github']})")
            
            with col_demo:
                if project['demo']:
                    st.markdown(f"[🚀 Demo]({project['demo']})")
                else:
                    st.markdown("🚧 Em desenvolvimento")
    
    # Estatísticas dos projetos
    st.markdown("---")
    st.markdown("## 📊 Estatísticas dos Projetos")
    
    # Gráfico de tecnologias mais usadas
    tech_count = {}
    for project in projects:
        for tech in project['tecnologias']:
            tech_count[tech] = tech_count.get(tech, 0) + 1
    
    col1, col2 = st.columns(2)
    
    with col1:
        tech_df = pd.DataFrame(list(tech_count.items()), columns=['Tecnologia', 'Projetos'])
        tech_df = tech_df.sort_values('Projetos', ascending=True)
        
        fig = px.bar(tech_df, x='Projetos', y='Tecnologia', orientation='h',
                     title='Tecnologias Mais Utilizadas',
                     color='Projetos',
                     color_continuous_scale='viridis')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Status dos projetos
        status_count = {}
        for project in projects:
            status = project['status']
            status_count[status] = status_count.get(status, 0) + 1
        
        fig = px.pie(values=list(status_count.values()), 
                     names=list(status_count.keys()),
                     title='Status dos Projetos')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

def show_contact_page():
    """Página de contato com formulário funcional"""
    st.markdown("# 📞 Entre em Contato")
    
    info = PortfolioData.get_personal_info()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="contact-form fade-in">
        <h3>💬 Vamos Conversar!</h3>
        <p>
        Estou sempre interessado em novos projetos e oportunidades. 
        Entre em contato comigo através do formulário abaixo ou pelos 
        canais de contato ao lado.
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Formulário de contato
        with st.form("contact_form", clear_on_submit=True):
            st.markdown("### 📝 Formulário de Contato")
            
            col_name, col_email = st.columns(2)
            
            with col_name:
                nome = st.text_input("Nome *", placeholder="Seu nome completo")
            
            with col_email:
                email = st.text_input("Email *", placeholder="seu@email.com")
            
            assunto = st.text_input("Assunto", placeholder="Sobre o que você gostaria de falar?")
            
            mensagem = st.text_area("Mensagem *", 
                                  placeholder="Conte-me mais sobre seu projeto ou ideia...",
                                  height=150)
            
            # Checkbox para newsletter
            newsletter = st.checkbox("Quero receber updates sobre novos projetos")
            
            # Botão de envio
            submitted = st.form_submit_button("📧 Enviar Mensagem", 
                                            type="primary",
                                            use_container_width=True)
            
            if submitted:
                # Validações
                if not nome or not email or not mensagem:
                    st.error("❌ Por favor, preencha todos os campos obrigatórios!")
                elif "@" not in email or "." not in email:
                    st.error("❌ Por favor, insira um email válido!")
                else:
                    # Simular envio (aqui você integraria com um serviço real)
                    with st.spinner("Enviando mensagem..."):
                        time.sleep(2)  # Simular processamento
                        
                    st.success("✅ Mensagem enviada com sucesso! Retornarei em breve.")
                    st.balloons()
                    
                    # Mostrar dados recebidos (para demonstração)
                    with st.expander("📋 Dados recebidos (Demo)"):
                        st.json({
                            "nome": nome,
                            "email": email,
                            "assunto": assunto,
                            "mensagem": mensagem,
                            "newsletter": newsletter,
                            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        })
    
    with col2:
        # Informações de contato
        st.markdown(f"""
        <div class="contact-form">
            <h3>📱 Informações de Contato</h3>
            
            <div style="margin-bottom: 1.5rem;">
                <h4>📧 Email</h4>
                <p><a href="mailto:{info['email']}">{info['email']}</a></p>
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <h4>📱 Telefone</h4>
                <p><a href="tel:{info['telefone']}">{info['telefone']}</a></p>
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <h4>📍 Localização</h4>
                <p>{info['localizacao']}</p>
            </div>
            
            <div style="margin-bottom: 1.5rem;">
                <h4>🌐 Redes Sociais</h4>
                <p>
                    <a href="{info['linkedin']}" target="_blank">🔗 LinkedIn</a><br>
                    <a href="{info['github']}" target="_blank">📂 GitHub</a>
                </p>
            </div>
            
            <div>
                <h4>⏰ Disponibilidade</h4>
                <p>
                Seg-Sex: 9h às 18h<br>
                Resposta em até 24h
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Status de disponibilidade
        st.markdown("### 🟢 Status Atual")
        
        status_options = {
            "🟢 Disponível para novos projetos": "success",
            "🟡 Parcialmente disponível": "warning", 
            "🔴 Indisponível no momento": "error"
        }
        
        current_status = "🟢 Disponível para novos projetos"
        st.success(current_status)
        
        # Tempo de resposta médio
        st.metric("⚡ Tempo médio de resposta", "4 horas", "⬇️ 2h")

def show_dashboard_page():
    """Página de dashboard com métricas e análises"""
    st.markdown("# 📊 Dashboard de Atividades")
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Projetos Ativos", "4", "↗️ +1")
    
    with col2:
        st.metric("Commits Este Mês", "127", "↗️ +23")
    
    with col3:
        st.metric("Horas Codificando", "45h", "↗️ +5h")
    
    with col4:
        st.metric("Issues Resolvidas", "18", "↗️ +3")
    
    # Gráficos de atividade
    st.markdown("### 📈 Atividade de Desenvolvimento")
    
    # Dados simulados para os gráficos
    dates = pd.date_range(start='2024-01-01', end='2024-08-15', freq='D')
    commits_data = {
        'Data': dates,
        'Commits': np.random.poisson(3, len(dates)),
        'Lines Added': np.random.normal(100, 30, len(dates)).astype(int),
        'Lines Removed': np.random.normal(50, 20, len(dates)).astype(int)
    }
    
    df_activity = pd.DataFrame(commits_data)
    df_activity['Lines Added'] = df_activity['Lines Added'].clip(lower=0)
    df_activity['Lines Removed'] = df_activity['Lines Removed'].clip(lower=0)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de commits ao longo do tempo
        fig = px.line(df_activity, x='Data', y='Commits', 
                     title='Commits por Dia',
                     color_discrete_sequence=['#667eea'])
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Gráfico de linhas de código
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df_activity['Data'], y=df_activity['Lines Added'],
                                mode='lines', name='Adicionadas', line=dict(color='#10B981')))
        fig.add_trace(go.Scatter(x=df_activity['Data'], y=df_activity['Lines Removed'],
                                mode='lines', name='Removidas', line=dict(color='#EF4444')))
        fig.update_layout(title='Linhas de Código por Dia', height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    # Linguagens mais usadas
    st.markdown("### 💻 Linguagens Mais Utilizadas")
    
    languages_data = {
        'Linguagem': ['Python', 'JavaScript', 'HTML/CSS', 'SQL', 'TypeScript', 'Shell'],
        'Horas': [120, 80, 45, 35, 25, 15],
        'Projetos': [8, 6, 10, 5, 3, 4]
    }
    
    df_langs = pd.DataFrame(languages_data)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.bar(df_langs, x='Linguagem', y='Horas',
                     title='Horas por Linguagem (Últimos 3 meses)',
                     color='Horas',
                     color_continuous_scale='viridis')
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.pie(df_langs, values='Projetos', names='Linguagem',
                     title='Distribuição por Projetos')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Heatmap de atividade
    st.markdown("### 🔥 Heatmap de Atividade")
    
    # Criar dados para heatmap (simulando GitHub)
    import numpy as np
    
    weeks = 52
    days = 7
    activity_data = np.random.poisson(2, (days, weeks))
    
    fig = go.Figure(data=go.Heatmap(
        z=activity_data,
        colorscale='Greens',
        showscale=True,
        hovertemplate='Dia: %{y}<br>Semana: %{x}<br>Commits: %{z}<extra></extra>'
    ))
    
    fig.update_layout(
        title='Atividade de Commits (Últimos 12 meses)',
        xaxis_title='Semanas',
        yaxis_title='Dias da Semana',
        height=200,
        yaxis=dict(
            tickmode='array',
            tickvals=list(range(7)),
            ticktext=['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb']
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Últimas atividades
    st.markdown("### 📝 Últimas Atividades")
    
    recent_activities = [
        {"acao": "Commit", "projeto": "Portfolio E2E", "descricao": "Adicionou testes de responsividade", "tempo": "2 horas atrás"},
        {"acao": "Pull Request", "projeto": "API REST", "descricao": "Implementou autenticação JWT", "tempo": "5 horas atrás"},
        {"acao": "Issue Resolvida", "projeto": "Dashboard Analytics", "descricao": "Corrigiu bug no filtro de datas", "tempo": "1 dia atrás"},
        {"acao": "Deploy", "projeto": "Portfolio E2E", "descricao": "Deploy em produção realizado", "tempo": "2 dias atrás"},
        {"acao": "Commit", "projeto": "ML Pipeline", "descricao": "Otimizou modelo de previsão", "tempo": "3 dias atrás"}
    ]
    
    for activity in recent_activities:
        icon_map = {
            "Commit": "💾",
            "Pull Request": "🔄",
            "Issue Resolvida": "✅",
            "Deploy": "🚀"
        }
        
        icon = icon_map.get(activity["acao"], "📝")
        
        st.markdown(f"""
        <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; margin-bottom: 0.5rem; border-left: 3px solid #667eea;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <strong>{icon} {activity["acao"]}</strong> em <code>{activity["projeto"]}</code>
                    <br><small style="color: #64748b;">{activity["descricao"]}</small>
                </div>
                <small style="color: #64748b;">{activity["tempo"]}</small>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ================================
# NAVEGAÇÃO PRINCIPAL
# ================================

def main():
    """Função principal da aplicação"""
    
    # Carregar CSS customizado
    load_custom_css()
    
    # Sidebar de navegação
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; color: white; margin-bottom: 1rem;">
            <h2>🚀 Portfolio E2E</h2>
            <p>Desenvolvedor Full Stack</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Menu de navegação
        pages = {
            "🏠 Home": "home",
            "👨‍💻 Sobre": "about", 
            "🚀 Projetos": "projects",
            "📞 Contato": "contact",
            "📊 Dashboard": "dashboard"
        }
        
        selected_page = st.radio("Navegação", list(pages.keys()), key="navigation")
        
        # Informações adicionais na sidebar
        st.markdown("---")
        st.markdown("### 🔗 Links Rápidos")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📂 GitHub", use_container_width=True):
                st.markdown("[GitHub](https://github.com/seu-usuario)", unsafe_allow_html=True)
        
        with col2:
            if st.button("💼 LinkedIn", use_container_width=True):
                st.markdown("[LinkedIn](https://linkedin.com/in/seu-perfil)", unsafe_allow_html=True)
        
        # Status online
        st.markdown("---")
        st.markdown("### 📱 Status")
        st.success("🟢 Online")
        st.caption("Última atividade: agora")
        
        # Modo escuro toggle (simulado)
        st.markdown("---")
        dark_mode = st.checkbox("🌙 Modo Escuro")
        if dark_mode:
            st.markdown("""
            <style>
            .stApp {
                background-color: #1e1e1e;
                color: white;
            }
            </style>
            """, unsafe_allow_html=True)
    
    # Roteamento de páginas
    page_key = pages[selected_page]
    
    if page_key == "home":
        show_home_page()
    elif page_key == "about":
        show_about_page()
    elif page_key == "projects":
        show_projects_page()
    elif page_key == "contact":
        show_contact_page()
    elif page_key == "dashboard":
        show_dashboard_page()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: #f8fafc; border-radius: 10px; margin-top: 2rem;">
        <p style="color: #64748b; margin: 0;">
            Desenvolvido com ❤️ usando <strong>Streamlit</strong><br>
            © 2024 Seu Nome. Todos os direitos reservados.
        </p>
        <div style="margin-top: 1rem;">
            <small style="color: #94a3b8;">
                Portfolio E2E v1.0 | Última atualização: Agosto 2024
            </small>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================================
# EXECUÇÃO DA APLICAÇÃO
# ================================

if __name__ == "__main__":
    # Imports necessários para funcionalidades avançadas
    import numpy as np
    
    # Configurações adicionais
    st.markdown("""
    <script>
    // Analytics tracking (substitua pelo seu código)
    // gtag('event', 'page_view', {
    //     page_title: document.title,
    //     page_location: window.location.href
    // });
    </script>
    """, unsafe_allow_html=True)
    
    # Executar aplicação principal
    main()