"""Page Objects for the SauceDemo checkout flow."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Locator = tuple[str, str]


class BaseShopPage:
    """Common browser actions shared by shop pages."""

    def __init__(self, driver: WebDriver) -> None:
        """Initialize the page with a Selenium WebDriver."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click(self, locator: Locator) -> None:
        """Wait until the element is clickable, then click it."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter(self, locator: Locator, value: str) -> None:
        """Clear an input element and enter the supplied text."""
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(value)


class LoginPage(BaseShopPage):
    """Login screen actions."""

    def open(self) -> None:
        """Open the SauceDemo website."""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """Sign in with the supplied credentials."""
        self.enter((By.ID, "user-name"), username)
        self.enter((By.ID, "password"), password)
        self.click((By.ID, "login-button"))


class MainShopPage(BaseShopPage):
    """Product listing page actions."""

    def add_product(self, product_id: str) -> None:
        """Add the product with the specified HTML suffix to the cart."""
        self.click((By.ID, f"add-to-cart-{product_id}"))

    def go_to_cart(self) -> None:
        """Open the shopping cart."""
        self.click((By.CSS_SELECTOR, ".shopping_cart_link"))


class CartPage(BaseShopPage):
    """Shopping cart page actions."""

    def get_product_names(self) -> list[str]:
        """Return the visible names of products in the cart."""
        items = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )
        return [item.text for item in items]

    def checkout(self) -> None:
        """Proceed to the checkout form."""
        self.click((By.ID, "checkout"))


class CheckoutPage(BaseShopPage):
    """Customer information and checkout summary actions."""

    def fill_customer(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        """Fill customer first name, surname, and postal code."""
        self.enter((By.ID, "first-name"), first_name)
        self.enter((By.ID, "last-name"), last_name)
        self.enter((By.ID, "postal-code"), postal_code)

    def continue_checkout(self) -> None:
        """Proceed from customer information to the order summary."""
        self.click((By.ID, "continue"))

    def get_total(self) -> str:
        """Return the displayed total, including its label."""
        element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".summary_total_label")
            )
        )
        return element.text
