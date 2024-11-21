import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()

    try:
        yield driver
    finally:
        driver.quit()
