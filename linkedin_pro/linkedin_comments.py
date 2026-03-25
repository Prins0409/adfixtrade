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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def write_output(data):
	with open('linkedin_comments.csv', mode='a',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["user_name","user_post","user_city_or_country","user_page_url"])
		for row in data:
			writer.writerow(row)
def fetch_data():
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get('https://www.linkedin.com/login')
	print ("Opened website")
	warnings.simplefilter(action='ignore', category=FutureWarning)
	currentDirectory = os.getcwd()
	sleep(5)

	usr='princegevariya1808@gmail.com'
	pwd='Prince1111@'
	sleep(5)
	username_box = driver.find_element(By.XPATH,'//*[@id="username"]')
	username_box.send_keys(usr)
	print ("Email Id entered")
	sleep(5)
	password_box = driver.find_element(By.XPATH,'//*[@id="password"]')
	password_box.send_keys(pwd)
	print ("Password entered")
	sleep(5) 
	login_box = driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
	login_box.click()
	sleep(5)
	driver.get("https://www.linkedin.com/posts/hannah-bouhamdi-267500160_evercore-investmentbanking-finance-activity-6972182273408253952-p3Bd/")
	last_height = driver.execute_script("return document.body.scrollHeight")

	for scroll in range(1,1000):
		try:
			reload_box = driver.find_element(By.XPATH,'//button[@class="comments-comments-list__load-more-comments-button artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view"]').click()
		except:
			time.sleep(10000)
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		time.sleep(8)
		new_height = driver.execute_script("return document.body.scrollHeight")
		if new_height == last_height:
			break
		last_height = new_height
		pageSource = driver.page_source
		soup = BeautifulSoup(pageSource, "html.parser")

	for user_url in soup.find_all("div",{"class":"comments-post-meta__profile-info-wrapper display-flex"}):
		if "https://www.linkedin.com" in str(user_url):
			user_page_url = user_url.find("a")["href"]
		else:
			user_page_url = "https://www.linkedin.com" + user_url.find("a")["href"]
		print(user_page_url)
		driver.get(user_page_url)
		sleep(5)
		pageSource1 = driver.page_source
		soup1 = BeautifulSoup(pageSource1, "lxml")
		try:
			user_name = soup1.find("h1",{"class":"text-heading-xlarge inline t-24 v-align-middle break-words"}).text.strip()
		except:
			user_name = ''
		try:
			user_post = soup1.find("div",{"class":"text-body-medium break-words"}).text.strip()
		except:
			user_post = ''
		try:
			user_city_or_country = soup1.find("span",{"class":"text-body-small inline t-black--light break-words"}).text.strip()
		except:
			user_city_or_country = ''
		print(user_name)
		store =[user_name,user_post,user_city_or_country,user_page_url]
		yield store
def scrape():
	data = fetch_data()
	write_output(data)
scrape()
