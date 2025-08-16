"""Dados de teste para os testes E2E"""

# Dados de teste para formulário de contato
CONTACT_FORM_DATA = {
    "valid": {
        "name": "João Silva",
        "email": "joao.silva@exemplo.com",
        "subject": "Proposta de Trabalho",
        "message": "Olá! Gostaria de discutir uma oportunidade de trabalho em sua empresa."
    },
    "invalid_email": {
        "name": "Maria Santos",
        "email": "email_invalido",
        "subject": "Dúvidas",
        "message": "Tenho algumas dúvidas sobre seus projetos."
    },
    "empty": {
        "name": "",
        "email": "",
        "subject": "",
        "message": ""
    }
}

# Dados de teste para projetos
PROJECTS_DATA = [
    {
        "title": "Dashboard Analytics",
        "description": "Dashboard interativo para análise de dados",
        "technologies": ["Python", "Streamlit", "Plotly"],
        "year": "2024"
    },
    {
        "title": "ML Predictor",
        "description": "Modelo de machine learning para previsões",
        "technologies": ["Python", "Scikit-learn", "Pandas"],
        "year": "2023"
    }
]

# URLs de teste
TEST_URLS = {
    "github": "https://github.com",
    "linkedin": "https://linkedin.com",
    "invalid": "invalid-url"
}

# Dados de métricas esperadas
EXPECTED_METRICS = {
    "projects": 15,
    "technologies": 12,
    "experience": 5
}

# Resoluções para testes de responsividade
SCREEN_RESOLUTIONS = [
    {"name": "desktop", "width": 1920, "height": 1080},
    {"name": "laptop", "width": 1366, "height": 768},
    {"name": "tablet", "width": 768, "height": 1024},
    {"name": "mobile", "width": 375, "height": 667}
]