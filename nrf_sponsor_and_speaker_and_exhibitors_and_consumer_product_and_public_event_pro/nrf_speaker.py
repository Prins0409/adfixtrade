import csv
from bs4 import BeautifulSoup
import requests

def write_output(data):
	with open('nrf_speaker.csv', mode='w',newline="",encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["speaker_full_name","speaker_first_name","speaker_last_name","speaker_job_title","speaker_company","speaker_description","speaker_website","speaker_linkedin","speakers_page_url"])
		for row in data:
			writer.writerow(row)

def fetch_data():
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "_gid=GA1.2.2100792723.1670390879; _mkto_trk=id:001-AOQ-559&token:_mch-nrf.com-1670390880380-75930; _gcl_au=1.1.2038696798.1670390881; _fbp=fb.1.1670390883643.14140490; ln_or=d; cb_user_id=null; cb_group_id=null; cb_anonymous_id=%22a8dc4799-d16a-493d-9a03-74491bf4dd79%22; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_2005052=eyJpZCI6ImY4MjNjZjAxLTk3NTgtNDZlMS1iYjcwLTU2ZjQ3ZTY2MTJjZiIsImNyZWF0ZWQiOjE2NzAzOTA4ODQ0ODksImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=1; _hjSessionUser_2005052=eyJpZCI6IjkyYjZmNTE1LWU4NWYtNWMyOS1hOWM3LTBmNjY5YjM1N2FjNSIsImNyZWF0ZWQiOjE2NzAzOTA4ODQ0NjYsImV4aXN0aW5nIjp0cnVlfQ==; __unam=78d5276-184eb0dfe56-7042980f-24; _ga_39FVVE9CL0=GS1.1.1670390881.1.1.1670396909.0.0.0; _ga=GA1.1.1829782061.1670390879",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    url = "https://nrfbigshow.nrf.com/speakers"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    for all_speakers in soup.find_all("div",{"class":"views-row"}):
        all_speakers_url = "https://nrfbigshow.nrf.com" + all_speakers.find("span",{"class":"field-content"}).find("a")["href"]
        print(all_speakers_url)
        headers1 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "_gid=GA1.2.2100792723.1670390879; _mkto_trk=id:001-AOQ-559&token:_mch-nrf.com-1670390880380-75930; _gcl_au=1.1.2038696798.1670390881; _fbp=fb.1.1670390883643.14140490; ln_or=d; cb_user_id=null; cb_group_id=null; cb_anonymous_id=%22a8dc4799-d16a-493d-9a03-74491bf4dd79%22; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_2005052=eyJpZCI6ImY4MjNjZjAxLTk3NTgtNDZlMS1iYjcwLTU2ZjQ3ZTY2MTJjZiIsImNyZWF0ZWQiOjE2NzAzOTA4ODQ0ODksImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=1; _hjSessionUser_2005052=eyJpZCI6IjkyYjZmNTE1LWU4NWYtNWMyOS1hOWM3LTBmNjY5YjM1N2FjNSIsImNyZWF0ZWQiOjE2NzAzOTA4ODQ0NjYsImV4aXN0aW5nIjp0cnVlfQ==; __unam=78d5276-184eb0dfe56-7042980f-24; _gat=1; _ga_39FVVE9CL0=GS1.1.1670390881.1.1.1670397394.0.0.0; _ga=GA1.1.1829782061.1670390879",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        response1 = requests.get(all_speakers_url, headers=headers1)
        soup1 = BeautifulSoup(response1.text, 'html.parser')
        speaker_full_name = soup1.find("span",{"class":"name-first"}).text.strip() + " " + soup1.find("span",{"class":"name-last"}).text.strip()
        speaker_first_name = soup1.find("span",{"class":"name-first"}).text.strip()
        speaker_last_name = soup1.find("span",{"class":"name-last"}).text.strip()
        try:
            speaker_job_title = soup1.find("div",{"class":"field field--name-field-job-title field--type-string field--label-hidden field__item"}).text.strip()
        except:
            speaker_job_title = ''
        try:
            speaker_company = soup1.find("div",{"class":"field field--name-field-speaker-company field--type-string field--label-hidden field__item"}).text.strip()
        except:
            speaker_company = ''
        speaker_description = soup1.find("div",{"class":"speaker-biography"}).text.strip()
        try:
            speaker_website = soup1.find("div",{"class":"speaker-website"}).find("a")["href"]
            if "https:" in speaker_website:
                speaker_website = speaker_website
            else:
                speaker_website = "https:" + speaker_website
        except:
            speaker_website = ''
        try:
            speaker_linkedin = soup1.find("div",{"class":"speaker-linkedin"}).find("a")["href"]
        except:
            speaker_linkedin = ''
        speakers_page_url = all_speakers_url
        store =[speaker_full_name,speaker_first_name,speaker_last_name,speaker_job_title,speaker_company,speaker_description,speaker_website,speaker_linkedin,speakers_page_url]
        yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()