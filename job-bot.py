from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os 
from dotenv import load_dotenv

load_dotenv()

driver = webdriver.Chrome(".\chromedriver.exe")
driver.get("https://www.linkedin.com/")

signin_button = driver.find_element_by_class_name("nav__button-secondary")
signin_button.click()
username = driver.find_element_by_id("username")
username.send_keys(os.getenv('EMAIL'))
