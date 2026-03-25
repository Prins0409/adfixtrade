import csv
from bs4 import BeautifulSoup
import requests
import json
import urllib.request
import os
def write_output(data):
	with open('union_online.csv', mode='a',newline="",encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name","sku","page_url","specifications","img_url"])
		for row in data:
			writer.writerow(row)

def fetch_data():
    headers = {
    "content-type": "application/json",
    "date": "Tue, 21 Jun 2022 10:48:04 GMT",
    "expires": "Tue, 21 Jun 2022 11:48:04 GMT",
    "referrer-policy": "strict-origin-when-cross-origin",
    "vary": "Accept-Encoding",
    "x-frame-options": "SAMEORIGIN",
    "x-served-by": "cache-bom4739-BOM",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    url = "https://www.uniononline.co.uk/content/api/v1/product-listing.json/uk/en/products/accessories/fixings-and-fastenings"
    data = requests.get(url, headers=headers)
    json_data = json.loads(data.text)
    for item in json_data['items']:
        try:
            name = item['title']
        except:
            name = ''
        sku = item['id']
        page_url = item['link']['url']
        try:
            specifications = item['text']
        except:
            specifications = ''
        try:
            img_url = item['image']['url']
        except:
            img_url = ''
        if img_url != '':
            try:    
                os.mkdir(name.replace('°',' ').replace('"',' ').replace("/",' ').replace(':'," ").strip())
            except:
                pass 
            files = name.replace('°',' ').replace('"',' ').replace("/",' ').replace(':'," ").strip()+"//"+name.replace('°',' ').replace('"',' ').replace("/",' ').replace(':'," ").strip()+".jpg"
            response = requests.get(img_url,verify=False)
            if response.status_code == 200:
                with open(files, 'wb') as f:
                    f.write(response.content)
        store =[name,sku,page_url,specifications,img_url]
        yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()