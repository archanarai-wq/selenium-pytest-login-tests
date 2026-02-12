import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class InvalidLog:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,5)
        self.username_input=(By.XPATH, "//input[@placeholder='Username']")
        self.password_input=(By.XPATH, "//input[@placeholder='Password']")
        self.login_button=(By.XPATH, "//input[@type='submit']")
        self.message=(By.XPATH, "//h3[@data-test='error']")

    def neg_username(self,text):
        username=self.driver.find_element(*self.username_input)
        username.send_keys(text)

    def neg_password(self,text):
        password=self.driver.find_element(*self.password_input)
        password.send_keys(text)

    def neg_login(self):
        login=self.driver.find_element(*self.login_button)
        login.click()
        msg=self.driver.find_element(*self.message)
        assert "Sorry" in msg.text
        print("Wrong username or password")
        time.sleep(1)
