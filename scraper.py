from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

baseUrl = "https://ticket.interpark.com/"

# Set up WebDriver and open the webpage
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(3)
driver.get(baseUrl)
# Find the title element by its tag name (assuming it's a <h1> element)
title_element = driver.find_element(By.TAG_NAME, 'h1')

# Print the text of the title element
print(title_element.text)

# Always remember to close the driver when finished
driver.quit()
