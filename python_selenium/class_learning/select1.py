from math import e
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://qaplayground.com/practice/dropdowns")

# Open dropdown
wait.until(
    EC.element_to_be_clickable((By.ID, "dropdown-fruit"))
).click()

# Select Grapes
driver.find_element(By.XPATH, "//*[text()='Grapes']").click()

# options = driver.find_elements(By.XPATH, "//*[@role='option']")
# options[2].click() 

# driver.find_element(By.XPATH, "//*[contains(text(),'Grapes')]").click()


# using sendkeys
# dropdown = driver.find_element(By.ID, "dropdown-fruit")

# dropdown.click()
# dropdown.send_keys("Grapes")
# dropdown.send_keys(Keys.ENTER)

# second dropown by java script executor
# Select India

try:
    option = wait.until(
    EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Scenario 2: Select by Value Attribute']"))
    )
    driver.execute_script("arguments[0].click();", option)
    time.sleep(3)
except Exception as e:
    print("Option not found:", e)