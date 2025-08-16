import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestNavigation:
    """Testes de navegação entre páginas"""
    
    def test_sidebar_navigation_exists(self, driver, streamlit_app, wait, streamlit_helper):
        """Testa se o sidebar de navegação existe"""
        driver.get(streamlit_app)
        streamlit_helper.wait_for_app_load(driver, wait)
        
        sidebar = driver.find_element(By.CSS_SELECTOR, "[data-testid='stSidebar']")
        assert sidebar.is_displayed()
        
        # Verifica se o título da navegação existe
        nav_title = sidebar.find_element(By.XPATH, "//div[contains(text(), 'Navegação')]")
        assert nav_title.is_displayed()
    
    def test_home_page_load(self, driver, streamlit_app, wait, streamlit_helper):
        """Testa se a página inicial carrega corretamente"""
        driver.get(streamlit_app)
        streamlit_helper.wait_for_app_load(driver, wait)
        
        # Verifica título da home
        title = wait(driver).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='home-title']"))
        )
        assert "Bem-vindo" in title.text
        
        # Verifica métricas
        metrics = driver.find_elements(By.CSS_SELECTOR, "[data-testid='metric-container']")
        assert len(metrics) >= 3
    
    def test_about_page_navigation(self, driver, streamlit_app, wait, streamlit_helper):
        """Testa navegação para página Sobre"""
        driver.get(streamlit_app)
        streamlit_helper.wait_for_app_load(driver, wait)
        
        # Navega para página Sobre
        streamlit_helper.select_sidebar_option(driver, "👤 Sobre")
        
        # Verifica se chegou na página correta
        title = wait(driver).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='about-title']"))
        )
        assert "Sobre Mim" in title.text
    
    def test_projects_page_navigation(self, driver, streamlit_app, wait, streamlit_helper):
        """Testa navegação para página Projetos"""
        driver.get(streamlit_app)
        streamlit_helper.wait_for_app_load(driver, wait)
        
        # Navega para página Projetos
        streamlit_helper.select_sidebar_option(driver, "💼 Projetos")
        
        # Verifica se chegou na página correta
        title = wait(driver).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='projects-title']"))
        )
        assert "Meus Projetos" in title.text
        
        # Verifica se os filtros existem
        tech_filter = driver.find_element(By.CSS_SELECTOR, "[data-testid='stMultiSelect']")
        assert tech_filter.is_displayed()
    
    def test_contact_page_navigation(self, driver, streamlit_app, wait, streamlit_helper):
        """Testa navegação para página Contato"""
        driver.get(streamlit_app)
        streamlit_helper.wait_for_app_load(driver, wait)
        
        # Navega para página Contato
        streamlit_helper.select_sidebar_option(driver, "📧 Contato")
        
        # Verifica se chegou na página correta
        title = wait(driver).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='contact-title']"))
        )
        assert "Entre em Contato" in title.text
    
    def test_all_pages_accessible(self, driver, streamlit_app, wait, streamlit_helper):
        """Testa se todas as páginas são acessíveis"""
        driver.get(streamlit_app)
        streamlit_helper.wait_for_app_load(driver, wait)
        
        pages = ["🏠 Home", "👤 Sobre", "💼 Projetos", "📧 Contato"]
        
        for page in pages:
            streamlit_helper.select_sidebar_option(driver, page)
            
            # Aguarda o carregamento da página
            wait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid$='-title']"))
            )
            
            # Verifica se não há erros na página
            error_elements = driver.find_elements(By.CSS_SELECTOR, "[data-testid='stException']")
            assert len(error_elements) == 0, f"Erro encontrado na página {page}"