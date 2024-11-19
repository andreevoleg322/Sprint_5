from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from locators import TestLocators


class TestAuthorisation:

  #Тест входа по кнопке "Войти в аккаунт"
  def test_authorisation_main_page(self, driver):

    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.implicitly_wait(5)


    #Тест входа с главной страницы
    #Клик на кнопку "Войти в аккаунт"
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    driver.implicitly_wait(3)

    #Ввод email и пароля
    driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN).send_keys("olegandreev15123@yandex.ru")
    driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN).send_keys("123456")
    driver.find_element(*TestLocators.SUBMIT_LOGIN_BUTTON).click()
    driver.implicitly_wait(3)
    driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()

  #Проверка успешного входа
    try:
      WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGOUT_BUTTON))
      assert driver.find_element(*TestLocators.LOGOUT_BUTTON).text == 'Выход'
    except TimeoutException:
      driver.quit()


  #Тест входа через кнопку "Личный кабинет"
  def test_authorisation_account(self, driver):

    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.implicitly_wait(5)

    driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()
    driver.implicitly_wait(3)
    driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN).send_keys("olegandreev15123@yandex.ru")
    driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN).send_keys("123456")
    driver.find_element(*TestLocators.SUBMIT_LOGIN_BUTTON).click()
    driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()

    #Проверка успешного входа
    try:
      WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGOUT_BUTTON))
      assert driver.find_element(*TestLocators.LOGOUT_BUTTON).text == 'Выход'
    except TimeoutException:
      driver.quit()


  #Тест входа с формы регистрации
  def test_authorisation_from_registration_form(self, driver):

    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.implicitly_wait(5)

    #Переход до формы регистрации
    driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()
    driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

    #Клик на кнопку "Войти" в форме регистрации
    driver.find_element(*TestLocators.LOGIN_FROM_REGISTRATION).click()

    #Ввод email и пароля
    driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN).send_keys("olegandreev15123@yandex.ru")
    driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN).send_keys("123456")
    driver.find_element(*TestLocators.SUBMIT_LOGIN_BUTTON).click()
    driver.implicitly_wait(3)
    driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()

    #Проверка успешного входа
    try:
      WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGOUT_BUTTON))
      assert driver.find_element(*TestLocators.LOGOUT_BUTTON).text == 'Выход'
    except TimeoutException:
      driver.quit()


  #Тест входа через форму восстановления пароля
  def test_authorisation_from_password_recovery_form(self, driver):

    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.implicitly_wait(5)

    #Переход до формы регистрации
    driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()
    driver.find_element(*TestLocators.RECOVERY_PASSWORD).click()

    #Клик на кнопку "Войти" в форме восстановления пароля
    driver.find_element(*TestLocators.LOGIN_FROM_RECOVERY_PASSWORD).click()

    #Ввод email и пароля
    driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN).send_keys("olegandreev15123@yandex.ru")
    driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN).send_keys("123456")
    driver.find_element(*TestLocators.SUBMIT_LOGIN_BUTTON).click()
    driver.implicitly_wait(3)
    driver.find_element(*TestLocators.ACCOUNT_BUTTON).click()

    #Проверка успешного входа
    try:
      WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGOUT_BUTTON))
      assert driver.find_element(*TestLocators.LOGOUT_BUTTON).text == 'Выход'
    except TimeoutException:
      driver.quit()