import pytest
from selenium import webdriver
from Login.validLogin import LoginPg


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/login")
    print(driver.title)
    print(driver.current_url)

    yield driver
    driver.quit()

@pytest.fixture
def seconddriver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    print(driver.title)
    print(driver.current_url)

    yield driver
    driver.quit()


@pytest.fixture
def valid_login(seconddriver):
    logged_in = LoginPg(seconddriver)
    logged_in.username("standard_user")
    logged_in.password("secret_sauce")
    logged_in.login()