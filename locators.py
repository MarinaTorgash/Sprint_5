from selenium.webdriver.common.by import By

#Главная страница
class MainPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") # кнопка Войти в аккаунт
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # кнопка Оформить заказ
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")# кнопка Личный кабинет
    BUN_BUTTON = (By.XPATH, "//span[text()='Булки']/parent::div")# кнопка Булки
    SAUSE_BUTTON = (By.XPATH, "//span[text()='Соусы']/parent::div")# кнопка Соусы
    FILLING_BUTTON = (By.XPATH, "//span[text()='Начинки']/parent::div")# кнопка Начинки
    BUNS = (By.XPATH, "//h2[text()='Булки']")  # трока Булки
    SAUSES = (By.XPATH, "//h2[text()='Соусы']")  # строка Соусы
    FILLINGS = (By.XPATH, "//h2[text()='Начинки']") # строка Начинки

#Страница входа
class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") # кнопка Войти
    EMAIL_FIELD = (By.NAME, "name") # поле Email
    PASSWORD_FIELD = (By.NAME, "Пароль") # поле Пароль
    RESTORE_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")# ссылка Восстановить пароль около надписи: Забыли пароль?
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")# кнопка Восстановить на странице восстановления
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']") # ссылка Войти около надписи: Вспомнили пароль?

#Страница регистрации
class RegistrationPageLocators:
    NAME_FIELD = (By.XPATH, "//input[@name='name']") # поле Имя
    EMAIL_FIELD = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input") # поле Email
    PASSWORD_FIELD = (By.NAME, "Пароль") # поле Пароль
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # кнопка Зарегистрироваться
    ERROR_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']") # сообщение об ошибке пароля
    LOGIN = (By.XPATH, "//a[text()='Войти']") # ссылка Войти около надписи: Уже зарегистрированы?

#Личный кабинет
class PersonalPageLocators:
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']") # кнопка Выход
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']") # кнопка Сохранить
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']/parent::a") # Конструктор
    LOGO_STELLAR_BURGERS =  (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']") # Логотип сайта

