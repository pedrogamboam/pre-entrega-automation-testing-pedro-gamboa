from selenium import webdriver
from selenium.webdriver.common.by import By

def iniciar_driver():
    """
    Inicializa el navegador Chrome y lo devuelve.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def login(driver, usuario="standard_user", clave="secret_sauce"):
    """
    Realiza el login en SauceDemo con credenciales por defecto.
    """
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(clave)
    driver.find_element(By.ID, "login-button").click()

