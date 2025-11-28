from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com/login")

# Email field by ID
email_field = driver.find_element(By.ID, "email")

# Login Button by XPATH
login_button = driver.find_element(By.XPATH, "//button[text()='Login']")

# Password field by name
password_field = driver.find_element(By.NAME, "password")

# Element Locating by CSS Selector
remember_me = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")