import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class verification:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,5)
        self.sort_button=(By.XPATH, "//select[@class='product_sort_container']")

    def sorting(self,text):
        sort=self.driver.find_element(*self.sort_button)
        dropdown=Select(sort)
        time.sleep(1)
        dropdown.select_by_visible_text(text)
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,500)")


