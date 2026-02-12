import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPg:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver, 5)
        self.username_input=(By.XPATH, "//input[@placeholder='Username']")
        self.password_input=(By.XPATH, "//input[@placeholder='Password']")
        self.login_button=(By.XPATH, "//input[@type='submit']")

    def username(self,text):
        username=self.driver.find_element(*self.username_input)
        username.send_keys(text)

    def password(self,text):
        password=self.driver.find_element(*self.password_input)
        password.send_keys(text)

    def login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button))
        login=self.driver.find_element(*self.login_button)
        login.click()
        time.sleep(1)

