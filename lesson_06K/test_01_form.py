from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_form_validation():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 15)
    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

        fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro",
        }
        for field_id, value in fields.items():
            wait.until(EC.visibility_of_element_located(
                (By.NAME, field_id)
            )).send_keys(value)

        # Zip code намеренно оставляем пустым.
        assert driver.find_element(By.NAME, "zip-code").get_attribute(
            "value"
        ) == ""

        wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type='submit']")
        )).click()

        zip_code = wait.until(EC.visibility_of_element_located(
            (By.ID, "zip-code")
        ))
        assert "alert-danger" in zip_code.get_attribute("class")

        for field_id in fields:
            field = driver.find_element(By.ID, field_id)
            assert "alert-success" in field.get_attribute("class"), (
                f"Поле {field_id} не подсвечено зелёным"
            )
    finally:
        driver.quit()
