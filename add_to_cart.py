import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddToCart:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,5)
        self.add_to_cart_button=(By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory ']")
        self.cart_badge=(By.XPATH, "//span[@data-test='shopping-cart-badge']")

    def add_to_cart(self,n):
        add_to_cart=self.driver.find_elements(*self.add_to_cart_button)
        for i in range(n):
            add_to_cart[i].click()
        time.sleep(2)

    def check_badge(self,n):
        check_badge=self.driver.find_element(*self.cart_badge)
        assert check_badge.text==n
        print(n, " items selected")
        time.sleep(1)




