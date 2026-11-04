"""Allure-labelled slow calculator test."""
import allure
from selenium import webdriver

from lesson_10.calculator_page import CalculatorPage


@allure.title("Калькулятор: сложение 7 + 8")
@allure.description(
    "Проверка вычисления 7 + 8 с задержкой 45 секунд."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator_page_object() -> None:
    """Check that the calculator displays 15 for 7 + 8."""
    driver = webdriver.Chrome()
    try:
        page = CalculatorPage(driver)
        with allure.step("Открыть калькулятор"):
            page.open()
        with allure.step("Установить задержку 45 секунд"):
            page.set_delay(45)
        with allure.step("Ввести выражение 7 + 8"):
            for key in ("7", "+", "8", "="):
                page.press(key)
        with allure.step("Дождаться результата вычисления"):
            result = page.wait_for_result("15")
        with allure.step("Проверить, что результат равен 15"):
            assert result == "15"
    finally:
        driver.quit()
