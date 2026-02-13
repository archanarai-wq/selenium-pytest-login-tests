import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#
# class AddToCart:
#     def __init__(self,driver):
#         self.driver=driver
#         self.wait=WebDriverWait(driver,10)
#         #self.add_to_cart_button=(By.XPATH, "//button[contains(@class,'btn_inventory')]")
#         #self.cart_badge=(By.XPATH, "//a[@class='shopping_cart_link']")
#         self.cart_count=(By.XPATH, "//div[@class='cart_item']")
#         self.add_to_cart_button = (By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory ']")
#         self.cart_click = (By.XPATH, "//a[@class='shopping_cart_link']")
# #
# # #def add_to_cart(self,n):
# #  #   for _ in range(n):
# #   #      button = self.wait.until(
# #    #         EC.element_to_be_clickable(
# #     #            (By.XPATH, "//button[starts-with(@data-test,'add-to-cart')]")
# #      #       )
# #       #  )
# #        # button.click()
# #     def add_to_cart(self, n):
# #         buttons = self.wait.until(
# #             EC.presence_of_all_elements_located())
# #
# #         for i in range(n):
# #             buttons[i].click()
# #
# #     #def check_badge(self,n):
# #         #check_badge=int(self.driver.find_element(*self.cart_badge).text)
# #      #   self.driver.find_element(*self.cart_badge).click()
# #       #  cart_items_count = len(self.driver.find_elements(*self.cart_count))
# #        # assert cart_items_count == n
# #         #print(n, " items added to cart")
# #         #time.sleep(1)
# #     def check_badge(self, n):
# #         self.wait.until(
# #             EC.element_to_be_clickable(self.cart_badge)
# #         ).click()
# #
# #         cart_items = self.wait.until(
# #             EC.presence_of_all_elements_located(self.cart_count)
# #         )
# #
# #         cart_items_count = len(cart_items)
# #
# #         assert cart_items_count == n
# #         print(n, " items added to cart")
#     def add_to_cart(self, n):
#         add_to_cart = self.driver.find_elements(*self.add_to_cart_button)
#         for i in range(n):
#             add_to_cart[i].click()
#             time.sleep(5)
#
#     def cart(self):
#         self.wait.until(EC.element_to_be_clickable(self.cart_click)).click()
#         time.sleep(5)
#
#
#
#
class AddToCart:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.items = (By.XPATH, "//div[@class='inventory_item']")
        self.name = (By.XPATH, ".//div[@class='inventory_item_name']")
        self.price = (By.XPATH, ".//div[@class='inventory_item_price']")
        self.sort_drop = (By.CLASS_NAME, "product_sort_container")
        # self.items=(By.XPATH,".//div[@class='inventory_item']")
        #self.firstitemfound = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        #self.seconditemfound = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
        self.add_to_cart_button = (By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory ']")
        self.cart_click = (By.XPATH, "//a[@class='shopping_cart_link']")

    def sort_products(self, visible_text):
        select = Select(self.driver.find_element(*self.sort_drop))
        select.select_by_visible_text(visible_text)

    def get_all_prices(self):
        elements = self.driver.find_elements(*self.items)
        price_list = []
        for p in elements:
            price_element = p.find_element(*self.price)
            raw_text = price_element.text
            clean_text = raw_text.replace('$', '')
            numeric_price = float(clean_text)
            price_list.append(numeric_price)
        return price_list

    time.sleep(5)

    def add_to_cart(self, n):
        # products = self.driver.find_elements(*self.items)
        # total_products = len(products)
        # print("Total products available:", total_products)
        # self.wait.until(EC.element_to_be_clickable(self.firstitemfound)).click()
        # time.sleep(1)
        # print("clicked")
        # self.wait.until(EC.element_to_be_clickable(self.seconditemfound)).click()
        # time.sleep(4)
        add_to_cart = self.driver.find_elements(*self.add_to_cart_button)
        for i in range(n):
            add_to_cart[i].click()
            time.sleep(5)

    def cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_click)).click()
        time.sleep(5)