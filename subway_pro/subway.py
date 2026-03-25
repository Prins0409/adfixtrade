import csv
from html.parser import HTMLParser
from itertools import count
from tkinter import N
from turtle import pos
from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime

def write_output(data):
	with open('subway.csv', mode='w',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name","addr","sublocality","city","postalcode","countryname","phone","direction_url","days","start_time","end_time","services","latitude","longitude"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
            }
    url1 = "https://restaurants.subway.com/united-kingdom"
    Base_url = 'https://restaurants.subway.com/'
    response = requests.request("GET", url1, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    for main_url in soup.find_all("a",{"class":"Directory-listLink"}):
        if "united-kingdom/additional-locations" == main_url['href']:
            continue
        sub_url = Base_url+main_url['href']
        response1 = requests.request("GET", sub_url, headers=headers)
        soup1 = BeautifulSoup(response1.text, 'html.parser')
        for dir in soup1.find_all("a",{"class":"Directory-listLink"}):
            if dir['data-count'] != '(1)':
                response2 = requests.request("GET", Base_url+dir['href'].replace("..",''), headers=headers)
                soup2 = BeautifulSoup(response2.text, 'html.parser')
                for page_url in soup2.find_all("a",{"class":"Teaser-title"}):
                    web_url = Base_url+page_url['href'].replace("../../",'')
                    print(web_url)
                    response3 = requests.request("GET", web_url, headers=headers)
                    soup3 = BeautifulSoup(response3.text, 'html.parser')
                    name = soup3.find("span",{"class","c-address-city"}).text
                    print(name,"#############")
                    address = soup3.find_all("div",{"class","c-AddressRow"})[0].text +","+ soup3.find_all("div",{"class","c-AddressRow"})[1].text
                    try:
                        sublocality = soup3.find_all("span",{"class","c-address-sublocality"})[0].text
                    except:
                        sublocality = ''
                    try:
                        city = soup3.find_all("span",{"class","c-address-city"})[1].text
                    except:
                        city = ''
                    try:
                        postalcode = soup3.find_all("span",{"class","c-address-postal-code"})[2].text
                    except:
                        postalcode = ''
                    countryname = soup3.find("abbr",{"class","c-address-country-name c-address-country-gb"}).text
                    try:
                        phone = soup3.find_all("div",{"class","Phone-display Phone-display--withLink"})[1].text
                    except:
                        phone = ''
                    direction_urls = soup3.find("div",{"class","Core-subColumn js-ignore-auto-sup"})
                    direction_url = direction_urls.find_all("a")[1]["href"]
                    days = json.loads(soup3.find("div",{"class":"js-hours-table"})['data-days'])
                    for day in days:
                        if 'dailyHolidayHours' in day:
                            for days1 in ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']:
                                days = days1
                                end_time = 'Closed'
                                start_time = 'Closed'
                        else:
                            for intervals in day['intervals']:
                                days = day['day']
                                if str(intervals['end']) == '0':
                                    end_time = '0:00'
                                else:
                                    end_time = datetime.strptime(str(intervals['end']), "%H%M").strftime("%I:%M %p")
                                if str(intervals['start']) == '0':
                                    start_time =  '0:00'
                                else:
                                    start_time = datetime.strptime(str(intervals['start']), "%H%M").strftime("%I:%M %p")
            else:
                web_url = Base_url+dir['href'].replace("../../",'')
                response3 = requests.request("GET", web_url, headers=headers)
                soup3 = BeautifulSoup(response3.text, 'html.parser')
                name = soup3.find("span",{"class","c-address-city"}).text
                print(name,"#############")
                address = soup3.find_all("div",{"class","c-AddressRow"})[0].text +","+ soup3.find_all("div",{"class","c-AddressRow"})[1].text
                try:
                    sublocality = soup3.find_all("span",{"class","c-address-sublocality"})[0].text
                except:
                    sublocality = ''
                try:
                    city = soup3.find_all("span",{"class","c-address-city"})[1].text
                except:
                    city = ''
                try:
                    postalcode = soup3.find_all("span",{"class","c-address-postal-code"})[2].text
                except:
                    postalcode = ''
                countryname = soup3.find("abbr",{"class","c-address-country-name c-address-country-gb"}).text
                phone = soup3.find_all("div",{"class","Phone-display Phone-display--withLink"})[1].text
                direction_urls = soup3.find("div",{"class","Core-subColumn js-ignore-auto-sup"})
                direction_url = direction_urls.find_all("a")[1]["href"]
                days = json.loads(soup3.find("div",{"class":"js-hours-table"})['data-days'])
                for day in days:
                    if 'dailyHolidayHours' in day:
                        for days1 in ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']:
                            days = days1
                            end_time = 'Closed'
                            start_time = 'Closed'
                    else:
                        for intervals in day['intervals']:
                            days = day['day']
                            if str(intervals['end']) == '0':
                                end_time = '0:00'
                            else:
                                end_time = datetime.strptime(str(intervals['end']), "%H%M").strftime("%I:%M %p")
                            if str(intervals['start']) == '0':
                                start_time =  '0:00'
                            else:
                                start_time = datetime.strptime(str(intervals['start']), "%H%M").strftime("%I:%M %p")
                try:
                    services = soup3.find("p",{"class","Core-service Core-service--delivery"}).text
                except:
                    services = ''
                latitude = soup3.find("span",{"class","coordinates"}).find("meta")["content"]
                longitude = soup3.find("span",{"class","coordinates"}).find("meta")["content"]
                store =[name,address,sublocality,city,postalcode,countryname,phone,direction_url,days,start_time,end_time,services,latitude,longitude]
                yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()