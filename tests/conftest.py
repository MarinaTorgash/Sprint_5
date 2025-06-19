import pytest
import random
from faker import Faker
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegistrationPageLocators
from locators import LoginPageLocators

faker = Faker()
fake = Faker('ru_RU')

@pytest.fixture
def generate_name():
    return fake.first_name()

@pytest.fixture
def generate_email():
    name = "marina"
    last_name = "torgash"
    number = random.randint(100, 999)
    return f"{name}{last_name}24{number}@yandex.ru"

@pytest.fixture
def generate_password():
    return faker.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)

@pytest.fixture
def generate_password_incorrect():
    return faker.password(length=4, special_chars=True, digits=True, upper_case=True, lower_case=True)

@pytest.fixture
def authorization_user(generate_name, generate_email, generate_password):
    user = {}
    user['name'] = generate_name
    user['email'] = generate_email
    user['password'] = generate_password

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys(user['name'])
    driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(user['email'])
    driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(user['password'])

    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((LoginPageLocators.LOGIN_BUTTON)))
    driver.quit()
    return user
