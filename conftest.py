import time

import pytest
from selenium import webdriver

from Login.test_valid import LoginPg


@pytest.fixture
def  driver(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    print(driver.title)
    print(driver.current_url)

    yield driver
    driver.quit()

@pytest.fixture
def valid_login(driver):
    logged_in = LoginPg(driver)
    logged_in.username("standard_user")
    logged_in.password("secret_sauce")
    logged_in.login()
    time.sleep(10)
