import requests
from bs4 import BeautifulSoup
import csv

def write_output(data):
    with open('royal_building_products.csv', mode='a',newline="", encoding="utf-8") as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(["name","address","phone","website","product_content"])
        for row in data:
            writer.writerow(row)
def fetch_data():
    # for data1 in open("latitude_and_longitude.csv",'r',encoding='utf-8'):
    #     print(data1.strip())
    url = "https://www.royalbuildingproducts.com/product-locator-stores?d_option=10mi&pl-accordion-1=on&b_tid%255B%255D=1885__10&pl-accordion-2=on&u_proximity=40.75368539999999%2C-73.9991637%3C%3D10mi&b_tid=347__0%2C2__1%2C3__2%2C4__3%2C1966__4%2C1967__5%2C1__6%2C1968__7%2C1969__8%2C1970__9%2C1885__10&s_type=all__0%2Call__1%2Call__2%2Call__3%2Call__4%2Call__5%2Call__6%2Call__7%2Call__8%2Call__9%2Call__10"
    # url = "=40.75368539999999%2C-73.9991637%3C%3D"
    # url = "=29.752554%2C-95.37040089999999%3C%3D"
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,gu;q=0.4,de;q=0.3',
    'cache-control': 'max-age=0',
    'cookie': '_gcl_au=1.1.1652423462.1670647711; sa-user-id=s%253A0-0adff713-6ad0-4af7-7d92-0fc81e31bfd2.bzJ%252FaevXRAESXVtgcpR8GvLP1mlXpQvqlFlL2NEYb7Y; sa-user-id-v2=s%253ACt_3E2rQSvd9kg_IHjG_0lknaMI.tLcuQzOcfiEtCDGoKHxoW8HqExSbTuyqMSwYDtNss9M; _fbp=fb.1.1670647713973.1173983589; _pin_unauth=dWlkPU1qYzNOVGcxTTJJdFlUa3laUzAwT1dZd0xXRTVNRFV0T0dReU5UY3pOREppT1RrNA; __qca=P0-1611937541-1670647712649; page_views=NaN; visitor_id592951=768407697; visitor_id592951-hash=3a0906fdeaa6b18fa81361207e7d945c214a298407399ab3811461f409138ab6ef7ef496c200e6398fc65c14b52599347de395d0; _gid=GA1.2.1499937093.1670826573; ln_or=d; _gat_UA-10776241-1=1; _dc_gtm_UA-10776241-1=1; _ga_F1WN6XFMVG=GS1.1.1670921551.6.1.1670921636.0.0.0; _ga=GA1.1.80558312.1670647712; __atuvc=9%7C49%2C14%7C50; __atuvs=63983d46a10febc5002; _uetsid=55cd70b079e611ed80b3f725d1818280; _uetvid=e69b9530784511ed8822b36f8c40f1f5',
    'if-none-match': 'W/"1670845436"',
    'referer': 'https://www.royalbuildingproducts.com/product-locator-stores?pl-accordion-1=on&b_tid%5B%5D=347__0&b_tid%5B%5D=2__1&b_tid%5B%5D=3__2&b_tid%5B%5D=4__3&b_tid%5B%5D=1966__4&b_tid%5B%5D=1967__5&b_tid%5B%5D=1__6&b_tid%5B%5D=1968__7&b_tid%5B%5D=1969__8&b_tid%5B%5D=1970__9&b_tid%5B%5D=1885__10&pl-accordion-2=on&u_proximity=40.75368539999999%2C-73.9991637%3C%3D50mi&b_tid=347__0%2C2__1%2C3__2%2C4__3%2C1966__4%2C1967__5%2C1__6%2C1968__7%2C1969__8%2C1970__9%2C1885__10&s_type=all__0%2Call__1%2Call__2%2Call__3%2Call__4%2Call__5%2Call__6%2Call__7%2Call__8%2Call__9%2Call__10',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    response = requests.request("GET", url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    for all_data in soup.find_all("div",{"class":"pl_result_box mtn5px hasBorderBottom"}):
        name = all_data.find("div",{"class":"ac_body_section_sub_section_header"}).text.strip()
        address = all_data.find("div",{"class":"ac_body_section_sub_section_content1 titleCase"}).text.strip()
        phone = all_data.find("div",{"class":"tdUnderLine width33 store-contactDetails--item store-contactDetails--phone"}).text.strip()
        try:
            website = all_data.find("div",{"class":"tdUnderLine width33 store-contactDetails--item store-contactDetails--website"}).find("a")["href"]
        except:
            website = ''
        product_content = all_data.find_all("div",{"class":"ac_body_section_sub_section_content1"})[1].text.strip()
        print(name)
        store =[name,address,phone,website,product_content]
        yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()