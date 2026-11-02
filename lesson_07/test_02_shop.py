from selenium import webdriver

from shop_pages import CartPage, CheckoutPage, LoginPage, MainShopPage


def test_shop_page_object():
    driver = webdriver.Firefox()
    try:
        login = LoginPage(driver)
        shop = MainShopPage(driver)
        cart = CartPage(driver)
        checkout = CheckoutPage(driver)

        login.open()
        login.login("standard_user", "secret_sauce")

        for product in (
            "sauce-labs-backpack",
            "sauce-labs-bolt-t-shirt",
            "sauce-labs-onesie",
        ):
            shop.add_product(product)

        shop.go_to_cart()
        cart.checkout()
        checkout.fill_customer("Алексей", "Иванов", "443000")
        checkout.continue_checkout()
        total = checkout.get_total()
    finally:
        driver.quit()

    assert total == "Total: $58.29"
