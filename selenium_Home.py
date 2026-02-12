from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

def test_home():
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys("Archana Rai")
    driver.find_element(By.XPATH, "(//input[@name='email'])[1]").send_keys("archana.rai@cbnits.com")
    driver.find_element(By.ID, "exampleInputPassword1").send_keys("123archana")
    driver.find_element(By.ID, "exampleCheck1").click()
    dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
    dropdown.select_by_visible_text("Female")
    driver.find_element(By.XPATH, "(//input[@class='form-check-input'])[2]").click()
    driver.find_element(By.XPATH, "(//input[@class='btn btn-success'])").click()

