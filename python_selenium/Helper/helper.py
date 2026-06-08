
    
    
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def click(xpath):
    driver.find_element(By.XPATH, xpath).click()

def type_text(xpath, value):
    driver.find_element(By.XPATH, xpath).send_keys(value)

def select_dropdown(xpath, value):
    Select(driver.find_element(By.XPATH, xpath)).select_by_visible_text(value)