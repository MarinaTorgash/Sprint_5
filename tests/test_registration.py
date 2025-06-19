from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegistrationPageLocators
from locators import LoginPageLocators
from urls import Urls


class TestRegistration:

    def test_registration_with_valid_data_successful(self, generate_name, generate_email, generate_password, driver):
        driver.get(Urls.REGISTER_PAGE)

        driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys(generate_name)
        driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(generate_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(generate_password)

        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))

        assert driver.current_url == Urls.LOGIN_PAGE


    def test_registration_with_short_password_fails_with_error(self, generate_name, generate_email, generate_password_incorrect, driver):
        driver.get(Urls.REGISTER_PAGE)

        driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys(generate_name)
        driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(generate_email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(generate_password_incorrect)

        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        error_message = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(RegistrationPageLocators.ERROR_MESSAGE)
        )

        assert error_message.text == "Некорректный пароль"
