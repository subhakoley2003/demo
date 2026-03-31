from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start browser (make sure ChromeDriver is installed)
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Wait for 5 seconds
time.sleep(5)

# Close browser
driver.quit()