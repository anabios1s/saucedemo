from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_add_product_to_cart(driver, wait):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    product = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bike Light']/ancestor::div[@class='inventory_item']")
    product_name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
    product_price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
    product.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "inventory_list")))
    cart_product_name = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    cart_product_price = driver.find_element(By.CLASS_NAME, "inventory_item_price").text

    assert cart_product_name == product_name, "Название товара не соответствует!"
    assert cart_product_price == product_price, "Цена товара изменилась!"
