В файле locators.py - локаторы, потребовавшиеся для работы тестов
В файле helpers.py - генератор пароля и email
В файле conftest.py - фикстура драйвера
Тесты:

Регистрация
В файле test_registration.py:
test_registration_success - Успешная регистрация. Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен: имя_фамилия_номер когорты_любые 3 цифры@домен. Минимальный пароль — шесть символов.
test_registration_fail_incorrect_password - Ошибка регистрации с некорректным паролем(меньше шести символов).

Вход
В файле test_authorisation.py:
test_authorisation_main_page - Вход по кнопке «Войти в аккаунт» на главной,
test_authorisation_account - Вход через кнопку «Личный кабинет»,
test_authorisation_from_registration_form - Вход через кнопку в форме регистрации,
test_authorisation_from_password_recovery_form - Вход через кнопку в форме восстановления пароля.

Переход в личный кабинет 
В файле test_go_to_account.py:
test_go_to_personal_account - Переход по клику на «Личный кабинет».

Переход из личного кабинета в конструктор 
В файле test_go_to_constructor_and_main_logo.py:
test_go_to_constructor - Переход по клику на «Конструктор» 
test_go_to_logo - Переход на главную страницу по клику на логотип Stellar Burgers.

Выход из аккаунта
В файле test_logout.py:
test_logout_success - Выход по кнопке «Выйти» в личном кабинете.

Раздел «Конструктор»
В файле test_constructor.py:
test_constructor - Проверка, что работают переходы к разделам «Булки», «Соусы», «Начинки».

Для запуска тестов ввести pytest -v .\tests#   S p r i n t _ 5 
 
 # Sprint_5
