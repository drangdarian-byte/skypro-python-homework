from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter(self, locator, value):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(value)


class LoginPage(BaseShopPage):
    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.enter((By.ID, "user-name"), username)
        self.enter((By.ID, "password"), password)
        self.click((By.ID, "login-button"))


class MainShopPage(BaseShopPage):
    def add_product(self, product_id):
        self.click((By.ID, f"add-to-cart-{product_id}"))

    def go_to_cart(self):
        self.click((By.CSS_SELECTOR, ".shopping_cart_link"))


class CartPage(BaseShopPage):
    def get_product_names(self):
        items = self.wait.until(EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "inventory_item_name")
        ))
        return [item.text for item in items]

    def checkout(self):
        self.click((By.ID, "checkout"))


class CheckoutPage(BaseShopPage):
    def fill_customer(self, first_name, last_name, postal_code):
        self.enter((By.ID, "first-name"), first_name)
        self.enter((By.ID, "last-name"), last_name)
        self.enter((By.ID, "postal-code"), postal_code)

    def continue_checkout(self):
        self.click((By.ID, "continue"))

    def get_total(self):
        element = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".summary_total_label")
        ))
        return element.text
