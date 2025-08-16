import pytest
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import time
import requests
from urllib.parse import urljoin

@pytest.fixture(scope="session")
def streamlit_app():
    """Inicia a aplicação Streamlit para os testes"""
    # Inicia o servidor Streamlit
    process = subprocess.Popen([
        "streamlit", "run", "app/main.py",
        "--server.port", "8501",
        "--server.headless", "true",
        "--browser.gatherUsageStats", "false"
    ])
    
    # Aguarda o servidor iniciar
    max_retries = 30
    for _ in range(max_retries):
        try:
            response = requests.get("http://localhost:8501")
            if response.status_code == 200:
                break
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    else:
        raise Exception("Falha ao iniciar o servidor Streamlit")
    
    yield "http://localhost:8501"
    
    # Encerra o processo
    process.terminate()
    process.wait()

@pytest.fixture
def driver():
    """Configura o driver do Selenium"""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    
    yield driver
    
    driver.quit()

@pytest.fixture
def wait():
    """WebDriverWait fixture"""
    def _wait(driver, timeout=10):
        return WebDriverWait(driver, timeout)
    return _wait

class StreamlitHelper:
    """Classe auxiliar para interações com Streamlit"""
    
    @staticmethod
    def wait_for_app_load(driver, wait_func):
        """Aguarda o carregamento completo da aplicação"""
        wait_func(driver).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='stSidebar']"))
        )
    
    @staticmethod
    def select_sidebar_option(driver, option_text):
        """Seleciona uma opção no sidebar"""
        sidebar = driver.find_element(By.CSS_SELECTOR, "[data-testid='stSidebar']")
        select_element = sidebar.find_element(By.TAG_NAME, "select")
        
        from selenium.webdriver.support.ui import Select
        select = Select(select_element)
        select.select_by_visible_text(option_text)
    
    @staticmethod
    def fill_form_field(driver, field_name, value):
        """Preenche um campo de formulário"""
        field = driver.find_element(By.CSS_SELECTOR, f"[data-testid='stTextInput'] input")
        field.clear()
        field.send_keys(value)
    
    @staticmethod
    def click_button(driver, button_text):
        """Clica em um botão pelo texto"""
        button = driver.find_element(By.XPATH, f"//button[contains(text(), '{button_text}')]")
        button.click()

@pytest.fixture
def streamlit_helper():
    """Fixture para helper do Streamlit"""
    return StreamlitHelper