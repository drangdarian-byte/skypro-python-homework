from selenium import webdriver
from selenium.webdriver.common.by import By


LINKS_URL = "https://httpbin.qa-territory.online/links/10"


def test_multiple_elements():
    driver = webdriver.Chrome()
    try:
        driver.get(LINKS_URL)

        links = driver.find_elements(By.TAG_NAME, "a")
        assert len(links) == 9, f"Ожидалось 9 ссылок, найдено {len(links)}"

        for link in links:
            assert link.is_displayed(), "Найдена невидимая ссылка"

        assert "1" in links[0].text
    finally:
        driver.quit()
