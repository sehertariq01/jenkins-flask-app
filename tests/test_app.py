from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def setup_driver():
    options = Options()

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    return driver


# Test Case 1
def test_homepage_text():
    driver = setup_driver()

    driver.get("http://172.17.0.1:5000")

    assert "Jenkins CI/CD Assignment Working!" in driver.page_source

    driver.quit()


# Test Case 2
def test_page_title():
    driver = setup_driver()

    driver.get("http://172.17.0.1:5000")

    assert driver.title is not None

    driver.quit()
