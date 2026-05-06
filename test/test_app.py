from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

driver.get("http://host.docker.internal:5000")

assert "Jenkins" in driver.page_source
assert driver.title is not None

driver.quit()
