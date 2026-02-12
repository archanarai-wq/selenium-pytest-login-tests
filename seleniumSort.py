from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

Sorted=[]
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
originalBrowser=driver.find_elements(By.XPATH, "//tr/td[1]")


for ele in originalBrowser:
    Sorted.append(ele.text)

#copy() method is faster than the older slice() method
newSorted=Sorted.copy()

Sorted.sort()

assert Sorted == newSorted





