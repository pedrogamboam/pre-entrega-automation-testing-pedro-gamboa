import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import iniciar_driver, login

@pytest.fixture
def driver():
    driver = iniciar_driver()
    yield driver
    driver.quit()

def test_login(driver):
    login(driver)
    assert "/inventory.html" in driver.current_url
    titulo = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo == "Products"

def test_inventario(driver):
    login(driver)
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0

def test_carrito(driver):
    login(driver)
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert badge.text == "1"
