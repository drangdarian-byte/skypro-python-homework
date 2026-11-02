from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 55)

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, seconds):
        field = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        field.clear()
        field.send_keys(str(seconds))

    def press(self, value):
        button = self.wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//span[contains(@class, 'btn') "
            f"and normalize-space()='{value}']",
        )))
        button.click()

    def wait_for_result(self, expected):
        self.wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), str(expected)
        ))
        screen = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return screen.text.strip()
