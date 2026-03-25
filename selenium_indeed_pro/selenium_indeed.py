import requests
from lib2to3.pgen2 import driver
from selenium import webdriver
import time,json,csv
from bs4 import BeautifulSoup
import os
import warnings
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from random import randint
from selenium.webdriver.common.by import By

def write_output(data):
	with open('selenium_indeed.csv', mode='a',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["job_name","job_company","job_rating","job_review_count","job_location_or_type","job_salary","job_description"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    for i in range(0,66):
        j = i*10
        print(j)
        driver.get('https://in.indeed.com/jobs?q=python&l=India&start='+str(j))
        pageSource = driver.page_source
        soup = BeautifulSoup(pageSource, "lxml")
        sleep(5)
        for data in soup.find_all("td",{"class":"resultContent"}):
            jk_data = data.find("a")["data-jk"]
            tk_data = data.find("a")["data-mobtk"]
            main_url = "https://in.indeed.com/viewjob?jk="+str(jk_data)+"&tk="+str(tk_data)+"&from=serp&vjs=3"
            print(main_url)
            driver.get(main_url)
            pageSource1 = driver.page_source
            soup1 = BeautifulSoup(pageSource1, "lxml")
            sleep(5)
            job_name = soup1.find("div",{"class":"jobsearch-JobInfoHeader-title-container"}).text.strip().replace("- job post","")
            job_company = soup1.find_all("div",{"class":"jobsearch-InlineCompanyRating-companyHeader"})[1].text.strip()
            try:
                job_rating = soup1.find("div",{"class":"icl-Ratings-count"}).text.strip()
            except:
                job_rating = ''
            try:
                job_review_count = soup1.find("meta",{"itemprop":"ratingValue"})["content"]
            except:
                job_review_count = ''
            try:
                job_location_or_type = soup1.find("div",{"class":"jobsearch-RelatedLinks-linkWrapper"}).text.strip().split("in")[1].strip()
            except:
                job_location_or_type = ''
            try:
                job_salary = soup1.find("div",{"class":"jobsearch-JobMetadataHeader-item"}).text.strip()
            except:
                job_salary = ''
            try:
                job_description = soup1.find("div",{"class":"jobsearch-jobDescriptionText"}).text.strip()
            except:
                job_description = ''
            print(job_name)
            store =[job_name,job_company,job_rating,job_review_count,job_location_or_type,job_salary,job_description]
            yield store
    driver.quit()
def scrape():
	data = fetch_data()
	write_output(data)
scrape()
