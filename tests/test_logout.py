from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from locators import TestLocators
from conftest import driver

class TestLogout:

    #Тест выхода из профиля
    def test_logout_success(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.implicitly_wait(5)
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        driver.implicitly_wait(3)

        #Ввод email и пароля
        driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN).send_keys("olegandreev15123@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN).send_keys("123456")
        driver.find_element(*TestLocators.SUBMIT_LOGIN_BUTTON).click()
        driver.implicitly_wait(3)
        driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()

        try:
            WebDriverWait(driver, 5).until(expected_conditions.url_contains("/login"))
            assert "/login" in driver.current_url
        except TimeoutException:
            driver.quit()
