import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.delete_all_cookies()
    driver.quit()
