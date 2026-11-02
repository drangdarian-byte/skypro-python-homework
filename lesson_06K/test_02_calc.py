from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_slow_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 55)
    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        delay = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#delay")
        ))
        delay.clear()
        delay.send_keys("45")

        for text in ("7", "+", "8", "="):
            wait.until(EC.element_to_be_clickable((
                By.XPATH,
                (
                    "//span[contains(@class, 'btn') "
                    f"and normalize-space()='{text}']"
                )
            ))).click()

        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"
        ))
        assert driver.find_element(
            By.CSS_SELECTOR, ".screen"
        ).text.strip() == "15"
    finally:
        driver.quit()
