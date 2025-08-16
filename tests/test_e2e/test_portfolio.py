import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestPortfolio:
    """Testes das funcionalidades do portfólio"""
    
    def test_home_metrics_display(self, driver, streamlit_app, wait, streamlit_helper):
        """Testa se as métricas da home são exibidas corretamente"""
        driver.get(streamlit_app)
        streamlit_helper.wait_for_app_load(driver, wait)
        
        # Verifica métricas
        metrics = driver.find_elements(By.CSS_SELECTOR, "[data-testid='metric-container']")
        assert len(metrics) >= 3
        
        # Verifica valores das métricas
        for metric in metrics:
            value = metric.find_element(By.CSS_SELECTOR, "[data-testid='metric-value']")
            assert value.text.strip() != ""
    
    def test_skills_buttons_interactive(self, driver, streamlit_app, wait, streamlit_helper):
        """Testa se os botões de habilidades são interativos"""
        driver.get(streamlit_app)
        streamlit_helper.wait_for_app_load(driver, wait)
        
        # Encontra botões de skills
        skill_buttons = driver.find_elements(
            By.XPATH, "//button[contains(@kind, 'secondary')]"
        )
        
        assert len(skill_buttons) > 0
        
        # Testa clique em um botão
        if skill_buttons:
            skill_buttons[0].click()
            # Verifica se o clique não gerou erro
            error_elements = driver.find_elements(By.CSS_SELECTOR, "[data-testid='stException']")
            assert len(error_elements) == 0
    
    def test_about_page_content(self, driver, streamlit_app, wait, streamlit_helper):
        """Testa o conteúdo da página Sobre"""
        driver.get(streamlit_app)
        streamlit_helper.wait_for_app_load(driver, wait)
        
        # Navega para página Sobre
        streamlit_helper.select_sidebar_option(driver, "👤 Sobre")
        
        # Verifica se a imagem está presente
        images = driver.find_elements(By.CSS_SELECTOR, "[data-testid='stImage']")
        assert len(images) >= 1
        
        # Verifica botão de download CV
        cv_button = wait(driver).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Download CV')]"))
        )
        assert cv_button.is_displayed()
    
    def test_projects_filtering(self, driver, streamlit_app, wait, streamlit_helper):
        """Testa funcionalidade de filtros na página de projetos"""
        driver.get(streamlit_app)
        streamlit_helper.wait_for_app_load(driver, wait)
        
        # Navega para página Projetos
        streamlit_helper.select_sidebar_option(driver, "💼 Projetos")
        
        # Verifica se os projetos são exibidos
        projects = wait(driver).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "[data-testid^='project-']")
            )
        )
        assert len(projects) > 0
        
        # Verifica filtros
        tech_filter = driver.find_element(By.CSS_SELECTOR, "[data-testid='stMultiSelect']")
        year_filter = driver.find_element(By.CSS_SELECTOR, "[data-testid='stSelectbox']")
        
        assert tech_filter.is_displayed()
        assert year_filter.is_displayed()
    
    def test_project_github_links(self, driver, streamlit_app, wait, streamlit_helper):
        """Testa se os links do GitHub nos projetos funcionam"""
        driver.get(streamlit_app)
        streamlit_helper.wait_for_app_load(driver, wait)
        
        # Navega para página Projetos
        streamlit_helper.select_sidebar_option(driver, "💼 Projetos")
        
        # Encontra links do GitHub
        github_links = wait(driver).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//a[contains(text(), 'GitHub')]")
            )
        )
        
        assert len(github_links) > 0
        
        # Verifica se os links têm href válido
        for link in github_links:
            href = link.get_attribute("href")
            assert href is not None
            assert "github.com" in href