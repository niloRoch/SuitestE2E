import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestPerformance:
    """Testes de performance da aplicação"""
    
    def test_page_load_time(self, driver, streamlit_app, wait, streamlit_helper):
        """Testa tempo de carregamento das páginas"""
        pages = ["🏠 Home", "👤 Sobre", "💼 Projetos", "📧 Contato"]
        max_load_time = 10  # segundos
        
        for page in pages:
            start_time = time.time()
            
            driver.get(streamlit_app)
            streamlit_helper.wait_for_app_load(driver, wait)
            
            if page != "🏠 Home":
                streamlit_helper.select_sidebar_option(driver, page)
            
            # Aguarda carregamento completo
            wait(driver).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid$='-title']"))
            )
            
            load_time = time.time() - start_time
            assert load_time < max_load_time, f"Página {page} demorou {load_time:.2f}s para carregar"
    
    def test_form_submission_response_time(self, driver, streamlit_app, wait, streamlit_helper):
        """Testa tempo de resposta do formulário"""
        driver.get(streamlit_app)
        streamlit_helper.wait_for_app_load(driver, wait)
        
        # Navega para contato
        streamlit_helper.select_sidebar_option(driver, "📧 Contato")
        
        # Preenche formulário
        fields = driver.find_elements(By.CSS_SELECTOR, "[data-testid='stTextInput'] input")
        if len(fields) >= 2:
            fields[0].send_keys("Test User")
            fields[1].send_keys("test@example.com")
        
        message_field = driver.find_element(By.CSS_SELECTOR, "[data-testid='stTextArea'] textarea")
        message_field.send_keys("Test message")
        
        # Mede tempo de submissão
        start_time = time.time()
        
        submit_button = driver.find_element(
            By.XPATH, "//button[contains(text(), 'Enviar Mensagem')]"
        )
        submit_button.click()
        
        # Aguarda resposta
        wait(driver).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='stAlert']"))
        )
        
        response_time = time.time() - start_time
        assert response_time < 5, f"Formulário demorou {response_time:.2f}s para responder"