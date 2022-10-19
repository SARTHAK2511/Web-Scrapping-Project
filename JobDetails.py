#importing libraries


import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

os.environ['PATH']+="C:/Users/HP/Desktop/Web Scrapping/Selenium"

# Initializing driver
browser = webdriver.Chrome()
browser.get("https://www.careerguide.com/career-options/")

#finding categories from carrierguide.com
categories = browser.find_elements(By.CLASS_NAME,"c-font-bold")
browser.implicitly_wait(5)
categories_list = []

for category in range(1,40):
    categories_list.append(categories[category].text)
 # finding subcategories from career guide.com
sub_categories = browser.find_elements(By.CLASS_NAME,"c-content-list-1")
sub_categories_list = []

cities=[]
Job_titles=[]
Company_Names=[]
location_name = []


for sub_category in sub_categories:
    print(sub_category.text.replace("\n",",").split(","))
    sub_categories_list.append(sub_category.text.replace("\n",",").split(","))
#logging into linkedin
    browser.get("https://www.linkedin.com")
    username = browser.find_element(By.ID,"session_key")
    username.send_keys(input("Enter User Name/ Email id/ Phone Number: "))
    password = browser.find_element(By.ID,"session_password")
    password.send_keys(input("Enter your password: "))
    
    login_button = browser.find_element(By.CLASS_NAME,"sign-in-form__submit-button")
    login_button.click()
    browser.get("https://www.linkedin.com/jobs/search")
    
#using loop to find data for each subcategory   
for sub_category in sub_categories_list:
        browser.get("https://www.linkedin.com/jobs/search")
        search_jobs = browser.find_element(By.ID,"jobs-search-box-keyword-id-ember25")
        search_jobs_by_location = browser.find_element(By.ID,"jobs-search-box-location-id-ember25")
        search_jobs.send_keys(sub_category)
        
        search_button = browser.find_element(By.CLASS_NAME, "jobs-search-box__submit-button")
        search_button.click()
        search_jobs.clear()
        search_jobs_by_location.clear()
        
        jobs=browser.find_elements(By.CLASS_NAME,"full-width.artdeco-entity-lockup__title.ember-view")
        browser.implicitly_wait(3)
        Companies = browser.find_elements(By.CLASS_NAME,"job-card-container__company-name.ember-view")
        browser.implicitly_wait(3)
        location = browser.find_elements(By.CLASS_NAME,"job-card-container__metadata-item")
        browser.implicitly_wait(3)

        for i in range(len(location)):
            location_name.append(location[i].text)

        for i in location_name:
            if i == 'Remote' or i == 'On-site' or i == 'Hybrid':
                location_name.remove(i)


        for i in location_name:
            cities.append(i.split(',')[0])

        for job in jobs:
            Job_titles.append(job.text)

        Company_Names=[]

        for i in Companies:
            Company_Names.append(i.text)

#Saving data into csv file    
df = pd.DataFrame({"Job Position":Job_titles,"Company":Companies,"Location":cities})
df.to_csv("Jobs.csv")