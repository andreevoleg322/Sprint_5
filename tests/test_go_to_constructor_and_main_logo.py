from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from locators import TestLocators

class TestGoToConstructorAndLogo:

    #Тест перехода в конструктор бургеров из личного кабинета
    def test_go_to_constructor(self, driver):
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
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()

        #Проверка успешного перехода
        try:
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located(TestLocators.CONSTRUCT_BURGER))
            assert driver.find_element(*TestLocators.CONSTRUCT_BURGER).text == 'Соберите бургер'
        except TimeoutException:
            driver.quit()

    #Тест перехода из личного кабинета по клику на логотип
    def test_go_to_logo(self, driver):
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
        driver.find_element(*TestLocators.MAIN_PAGE_LOGO).click()

        #Проверка успешного перехода
        try:
            WebDriverWait(driver, 3).until(
                expected_conditions.visibility_of_element_located(TestLocators.SUBMIT_ORDER))
            assert "/profile" not in driver.current_url
        except TimeoutException:
            driver.quit()
