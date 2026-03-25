import csv
from html.parser import HTMLParser
from itertools import count
from tkinter import N
from bs4 import BeautifulSoup
import requests
import json
def write_output(data):
	with open('wear_post.csv', mode='w',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["drName","speciality","info","addr","area","zipcode","contactNo"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    for i in range(1,11):
        url = "https://wearenorthern.org/wp-admin/admin-ajax.php"
        payload = "action=do_filter_doctors&params%5Bpage%5D="+str(i)
        headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '43',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '_gid=GA1.2.1231742160.1653825016; _ga=GA1.2.273151235.1653646140; _ga_76JWY9XTPN=GS1.1.1653901669.5.1.1653903435.0',
        'origin': 'https://wearenorthern.org',
        'referer': 'https://wearenorthern.org/find-a-doctor/',
        'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        data = json.loads(response.text)['data']['content']
        soup = BeautifulSoup(data, 'html.parser')
        for index,drName in enumerate(soup.find_all('h3', {"class":"mt-0"})): 
            drName = drName.text
            speciality1 = soup.find_all('div',{"class":"media"})[index].find('p').text
            speciality = speciality1.replace('Specialty: ', '')
            try:
                info = soup.find_all('div',{"class":"location_name mr-auto align-self-center"})[index].find('h5').text
            except:
                info1 = str(soup.find_all('div',{"class":"location_name mr-auto align-self-center"})[index]).split('">')[1]
                info = info1.split('<')[0]
            try:    
                addr = soup.find_all('div',{"class":"location_name"})[index].find('span', {"class":"address"}).text
            except:
                addr = ''
            addr.split(',')[0]
            try:    
                addr = soup.find_all('div',{"class":"location_name"})[index].find('span', {"class":"address"}).text
            except:
                addr = ''
            x = addr.split(',')[-1]
            area1 = x.replace('27030', '')
            area2 = area1.replace('28803-3505', '')
            area = area2.replace('830 Rockford Street', '')
            try:    
                addr = soup.find_all('div',{"class":"location_name"})[index].find('span', {"class":"address"}).text
            except:
                addr = ''
            x = addr.split(',')[-1]
            y = x.split(' ')[-1]
            zipcode = y.replace('Street', '')
            try:
                contactNo = soup.find_all('div',{"class":"phone align-self-center"})[index].find('a').text
            except:
                contactNo = ''
            store =[drName,speciality,info,addr,area,zipcode,contactNo]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()