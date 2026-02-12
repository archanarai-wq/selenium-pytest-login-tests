from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(10)
driver.maximize_window()
print(driver.title)
driver.find_element(By.XPATH, "(//input[@class='radioButton'])[2]").click()
driver.find_element(By.ID, "autocomplete").send_keys("In")



countries=driver.find_elements(By.CLASS_NAME, "ui-menu-item")
for country in countries:
    if country.text=="India":
        country.click()

driver.find_element(By.ID, "dropdown-class-example").click()
dropdown= Select(driver.find_element(By.ID, "dropdown-class-example"))
dropdown.select_by_visible_text("Option3")





