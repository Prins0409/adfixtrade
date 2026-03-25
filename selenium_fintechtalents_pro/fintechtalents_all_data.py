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
	with open('fintechtalents_data.csv', mode='a',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["employee_Fullname","job_title","company_name","linkedin_urls","count_employee"])
		for row in data:
			writer.writerow(row)
def fetch_data():
	url = "https://www.fintechtalents.com/events/london/speakers/"
	headers = {
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'cache-control': 'max-age=0',
	'cookie': '_clck=refnxz|1|f5v|0; _gcl_au=1.1.244395466.1666243211; _gid=GA1.2.1115420107.1666243211; _fbp=fb.1.1666243211225.1962389407; _hjFirstSeen=1; _hjIncludedInSessionSample=1; _hjSession_2480205=eyJpZCI6ImM2YjBhY2E0LWYwZjEtNGIyMS1iYzYzLWZjYWU3YWNkZDkzZiIsImNyZWF0ZWQiOjE2NjYyNDMyMTE4NTYsImluU2FtcGxlIjp0cnVlfQ==; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; __hstc=39382716.65a4e16f07e71aa92da31155baab13ad.1666243248399.1666243248399.1666243248399.1; hubspotutk=65a4e16f07e71aa92da31155baab13ad; __hssrc=1; _hjSessionUser_2480205=eyJpZCI6ImYwYTI5YzIxLWZlOTktNTViOS05NDllLTJkY2YwYjc1ZDk5NCIsImNyZWF0ZWQiOjE2NjYyNDMyMTE3MzgsImV4aXN0aW5nIjp0cnVlfQ==; form_p2c176681f24=1; wpca_consent=0; _ga=GA1.1.907261021.1666243211; _clsk=12b78wi|1666243456033|6|1|m.clarity.ms/collect; __hssc=39382716.6.1666243248399; _ga_YNTGWGX0FW=GS1.1.1666243210.1.1.1666243505.0.0.0',
	'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'sec-fetch-dest': 'document',
	'sec-fetch-mode': 'navigate',
	'sec-fetch-site': 'none',
	'sec-fetch-user': '?1',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
	}
	response = requests.request("GET", url, headers=headers)
	soup = BeautifulSoup(response.text, 'html.parser')

	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get('https://www.linkedin.com/login')
	print ("Opened website")
	warnings.simplefilter(action='ignore', category=FutureWarning)
	currentDirectory = os.getcwd()
	sleep(2)

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
	for i in range(1,67):
		datas = soup.find_all("div",{"class":"tmm_container"})[i]
		for data in datas.find_all("div",{"class":"tmm_member"}):
			employee_Fullname = data.find("span",{"class":"tmm_fname"}).text + data.find("span",{"class":"tmm_lname"}).text
			try:
				job_title = data.find("div",{"class":"tmm_job"}).text
			except:
				job_title = ''
			company_name = data.find("div",{"class":"tmm_desc"}).text
			linkedin_href = data.find("div",{"class":"tmm_scblock"})
			try:
				if "https://www.linkedin.com" in linkedin_href.find("a")["href"]:
					try:
						linkedin_urls = linkedin_href.find("a")["href"]
					except:
						linkedin_urls = ''
			except:
				continue
			if linkedin_urls == "https://www.linkedin.com/in/marie-dzanis-cima-6b13414/?originalSubdomain=uk":
				continue
			print("url--",linkedin_urls)
			driver.get(linkedin_urls)
			sleep(randint(5,10))
			pageSource = driver.page_source
			soup1 = BeautifulSoup(pageSource, "lxml")
			try:
				company_url = soup1.find("a",{"data-field":"experience_company_logo"})['href']
			except:
				company_url = ''
			driver.get(company_url)
			sleep(randint(5,10))
			pageSource1 = driver.page_source
			sleep(5)
			soup2 = BeautifulSoup(pageSource1, "lxml")
			try:
				count_employee = soup2.find("div",{"class":"display-flex mt2 mb1"}).text.strip().split("all ")[1].split(" employees")[0].replace(",","")
			except:
				count_employee = ''
			store =[employee_Fullname,job_title,company_name,linkedin_urls,count_employee]
			yield store
def scrape():
	data = fetch_data()
	write_output(data)
scrape()