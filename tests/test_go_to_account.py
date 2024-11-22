from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.locators import TestLocators


class TestGoToAccount:

  #Тест перехода в личный кабинет по кнопке "Личный кабинет"
  def test_go_to_personal_account(self, driver):

    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.MAIN_PAGE_LOGO))

    #Клик на кнопку "Войти в аккаунт"
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.EMAIL_FIELD_LOGIN))

    #Ввод email и пароля
    driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN).send_keys("olegandreev15123@yandex.ru")
    driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN).send_keys("123456")
    driver.find_element(*TestLocators.SUBMIT_LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(TestLocators.ACCOUNT_BUTTON))
    driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()

    #Проверка успешного перехода в личный кабинет
    WebDriverWait(driver, 5).until(expected_conditions.url_contains("/profile"))
    assert "/profile" in driver.current_url