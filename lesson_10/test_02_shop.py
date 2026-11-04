"""Allure-labelled SauceDemo checkout test."""
import allure
from selenium import webdriver

from lesson_10.shop_pages import (
    CartPage,
    CheckoutPage,
    LoginPage,
    MainShopPage,
)


@allure.title("SauceDemo: итоговая стоимость трёх товаров")
@allure.description(
    "Авторизация, добавление трёх товаров и проверка суммы заказа."
)
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_page_object() -> None:
    """Check the total price of three selected SauceDemo products."""
    driver = webdriver.Firefox()
    try:
        login = LoginPage(driver)
        shop = MainShopPage(driver)
        cart = CartPage(driver)
        checkout = CheckoutPage(driver)

        with allure.step("Открыть магазин и авторизоваться"):
            login.open()
            login.login("standard_user", "secret_sauce")
        with allure.step("Добавить три товара в корзину"):
            for product in (
                "sauce-labs-backpack",
                "sauce-labs-bolt-t-shirt",
                "sauce-labs-onesie",
            ):
                shop.add_product(product)
        with allure.step("Перейти в корзину и начать оформление"):
            shop.go_to_cart()
            cart.checkout()
        with allure.step("Заполнить данные покупателя"):
            checkout.fill_customer("Алексей", "Иванов", "443000")
            checkout.continue_checkout()
        with allure.step("Получить итоговую сумму заказа"):
            total = checkout.get_total()
        with allure.step("Проверить, что сумма равна $58.29"):
            assert total == "Total: $58.29"
    finally:
        driver.quit()
