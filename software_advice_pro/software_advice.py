import requests
import csv
from bs4 import BeautifulSoup
import json

def write_output(data):
	with open('software_advice.csv', mode='a', newline="", encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name", "industry"])
		for row in data:
			writer.writerow(row)

def fetch_data():
    for i in range(0, 2):
        j = i * 25
        print(i)
        url = "https://review-search-api.softwareadvice.com/production/reviews?q=s*%7C-s*&facet.gdm_industry_id=%7B%22sort%22:%22bucket%22,%22size%22:200%7D&facet.overall_quality=%7B%7D&fq=(and+product_id:+%2787134%27+listed:1+(or+(prefix+field%3Dreview+%27%27)+(prefix+field%3Dpros+%27%27)+(prefix+field%3Dcons+%27%27)))&q.options=%7B%22fields%22:[%22pros%5E5%22,%22cons%5E5%22,%22advice%5E5%22,%22review%5E5%22,%22review_title%5E5%22,%22vendor_response%5E5%22]%7D&highlight.pros=&highlight.cons=&highlight.advice=&highlight.review=&highlight.review_title=&highlight.vendor_response=&size=25&start="+str(j)+"&sort=completeness_score+desc,date_submitted+desc"
        headers = {
            "authorization": "Basic c2FndWVzdDo5eTR2dQ==",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        response = requests.request("GET", url, headers=headers)
        json_data = json.loads(response.text)
        for data in json_data["hits"]["hit"]:
            try:
                name = data["fields"]["f_name"].strip()
            except:
                continue
            try:
                industry = data["fields"]["gdm_industry_name"]
            except:
                continue

            store =[name, industry]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()

