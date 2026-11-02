from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


SCREENSHOT = Path.cwd() / "lesson06_dynamic_loading.png"


def test_dynamic_loading():
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
        wait = WebDriverWait(driver, 15)
        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
        ).click()
        message = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
        )
        assert driver.save_screenshot(str(SCREENSHOT))
        assert message.text == "Hello World!"
    finally:
        driver.quit()
