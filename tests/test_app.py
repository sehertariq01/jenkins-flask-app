from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_homepage():
    options = Options()

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    driver.get("http://172.17.0.1:5000")

    assert "Jenkins CI/CD Assignment Working!" in driver.page_source

    driver.quit()
