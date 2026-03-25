import csv
from tkinter import N
import requests
import json
import pandas as pd

def write_output(data):
	with open('upxlandme.csv', mode='w',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["building_name","structured_build_start_date","structured_build_end_date","estimated_structured_build_end_date"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    urls = pd.read_excel('upland_props.xlsx')['address2'].to_list()
    for url in urls:
        main_api_link = "https://api.upxland.me/properties?status=all&fsa_option=all&sort_by=mint_price&sort_dir=asc&city=9&address=" + url.replace("%20","+")
        headers = {
        'accept': 'application/json, text/plain, */*',
        'origin': 'https://upxland.me',
        'referer': 'https://upxland.me/',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }
        data = requests.get(main_api_link, headers=headers)
        for json_data in json.loads(data.text):
            if "building" in json_data:
                nft_id = json_data['building']['nft_id']
                url_link = "https://api.upxland.me/structures/" + str(nft_id)
                data = requests.get(url_link, headers=headers)
                main_json_data = json.loads(data.text)
                building_name = main_json_data['building_name']
                print(building_name)
                structured_build_start_date = main_json_data['start_date']
                try:
                    structured_build_end_date = main_json_data['end_date']
                except:
                    structured_build_end_date = ''
                estimated_structured_build_end_date = main_json_data['estimated_end_date']
                store =[building_name,structured_build_start_date,structured_build_end_date,estimated_structured_build_end_date]
                yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()