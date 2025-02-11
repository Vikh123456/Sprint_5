from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.all_locators import NAME_BUTTON, EMAIL_BUTTON, PASSWORD_BUTTON, REGISTER_BUTTON, WRONG_PASSWORD_BUTTON, \
    PASSWORD_RECOVER_BUTTON
from tests.base_test_class import BaseTestClass
from tests.conftest import browser


class TestRegisterPage(BaseTestClass):

    def test_success_register(self, browser):
        browser.get(self.register_page_url)
        name, email = self.get_random_string_and_email()
        password, _ = self.get_random_string_and_email()

        browser.find_element(By.XPATH, NAME_BUTTON).send_keys(name)
        browser.find_element(By.XPATH, EMAIL_BUTTON).send_keys(email)
        browser.find_element(By.XPATH, PASSWORD_BUTTON).send_keys(password)

        browser.find_element(By.XPATH, REGISTER_BUTTON).click()
        button = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, PASSWORD_RECOVER_BUTTON)))
        assert button.text == "Восстановить пароль"

        assert browser.current_url == self.login_page_url


    def test_wrong_password(self, browser):
        browser.get(self.register_page_url)
        name, email = self.get_random_string_and_email()
        password = name[:2]

        browser.find_element(By.XPATH, NAME_BUTTON).send_keys(name)
        browser.find_element(By.XPATH, EMAIL_BUTTON).send_keys(email)
        browser.find_element(By.XPATH, PASSWORD_BUTTON).send_keys(password)
        browser.find_element(By.XPATH, REGISTER_BUTTON).click()
        button = WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.XPATH, WRONG_PASSWORD_BUTTON)))
        assert button.text == "Некорректный пароль"
