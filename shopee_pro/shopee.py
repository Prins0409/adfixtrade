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
driver = webdriver.Chrome(ChromeDriverManager().install())

for i in range(0,50):   
    driver.get('https://shopee.sg/search?keyword=candy&page='+str(i)+'&trackingId=searchhint-1671255388-c0f8c84b-7dcc-11ed-8733-f4ee0816c11f')
    # driver.execute_script("window.scrollTo(0, window.scrollY + 5000)")
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    sleep(20)
    pageSource = driver.page_source
    soup = BeautifulSoup(pageSource, "html5lib")
    for data in soup.find_all("div",{"class":"shopee-search-item-result__item"}):
        page_urls = "https://shopee.sg" + data.find("a")["href"]
        print(page_urls)

    driver.quit()
    break
