from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.helpers import generate_unique_email, generate_password
from tests.locators import TestLocators

class TestRegistration:

    #Успешная регистрация
    def test_registration_success(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_PAGE_LOGO))

        cohort_number = 15
        password = generate_password(8)
        email = generate_unique_email(cohort_number)

        driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.NAME_FIELD))
        driver.find_element(*TestLocators.NAME_FIELD).send_keys('Олег')
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*TestLocators.SUBMIT_REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.url_contains("/login"))
        assert "/login" in driver.current_url

    #Ошибка при регистрации из-за некорректного пароля
    def test_registration_fail_incorrect_password(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_PAGE_LOGO))

        cohort_number = 15
        password = generate_password(4)
        email = generate_unique_email(cohort_number)

        driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.NAME_FIELD))
        driver.find_element(*TestLocators.NAME_FIELD).send_keys('Олег')
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*TestLocators.SUBMIT_REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.ERROR_INCORRECT_PASSWORD_REGISTRATION))
        assert driver.find_element(*TestLocators.ERROR_INCORRECT_PASSWORD_REGISTRATION).text == 'Некорректный пароль'
