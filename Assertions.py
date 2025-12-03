from selenium import webdriver
from selenium.webdriver.common.by import By

driver.get("https://example.com/login")

driver.find_element(By.ID, "email").send_keys("test@example.com")
driver.find_element(By.ID, "password").send_keys("password123")
driver.find_element(By.XPATH, "//button[text()='Login']").click()

# Assertion: We check that the Dashboard heading appears on the page.
dashboard_title = driver.find_element(By.TAG_NAME, "h1").text

assert dashboard_title == "Dashboard", "Login failed: Dashboard not displayed"
