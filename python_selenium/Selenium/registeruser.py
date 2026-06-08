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

actions.pause(30).perform()

# ---------------- VERIFY LOGO ----------------
logo = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//img[@alt='Website for automation practice']")
    )
)

assert logo.is_displayed(), "Logo is not displayed"
print("SUCCESS: Logo is displayed")

# ---------------- SIGNUP PAGE ----------------
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


driver.execute_script("arguments[0].click();", signup)

newsletter = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h2[normalize-space()='New User Signup!']")
    )
)

assert newsletter.is_displayed(), "Signup section is not displayed"
print("SUCCESS: Signup section is displayed")

# ---------------- SIGNUP DETAILS ----------------
type_text("//input[@placeholder='Name']", "Tamilarasu")
type_text("//input[@data-qa='signup-email']", "tamilsua@gmail.com")
click("//button[normalize-space()='Signup']")

# ---------------- ACCOUNT INFO ----------------
click("//input[@id='id_gender2']")
type_text("//input[@id='password']", "Tamil@2004")

select_dropdown("//select[@id='days']", "20")
select_dropdown("//select[@id='months']", "June")
select_dropdown("//select[@id='years']", "2000")

# ---------------- CHECKBOXES ----------------
click("//input[@id='newsletter']")
click("//input[@id='optin']")

# ---------------- ADDRESS DETAILS ----------------
type_text("//input[@id='first_name']", "Tamil")
type_text("//input[@id='last_name']", "Arasu")
type_text("//input[@id='company']", "ABC Company")
type_text("//input[@id='address1']", "Chennai Main Road")
type_text("//input[@id='address2']", "Near Bus Stand")

select_dropdown("//select[@id='country']", "Canada")

type_text("//input[@id='state']", "Ontario")
type_text("//input[@id='city']", "Toronto")
type_text("//input[@id='zipcode']", "M1B 1A1")
type_text("//input[@id='mobile_number']", "9876543210")

# ---------------- CREATE ACCOUNT ----------------
click("//button[normalize-space()='Create Account']")

actions.pause(5).perform()

driver.quit()