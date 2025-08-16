import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class TestContact:
    """Testes da funcionalidade de contato"""
    
    def test_contact_form_exists(self, driver, streamlit_app, wait, streamlit_helper):
        """Testa se o formulário de contato existe"""
        driver.get(streamlit_app)
        streamlit_helper.wait_for_app_load(driver, wait)
        
        # Navega para página Contato
        streamlit_helper.select_sidebar_option(driver, "📧 Contato")
        
        # Verifica campos do formulário
        name_field = wait(driver).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='stTextInput'] input")
            )
        )
        assert name_field.is_displayed()
        
        # Verifica área de texto
        message_field = driver.find_element(
            By.CSS_SELECTOR, "[data-testid='stTextArea'] textarea"
        )
        assert message_field.is_displayed()
        
        # Verifica botão de envio
        submit_button = driver.find_element(
            By.XPATH, "//button[contains(text(), 'Enviar Mensagem')]"
        )
        assert submit_button.is_displayed()
    
    def test_contact_form_validation(self, driver, streamlit_app, wait, streamlit_helper):
        """Testa validação do formulário de contato"""
        driver.get(streamlit_app)
        streamlit_helper.wait_for_app_load(driver, wait)
        
        # Navega para página Contato
        streamlit_helper.select_sidebar_option(driver, "📧 Contato")
        
        # Tenta enviar formulário vazio
        submit_button = wait(driver).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Enviar Mensagem')]")
            )
        )
        submit_button.click()
        
        # Verifica mensagem de erro
        error_message = wait(driver).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='stAlert']"))
        )
        assert "preencha todos os campos" in error_message.text.lower()
    
    def test_contact_form_submission(self, driver, streamlit_app, wait, streamlit_helper):
        """Testa envio do formulário de contato"""
        driver.get(streamlit_app)
        streamlit_helper.wait_for_app_load(driver, wait)
        
        # Navega para página Contato
        streamlit_helper.select_sidebar_option(driver, "📧 Contato")
        
        # Preenche o formulário
        name_field = wait(driver).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='stTextInput'] input")
            )
        )
        name_field.send_keys("João Silva")
        
        # Email field (segundo input)
        email_inputs = driver.find_elements(By.CSS_SELECTOR, "[data-testid='stTextInput'] input")
        if len(email_inputs) > 1:
            email_inputs[1].send_keys("joao@exemplo.com")
        
        # Seleciona assunto
        subject_select = driver.find_element(By.CSS_SELECTOR, "[data-testid='stSelectbox'] select")
        select = Select(subject_select)
        select.select_by_visible_text("Proposta de Trabalho")
        
        # Mensagem
        message_field = driver.find_element(By.CSS_SELECTOR, "[data-testid='stTextArea'] textarea")
        message_field.send_keys("Olá! Gostaria de discutir uma oportunidade de trabalho.")
        
        # Envia formulário
        submit_button = driver.find_element(
            By.XPATH, "//button[contains(text(), 'Enviar Mensagem')]"
        )
        submit_button.click()
        
        # Verifica mensagem de sucesso
        success_message = wait(driver).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='stAlert']"))
        )
        assert "sucesso" in success_message.text.lower()
    
    def test_contact_info_display(self, driver, streamlit_app, wait, streamlit_helper):
        """Testa se as informações de contato são exibidas"""
        driver.get(streamlit_app)
        streamlit_helper.wait_for_app_load(driver, wait)
        
        # Navega para página Contato
        streamlit_helper.select_sidebar_option(driver, "📧 Contato")
        
        # Verifica se as informações de contato estão visíveis
        page_content = driver.find_element(By.CSS_SELECTOR, "[data-testid='stVerticalBlock']")
        content_text = page_content.text
        
        # Verifica informações específicas
        assert "Email:" in content_text
        assert "LinkedIn:" in content_text
        assert "GitHub:" in content_text
        assert "Disponibilidade" in content_text