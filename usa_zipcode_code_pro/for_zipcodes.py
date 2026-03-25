import csv
from bs4 import BeautifulSoup
import requests

def write_output(data):
    with open('warwick_zipcode.csv', mode='a',newline="", encoding="utf-8") as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(["zipcodes"])
        for row in data:
            writer.writerow(row)
def fetch_data():
    count = 1
    while True:
        print(count)
        url = "https://ri.postcodebase.com/zipcode5/02818?page="+str(count)
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "cache-control": "max-age=0",
            "cookie": "fs.bot.check=true; _ga=GA1.2.1317068200.1670304781; _gid=GA1.2.1330604295.1670304781; fs.session.id=dbed1092-6fd0-4657-a768-6997b87b67cd; __gpi=UID=0000090a42ec8888:T=1670304790:RT=1670304790:S=ALNI_Ma23sXwz5S9rCWJC-xTVWhHH39IzQ; _pbjs_userid_consent_data=3524755945110770; __qca=P0-999731853-1670304783847; __gads=ID=836a3206d8ef7bc0-2246b220ddd80025:T=1670304790:S=ALNI_MYbEjwVzMqzmvUN07Y3-dIt6W3DEQ; _au_1d=AU1D-0100-001670304801-8UALT9AA-L22N; _au_last_seen_pixels=eyJhcG4iOjE2NzAzMDQ4MDEsInR0ZCI6MTY3MDMwNDgwMSwicHViIjoxNjcwMzA0ODAxLCJhZHgiOjE2NzAzMDQ4MDEsImdvbyI6MTY3MDMwNDgwMSwiYWRvIjoxNjcwMzA0ODAxLCJydWIiOjE2NzAzMDQ4MDEsInVucnVseSI6MTY3MDMwNDgwMSwib3BlbngiOjE2NzAzMDQ4MDEsImJlZXMiOjE2NzAzMDQ4MDEsImltcHIiOjE2NzAzMDQ4MDEsInBwbnQiOjE2NzAzMDQ4MDEsInNvbiI6MTY3MDMwNDgwMSwic21hcnQiOjE2NzAzMDQ4MDEsIm1lZGlhbWF0aCI6MTY3MDMwNDgwMSwidGFib29sYSI6MTY3MDMwNDgwMX0=; _au_last_seen_iab_tcf=1670304803981; _lr_retry_request=true; _lr_env_src_ats=false; pbjs-unifiedid=%7B%22TDID%22%3A%225a204128-a675-42f0-815a-69a62e8cf1ae%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222022-11-06T05%3A33%3A27%22%7D; pbjs-unifiedid_last=Tue%2C%2006%20Dec%202022%2005%3A33%3A27%20GMT; _cc_id=994771fdee48fb067b7282f40c123070; panoramaId_expiry=1670391208862; _fbp=fb.1.1670304819245.160385900; _awl=3.1670305497.0.5-aa4c01e9ad0a1d1fb377e60839f526dc-6763652d75732d7765737431-0",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
            }
        data = requests.get(url, headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')
        if soup.find_all("div",{"class":"table_roll"})[1] == None:
            break
        info = soup.find_all("div",{"class":"table_roll"})[1]
        for item in range(0,10):
            for zipcode in info.find_all("a")[item]:
                print(zipcode)
                store =[zipcode]
                yield store
        count += 1
def scrape():
    data = fetch_data()
    write_output(data)
scrape()