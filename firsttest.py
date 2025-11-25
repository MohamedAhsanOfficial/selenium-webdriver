from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')

# FIX PATH — choose the correct one
service = Service('/usr/bin/chromedriver/chromedriver')

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title
assert title == "Web form"

driver.implicitly_wait(0.5)

text_box = driver.find_element(By.NAME, "my-text")
submit_button = driver.find_element(By.CSS_SELECTOR, "button")

text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(By.ID, "message")
value = message.text
print(value)

assert value == "Received!"
driver.quit()
