from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.all_locators import (ENTER_TO_ACCOUNT_BUTTON, CREATE_ORDER_BUTTON, PERSONAL_ACCOUNT_BUTTON,
                                   ENTER_BUTTON_ON_REGISTRATION, \
                                   PASSWORD_RECOVER_BUTTON, RECOVER_TEXT_PLACE, LOGIN_EMAIL_BUTTON, \
                                   LOGIN_PASSWORD_BUTTON, LOGIN_SUBMIT_BUTTON, RECOVER_PASSWORD_BUTTON)
from tests.base_test_class import BaseTestClass
from tests.conftest import browser


class TestEnterPage(BaseTestClass):

    def fill_form_and_check_authorization(self, browser):
        email, password = self.registered_user

        browser.find_element(By.XPATH, LOGIN_EMAIL_BUTTON).send_keys(email)
        browser.find_element(By.XPATH, LOGIN_PASSWORD_BUTTON).send_keys(password)
        browser.find_element(By.XPATH, LOGIN_SUBMIT_BUTTON).click()

        button = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, CREATE_ORDER_BUTTON)))
        assert button.text == "Оформить заказ"
        assert browser.current_url == self.main_page_url


    def test_authorization_via_account_enter(self, browser):
        browser.get(self.main_page_url)

        browser.find_element(By.XPATH, ENTER_TO_ACCOUNT_BUTTON).click()
        self.fill_form_and_check_authorization(browser)


    def test_authorization_via_personal_account(self, browser):
        browser.get(self.main_page_url)

        browser.find_element(By.CSS_SELECTOR, PERSONAL_ACCOUNT_BUTTON).click()
        self.fill_form_and_check_authorization(browser)

    def test_authorization_via_register(self, browser):
        browser.get(self.register_page_url)

        browser.find_element(By.XPATH, ENTER_BUTTON_ON_REGISTRATION).click()
        self.fill_form_and_check_authorization(browser)

    def test_authorization_via_password_recover(self, browser):
        browser.get(self.login_page_url)
        email, _ = self.registered_user

        browser.find_element(By.XPATH, PASSWORD_RECOVER_BUTTON).click()
        browser.find_element(By.XPATH, LOGIN_EMAIL_BUTTON).send_keys(email)
        browser.find_element(By.XPATH, RECOVER_PASSWORD_BUTTON).click()

        button = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, RECOVER_TEXT_PLACE)))
        assert button.text == "Восстановление пароля"
