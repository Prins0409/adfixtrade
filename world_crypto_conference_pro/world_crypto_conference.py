import requests
from bs4 import BeautifulSoup
import csv

def write_output(data):
    with open('world_crypto_conference_speakers_data.csv', mode='a',newline="", encoding="utf-8") as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(["speakers_name","speakers_post","speakers_linkedin_or_twitter_url"])
        for row in data:
            writer.writerow(row)
def fetch_data():
    url = "https://worldcryptoconference.org/"
    headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "cache-control": "max-age=0",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    for data in soup.find_all("div",{"class":"inner-box"}):
        speakers_name = data.find("div",{"class":"info-box"}).find("h4",{"class":"name"}).text.strip()
        if data.find("div",{"class":"info-box"}) == "":
            break
        speakers_post = data.find("div",{"class":"info-box"}).find("span",{"class":"designation"}).text.strip().replace("  "," ").replace("\\n"," ")
        try:
            speakers_linkedin_or_twitter_url = data.find("div",{"class":"social-box"}).find("a")["href"]
        except:
            speakers_linkedin_or_twitter_url = ''
        print(speakers_name)
        store =[speakers_name,speakers_post,speakers_linkedin_or_twitter_url]
        yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()
