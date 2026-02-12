import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.youtube.com/")

driver.maximize_window()

driver.implicitly_wait(5)

driver.find_element(By.XPATH, "//input[@class='ytSearchboxComponentInput yt-searchbox-input title']").send_keys("tmkoc episodes no")
driver.find_element(By.XPATH, "//button[@title='Search']").click()

time.sleep(5)



episodes=driver.find_elements(By.XPATH, "//yt-formatted-string[@class='style-scope ytd-video-renderer']")
for episode in episodes:
    if "597" in episode.text:
        episode.click()
        break

time.sleep(5)

driver.execute_script("window.scrollBy(0,800);")
time.sleep(3)

driver.find_element(By.ID, "simplebox-placeholder").click()
time.sleep(2)
driver.find_element(By.ID, "contenteditable-root").send_keys("Good")


