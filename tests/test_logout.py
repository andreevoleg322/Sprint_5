from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from tests.locators import TestLocators

class TestLogout:

    #Тест выхода из профиля
    def test_logout_success(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_PAGE_LOGO))
        driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.EMAIL_FIELD_LOGIN))

        #Ввод email и пароля
        driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN).send_keys("olegandreev15123@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN).send_keys("123456")
        driver.find_element(*TestLocators.SUBMIT_LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.ACCOUNT_BUTTON))
        driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.LOGOUT_BUTTON))
        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_contains("/login"))
        assert "/login" in driver.current_url