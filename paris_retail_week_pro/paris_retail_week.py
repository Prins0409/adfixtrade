import requests
from  bs4 import BeautifulSoup
import json,re,csv

def write_output(data):
    with open("parisretailweek.csv", mode="a", encoding="utf-8",newline='') as output_file:
        writer = csv.writer(output_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(["compnay_name","website","facebook","linkdein","twitter","img","city","emails","address","description","presentation","business_challenge","business_sector","business_solution","business_intervention","business_product_name","business_product_description"])
        for row in data:
            writer.writerow(row)

def fetch_data():
    url1 = "https://liste-exposants.hubj2c.com/parisRetailWeek22/list/loadTableForDatatable?lang=en&_=1662719918425"
    response1 = requests.get(url1).json()['data']
    for item in response1:
        print(item['DT_RowId'])
        compnay_name = item['exposant']
        url = "https://liste-exposants.hubj2c.com/parisRetailWeek22/list/getForm"
        payload = "idSociete="+str(item['DT_RowId'])+"&lang=en"
        headers = {
        'Content-Length':'54',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin':'https://liste-exposants.hubj2c.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
        'Cookie':'PHPSESSID=utjccbrsii7968qeekdtdhhrc5'
        }
        response = requests.request("POST", url, headers=headers, data=payload).json()['html']
        soup = BeautifulSoup(response,'lxml')
        with open ("add.txt", "w", encoding="utf-8") as f:
            f.write(str(soup))
        try:
            emails = soup.find("div",{"class":"fe-lien"}).find("a").text
        except:
            emails = ''
        try:
            address = soup.find_all("div",{"class":"fe-colonne"})[1].text
        except:
            address = ''
        try:
            website = soup.find_all("div",{"class":"fe-lien"})[1].find("a")['href']
        except:
            website = ''
        try:
            address = soup.find_all("div",{"class":"fe-colonne"})[1].text.strip()
        except:
            address = ''
        try:    
            img = "https://liste-exposants.hubj2c.com"+soup.find("div",{"class":"fe-colonne-centre"}).find("img")['src']
        except:
            img =''
        try:    
            city = soup.find("div",{"class":"fe-colonne-centre"}).find("img")['title']
        except:
            city = ''
        try:
            description = soup.find("div",{"class":"fe-intervention-titre"}).text                                                                
        except:
            description = ''
        try:
            if 'www.linkedin.com' in soup.find("div",{"class":"fe-bloc-social"}).find("a",{"class":"fe-social"})['href']:
                linkdein = soup.find("div",{"class":"fe-bloc-social"}).find("a",{"class":"fe-social"})['href']
            elif 'www.linkedin.com' in soup.find("div",{"class":"fe-bloc-social"}).find_all("a",{"class":"fe-social"})[1]['href']:
                linkdein = soup.find("div",{"class":"fe-bloc-social"}).find_all("a",{"class":"fe-social"})[1]['href']
            else:
                linkdein = soup.find("div",{"class":"fe-bloc-social"}).find_all("a",{"class":"fe-social"})[2]['href']
        except:
            linkdein = ''
        try:
            if 'www.facebook.com' in soup.find("div",{"class":"fe-bloc-social"}).find("a",{"class":"fe-social"})['href']:
                facebook = soup.find("div",{"class":"fe-bloc-social"}).find("a",{"class":"fe-social"})['href']
            elif 'www.facebook.com' in soup.find("div",{"class":"fe-bloc-social"}).find_all("a",{"class":"fe-social"})[1]['href']:
                facebook = soup.find("div",{"class":"fe-bloc-social"}).find_all("a",{"class":"fe-social"})[1]['href']
            else:
                facebook = soup.find("div",{"class":"fe-bloc-social"}).find_all("a",{"class":"fe-social"})[2]['href']
        except:
            facebook = ''
        try:
            if 'twitter.com' in soup.find("div",{"class":"fe-bloc-social"}).find("a",{"class":"fe-social"})['href']:
                twitter = soup.find("div",{"class":"fe-bloc-social"}).find("a",{"class":"fe-social"})['href']
            elif 'twitter.com' in soup.find("div",{"class":"fe-bloc-social"}).find_all("a",{"class":"fe-social"})[1]['href']:
                twitter = soup.find("div",{"class":"fe-bloc-social"}).find_all("a",{"class":"fe-social"})[1]['href']
            else:
                twitter = soup.find("div",{"class":"fe-bloc-social"}).find_all("a",{"class":"fe-social"})[2]['href']
        except:
            twitter = ''
        presentation = ''
        try:
            presentation_data = soup.find("div",{"class":"col-xl-8 mb-2"}).find("div",{"class":"card-header"}).text
            try:
                if presentation_data == "PRESENTATION":
                    presentation = soup.find("div",{"class":"col-xl-8 mb-2"}).find("div",{"class":"card-block fe-padding"}).text.strip()
            except:
                presentation = ''
        except:
            presentation_data = ''
        try:
            business_challenge = soup.find("div",{"class":"fe-main-business n1"}).text
        except:
            business_challenge = ''
        try:
            business_sector = soup.find("div",{"class":"fe-bloc-activites"}).text.strip()
        except:
            business_sector = ''
        try:
            business_solution = soup.find("div",{"class":"atelierExposantFiche"}).text.strip()
        except:
            business_solution = ''
        try:
            business_intervention = soup.find("div",{"class":"fe-intervention-titre"}).text.strip()
        except:
            business_intervention = ''
        business_product_name = ''
        try:
            for product_name in soup.find_all("div",{"class":"fe-textes-produit"}):
                business_product_name = product_name.find("div",{"class":"fe-titre-produit"}).text
        except:
            business_product_name = ''
        business_product_description = ''
        try:
            for product_description in soup.find_all("div",{"class":"fe-textes-produit"}):
                business_product_description = product_description.find("div",{"class":"fe-designation-produit"}).text
        except:
            business_product_description = ''
        yield [compnay_name,website,facebook,linkdein,twitter,img,city,emails,address,description,presentation,business_challenge,business_sector,business_solution,business_intervention,business_product_name,business_product_description]
def scrape():
    data = fetch_data()
    write_output(data)
scrape()