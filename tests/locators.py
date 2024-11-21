from selenium.webdriver.common.by import By

class TestLocators:

    #Кнопки/ссылки
    REGISTRATION_BUTTON = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and @href='/register' and text()='Зарегистрироваться']") #Ссылка "зарегистрироваться"
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_size_large__G21Vg') and text()='Войти в аккаунт']")  #Кнопка "войти в аккаунт"
    LOGOUT_BUTTON = (By.XPATH, "//li[@class='Account_listItem__35dAP']//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']")  # Кнопка "Выход"
    ACCOUNT_BUTTON = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and contains(p, 'Личный Кабинет')]") #Кнопка "личный кабинет"

    LOGIN_FROM_REGISTRATION = (By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login' and text()='Войти']") #Ссылка "войти"
    LOGIN_FROM_RECOVERY_PASSWORD = (By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login' and text()='Войти']")

    RECOVERY_PASSWORD = (By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/forgot-password' and text()='Восстановить пароль']") #Ссылка "восстановить пароль"
    MAIN_PAGE_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']") #Логотип на главной странице

    # Форма регистрации
    NAME_FIELD = (By.XPATH, "//input[@type='text' and @name='name']") #Строка ввода имени при регистрации
    EMAIL_FIELD = (By.XPATH, "//input[@type='text' and @name='name' and @value='']") #Строка ввода имейла при регистрации
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password' and @name='Пароль']") #Строка ввода пароля при регистрации
    SUBMIT_REGISTRATION_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Зарегистрироваться']") #Кнопка "Зарегистрироваться"
    ERROR_INCORRECT_PASSWORD_REGISTRATION = (By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']") #Ошибка после введения короткого пароля при регистрации

    # Форма входа
    EMAIL_FIELD_LOGIN = (By.XPATH, "//div[contains(@class, 'input_type_text') and contains(@class, 'input_size_default')]//input[@type='text' and @name='name']") #Строка ввода имейла при входе
    PASSWORD_FIELD_LOGIN = (By.XPATH, "//div[contains(@class, 'input_type_password') and contains(@class, 'input_size_default')]//input[@type='password' and @name='Пароль']") #Строка ввода пароля при входе
    SUBMIT_LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and text()='Войти']") #Кнопка "Войти"

    # Конструктор бургеров
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']") #Кнопка конструктора
    CONSTRUCT_BURGER = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']") #Надпись "Соберите бургер"
    SUBMIT_ORDER = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']") #Кнопка "Оформить заказ"
    BREAD_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Булки')]") #Раздел "Булки"
    SAUCE_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Соусы')]") #Раздел "Соусы"
    FILLINGS_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Начинки')]") #Раздел "Начинки"
