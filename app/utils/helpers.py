"""Utilitários auxiliares para os testes E2E"""

import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestUtils:
    """Classe com utilitários para testes"""
    
    @staticmethod
    def take_screenshot(driver, name):
        """Captura screenshot para debugging"""
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        
        timestamp = int(time.time())
        filename = f"screenshots/{name}_{timestamp}.png"
        driver.save_screenshot(filename)
        return filename
    
    @staticmethod
    def wait_for_element_text(driver, locator, expected_text, timeout=10):
        """Aguarda elemento conter texto específico"""
        from selenium.webdriver.support.ui import WebDriverWait
        wait = WebDriverWait(driver, timeout)
        
        def text_present(driver):
            element = driver.find_element(*locator)
            return expected_text.lower() in element.text.lower()
        
        return wait.until(text_present)
    
    @staticmethod
    def scroll_to_element(driver, element):
        """Faz scroll até o elemento"""
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)  # Pequena pausa para o scroll
    
    @staticmethod
    def get_console_logs(driver):
        """Obtém logs do console do browser"""
        return driver.get_log('browser')
    
    @staticmethod
    def check_for_errors(driver):
        """Verifica se há erros na página"""
        error_elements = driver.find_elements(By.CSS_SELECTOR, "[data-testid='stException']")
        return len(error_elements) == 0
    
    @staticmethod
    def wait_for_stable_page(driver, timeout=10):
        """Aguarda página estabilizar (útil para Streamlit)"""
        from selenium.webdriver.support.ui import WebDriverWait
        
        def page_stable(driver):
            # Verifica se não há elementos de loading
            loading_elements = driver.find_elements(By.CSS_SELECTOR, ".stSpinner")
            return len(loading_elements) == 0
        
        wait = WebDriverWait(driver, timeout)
        return wait.until(page_stable)