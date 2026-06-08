import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

# ---------------- DRIVER SETUP ----------------
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# ---------------- COMMON FUNCTIONS ----------------
def click(xpath):
    element = wait.until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    driver.execute_script("arguments[0].click();", element)

def type_text(xpath, text):
    element = wait.until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    element.clear()
    element.send_keys(text)

def select_dropdown(xpath, value):
    dropdown = wait.until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    Select(dropdown).select_by_visible_text(value)

# Create ActionChains object
actions = ActionChains(driver)

# ---------------- OPEN WEBSITE ----------------
driver.get("https://automationexercise.com")
driver.maximize_window()


click("//a[normalize-space()='Signup / Login']")
type_text("//input[@data-qa='login-email']","tamilsuaxcvh@gmail.com")
type_text("//input[@placeholder='Password']","Tamil@2004")
click("//button[normalize-space()='Login']")






Error = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//p[normalize-space()='Your email or password is incorrect!']")
    )
)

assert Error.is_displayed(), "Signup section is not displayed"
print("SUCCESS: Signup section is displayed")