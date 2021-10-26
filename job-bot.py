from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
import os
import time
from dotenv import load_dotenv

# LOAD ENVIRONMENT VARIABLES
load_dotenv()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(".\chromedriver.exe", options=options)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_WT=2&geoId=101165590&keywords=python&location=United%20Kingdom")

signin_button = driver.find_element_by_class_name("nav__button-secondary")
signin_button.click()
username = driver.find_element_by_id("username")
username.send_keys(os.getenv("EMAIL"))
password = driver.find_element_by_id("password")
password.send_keys(os.getenv("PASSWORD"))


main_signin_button = driver.find_element_by_class_name("btn__primary--large")
main_signin_button.click()

time.sleep(3)
all_posts = driver.find_elements_by_class_name("job-card-container--clickable")

for post in all_posts:
    print(post)
    post.click()

# def find(driver):
#     all_posts = driver.find_element_by_class_name("job-card-container--clickable")
#     if all_posts:
#         return all_posts
#     else:
#         return False

