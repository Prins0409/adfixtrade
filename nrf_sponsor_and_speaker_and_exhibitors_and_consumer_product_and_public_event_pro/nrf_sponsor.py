import csv
from bs4 import BeautifulSoup
import requests

def write_output(data):
	with open('nrf_sponsor.csv', mode='w',newline="",encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["sponser_name","sponser_level","sponser_city","sponser_state","sponser_country","sponser_description","sponser_website","sponser_linkedin","sponser_page_url"])
		for row in data:
			writer.writerow(row)

def fetch_data():
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "_gid=GA1.2.2100792723.1670390879; _mkto_trk=id:001-AOQ-559&token:_mch-nrf.com-1670390880380-75930; _gcl_au=1.1.2038696798.1670390881; _fbp=fb.1.1670390883643.14140490; ln_or=d; cb_user_id=null; cb_group_id=null; cb_anonymous_id=%22a8dc4799-d16a-493d-9a03-74491bf4dd79%22; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_2005052=eyJpZCI6ImY4MjNjZjAxLTk3NTgtNDZlMS1iYjcwLTU2ZjQ3ZTY2MTJjZiIsImNyZWF0ZWQiOjE2NzAzOTA4ODQ0ODksImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=1; _hjSessionUser_2005052=eyJpZCI6IjkyYjZmNTE1LWU4NWYtNWMyOS1hOWM3LTBmNjY5YjM1N2FjNSIsImNyZWF0ZWQiOjE2NzAzOTA4ODQ0NjYsImV4aXN0aW5nIjp0cnVlfQ==; __unam=78d5276-184eb0dfe56-7042980f-4; _gat=1; _ga_39FVVE9CL0=GS1.1.1670390881.1.1.1670391569.0.0.0; _ga=GA1.1.1829782061.1670390879",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    url = "https://nrfbigshow.nrf.com/sponsors"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    for data in soup.find_all("div",{"class":"view-content"}):
        level_name = data.find("h3").text
        for data1 in data.find_all("div",{"class":"views-field views-field-nothing"}):
            sponsers_name = data1.find("img")["alt"].replace(",","").replace(".","").lower().replace(" ","-").replace("&","").replace("-for","").replace("-of","").replace("'","").replace("-|","").replace("-in-","-").replace("a-is","a")
            if sponsers_name == "aruba-a-hewlett-packard-enterprise-company":
                sponsers_name = data1.find("img")["alt"].replace(", a","").replace(".","").lower().replace(" ","-")
            all_sponsors_url = "https://nrfbigshow.nrf.com/company/" + sponsers_name
            print(all_sponsors_url)
            headers1 = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Connection": "keep-alive",
            "Cookie": "__sharethis_cookie_test__=1; _gid=GA1.2.2100792723.1670390879; _mkto_trk=id:001-AOQ-559&token:_mch-nrf.com-1670390880380-75930; _gcl_au=1.1.2038696798.1670390881; _fbp=fb.1.1670390883643.14140490; ln_or=d; cb_user_id=null; cb_group_id=null; cb_anonymous_id=%22a8dc4799-d16a-493d-9a03-74491bf4dd79%22; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_2005052=eyJpZCI6ImY4MjNjZjAxLTk3NTgtNDZlMS1iYjcwLTU2ZjQ3ZTY2MTJjZiIsImNyZWF0ZWQiOjE2NzAzOTA4ODQ0ODksImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=1; _hjSessionUser_2005052=eyJpZCI6IjkyYjZmNTE1LWU4NWYtNWMyOS1hOWM3LTBmNjY5YjM1N2FjNSIsImNyZWF0ZWQiOjE2NzAzOTA4ODQ0NjYsImV4aXN0aW5nIjp0cnVlfQ==; __unam=78d5276-184eb0dfe56-7042980f-8; _gat=1; _ga_39FVVE9CL0=GS1.1.1670390881.1.1.1670392656.0.0.0; _ga=GA1.1.1829782061.1670390879",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
            }
            response1 = requests.get(all_sponsors_url, headers=headers1)
            soup1 = BeautifulSoup(response1.text, 'html.parser')
            sponser_name = soup1.find("div",{"class":"company_name"}).text.strip()
            sponser_level = soup1.find("div",{"class":"views-field views-field-field-sponsor-level"}).find("div",{"class":"field-content"}).text.strip()
            print(sponser_level)
            sponser_city = soup1.find("div",{"class":"company_contact_city_state"}).text.strip().split(",")[0]
            try:
                sponser_state = soup1.find("div",{"class":"company_contact_city_state"}).text.strip().split(", ")[1]
            except:
                sponser_state = ''
            sponser_country = soup1.find("div",{"class":"company_country"}).text.strip()
            try:
                sponser_description = soup1.find("div",{"class":"views-field views-field-body"}).find("div",{"class":"field-content"}).text.strip()
            except:
                sponser_description = ''
            try:
                sponser_website = soup1.find("div",{"class":"company_website"}).find("a")["href"]
            except:
                sponser_website = ''
            try:
                sponser_linkedin = soup1.find("div",{"class":"company_linkedin"}).find("a")["href"]
            except:
                sponser_linkedin = ''
            sponser_page_url = all_sponsors_url
            store =[sponser_name,sponser_level,sponser_city,sponser_state,sponser_country,sponser_description,sponser_website,sponser_linkedin,sponser_page_url]
            yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()