import csv
from bs4 import BeautifulSoup
import requests

def write_output(data):
	with open('nrf_exhibitor.csv', mode='w',newline="",encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["exhibitor_company_name","exhibitor_city","exhibitor_state","exhibitor_country","exhibitor_description","exhibitor_website","exhibitor_linkedin","exhibitors_page_url"])
		for row in data:
			writer.writerow(row)

def fetch_data():
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "_mkto_trk=id:001-AOQ-559&token:_mch-nrf.com-1670390880380-75930; _gcl_au=1.1.2038696798.1670390881; _fbp=fb.1.1670390883643.14140490; cb_user_id=null; cb_group_id=null; cb_anonymous_id=%22a8dc4799-d16a-493d-9a03-74491bf4dd79%22; _hjSessionUser_2005052=eyJpZCI6IjkyYjZmNTE1LWU4NWYtNWMyOS1hOWM3LTBmNjY5YjM1N2FjNSIsImNyZWF0ZWQiOjE2NzAzOTA4ODQ0NjYsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.971742407.1670500484; ln_or=d; _hjIncludedInSessionSample=0; _hjSession_2005052=eyJpZCI6ImNiZDNkZmI4LWJkYzktNDc3YS04NTQ0LTE5ZWJiMWQyODI5MiIsImNyZWF0ZWQiOjE2NzA1MDA0ODY5MDIsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; __unam=78d5276-184eb0dfe56-7042980f-26; _gat=1; _ga=GA1.1.1829782061.1670390879; _ga_39FVVE9CL0=GS1.1.1670500486.3.1.1670500855.0.0.0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    url = "https://nrfbigshow.nrf.com/exhibitors"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    for all_exhibitors in soup.find_all("td",{"headers":"view-title-table-column"}):
        all_exhibitors_url = "https://nrfbigshow.nrf.com" + all_exhibitors.find("a")["href"]
        print(all_exhibitors_url)
        headers1 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "__sharethis_cookie_test__=1; _mkto_trk=id:001-AOQ-559&token:_mch-nrf.com-1670390880380-75930; _gcl_au=1.1.2038696798.1670390881; _fbp=fb.1.1670390883643.14140490; cb_user_id=null; cb_group_id=null; cb_anonymous_id=%22a8dc4799-d16a-493d-9a03-74491bf4dd79%22; _hjSessionUser_2005052=eyJpZCI6IjkyYjZmNTE1LWU4NWYtNWMyOS1hOWM3LTBmNjY5YjM1N2FjNSIsImNyZWF0ZWQiOjE2NzAzOTA4ODQ0NjYsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.971742407.1670500484; ln_or=d; _hjIncludedInSessionSample=0; _hjSession_2005052=eyJpZCI6ImNiZDNkZmI4LWJkYzktNDc3YS04NTQ0LTE5ZWJiMWQyODI5MiIsImNyZWF0ZWQiOjE2NzA1MDA0ODY5MDIsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; _gat=1; __unam=78d5276-184eb0dfe56-7042980f-27; _ga=GA1.1.1829782061.1670390879; _ga_39FVVE9CL0=GS1.1.1670500486.3.1.1670501146.0.0.0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        response1 = requests.get(all_exhibitors_url, headers=headers1)
        soup1 = BeautifulSoup(response1.text, 'html.parser')
        exhibitor_company_name = soup1.find("div",{"class":"company_name"}).text.strip()
        exhibitor_city = soup1.find("div",{"class":"company_contact_city_state"}).text.strip().split(",")[0]
        try:
            exhibitor_state = soup1.find("div",{"class":"company_contact_city_state"}).text.strip().split(", ")[1]
        except:
            exhibitor_state = ''
        exhibitor_country = soup1.find("div",{"class":"company_country"}).text.strip()
        try:
            exhibitor_description = soup1.find("div",{"class":"views-field views-field-body"}).find("div",{"class":"field-content"}).text.strip()
        except:
            exhibitor_description = ''
        try:
            exhibitor_website = soup1.find("div",{"class":"company_website"}).find("a")["href"]
            if "https:" in exhibitor_website:
                exhibitor_website = exhibitor_website
            else:
                exhibitor_website = "https:" + exhibitor_website
        except:
            exhibitor_website = ''
        try:
            exhibitor_linkedin = soup1.find("div",{"class":"company_linkedin"}).find("a")["href"]
        except:
            exhibitor_linkedin = ''
        exhibitors_page_url = all_exhibitors_url
        store =[exhibitor_company_name,exhibitor_city,exhibitor_state,exhibitor_country,exhibitor_description,exhibitor_website,exhibitor_linkedin,exhibitors_page_url]
        yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()