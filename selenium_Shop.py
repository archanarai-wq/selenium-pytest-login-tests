#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")


def test_Shop():
    driver.find_element(By.XPATH, "(//a[@class='nav-link'])[2]").click()

    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

    for product in products:
        name = product.find_element(By.XPATH, "div/h4/a").text
        if name in ["Nokia Edge", "Samsung Note 8"]:
            product.find_element(By.XPATH, "div/button").click()

    #driver.find_element(By.XPATH, "//span[@class='navbar-toggler-icon']").click()

    driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

    driver.find_element(By.ID, "country").send_keys("ind")

    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    driver.find_element(By.LINK_TEXT, "India").click()

    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.CSS_SELECTOR, "[type= 'submit']").click()
    successText = driver.find_element(By.CLASS_NAME, 'alert-success').text
    assert "Success! Thank you!" in successText
    driver.close()
