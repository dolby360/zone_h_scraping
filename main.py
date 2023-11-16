from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import urllib.request

url = "https://www.zone-h.org/archive/filter=1/published=0/domain=.il/fulltext=1/page=1?hz=1"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

# Set up the WebDriver for Firefox (assuming you have the appropriate geckodriver installed)
driver = webdriver.Firefox()

# Open the webpage with the captcha image
driver.get(url)

# Locate the image element by its ID
captcha_element = driver.find_element(By.ID, "cryptogram")

# Get the source attribute containing the image URL
captcha_image_url = captcha_element.get_attribute("src")

# Specify the destination path where you want to save the image
destination_path = "image.png"

# Download the image
urllib.request.urlretrieve(captcha_image_url, destination_path)

# Continue with your existing code using the updated captcha image URL
# ...

# Close the WebDriver
driver.quit()
