# Sprint_5

Stellar Burgers — Тесты для автотестирования
Описание
Этот проект содержит автоматизированные тесты для проверки функциональности веб-приложения Stellar Burgers. 
В тестах используется:

Python
Pytest
Selenium WebDriver
Faker (для генерации тестовых данных)

Регистрация:
1. test_registration_with_valid_data_successful - Успешная регистрация при введенных валидных данных
2. test_registration_with_short_password_fails_with_error - Обработка ошибки короткого пароля

Вход:
1. test_login_via_main_page_login_button_with_valid_credentials_successful_authorization - Вход через кнопку "Войти" на главной
2. test_login_via_personal_account_button_with_valid_credentials_successful_authorization -  Вход через кнопку "Личный кабинет"
3. test_login_via_signup_form_button_with_valid_credentials_successful_authorization -  Вход через ссылку на странице регистрации
4. test_login_via_login_button_on_password_recovery_page_valid_credentials_successful_authorization -  Вход через ссылку на странице восстановления пароля

Личный кабинет:
1. Переход в личный кабинет 
   1. test_authorized_user_can_go_to_personal_account - Переход в личный кабинет после авторизованного пользователя
   2. test_unauthorized_user_redirected_to_login_from_account_button - Переход в личный кабинет после неавторизованного пользователя
2. Переход из личного кабинета в конструктор:
   1. test_navigate_from_account_to_constructor_via_constructor_button - Переход в конструктор по клику на «Конструктор»
   2. test_navigate_from_account_to_constructor_via_logo Переход в конструктор по клику на логотип Stellar Burgers
3. Выход из аккаунта:
   1. test_logout_via_logout_button_in_personal_account - Выход из аккаунта из личного кабинета

Раздел «Конструктор»:

1. test_constructor_successful_buns_section_switch - Переход в раздел "Булки"
2. test_constructor_successful_sauces_section_switch - Переход в раздел "Соусы"
3. test_constructor_successful_fillings_section_switch - Переход в раздел "Начинки"



