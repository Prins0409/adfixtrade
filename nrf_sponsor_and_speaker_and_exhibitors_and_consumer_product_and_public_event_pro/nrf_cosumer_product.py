import csv
from bs4 import BeautifulSoup
import requests
import json

def write_output(data):
	with open('nrf_cosumer_product.csv', mode='w',newline="",encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["cosumer_product_company_name","cosumer_product_city","cosumer_product_state","cosumer_product_country","cosumer_product_description","cosumer_product_website","cosumer_product_linkedin","cosumer_products_page_url"])
		for row in data:
			writer.writerow(row)

def fetch_data():
    url = "https://img14.a2zinc.net/api/exhibitor?callback=jQuery211009364610515548777_1670568894771&mapId=124&eventId=167&appId=VEANgX18thjf0ErIFC5hDuFEAu9oy033HnuyF7j4IFnEursxdYEROXEzR7yFZCmI&floorplanViewType=View4&langId=1&boothId=&shMode=E&minLblSize=2&maxLblSize=10&minCnSize=2&maxCnSize=11&_=1670568894774"
    headers = {
    "accept": "*/*",
    "referer": "https://events.nrf.com/annual2023/Public/eventmap.aspx?shmode=E&thumbnail=1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    data = response.text.replace("jQuery211009364610515548777_1670568894771([{","[{").replace("]}}])","]}}]")
    json_data = json.loads(data)

    for i in range(0,61):
        name = json_data[i]['name'].lower().replace(" ","-")
        if name == "":
            continue
        all_cosumer_product_url = "https://nrfbigshow.nrf.com/company/" + name.replace("the-","").replace("-&","").replace(".","").replace("!","").replace("'","").replace("vitavate™","vitavatetm")
        if all_cosumer_product_url == "https://nrfbigshow.nrf.com/company/dress-it-up":
            continue
        if all_cosumer_product_url == "https://nrfbigshow.nrf.com/company/mr-tortilla,-inc":
            continue
        if all_cosumer_product_url == "https://nrfbigshow.nrf.com/company/smell-of-love-candles,-llc":
            continue
        headers1 = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Cookie": "__sharethis_cookie_test__=1; _mkto_trk=id:001-AOQ-559&token:_mch-nrf.com-1670390880380-75930; _gcl_au=1.1.2038696798.1670390881; _fbp=fb.1.1670390883643.14140490; cb_user_id=null; cb_group_id=null; cb_anonymous_id=%22a8dc4799-d16a-493d-9a03-74491bf4dd79%22; _hjSessionUser_2005052=eyJpZCI6IjkyYjZmNTE1LWU4NWYtNWMyOS1hOWM3LTBmNjY5YjM1N2FjNSIsImNyZWF0ZWQiOjE2NzAzOTA4ODQ0NjYsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.971742407.1670500484; ln_or=d; _hjSession_2005052=eyJpZCI6IjhlNjQzMDQ5LTMyMGUtNGE2ZC1iM2NiLWNkMWFkYWY3OGUyMyIsImNyZWF0ZWQiOjE2NzA1Njg2OTI5MTIsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; __unam=78d5276-184eb0dfe56-7042980f-34; _hjIncludedInPageviewSample=1; _hjIncludedInSessionSample=0; _ga=GA1.1.1829782061.1670390879; _ga_39FVVE9CL0=GS1.1.1670568691.4.1.1670570411.0.0.0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        response1 = requests.get(all_cosumer_product_url, headers=headers1)
        soup1 = BeautifulSoup(response1.text, 'html.parser')
        cosumer_product_company_name = soup1.find("div",{"class":"company_name"}).text.strip()
        print(cosumer_product_company_name)
        cosumer_product_city = soup1.find("div",{"class":"company_contact_city_state"}).text.strip().split(",")[0]
        try:
            cosumer_product_state = soup1.find("div",{"class":"company_contact_city_state"}).text.strip().split(", ")[1]
        except:
            cosumer_product_state = ''
        cosumer_product_country = soup1.find("div",{"class":"company_country"}).text.strip()
        try:
            cosumer_product_description = soup1.find("div",{"class":"views-field views-field-body"}).find("div",{"class":"field-content"}).text.strip()
        except:
            cosumer_product_description = ''
        try:
            cosumer_product_website = soup1.find("div",{"class":"company_website"}).find("a")["href"]
        except:
            cosumer_product_website = ''
        try:
            cosumer_product_linkedin = soup1.find("div",{"class":"company_linkedin"}).find("a")["href"]
        except:
            cosumer_product_linkedin = ''
        cosumer_products_page_url = all_cosumer_product_url
        store =[cosumer_product_company_name,cosumer_product_city,cosumer_product_state,cosumer_product_country,cosumer_product_description,cosumer_product_website,cosumer_product_linkedin,cosumer_products_page_url]
        yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()