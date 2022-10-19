

import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

browser = webdriver.Chrome('E:\Coding\Python Projects\WebScrapping\careerguide\careerguide\spiders\chromedriver.exe')
browser.get('https://www.linkedin.com/login')

username = browser.find_element_by_id('username')
username.send_keys('your username') # Replace it with your Username
password = browser.find_element_by_id('password')
password.send_keys('your password')# Replace it with your Password

login_button = browser.find_element_by_class_name('login__form_action_container ')
login_button.click()

c = input("Company name: ") # Provide the name of the company you want the details of
browser.get(f'https://www.linkedin.com/company/{c}/?trk=companies_directory')

# Overview of the company
overview = ""
des = browser.find_elements_by_class_name('break-words.white-space-pre-wrap.mb5.text-body-small.t-black--light')
for i in des:
    overview+=i.text
print("Overview:",overview)

# Company's location
location = []
company = browser.find_elements_by_class_name('org-top-card-summary-info-list__info-item')
for i in company:
    location.append(i.text)
print("Location",location[1:2])

# Number of employees
employees = ""
emp = browser.find_elements_by_class_name('text-body-small.t-black--light.mb1')
for i in emp:
    employees+=i.text
print("No. of employees:",employees)
