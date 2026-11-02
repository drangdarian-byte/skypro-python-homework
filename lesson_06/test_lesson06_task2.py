
import json
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


BASE_URL = "https://gitflic.ru/"
PROFILE_1 = BASE_URL + "user/darian1926"
PROFILE_2 = BASE_URL + "user/darian192630"


def load_cookie(filename):
    path = Path.home() / filename
    return json.loads(path.read_text(encoding="utf-8"))


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get(BASE_URL)

        # Авторизация первого пользователя
        driver.delete_all_cookies()
        driver.add_cookie(load_cookie("gitflic_user1.json"))
        driver.refresh()

        driver.get(PROFILE_1)
        wait.until(lambda d: d.current_url.startswith(PROFILE_1))
        url_1 = driver.current_url

        # Выход из первого аккаунта
        driver.get(BASE_URL)
        driver.delete_all_cookies()
        driver.refresh()

        # Авторизация второго пользователя
        driver.add_cookie(load_cookie("gitflic_user2.json"))
        driver.refresh()

        driver.get(PROFILE_2)
        wait.until(lambda d: d.current_url.startswith(PROFILE_2))
        url_2 = driver.current_url

        # Проверка различий
        assert url_1 != url_2

    finally:
        driver.quit()
