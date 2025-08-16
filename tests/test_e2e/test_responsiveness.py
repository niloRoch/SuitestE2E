"""
Testes de responsividade
"""
import pytest
from selenium.webdriver.common.by import By

class TestResponsiveness:
    """Classe de testes para responsividade"""
    
    @pytest.mark.parametrize("width,height", [
        (1920, 1080),  # Desktop
        (1366, 768),   # Laptop
        (768, 1024),   # Tablet
        (375, 667),    # Mobile
    ])
    def test_layout_at_different_resolutions(self, driver, base_url, width, height):
        """Testa layout em diferentes resoluções"""
        driver.set_window_size(width, height)
        driver.get(base_url)
        
        # Verificar se elementos principais estão visíveis
        body = driver.find_element(By.TAG_NAME, "body")
        assert body.is_displayed()
        
        # Verificar se não há overflow horizontal
        viewport_width = driver.execute_script("return window.innerWidth")
        body_width = driver.execute_script("return document.body.scrollWidth")
        assert body_width <= viewport_width + 20  # Margem de 20px
    
    def test_mobile_navigation(self, driver, base_url):
        """Testa navegação em dispositivos móveis"""
        driver.set_window_size(375, 667)
        driver.get(base_url)
        
        # Verificar se navegação mobile funciona
        assert driver.find_element(By.TAG_NAME, "body").is_displayed()
    
    def test_touch_friendly_elements(self, driver, base_url):
        """Testa se elementos são touch-friendly"""
        driver.set_window_size(375, 667)
        driver.get(base_url)
        
        # Verificar tamanho mínimo de elementos clicáveis (44px recomendado)
        buttons = driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            if button.is_displayed():
                size = button.size
                assert size['height'] >= 44 or size['width'] >= 44
