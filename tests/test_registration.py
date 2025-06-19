from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from locators import RegistrationPageLocators
from locators import LoginPageLocators


def test_registration_with_valid_data_successful(generate_name, generate_email, generate_password):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys(generate_name)
    driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(generate_email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(generate_password)

    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((LoginPageLocators.LOGIN_BUTTON)))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
    driver.quit()


def test_registration_with_short_password_fails_with_error(generate_name, generate_email, generate_password_incorrect):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys(generate_name)
    driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(generate_email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(generate_password_incorrect)

    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    time.sleep(1)
    error_message = driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE)

    assert error_message.text == "Некорректный пароль"
    driver.quit()
