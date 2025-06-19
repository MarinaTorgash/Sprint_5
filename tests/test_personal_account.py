from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import PersonalPageLocators
from locators import MainPageLocators
from locators import LoginPageLocators

def test_authorized_user_can_go_to_personal_account(authorization_user):
    user = {}
    user.update(authorization_user)

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(user['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(user['password'])

    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((MainPageLocators.ORDER_BUTTON)))

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((PersonalPageLocators.SAVE_BUTTON)))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
    driver.quit()

def test_unauthorized_user_redirected_to_login_from_account_button():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((LoginPageLocators.LOGIN_BUTTON)))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    driver.quit()

def test_navigate_from_account_to_constructor_via_constructor_button(authorization_user):
    user = {}
    user.update(authorization_user)

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(user['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(user['password'])

    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((MainPageLocators.ORDER_BUTTON)))

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((PersonalPageLocators.SAVE_BUTTON)))

    driver.find_element(*PersonalPageLocators.CONSTRUCTOR).click()
    button = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((MainPageLocators.ORDER_BUTTON)))

    assert button.text == 'Оформить заказ' and driver.current_url == "https://stellarburgers.nomoreparties.site/"
    driver.quit()

def test_navigate_from_account_to_constructor_via_logo(authorization_user):
    user = {}
    user.update(authorization_user)

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(user['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(user['password'])

    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((MainPageLocators.ORDER_BUTTON)))

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((PersonalPageLocators.SAVE_BUTTON)))

    driver.find_element(*PersonalPageLocators.LOGO_STELLAR_BURGERS).click()
    button = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((MainPageLocators.ORDER_BUTTON)))

    assert button.text == 'Оформить заказ' and driver.current_url == "https://stellarburgers.nomoreparties.site/"
    driver.quit()

def test_logout_via_logout_button_in_personal_account(authorization_user):
    user = {}
    user.update(authorization_user)

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")

    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(user['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(user['password'])

    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((MainPageLocators.ORDER_BUTTON)))

    driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((PersonalPageLocators.SAVE_BUTTON)))

    driver.find_element(*PersonalPageLocators.EXIT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((LoginPageLocators.LOGIN_BUTTON)))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    driver.quit()