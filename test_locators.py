from selenium.webdriver.common.by import By


def test_basic_locators(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "shopping_cart_container")
    driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
    driver.find_element(By.CLASS_NAME, "bm-burger-button")
    driver.find_element(By.TAG_NAME, "select")
    driver.find_element(By.LINK_TEXT, "Sauce Labs Backpack")
    driver.find_element(By.PARTIAL_LINK_TEXT, "Bike Light")

def test_xpath_locators(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
    driver.find_element(By.XPATH, "//span[text()='Products']")
    driver.find_element(By.XPATH, "//button[contains(@id, 'sauce-labs-bike-light')]")
    driver.find_element(By.XPATH, "//div[contains(text(), 'Sauce Labs Bolt')]")
    driver.find_element(By.XPATH,"//div[text()='Sauce Labs Backpack']/ancestor::div[@class='inventory_item']")
    driver.find_element(By.XPATH, "//select[@class='product_sort_container' and @data-test='product-sort-container']")

def test_css_locators(driver):
    driver.get("https://www.saucedemo.com/")

    #поиск элемента по двум классам одновременно удался только на странице авторизации
    driver.find_element(By.CSS_SELECTOR, ".submit-button.btn_action")

    #авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.CSS_SELECTOR, ".bm-burger-button")
    driver.find_element(By.CSS_SELECTOR, ".header_secondary_container .title")
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    driver.find_element(By.CSS_SELECTOR, "select")
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link")

    driver.find_element( By.CSS_SELECTOR, "[id='add-to-cart-sauce-labs-bike-light']")
    driver.find_element(By.CSS_SELECTOR, "[class~='bm-burger-button']")
    driver.find_element(By.CSS_SELECTOR, "[data-test|='item-4-img']")
    driver.find_element(By.CSS_SELECTOR, "[class^='right']")
    driver.find_element(By.CSS_SELECTOR, "[id$='bike-light']")
    driver.find_element(By.CSS_SELECTOR, "[id*='opping_cart_con']")
