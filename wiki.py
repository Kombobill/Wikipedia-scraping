from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Set up the Chrome WebDriver with the ChromeDriver path
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Load the Wikipedia page
url = 'https://en.wikipedia.org/wiki/Kenya'
driver.get(url)

# Optional: Wait for the page to load
time.sleep(2)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
content = soup.find('div', class_='mw-parser-output').find_all('p')

# Print the text of each paragraph found
for paragraph in content:
    print(paragraph.text)

# Close the browser
driver.quit()

