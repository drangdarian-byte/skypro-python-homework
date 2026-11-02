from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_shop_total():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 20)
    total = None

    try:
        driver.get("https://www.saucedemo.com/")
        wait.until(EC.visibility_of_element_located(
            (By.ID, "user-name")
        )).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        wait.until(EC.element_to_be_clickable(
            (By.ID, "login-button")
        )).click()

        products = (
            "sauce-labs-backpack",
            "sauce-labs-bolt-t-shirt",
            "sauce-labs-onesie",
        )
        for product in products:
            wait.until(EC.element_to_be_clickable(
                (By.ID, f"add-to-cart-{product}")
            )).click()

        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".shopping_cart_link")
        )).click()
        wait.until(EC.element_to_be_clickable(
            (By.ID, "checkout")
        )).click()

        wait.until(EC.visibility_of_element_located(
            (By.ID, "first-name")
        )).send_keys("Алексей")
        driver.find_element(By.ID, "last-name").send_keys("Иванов")
        driver.find_element(By.ID, "postal-code").send_keys("443000")
        wait.until(EC.element_to_be_clickable(
            (By.ID, "continue")
        )).click()

        total = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".summary_total_label")
        )).text
    finally:
        driver.quit()

    assert total is not None
    assert total.split("$")[-1] == "58.29", (
        f"Ожидалось $58.29, фактически: {total}"
    )
