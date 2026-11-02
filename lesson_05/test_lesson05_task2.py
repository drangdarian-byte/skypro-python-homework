from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


FORM_URL = "https://httpbin.qa-territory.online/forms/post"


def test_form_submission():
    driver = webdriver.Chrome()
    try:
        driver.get(FORM_URL)
        original_url = driver.current_url

        name_field = driver.find_element(By.NAME, "custname")
        name_field.send_keys("Алексей")

        submit_button = driver.find_element(
            By.XPATH,
            "//button[contains(normalize-space(), 'Submit')]"
        )
        submit_button.click()

        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url != original_url
        )
        assert driver.current_url != original_url
    finally:
        driver.quit()
