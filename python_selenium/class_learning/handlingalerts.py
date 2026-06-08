from math import e
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']").click()
# //alert
alert = driver.switch_to.alert
print(alert.text)
alert.accept()


# alertconfirmation
driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()


# alert prompt
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
alert = driver.switch_to.alert
print(alert.text)
alert.send_keys("Selenium")
alert.accept()  

driver.quit()