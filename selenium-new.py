from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


# Create a WebDriver instance
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to your web application
driver.get('http://127.0.0.1:8000/')

# # Find an input field and enter text

# input_field.send_keys('test')

# Add a wait of 10 seconds for the element to be located
wait = WebDriverWait(driver, 10)
button = wait.until(EC.presence_of_element_located((By.ID, 'submit')))

# # Click a button
# button = driver.find_element_by_id('button_id')
# button.click()

# # Wait for page to load or specific element to appear
# driver.implicitly_wait(10)  # Wait for 10 seconds

# # Assert that a specific element or text is present
# assert 'expected_text' in driver.page_source


# Find the input field by its ID and enter "Toronto"
input_field = driver.find_element(By.ID,'id_city')
input_field.clear()  # Clear any existing text
input_field.send_keys('Toronto')

# Click the "Get Weather" button
button = driver.find_element(By.ID,'submit')
button.click()

# Wait for the weather info to load
time.sleep(5)  # Wait for 10 seconds (you may adjust this time as needed)

# Find the weather info elements and assert their presence
weather_info = driver.find_element(By.CLASS_NAME,'weather-info')
assert weather_info.is_displayed(), "Weather info is not displayed"

# Further assertions can be added to validate the weather information content if needed

# Close the browser window
driver.quit()
