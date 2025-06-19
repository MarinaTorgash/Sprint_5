# Sprint_5

Stellar Burgers — Тесты для автотестирования
Описание
Этот проект содержит автоматизированные тесты для проверки функциональности веб-приложения Stellar Burgers. 
В тестах используется:

Python
Pytest
Selenium WebDriver
Faker (для генерации тестовых данных)

1.1 test_constructor_successful_buns_section_switch Переход в раздел "Булки"
1.2 test_constructor_successful_sauces_section_switch Переход в раздел "Соусы"
1.3 test_constructor_successful_fillings_section_switch Переход в раздел "Начинки"
2.1 test_login_via_main_page_login_button... Вход через кнопку "Войти" на главной
2.2 test_login_via_personal_account_button... Вход через кнопку "Личный кабинет"
2.3 test_login_via_signup_form_button... Вход через ссылку на странице регистрации
2.4 test_login_via_login_button_on_password_recovery_page... Вход через ссылку на странице восстановления пароля
3.1 test_authorized_user_can_go_to_personal_account Переход в личный кабинет после входа
3.2 test_unauthorized_user_redirected_to_login_from_account_button Неавторизованный — перенаправление в /login
3.3 test_navigate_from_account_to_constructor_via_constructor_button Переход в конструктор через кнопку 
3.4 test_navigate_from_account_to_constructor_via_logo Переход в конструктор через логотип
3.5 test_logout_via_logout_button_in_personal_account Выход из аккаунта
4.1 test_registration_with_valid_data_successful Успешная регистрация
4.2 test_registration_with_short_password_fails_with_error Обработка ошибки короткого пароля


1. Тесты для переключения разделов конструктора
1.1 test_constructor_successful_buns_section_switch
Цель: Проверить возможность перехода к разделу "Булки".
Действия:
Открыть главную страницу.
Перейти в раздел "Начинки", затем — в раздел "Булки".
Прокрутить до заголовка "Булки".
Ожидаемый результат: Заголовок "Булки" отображается на странице.

1.2. test_constructor_successful_sauces_section_switch
Цель: Проверить возможность перехода к разделу "Соусы".
Действия:
Открыть главную страницу.
Перейти в раздел "Соусы".
Прокрутить до заголовка "Соусы".
Ожидаемый результат: Заголовок "Соусы" отображается на странице.

1.3. test_constructor_successful_fillings_section_switch
Цель: Проверить возможность перехода к разделу "Начинки".
Действия:
Открыть главную страницу.
Перейти в раздел "Начинки".
Прокрутить до заголовка "Начинки".
Ожидаемый результат: Заголовок "Начинки" отображается на странице.

2. Тесты авторизации пользователя
2.1. test_login_via_main_page_login_button_with_valid_credentials_successful_authorization
Цель: Авторизация через кнопку "Войти" на главной странице.
Действия:
Нажать "Личный кабинет".
Ввести email и пароль зарегистрированного пользователя.
Нажать "Войти".
Ожидаемый результат: Пользователь успешно вошёл (появляется кнопка "Оформить заказ", URL остаётся на главной).

2.2. test_login_via_personal_account_button_with_valid_credentials_successful_authorization
Цель: Авторизация через кнопку "Личный кабинет".
Действия:
Перейти в "Личный кабинет".
Ввести email и пароль.
Нажать "Войти".
Ожидаемый результат: Пользователь авторизован, находится на главной странице.

2.3. test_login_via_signup_form_button_with_valid_credentials_successful_authorization
Цель: Авторизация через ссылку "Войти" на странице регистрации.
Действия:
Перейти на страницу регистрации.
Нажать "Войти".
Ввести учетные данные.
Нажать "Войти".
Ожидаемый результат: Успешная авторизация, редирект на главную страницу.

2.4. test_login_via_login_button_on_password_recovery_page_valid_credentials_successful_authorization
Цель: Авторизация через ссылку "Войти" на странице восстановления пароля.
Действия:
Перейти на страницу восстановления пароля.
Нажать ссылку "Войти".
Ввести корректные учетные данные.
Нажать "Войти".
Ожидаемый результат: Пользователь авторизован, находится на главной странице.

3. Тесты работы с личным кабинетом
3.1. test_authorized_user_can_go_to_personal_account
Цель: Проверить переход в личный кабинет после авторизации.
Действия:
Авторизоваться.
Нажать "Личный кабинет".
Ожидаемый результат: URL = https://stellarburgers.nomoreparties.site/account/profile.

3.2. test_unauthorized_user_redirected_to_login_from_account_button
Цель: Проверить, что неавторизованный пользователь перенаправляется на страницу входа при нажатии "Личный кабинет".
Действия:
Нажать "Личный кабинет".
Ожидаемый результат: URL = https://stellarburgers.nomoreparties.site/login.

3.3. test_navigate_from_account_to_constructor_via_constructor_button
Цель: Проверить переход из личного кабинета в конструктор бургеров через кнопку "Конструктор".
Действия:
Авторизоваться.
Перейти в личный кабинет.
Нажать "Конструктор".
Ожидаемый результат: Находится на главной странице сайта (https://stellarburgers.nomoreparties.site/), 
видит кнопку "Оформить заказ".

3.4. test_navigate_from_account_to_constructor_via_logo
Цель: Проверить переход из личного кабинета в конструктор бургеров через логотип сайта.
Действия:
Авторизоваться.
Перейти в личный кабинет.
Нажать на логотип Stellar Burgers.
Ожидаемый результат: Находится на главной странице сайта, видит кнопку "Оформить заказ".

3.5. test_logout_via_logout_button_in_personal_account
Цель: Проверить выход из аккаунта через кнопку "Выход".
Действия:
Авторизоваться.
Перейти в личный кабинет.
Нажать "Выход".
Ожидаемый результат: Редирект на страницу входа (https://stellarburgers.nomoreparties.site/login).

4. Тесты регистрации пользователя

4.1. test_registration_with_valid_data_successful
Цель: Проверить успешную регистрацию пользователя с корректными данными.
Действия:
Заполнить форму регистрации:
Имя
Email
Пароль
Нажать "Зарегистрироваться".
Ожидаемый результат: Редирект на страницу входа (https://stellarburgers.nomoreparties.site/login).
5. 
4.2. test_registration_with_short_password_fails_with_error
Цель: Проверить обработку ошибки при регистрации с некорректным (слишком коротким) паролем.
Действия:
Заполнить форму регистрации с паролем менее 6 символов.
Нажать "Зарегистрироваться".
Ожидаемый результат: Отображение сообщения об ошибке: "Некорректный пароль".
