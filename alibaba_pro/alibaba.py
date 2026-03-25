from bs4 import BeautifulSoup
import requests
import csv, json

def write_output(data):
	with open('alibaba.csv', mode='a', newline="", encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["title","sku_id","rating","min_order","description","images","sample_item_price","prices","certificate_CE","certificate_FCC","seller_name","seller_country","seller_year","review_count","tags","verify_tag_url","main_product","video_url","page_url"])
		for row in data:
			writer.writerow(row)

def fetch_data():
    for i in range(1,101):
        print(i)
        url = "https://www.alibaba.com/trade/search?spm=a2700.galleryofferlist.0.0.274c4e12oIyV1k&fsb=y&IndexArea=product_en&keywords=ram&tab=all&viewtype=L&&page=" + str(i)
        headers = {
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        response = requests.request("GET", url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = str(soup).split("window.__page__data__config = ")[1].split("window.__page__data = window.__page__data__config.props")[0]
        json_data = json.loads(data)
        for data1 in json_data["props"]["offerResultData"]["offerList"]:
            urls = "https:" + data1["information"]["productUrl"]
            print(urls)
            response1 = requests.request("GET", urls, headers=headers)
            soup1 = BeautifulSoup(response1.text, 'html.parser')
            data2 = str(soup1.find("script",{"type":"application/ld+json"})).replace('<script type="application/ld+json">',"").replace('</script>',"")
            json_data1 = json.loads(data2)
            page_url = urls
            data8 = str(soup1).split('window.detailData = ')[1].split('window.detailData.scVersion =')[0].replace("\\n","").replace("\\r","")
            json_data2 = json.loads(data8)
            title = json_data2["globalData"]["product"]["subject"]
            sku_id = json_data2["globalData"]["buyer"]["fastFeedBackView"]["feedBackObjectId"]
            rating = json_data2["globalData"]["seller"]["supplierRatingReviews"]["averageStar"]
            min_order = json_data2["globalData"]["i18n"]["202107_detail_pc_ShippingFloor_MOQ"]
            try:
                description = json_data1[0]["description"].strip()
            except:
                description = json_data1["description"].strip()
            image = []
            for data3 in soup1.find("div",{"class":"detail-next-slick-container detail-next-slick-initialized"}).find_all("img"):
                data4 = data3["src"]
                image.append(data4)
            images = ", ".join(image)
            try:
                sample_item_price = soup1.find("strong",{"class":"sample-item"}).text.strip()
            except:
                sample_item_price = ''
            price = []
            try:
                for data7 in soup1.find("div",{"class":"product-price"}).find("div",{"class":"price-range"}):
                    price.append(data7.text.strip().split("|")[0].replace(",",""))
            except:
                for price_count in soup1.find("div",{"class":"product-price"}).find_all("div",{"class":"price-item"}):
                    data5 = price_count.find("div",{"class":"quality"}).text.strip()
                    data6 = price_count.find("div",{"class":"price"}).text.strip()
                    data7 = str(data5) + "=" + str(data6)
                    price.append(data7) 
            prices = ", ".join(price)
            try:
                certificate_CE = soup1.find("a",{"class":"company-qualificationCertificate service-3"}).find("div",{"class":"attr-item"}).find("div",{"class":"attr-content"}).find("img",{"title":"CE"})["src"]
            except:
                certificate_CE = ''
            try:
                certificate_FCC = soup1.find("a",{"class":"company-qualificationCertificate service-3"}).find("div",{"class":"attr-item"}).find("div",{"class":"attr-content"}).find("img",{"title":"FCC"})["src"]
            except:
                certificate_FCC = ''
            try:
                seller_name = json_data2["globalData"]["seller"]["accountFirstName"]
            except:
                seller_name = ''
            try:
                seller_country = json_data2["globalData"]["seller"]["companyRegisterCountry"]
            except:
                seller_country = ''
            try:
                seller_year = json_data2["globalData"]["seller"]["companyJoinYears"]
            except:
                seller_year = ''
            try:
                review_count = json_data2["globalData"]["seller"]["supplierRatingReviews"]["totalReviewOrderCount"]
            except:
                review_count = ''
            try:
                tags = json_data2["globalData"]["i18n"]["Verified.tag.detail.mj"]
            except:
                tags = ''
            try:
                verify_tag_url = "https:" + soup1.find("div",{"class":"card-central-logo"}).find("a")["href"]
            except:
                verify_tag_url = ''
            try:
                main_product = json_data2["globalData"]["seo"]["breadCrumb"]["pathList"][4]["hrefObject"]["name"]
            except:
                main_product = json_data2["globalData"]["seo"]["breadCrumb"]["pathList"][3]["hrefObject"]["name"]
            try:
                video_url = json_data2["globalData"]["product"]["mediaItems"][0]["videoUrl"]["sd"]["videoUrl"]
            except:
                video_url = ''
            store =[title,sku_id,rating,min_order,description,images,sample_item_price,prices,certificate_CE,certificate_FCC,seller_name,seller_country,seller_year,review_count,tags,verify_tag_url,main_product,video_url,page_url]
            yield store

def scrape():
    data = fetch_data()
    write_output(data)
scrape()
