from selenium.webdriver.common.by import By

class TestLocators:

    # Кнопки/ссылки
    REGISTRATION_BUTTON = (By.XPATH, "/html/body/div[1]/div/main/div/div/p[1]/a") #Ссылка "зарегистрироваться"
    LOGIN_BUTTON = (By.XPATH, "/html/body/div[1]/div/main/section[2]/div/button")  #Ссылка войти
    ACCOUNT_BUTTON = (By.XPATH, "/html/body/div[1]/div/header/nav/a") #Кнопка "личный кабинет"
    LOGIN_FROM_REGISTRATION = (By.XPATH, "/html/body/div[1]/div/main/div/div/p/a") #Ссылка "войти" в форме регистрации
    LOGIN_FROM_RECOVERY_PASSWORD = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a') #Ссылка "войти" в форме восстановления пароля
    RECOVERY_PASSWORD = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a') #Ссылка "восстановить пароль"
    MAIN_PAGE_LOGO = (By.XPATH, '//*[@id="root"]/div/header/nav/div/a') #Логотип на главной странице

    # Форма регистрации
    NAME_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input") #Строка ввода имени при регистрации
    EMAIL_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input") #Строка ввода имейла при регистрации
    PASSWORD_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input") #Строка ввода пароля при регистрации
    SUBMIT_REGISTRATION_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_button__24w6s') and contains(@class, 'Auth_form__35F1n')]") #Кнопка "Зарегистрироваться"
    ERROR_INCORRECT_PASSWORD_REGISTRATION = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p') #Ошибка после введения короткого пароля при регистрации

    # Форма входа
    EMAIL_FIELD_LOGIN = (By.XPATH, "/html/body/div[1]/div/main/div/form/fieldset[1]/div/div/input") #Строка ввода имейла при входе
    PASSWORD_FIELD_LOGIN = (By.XPATH, "/html/body/div[1]/div/main/div/form/fieldset[2]/div/div/input") #Строка ввода пароля при входе
    SUBMIT_LOGIN_BUTTON = (By.XPATH, "/html/body/div[1]/div/main/div/form/button") #Кнопка "Войти"

    # Профиль пользователя
    PROFILE_ICON = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[1]/a') #Кнопка "Профиль"
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button') #Кнопка "Выход"

    # Конструктор бургеров
    CONSTRUCTOR_BUTTON = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p") #Кнопка конструктора
    CONSTRUCT_BURGER = (By.XPATH, "//*[@id='root']/div/main/section[1]/h1") #Надпись "Соберите бургер"
    SUBMIT_ORDER = (By.XPATH, "//*[@id='root']/div/main/section[2]/div/button") #Кнопка "Оформить заказ"
    BREAD_BUTTON = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[1]") #Раздел "Булки"
    SAUCE_BUTTON = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]") #Раздел "Соусы"
    FILLINGS_BUTTON = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]") #Раздел "Начинки"
