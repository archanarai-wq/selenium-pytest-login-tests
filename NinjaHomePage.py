import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

driver=webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/")
driver.maximize_window()

driver.implicitly_wait(5)

#opened the phones window
driver.find_element(By.XPATH, "//a[text()='Phones & PDAs']").click()

#clicked on the iphone link
driver.find_element(By.XPATH, "//a[text()='iPhone']").click()

#taking the screenshot
driver.find_element(By.XPATH, "//ul[@class='thumbnails']/li[1]").click()
first_pic=driver.find_element(By.XPATH, "//button[@title='Next (Right arrow key)']")
for i in range(6):
    first_pic.click()
    time.sleep(2)
#driver.save_screenshot('screenshot.png' + str(random.randint(0,101)))
#closing the picture window
driver.find_element(By.XPATH, "//button[@title='Close (Esc)']").click()


#select two iphones.
#driver.find_element(By.ID, "input-quantity").clear()
#driver.find_element(By.ID, "input-quantity").send_keys("2")


#adding to cart iphones
#add_to_cart=driver.find_element(By.ID, "button-cart")
#add_to_cart.click()

#Laptops and selecting windows
driver.find_element(By.XPATH, "//a[text()='Laptops & Notebooks']").click()
driver.find_element(By.XPATH, "//a[text()='Show AllLaptops & Notebooks']").click()

#scrolling
driver.execute_script("window.scrollTo(0, 700);")

#selecting laptop HP LP3065
driver.find_element(By.XPATH, "//a[text()='HP LP3065']").click()

#changing laptop quantity
quantity=driver.find_element(By.ID, "input-quantity")
quantity.clear()
quantity.send_keys("3")

#selecting calendar
calendar=driver.find_element(By.XPATH, "//i[@class='fa fa-calendar']")
calendar.click()


#selecting 31st december, 2022
month_year=driver.find_element(By.XPATH, "//th[@class='picker-switch']")
next1=driver.find_element(By.XPATH, "//th[@class='next']")
while month_year.text != "December 2022":
    next1.click()

dates=driver.find_elements(By.XPATH, "//td[@class='day']")
for date in dates:
    if date.text == "31":
        date.click()

#add_to-cart of laptop
driver.find_element(By.ID, "button-cart").click()

#check_out button
driver.find_element(By.ID, "cart-total").click()
time.sleep(1)
checkout= driver.find_element(By.XPATH, '(//i[@class="fa fa-share"])[2]')
checkout.click()


#guest checkout button
driver.find_element(By.XPATH, "(//input[@type='radio'])[2]").click()

driver.find_element(By.ID, "button-account").click()

#scrolling
driver.execute_script("window.scrollBy(0,300)")
time.sleep(1)

#entering details
driver.find_element(By.ID, "input-payment-firstname").send_keys("Tom")
driver.find_element(By.ID, "input-payment-lastname").send_keys("Curry")
driver.find_element(By.ID, "input-payment-email").send_keys("tomcurry@gmail.com")
driver.find_element(By.ID, "input-payment-telephone").send_keys("123456")
driver.find_element(By.ID, "input-payment-address-1").send_keys("New York")
driver.find_element(By.ID, "input-payment-city").send_keys("Asparagus")
driver.find_element(By.ID, "input-payment-postcode").send_keys("321456")


#country selection
country=driver.find_element(By.ID, "input-payment-country")
dropdown=Select(country)
time.sleep(2)
dropdown.select_by_index(99)


#region selection
region=driver.find_element(By.ID, "input-payment-zone")
dropdown2=Select(region)
time.sleep(2)
dropdown2.select_by_visible_text('Bihar')
driver.find_element(By.ID, "button-guest").click()


#commenting
driver.find_element(By.XPATH, "//textarea[@name='comment']").send_keys("commented")
driver.find_element(By.ID, "button-shipping-method").click()


alert = driver.switch_to.alert
alert.accept()













time.sleep(2)