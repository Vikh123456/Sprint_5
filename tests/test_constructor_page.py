import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.all_locators import SAUCE_TAB, CONSTRUCTOR_SECTION, SPICY_X_SAUCE, TOPPINGS_TAB, SHELLFISH_MEAT
from tests.base_test_class import BaseTestClass
from tests.conftest import browser


class TestConstructorPage(BaseTestClass):

    def test_bun_sauce_and_toppings_click(self, browser):
        browser.get(self.main_page_url)
        constructor_section = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                               CONSTRUCTOR_SECTION)))
        assert constructor_section.is_displayed(), "Раздел конструктора бургеров отсутствует"

        sauce_tab = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, SAUCE_TAB))
        )
        sauce_tab.click()
        time.sleep(2)

        spicy_x_sauce = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, SPICY_X_SAUCE))
        )
        assert spicy_x_sauce.is_displayed(), "Скролл до раздела 'Соусы' не произошел"

        toppings_tab = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, TOPPINGS_TAB))
        )
        toppings_tab.click()

        shellfish_meat = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, SHELLFISH_MEAT))
        )
        assert shellfish_meat.is_displayed(), "Скролл до раздела 'Начинки' не произошел"
