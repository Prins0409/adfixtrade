import csv
from bs4 import BeautifulSoup
import requests
import json
import urllib.request
import os
def write_output(data):
	with open('toojays.csv', mode='w',newline="",encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["title","address","lat","lng","phone_number","order_online_url","opening_hours","directions_url","page_url"])
		for row in data:
			writer.writerow(row)

def fetch_data():
    headers = {
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,gu;q=0.4,de;q=0.3',
    'cookie': '_gcl_au=1.1.432479514.1659631608; _ga=GA1.2.1363893191.1659631608; _gid=GA1.2.633419433.1659631608; _fbp=fb.1.1659631608451.1661527037; __adroll_fpc=2d662679d7e3752af9567e518feb7cf9-1659631608887; __attentive_cco=1659631610997; __attentive_id=e54d211dee604e1589f61c007b9aa908; __attentive_ss_referrer="https://www.toojays.com/"; _attn_=eyJ1Ijoie1wiY29cIjoxNjU5NjMxNjExNzMyLFwidW9cIjoxNjU5NjMxNjExNzMyLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImU1NGQyMTFkZWU2MDRlMTU4OWY2MWMwMDdiOWFhOTA4XCJ9In0=; __attentive_dv=1; _uetsid=0551fe90141511edb90bdb7279ad4472; _uetvid=05522b40141511ed992b5d151a8f94d5; _gat_UA-102831953-1=1; __attentive_pv=5; __ar_v4=XYXVRRYJJZEMLGJO4NCA4Y%3A20220803%3A5%7CNHE6GAXXPZDAJDZ6UENPCK%3A20220803%3A5%7CQKJ2B33K4VE3VNNSLRNKAL%3A20220803%3A5',
    'referer': 'https://www.toojays.com/locations/',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Windows',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    url = "https://www.toojays.com/wp-json/toojays/v1/locations/lat=21.2403471/lng=72.8869815"
    data = requests.get(url, headers=headers)
    json_data = json.loads(data.text)
    for item in json_data:
            title = item['title']
            address = item['address']['address']
            lat = item['address']['lat']
            lng = item['address']['lng']
            phone_number = item['phone_number']
            order_online_url = item['order_online_url']
            opening_hours = item['opening_hours']
            directions_url = item['directions_url']
            page_url = item['url']
            store =[title,address,lat,lng,phone_number,order_online_url,opening_hours,directions_url,page_url]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()