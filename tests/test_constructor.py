from selenium import webdriver
from locators import MainPageLocators

def test_constructor_successful_buns_section_switch():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*MainPageLocators.FILLING_BUTTON).click()
    driver.find_element(*MainPageLocators.BUN_BUTTON).click()

    element = driver.find_element(*MainPageLocators.BUNS)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    assert 'Булки' in element.text
    driver.quit()

def test_constructor_successful_sauces_section_switch():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*MainPageLocators.SAUSE_BUTTON).click()

    element = driver.find_element(*MainPageLocators.SAUSES)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    assert 'Соусы' in element.text
    driver.quit()

def test_constructor_successful_fillings_section_switch():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(*MainPageLocators.FILLING_BUTTON).click()

    element = driver.find_element(*MainPageLocators.FILLINGS)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    assert 'Начинки' in element.text
    driver.quit()
