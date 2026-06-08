from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://demo.smart-hospital.in/site/login")

# Click Super Admin
wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[normalize-space()='Super Admin']")
    )
).click()

# Click Sign In button
wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit']")
    )
).click()


wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//span[@class='logo-lg']//img[@alt='Smart Hospital & Research Center']")
    )
).click()


# scroll_to_element(element)
 

# element = wait.until(
#     EC.presence_of_element_located(
#         (By.XPATH, "//li[23]//a[1]")
#     )
# )
element = driver.find_element(By.XPATH, "//li[23]//a[1]")
actions = ActionChains(driver)
actions.scroll_to_element(element).perform()
time.sleep(3)
element.click()
time.sleep(3)



# ScrollOrigin method
body = driver.find_element(By.TAG_NAME, "body")
origin = ScrollOrigin.from_element(body)

actions.scroll_from_origin(origin, 0, 500).perform()
time.sleep(2)



# scroll down
actions.scroll_by_amount(0, 800).perform()
time.sleep(2)

# scroll more down
actions.scroll_by_amount(0, 800).perform()
time.sleep(2)