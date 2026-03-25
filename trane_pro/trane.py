import csv
import requests
import json
from bs4 import BeautifulSoup

def write_output(data):
	with open('trane.csv', mode='a',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name","city","state","zipcode","address","phone_no","page_url"])
		for row in data:
			writer.writerow(row)
def fetch_data():
    url = "https://www.trane.com/residential/en/dealers/"
    headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "cookie": "googleClientIdFired=1; filo-alias=ffbd3ce6-9300-4916-bf67-146d8bec378f; filodom-autopop-pops=1; filodom-window-state=open; filodom-notifications=0; chsn_cnsnt=www.trane.com%3AC0001%2CC0002%2CC0003%2CC0004%2CC0005; tglr_anon_id=169d3ec3-c2cc-4bb5-8dd2-78cc8bf60fc5; tglr_sess_id=ffbd3ce6-9300-4916-bf67-146d8bec378f; tglr_req=https://www.trane.com/residential/en/dealer-locator/; tglr_sess_count=1; tglr_tenant_id=fb26b6c1-d34d-4e35-9034-50a17b8f322a; pmpdid=c1d85b9f-aa11-49a5-bc42-c0ecc15767a3; cohsn_xs_id=d52fa462-5933-470c-b90c-b52c4f647e29; _gid=GA1.2.255896703.1670651577; _gcl_au=1.1.1073919069.1670651580; fuseid=8cd7b53a-4247-4a34-8b66-de5c2251bdee; _fbp=fb.1.1670651584426.1963678522; _tt_enable_cookie=1; _ttp=86552456-1e6d-4dea-8e66-20b71784234c; _mkto_trk=id:313-JXD-585&token:_mch-trane.com-1670651586300-67532; BVBRANDID=52c96b33-2c00-4798-9312-8fa7ffa34b5b; BVBRANDSID=51b0e499-48f2-4a73-9b76-e5ccabacb5b0; tglr_ref=https://www.trane.com/residential/en/dealer-locator/; com.silverpop.iMAWebCookie=73593188-b607-4086-9a14-bb8ebb25036c; com.silverpop.iMA.session=8e4ba173-eab1-ebc3-3009-728dc5d32cbb; mdLogger=false; kampyle_userid=9aff-dd71-9368-2bbc-92ee-dce4-5384-52d4; DECLINED_DATE=1670651931530; com.silverpop.iMA.page_visit=1411630337:-769136895:; kampyleUserSession=1670651974826; kampyleUserSessionsCount=2; kampyleSessionPageCounter=1; kampyleUserPercentile=43.89922763866358; ONSITE_SESSION_TAB_644801309536=644801309536; kampylePageLoadedTimestamp=1670651974847; da_sid=7805F42E8E3DAE8824AFAA13B0ACFCDEBE|3|0|3; da_lid=4B36C71D9A7DEA13B1FEBB99F2AEB6D50D|0|0|0; da_intState=; _gat=1; _ga_Q6NCWTX4FM=GS1.1.1670651585.1.1.1670652429.0.0.0; _ga=GA1.1.169d3ec3-c2cc-4bb5-8dd2-78cc8bf60fc5; _uetsid=eae67660784e11ed99f7b36c05c9a7c9; _uetvid=eae68560784e11ed82273db00ba43e77",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    response = requests.request("GET", url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    item = "'''" + str(soup.find("script",{"type":"application/json"})) + "'''"
    soup1 = BeautifulSoup(item, 'html.parser')
    data = soup1.find("script")
    json_object = json.loads(data.contents[0])

    for datas in json_object['props']['pageProps']['dealerList']['nodes']:
        trane_all_page_urls = "https://www.trane.com/residential/en/dealers/" + datas['uri'].replace("/dealer_list/","")
        print(trane_all_page_urls)
        if trane_all_page_urls == "https://www.trane.com/residential/en/dealers/temp-control-nashville-tn/":
            continue
        headers1 = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "cookie": "filodom-notifications=1; filo-alias=56ddbedd-7d84-4b5d-8775-b7059ff07e7e; googleClientIdFired=1; filodom-autopop-pops=1; filodom-window-state=open; filodom-notifications=1; filo-alias=56ddbedd-7d84-4b5d-8775-b7059ff07e7e; chsn_cnsnt=www.trane.com%3AC0001%2CC0002%2CC0003%2CC0004%2CC0005; tglr_anon_id=169d3ec3-c2cc-4bb5-8dd2-78cc8bf60fc5; tglr_tenant_id=fb26b6c1-d34d-4e35-9034-50a17b8f322a; pmpdid=c1d85b9f-aa11-49a5-bc42-c0ecc15767a3; cohsn_xs_id=d52fa462-5933-470c-b90c-b52c4f647e29; _gid=GA1.2.255896703.1670651577; _gcl_au=1.1.1073919069.1670651580; fuseid=8cd7b53a-4247-4a34-8b66-de5c2251bdee; _fbp=fb.1.1670651584426.1963678522; _tt_enable_cookie=1; _ttp=86552456-1e6d-4dea-8e66-20b71784234c; _mkto_trk=id:313-JXD-585&token:_mch-trane.com-1670651586300-67532; BVBRANDID=52c96b33-2c00-4798-9312-8fa7ffa34b5b; com.silverpop.iMAWebCookie=73593188-b607-4086-9a14-bb8ebb25036c; mdLogger=false; kampyle_userid=9aff-dd71-9368-2bbc-92ee-dce4-5384-52d4; DECLINED_DATE=1670651931530; tglr_sess_id=56ddbedd-7d84-4b5d-8775-b7059ff07e7e; tglr_req=https://www.trane.com/residential/en/dealers/; tglr_sess_count=3; tglr_ref=https://www.trane.com/residential/en/dealers/; BVBRANDSID=b7fecd34-3fc5-4e73-81f6-57af4036c83b; com.silverpop.iMA.session=2ae57d0d-ea24-7163-8675-794e2beeacd5; kampyleUserSession=1670671955877; kampyleUserSessionsCount=5; kampyleUserPercentile=53.25259318773809; ONSITE_SESSION_TAB_195861766000=195861766000; com.silverpop.iMA.page_visit=1189317235:1411630337:1547978029:; da_sid=918F25598E32AE8C0B00AA13B0ADB6EFA9|3|0|3; da_lid=4B36C71D9A7DEA13B1FEBB99F2AEB6D50D|0|0|0; da_intState=0; kampyleSessionPageCounter=2; kampylePageLoadedTimestamp=1670672659292; _gat=1; _uetsid=eae67660784e11ed99f7b36c05c9a7c9; _uetvid=eae68560784e11ed82273db00ba43e77; _ga_Q6NCWTX4FM=GS1.1.1670671949.3.1.1670672792.0.0.0; _ga=GA1.1.169d3ec3-c2cc-4bb5-8dd2-78cc8bf60fc5",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        response1 = requests.request("GET", trane_all_page_urls, headers=headers1)
        status_code = response1.status_code
        if status_code == 500:
            continue
        soup1 = BeautifulSoup(response1.text, 'html.parser')
        name =  datas['title']
        print(name)
        try:
            phone_no = soup1.find("div",{"class":"bg-white grid grid-cols-1 md:grid-cols-2 gap-2 p-6 mb-1"}).find("a").text.strip()
        except:
            phone_no = ''
        try:
            city = datas['dealerDetails']['city']
        except:
            city = ''
        try:
            state = datas['dealerDetails']['state']
        except:
            state = ''
        try:
            zipcode = datas['dealerDetails']['zipcode']
        except:
            zipcode = ''
        try:
            address = str(city) +" "+ str(state) +", "+ datas['dealerDetails']['country'] +"-"+ str(zipcode)
        except:
            address = ''
        page_url = trane_all_page_urls
        store =[name,city,state,zipcode,address,phone_no,page_url]
        yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()