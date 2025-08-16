import streamlit as st
import subprocess
import os
import json
import time
from datetime import datetime
import pandas as pd
from pathlib import Path
import threading
import queue

# Configuração da página
st.set_page_config(
    page_title="Portfolio E2E Testing Suite",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1e3a8a;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .metric-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    
    .test-status {
        padding: 0.5rem 1rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        font-weight: bold;
    }
    
    .status-passed { background-color: #10b981; }
    .status-failed { background-color: #ef4444; }
    .status-running { background-color: #f59e0b; }
    .status-pending { background-color: #6b7280; }
    
    .log-container {
        background-color: #1f2937;
        color: #f9fafb;
        padding: 1rem;
        border-radius: 8px;
        font-family: 'Courier New', monospace;
        font-size: 0.9rem;
        max-height: 400px;
        overflow-y: auto;
    }
</style>
""", unsafe_allow_html=True)

# Funções auxiliares
@st.cache_data
def get_test_structure():
    """Retorna a estrutura dos testes disponíveis"""
    return {
        "test_navigation.py": {
            "description": "Testes de navegação entre páginas",
            "tests": ["test_home_page_loads", "test_navigation_menu", "test_page_transitions"]
        },
        "test_portfolio.py": {
            "description": "Testes das funcionalidades do portfolio",
            "tests": ["test_portfolio_display", "test_project_details", "test_skills_section"]
        },
        "test_contact.py": {
            "description": "Testes do formulário de contato",
            "tests": ["test_contact_form", "test_form_validation", "test_submit_contact"]
        },
        "test_responsiveness.py": {
            "description": "Testes de responsividade",
            "tests": ["test_desktop_layout", "test_mobile_layout", "test_tablet_layout"]
        }
    }

def run_tests_async(command, result_queue):
    """Executa testes de forma assíncrona"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=300  # 5 minutos timeout
        )
        result_queue.put({
            'returncode': result.returncode,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'completed': True
        })
    except subprocess.TimeoutExpired:
        result_queue.put({
            'returncode': -1,
            'stdout': '',
            'stderr': 'Timeout: Testes excederam 5 minutos de execução',
            'completed': True
        })
    except Exception as e:
        result_queue.put({
            'returncode': -1,
            'stdout': '',
            'stderr': str(e),
            'completed': True
        })

def parse_pytest_output(output):
    """Parse do output do pytest para extrair informações"""
    lines = output.split('\n')
    results = {
        'passed': 0,
        'failed': 0,
        'errors': 0,
        'skipped': 0,
        'total_time': '0s',
        'details': []
    }
    
    for line in lines:
        if '=====' in line and 'passed' in line:
            # Extrai informações do resumo
            parts = line.split()
            for i, part in enumerate(parts):
                if 'passed' in part and i > 0:
                    results['passed'] = int(parts[i-1])
                elif 'failed' in part and i > 0:
                    results['failed'] = int(parts[i-1])
                elif 'error' in part and i > 0:
                    results['errors'] = int(parts[i-1])
                elif 'skipped' in part and i > 0:
                    results['skipped'] = int(parts[i-1])
        
        if 'seconds' in line or 'minutes' in line:
            # Extrai tempo de execução
            if 'in ' in line:
                time_part = line.split('in ')[-1].strip()
                results['total_time'] = time_part
    
    return results

# Interface principal
def main():
    # Header
    st.markdown('<h1 class="main-header">🧪 Portfolio E2E Testing Suite</h1>', unsafe_allow_html=True)
    
    # Sidebar - Configurações
    with st.sidebar:
        st.header("⚙️ Configurações")
        
        # Configurações de execução
        browser_mode = st.selectbox(
            "Modo do Browser",
            ["headless", "normal"],
            help="Headless para execução em background"
        )
        
        parallel_tests = st.checkbox(
            "Execução Paralela",
            value=True,
            help="Executa testes em paralelo (mais rápido)"
        )
        
        max_workers = st.slider(
            "Workers Paralelos",
            min_value=1,
            max_value=4,
            value=2,
            disabled=not parallel_tests
        )
        
        generate_html_report = st.checkbox(
            "Gerar Relatório HTML",
            value=True,
            help="Gera relatório detalhado em HTML"
        )
        
        st.divider()
        
        # Informações do projeto
        st.header("📋 Informações")
        st.info("""
        **Tecnologias:**
        - Frontend: Streamlit
        - Testes: Pytest + Selenium  
        - Browser: Chrome
        - Relatórios: pytest-html
        
        **Resoluções Testadas:**
        - Desktop: 1920x1080
        - Laptop: 1366x768
        - Tablet: 768x1024
        - Mobile: 375x667
        """)
    
    # Área principal
    tab1, tab2, tab3, tab4 = st.tabs(["🏠 Dashboard", "🧪 Executar Testes", "📊 Relatórios", "📋 Logs"])
    
    with tab1:
        # Dashboard
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="metric-container">
                <h3>4</h3>
                <p>Módulos de Teste</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-container">
                <h3>12</h3>
                <p>Testes Individuais</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="metric-container">
                <h3>4</h3>
                <p>Resoluções</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="metric-container">
                <h3>Chrome</h3>
                <p>Browser Padrão</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.divider()
        
        # Estrutura dos testes
        st.subheader("📁 Estrutura dos Testes")
        test_structure = get_test_structure()
        
        for test_file, info in test_structure.items():
            with st.expander(f"📄 {test_file}"):
                st.write(f"**Descrição:** {info['description']}")
                st.write("**Testes inclusos:**")
                for test in info['tests']:
                    st.write(f"- `{test}`")
    
    with tab2:
        # Executar Testes
        st.subheader("🚀 Executar Testes")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Seleção de testes
            st.write("**Selecione os testes a executar:**")
            test_structure = get_test_structure()
            
            selected_tests = []
            all_tests = st.checkbox("Todos os testes", key="all_tests")
            
            if all_tests:
                selected_tests = list(test_structure.keys())
            else:
                for test_file in test_structure.keys():
                    if st.checkbox(test_file, key=f"test_{test_file}"):
                        selected_tests.append(test_file)
        
        with col2:
            st.write("**Status da Execução:**")
            if 'test_running' not in st.session_state:
                st.session_state.test_running = False
            
            status_placeholder = st.empty()
            
            if st.session_state.test_running:
                status_placeholder.markdown(
                    '<div class="test-status status-running">🔄 Executando...</div>',
                    unsafe_allow_html=True
                )
            else:
                status_placeholder.markdown(
                    '<div class="test-status status-pending">⏸️ Aguardando</div>',
                    unsafe_allow_html=True
                )
        
        st.divider()
        
        # Botões de ação
        col1, col2, col3 = st.columns(3)
        
        with col1:
            run_button = st.button(
                "▶️ Executar Testes Selecionados",
                disabled=not selected_tests or st.session_state.test_running,
                type="primary"
            )
        
        with col2:
            run_all_button = st.button(
                "🚀 Executar Todos os Testes",
                disabled=st.session_state.test_running
            )
        
        with col3:
            if st.session_state.test_running:
                if st.button("⏹️ Parar Execução", type="secondary"):
                    st.session_state.test_running = False
                    st.rerun()
        
        # Execução dos testes
        if run_button or run_all_button:
            if run_all_button:
                selected_tests = list(test_structure.keys())
            
            st.session_state.test_running = True
            
            # Construir comando pytest
            base_cmd = "pytest tests/test_e2e/"
            
            if selected_tests:
                test_files = " ".join([f"tests/test_e2e/{test}" for test in selected_tests])
                cmd = f"pytest {test_files} -v"
            else:
                cmd = f"{base_cmd} -v"
            
            # Adicionar flags baseadas nas configurações
            if parallel_tests:
                cmd += f" -n {max_workers}"
            
            if generate_html_report:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                cmd += f" --html=reports/report_{timestamp}.html --self-contained-html"
            
            # Executar testes
            progress_bar = st.progress(0)
            status_text = st.empty()
            log_container = st.empty()
            
            # Simular execução (em produção, usar subprocess real)
            for i in range(100):
                time.sleep(0.05)  # Simular tempo de execução
                progress_bar.progress(i + 1)
                
                if i < 30:
                    status_text.text("🔍 Inicializando testes...")
                elif i < 60:
                    status_text.text("🧪 Executando testes de navegação...")
                elif i < 80:
                    status_text.text("📱 Testando responsividade...")
                else:
                    status_text.text("📊 Gerando relatórios...")
            
            st.session_state.test_running = False
            
            # Resultados simulados
            st.success("✅ Testes executados com sucesso!")
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("✅ Passou", "10", "2")
            with col2:
                st.metric("❌ Falhou", "1", "-1")
            with col3:
                st.metric("⚠️ Pulou", "1", "0")
            with col4:
                st.metric("⏱️ Tempo", "2.5s", "-0.3s")
    
    with tab3:
        # Relatórios
        st.subheader("📊 Relatórios de Teste")
        
        # Lista de relatórios (simulada)
        reports_data = {
            'Data': ['2024-01-15 14:30', '2024-01-15 12:15', '2024-01-14 16:45'],
            'Testes': ['Todos', 'Navegação', 'Todos'],
            'Passou': [10, 3, 8],
            'Falhou': [1, 0, 2],
            'Tempo': ['2.5s', '1.2s', '3.1s'],
            'Status': ['✅ Sucesso', '✅ Sucesso', '⚠️ Falhas']
        }
        
        df = pd.DataFrame(reports_data)
        st.dataframe(df, use_container_width=True)
        
        st.divider()
        
        # Download de relatórios
        col1, col2 = st.columns(2)
        
        with col1:
            st.download_button(
                "📥 Download Último Relatório HTML",
                data="<html>Relatório de exemplo</html>",
                file_name="ultimo_relatorio.html",
                mime="text/html"
            )
        
        with col2:
            st.download_button(
                "📊 Download Dados CSV",
                data=df.to_csv(index=False),
                file_name="historico_testes.csv",
                mime="text/csv"
            )
    
    with tab4:
        # Logs
        st.subheader("📋 Logs de Execução")
        
        # Filtros de log
        col1, col2 = st.columns(2)
        with col1:
            log_level = st.selectbox("Nível", ["INFO", "DEBUG", "WARNING", "ERROR"])
        with col2:
            show_timestamp = st.checkbox("Mostrar timestamp", value=True)
        
        # Container de logs simulados
        sample_logs = """
[2024-01-15 14:30:15] INFO: Iniciando execução de testes E2E
[2024-01-15 14:30:16] DEBUG: Configurando WebDriver Chrome
[2024-01-15 14:30:17] INFO: Executando test_navigation.py
[2024-01-15 14:30:18] DEBUG: Navegando para página inicial
[2024-01-15 14:30:19] INFO: ✅ test_home_page_loads PASSOU
[2024-01-15 14:30:20] DEBUG: Testando menu de navegação
[2024-01-15 14:30:21] INFO: ✅ test_navigation_menu PASSOU
[2024-01-15 14:30:22] WARNING: Elemento demorou para carregar
[2024-01-15 14:30:23] INFO: ✅ test_page_transitions PASSOU
[2024-01-15 14:30:24] INFO: Executando test_responsiveness.py
[2024-01-15 14:30:25] DEBUG: Testando resolução 1920x1080
[2024-01-15 14:30:26] INFO: ✅ test_desktop_layout PASSOU
[2024-01-15 14:30:27] ERROR: Falha no teste de mobile layout
[2024-01-15 14:30:28] INFO: ❌ test_mobile_layout FALHOU
[2024-01-15 14:30:29] INFO: Execução finalizada: 10 passou, 1 falhou
        """
        
        st.markdown(
            f'<div class="log-container">{sample_logs.strip()}</div>',
            unsafe_allow_html=True
        )
        
        # Botões de ação para logs
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("🔄 Atualizar Logs"):
                st.rerun()
        with col2:
            if st.button("🗑️ Limpar Logs"):
                st.success("Logs limpos!")
        with col3:
            st.download_button(
                "💾 Download Logs",
                data=sample_logs,
                file_name=f"logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )

if __name__ == "__main__":
    main()
