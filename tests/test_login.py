from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import MainPageLocators
from locators import LoginPageLocators
from locators import RegistrationPageLocators
from urls import Urls


class TestLogin:

    def test_login_via_main_page_login_button_with_valid_credentials_successful_authorization(self, authorization_user, driver):
        user = {}
        user.update(authorization_user)

        driver.get(Urls.MAIN_PAGE)

        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))

        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(user['password'])

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        button = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            MainPageLocators.ORDER_BUTTON))

        assert button.text == 'Оформить заказ' and driver.current_url == Urls.MAIN_PAGE

    def test_login_via_personal_account_button_with_valid_credentials_successful_authorization(self, authorization_user, driver):
        user = {}
        user.update(authorization_user)

        driver.get(Urls.MAIN_PAGE)

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))

        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(user['password'])

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        button = WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            MainPageLocators.ORDER_BUTTON))

        assert button.text == 'Оформить заказ' and driver.current_url == Urls.MAIN_PAGE

    def test_login_via_signup_form_button_with_valid_credentials_successful_authorization(self, authorization_user, driver):
        user = {}
        user.update(authorization_user)

        driver.get(Urls.REGISTER_PAGE)

        driver.find_element(*RegistrationPageLocators.LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))

        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(user['password'])

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        button = WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.ORDER_BUTTON))

        assert button.text == 'Оформить заказ' and driver.current_url == Urls.MAIN_PAGE

    def test_login_via_login_button_on_password_recovery_page_valid_credentials_successful_authorization(self, authorization_user, driver):
        user = {}
        user.update(authorization_user)

        driver.get(Urls.LOGIN_PAGE)

        driver.find_element(*LoginPageLocators.RESTORE_PASSWORD).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.RESTORE_BUTTON))

        driver.find_element(*LoginPageLocators.LOGIN_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))

        driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(user['password'])

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        button = WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.ORDER_BUTTON))

        assert button.text == 'Оформить заказ' and driver.current_url == Urls.MAIN_PAGE