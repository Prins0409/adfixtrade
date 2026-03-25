from encodings.utf_8 import encode
from bs4 import BeautifulSoup
import requests
import csv, json

def write_output(data):
	with open('yellow_pages.csv', mode='a', newline="", encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["title_name","address_country","street_address","address_locality","address_region","telephone","email","website_url","check_claimed_or_not","ratings","description","open_hours","categories","other_phone_no","other_websites","page_urls"])
		for row in data:
			writer.writerow(row)

def fetch_data():
    for i in range(80,87):
        print(i)
        url = "https://www.yellowpages.com/search?search_terms=banks&geo_location_terms=new%20york&page=" + str(i)
        headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Cookie": "vrid=fbfdb6e2-9cde-4ff0-b05d-9553c0e5ac4e; bucket=ypu%3Aypu%3Aserpbpp-cta2; bucketsrc=front; zone=330; AMCVS_A57E776A5245AEA80A490D44%40AdobeOrg=1; _ga=GA1.2.514696195.1671281276; s_ecid=MCMID%7C39174526133917522652960014234873387842; s_cc=true; s_prop70=December; s_prop71=51; location=geo_term%3ANew%20York%2C%20NY%7Clat%3A40.7142691%7Clng%3A-74.0059729%7Ccity%3ANew%20York%7Cstate%3ANY%7Cdisplay_geo%3ANew%20York%2C%20NY; search_terms=banks; sorted=false; __gsas=ID=3f3cbc2716e74501:T=1671281537:S=ALNI_MZpE_sBW92XnicZQAzgoUaQhGpfPg; __gads=ID=72cde059d89e6e02:T=1671281537:S=ALNI_MZ5HMA9lIQwOlvZjp9NB8KhnUDb7w; s_sq=%5B%5BB%5D%5D; express:sess=eyJka3MiOiJlNjJlNTczOC1kMzE5LTQ0MTItOTE3Ni1hOTJlYzJlMDg4NTQiLCJmbGFzaCI6e30sInByZXZpb3VzUGFnZSI6InNycCJ9; express:sess.sig=KbZ8dSCE0z9sdjEf-4e2QzZGdnA; s_nr=1671283585641; AMCV_A57E776A5245AEA80A490D44%40AdobeOrg=-1303530583%7CMCIDTS%7C19346%7CMCMID%7C39174526133917522652960014234873387842%7CMCAAMLH-1672031013%7C12%7CMCAAMB-1672031013%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1671433413s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.3.0; _gid=GA1.2.1598160574.1671426214; _gat=1; __gpi=UID=00000b923aa2bc83:T=1671281537:RT=1671426217:S=ALNI_MYiIMMWJarrNysa-yM6TTPmuVM4eQ; s_tp=7746; s_ppv=search_results%2C26%2C26%2C2023",
        "Referer": "https://www.yellowpages.com/search?search_terms=banks&geo_location_terms=Gurgaon%2C+10",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        response = requests.request("GET", url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        for data in soup.find_all("div",{"class":"info-section info-primary"}):
            urls = "https://www.yellowpages.com" + data.find("a")["href"]
            page_urls = urls
            print(urls)
            response1 = requests.request("GET", urls, headers=headers)
            soup1 = BeautifulSoup(response1.text, 'html.parser')
            data1 = str(soup1.find("script",{"type":"application/ld+json"})).replace('<script type="application/ld+json">',"").replace('</script>',"").strip()
            json_data = json.loads(data1)
            title_name = json_data["name"]
            try:
                address_country = json_data["address"]["addressCountry"]
            except:
                address_country = ''
            try:
                street_address = json_data["address"]["streetAddress"]
            except:
                street_address = ''
            try:
                address_locality = json_data["address"]["addressLocality"]
            except:
                address_locality = ''
            try:
                address_region = json_data["address"]["addressRegion"]
            except:
                address_region = ''
            try:
                telephone = json_data["telephone"]
            except:
                telephone = ''
            try:
                email = json_data["email"].replace("mailto:","")
            except:
                email = ''
            try:
                website_url = json_data["url"]
            except:
                website_url = ''
            try:
                check_claimed_or_not = soup1.find("div",{"class":"mobile-claimed-category"}).find("div",{"id":"claimed"}).text.replace("claimed","Claimed")
            except:
                check_claimed_or_not = "Not Claimed"
            try:
                ratings = str(soup1.find("div",{"class":"mobile-ratings"}).find("a",{"class":"yp-ratings"}).find("div")["class"]).replace("[","").replace("]","").replace("'","").replace(",","").replace("rating-stars","").strip()
            except:
                ratings = ''
            try:
                description = soup1.find("dd",{"class":"general-info"}).text
            except:
                description = ''
            open_hours = soup1.find("section",{"id":"aside-hours"}).find("dd",{"class":"open-hours"}).text.replace("Hours","Hours:").replace(" pm"," pm & ").strip()
            categories = soup1.find("dd",{"class":"categories"}).find("div",{"class":"categories"}).text.strip()
            try:
                other_phone_no = str(soup1.find("dd",{"class":"extra-phones"}).find_all("p")).replace("[","").replace("]","").replace("<p>","").replace("</span>","").replace("</p>","").replace("<span>","").replace("rating-stars","").strip()
            except:
                other_phone_no = ''
            try:
                other_website = []
                for data2 in soup1.find("dd",{"class":"weblinks"}).find_all("a"):
                    other_links = data2.text
                    other_website.append(other_links)
                other_websites = ", ".join(other_website)
            except:
                other_websites = ''

            store =[title_name,address_country,street_address,address_locality,address_region,telephone,email,website_url,check_claimed_or_not,ratings,description,open_hours,categories,other_phone_no,other_websites,page_urls]
            yield store

def scrape():
    data = fetch_data()
    write_output(data)
scrape()
