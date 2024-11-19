import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--window-size=640x480')
    driver = webdriver.Chrome()

    try:
        yield driver
    finally:
        driver.quit()
