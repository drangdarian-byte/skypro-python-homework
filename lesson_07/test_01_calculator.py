from selenium import webdriver

from calculator_page import CalculatorPage


def test_calculator_page_object():
    driver = webdriver.Chrome()
    try:
        page = CalculatorPage(driver)
        page.open()
        page.set_delay(45)
        for key in ("7", "+", "8", "="):
            page.press(key)
        result = page.wait_for_result("15")
    finally:
        driver.quit()

    assert result == "15"
