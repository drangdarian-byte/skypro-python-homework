from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


BASE_URL = "https://httpbin.qa-territory.online"


def test_navigation():
    driver = webdriver.Chrome()
    try:
        driver.get(BASE_URL)
        original_url = driver.current_url

        # В разных частях задания ссылка названа HTML Form / HTML Forms.
        links = driver.find_elements(By.LINK_TEXT, "HTML Form")
        if not links:
            links = driver.find_elements(By.LINK_TEXT, "HTML Forms")
        assert links, "Не найдена ссылка HTML Form(s)"
        links[0].click()

        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.endswith("/forms/post")
        )
        assert driver.current_url.endswith("/forms/post")

        driver.back()
        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url == original_url
        )
        assert driver.current_url == original_url
    finally:
        driver.quit()
