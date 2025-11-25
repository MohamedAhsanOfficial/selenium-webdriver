from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def main():
    # Chrome Options for headless mode (important for Jenkins/servers)
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Setup Chrome with webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Test Step 1: Open Google homepage
    driver.get("https://www.google.com")

    # Test Step 2: Validate title contains "Google"
    assert "Google" in driver.title

    # Print output expected in Jenkins
    print("Received!")

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
