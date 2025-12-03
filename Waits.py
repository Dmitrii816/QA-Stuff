from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get("https://example.com/dashboard")

wait = WebDriverWait(driver, 10)

# Waiting for button to appear
profile_button = wait.until(
    EC.visibility_of_element_located((By.ID, "profile-btn"))
)

# Wait until button becomes clickable
wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Start']"))
).click()
