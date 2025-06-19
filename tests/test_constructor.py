from locators import MainPageLocators
from urls import Urls
from data import DataConstructor


class TestConstruction:

    def test_constructor_successful_buns_section_switch(self, driver):
        driver.get(Urls.MAIN_PAGE)

        driver.find_element(*MainPageLocators.FILLING_BUTTON).click()
        driver.find_element(*MainPageLocators.BUN_BUTTON).click()

        element = driver.find_element(*MainPageLocators.BUNS)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        assert DataConstructor.SECTION_BUNS in element.text

    def test_constructor_successful_sauces_section_switch(self, driver):
        driver.get(Urls.MAIN_PAGE)

        driver.find_element(*MainPageLocators.SAUSE_BUTTON).click()

        element = driver.find_element(*MainPageLocators.SAUSES)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        assert DataConstructor.SECTION_SAUCES in element.text

    def test_constructor_successful_fillings_section_switch(self, driver):
        driver.get(Urls.MAIN_PAGE)

        driver.find_element(*MainPageLocators.FILLING_BUTTON).click()

        element = driver.find_element(*MainPageLocators.FILLINGS)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        assert DataConstructor.SECTION_FILLINGS in element.text
