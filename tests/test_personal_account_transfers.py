import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.all_locators import (NAME_BUTTON, EMAIL_BUTTON, REGISTER_BUTTON,
    ENTER_TO_ACCOUNT_BUTTON, PERSONAL_ACCOUNT_BUTTON, CONSTRUCTOR_BUTTON, BURGER_TEXT,
    LOGO_BURGERS_BUTTON, PROFILE_BUTTON, EXIT_BUTTON, ENTER_TEXT)
from tests.base_test_class import BaseTestClass
from tests.conftest import browser



class TestTransfersViaPages(BaseTestClass):

    def go_to_personal_account_page(self, browser):
        email, password = self.registered_user
        browser.find_element(By.XPATH, ENTER_TO_ACCOUNT_BUTTON).click()

        browser.find_element(By.XPATH, NAME_BUTTON).send_keys(email)
        browser.find_element(By.XPATH, EMAIL_BUTTON).send_keys(password)
        browser.find_element(By.XPATH, REGISTER_BUTTON).click()

        browser.find_element(By.XPATH, PERSONAL_ACCOUNT_BUTTON).click()

    def test_open_personal_account_page(self, browser):
        browser.get(self.main_page_url)
        self.go_to_personal_account_page(browser)

        WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, PROFILE_BUTTON)))
        assert browser.current_url == self.profile_page_url

    @pytest.mark.parametrize("button", [CONSTRUCTOR_BUTTON, LOGO_BURGERS_BUTTON])
    def test_open_personal_account_page_and_constructor_and_logo(self, browser, button):
        browser.get(self.main_page_url)
        self.go_to_personal_account_page(browser)

        browser.find_element(By.XPATH, button).click()
        button = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, BURGER_TEXT)))
        assert button.text == "Соберите бургер"
        assert browser.current_url == self.main_page_url

    def test_exit_from_account(self, browser):
        browser.get(self.main_page_url)
        self.go_to_personal_account_page(browser)

        exit_button = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, EXIT_BUTTON)))
        exit_button.click()
        button = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, ENTER_TEXT)))
        assert button.text == "Вход"
        assert browser.current_url == self.login_page_url
