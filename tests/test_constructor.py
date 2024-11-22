from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.locators import TestLocators

#Тест переходов к разделам "Булки", "Соусы" и "Начинки" в конструкторе
class TestConstructor:

    def test_constructor_bread(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.MAIN_PAGE_LOGO))

        #Проверяем, что на странице есть три раздела: "Булки", "Соусы" и "Начинки"
        driver.find_element(*TestLocators.BREAD_BUTTON)
        driver.find_element(*TestLocators.SAUCE_BUTTON)
        driver.find_element(*TestLocators.FILLINGS_BUTTON)

        assert driver.find_element(*TestLocators.BREAD_BUTTON).text == "Булки"
        assert driver.find_element(*TestLocators.SAUCE_BUTTON).text == "Соусы"
        assert driver.find_element(*TestLocators.FILLINGS_BUTTON).text == "Начинки"

        bread_button = driver.find_element(*TestLocators.BREAD_BUTTON)

        # Проверяем переключение между вкладками
        driver.execute_script("arguments[0].click();", bread_button)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.BREAD_BUTTON))
        assert bread_button.is_enabled()


    def test_constructor_sauces(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.MAIN_PAGE_LOGO))

        #Проверяем, что на странице есть три раздела: "Булки", "Соусы" и "Начинки"
        driver.find_element(*TestLocators.BREAD_BUTTON)
        driver.find_element(*TestLocators.SAUCE_BUTTON)
        driver.find_element(*TestLocators.FILLINGS_BUTTON)

        assert driver.find_element(*TestLocators.BREAD_BUTTON).text == "Булки"
        assert driver.find_element(*TestLocators.SAUCE_BUTTON).text == "Соусы"
        assert driver.find_element(*TestLocators.FILLINGS_BUTTON).text == "Начинки"

        sauce_button = driver.find_element(*TestLocators.SAUCE_BUTTON)

        # Проверяем переключение между вкладками
        driver.execute_script("arguments[0].click();", sauce_button)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.SAUCE_BUTTON))
        assert sauce_button.is_enabled()


    def test_constructor_fillings(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/")
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.BREAD_BUTTON))

        #Проверяем, что на странице есть три раздела: "Булки", "Соусы" и "Начинки"
        driver.find_element(*TestLocators.BREAD_BUTTON)
        driver.find_element(*TestLocators.SAUCE_BUTTON)
        driver.find_element(*TestLocators.FILLINGS_BUTTON)

        assert driver.find_element(*TestLocators.BREAD_BUTTON).text == "Булки"
        assert driver.find_element(*TestLocators.SAUCE_BUTTON).text == "Соусы"
        assert driver.find_element(*TestLocators.FILLINGS_BUTTON).text == "Начинки"

        fillings_button = driver.find_element(*TestLocators.FILLINGS_BUTTON)

        # Проверяем переключение между вкладками
        driver.execute_script("arguments[0].click();", fillings_button)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.FILLINGS_BUTTON))
        assert fillings_button.is_enabled()
