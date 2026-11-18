import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)

@pytest.fixture
def driver():
    options = Options()

    # Отключаем менеджер паролей Chrome
    chrome_prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }

    options.add_experimental_option("prefs", chrome_prefs)

    # Настройки браузера
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()
