import requests
import csv
from bs4 import BeautifulSoup
import json

def write_output(data):
	with open('stockx.csv', mode='a', newline="", encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["title","primaryTitle","secondaryTitle","condition","primaryCategory","Style","Colorway","retailPrice","releaseDate","smallImageUrl","brand","model","description","styleId","currencyCode","countryCode","marketName","lowestAsk","numberOfAsks","highestBid","numberOfBids","annualHigh","annualLow","volatility","pricePremium","lastSale","changeValue","changePercentage","salesLast72Hours","size_wise_prices","page_url"])
		for row in data:
			writer.writerow(row)

def fetch_data():
    # proxies = { 'https' : 'https://brd-customer-c_878f6dc2-zone-zone_priceline_development-country-us:ixuzrn0hwwpw@zproxy.lum-superproxy.io:22225' }
    for i in range(1,26):
        print(i)
        url = "https://stockx.com/sneakers?page=" + str(i)
        headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'cookie': 'stockx_device_id=27b0cac3-59dc-4b8b-822c-8fd25423c6bf; language_code=en; stockx_selected_region=US; pxcts=7c14f0e7-84ed-11ed-9579-48765a78614c; _pxvid=7c14e0e7-84ed-11ed-9579-48765a78614c; __pxvid=7cf2bd1f-84ed-11ed-9d2e-0242ac120002; _ga=GA1.2.132085627.1672039111; _gid=GA1.2.718858729.1672039111; _gcl_au=1.1.366429463.1672039112; ajs_anonymous_id=525b7f16-eb79-4eea-80a8-ec7573557ed5; rbuid=rbcr-95848696-810e-4f8c-a225-ac7bb739ae75; _pin_unauth=dWlkPU1qYzNOVGcxTTJJdFlUa3laUzAwT1dZd0xXRTVNRFV0T0dReU5UY3pOREppT1RrNA; IR_gbd=stockx.com; _rdt_uuid=1672039117689.f2be3324-b3de-4bce-b4a6-491295f03b1b; __pdst=2c485001a10c4a3099da12290224f58f; rskxRunCookie=0; rCookie=solphfa49x8604wz4nungolc4gx9u4; __ssid=5fac71da3bc003e36d50ebc1b090fa4; QuantumMetricUserID=026f533f70dafbeb8f42db2ea0c59e9a; stockx_homepage=sneakers; stockx_preferred_market_activity=sales; _ga=GA1.2.132085627.1672039111; _px3=a8b2ee2297a3995698aca5bb819952dd3efbb742e953de0c8f1e6ed55c33edec:QlXM/yur4K+nk3f8arFRG227NdD5YMK/pogFYooTetgVaGZwQmJU/v/bBNuR2C2Zh0IktsSze7NpSFAKgQ37UA==:1000:t8Eu6bd/LCn/wBg64bUFnWrhb5t8okfKoAx5KnSqAAXJvvAxSMOQpR1d5wZHROf5wp/w5KOdwRhjlVrSaBVia85WITJj4ZZ7nAAbiSX1IyTD+2EHq5OmF/2T1UHpn5zFil7lFxRM3iXOq0oAAPhNCrbPm4g6QarfWpvZnFYFE9c41fzR3rPHai0WMJGVtkQ/UsqU4jPperLtTXcOQlbCZg==; stockx_session=%22b0e9f96f-d680-4abb-a1bb-5a2a3e146d95%22; __cf_bm=eRI18FInJIx8n1T0lB2BiMqDAC4XSu4vwGGuAIxQOBM-1672045514-0-AVHS5Ewk5FZoA7xq3DW2arb688b7LRCtBFo0Kbh5Bk0bC0chxKnsOY0BXg8OYjkRAllwb+aM3pwTTqESe68Fr5k=; _gat=1; lastRskxRun=1672045519603; _uetvid=812df6a084ed11edb71faf621b68bd83; QuantumMetricSessionID=273626458a4fd962eb77cb064dde5758; stockx_product_visits=3; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; _pxff_idp_c=1,s; _pxff_fed=5000; _pxde=148bd9d110b144cf0ea154dbad7b07acb2f2353744174facf8242ff497d97828:eyJ0aW1lc3RhbXAiOjE2NzIwNDU1MjIxNjUsImZfa2IiOjB9; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Dec+26+2022+14%3A35%3A26+GMT%2B0530+(India+Standard+Time)&version=202211.2.0&isIABGlobal=false&hosts=&consentId=0092244c-ac2a-4d51-9f4b-15afc4315970&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CC0005%3A1%2CC0003%3A1&AwaitingReconsent=false; IR_9060=1672045526269%7C0%7C1672045526269%7C%7C; IR_PI=83798cc7-84ed-11ed-a762-e5e3795d3b5c%7C1672131926269; _dd_s=rum=0&expire=1672046426054; forterToken=60f741f43f2b471dbe0dff774fb53888_1672045525972__UDF43_13ck; _uetsid=812dbaa084ed11edad90d77b9e27b263',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
        # response = requests.request("GET", url, headers=headers, proxies=proxies)
        response = requests.request("GET", url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = str(soup.find("script",{"data-name":"query"})).split("window.__REACT_QUERY_STATE__ = ")[1].strip().split("</script>")[0].replace("}]};","}]}")
        json_data = json.loads(data)
        for datas in json_data["queries"][4]["state"]["data"]["browse"]["results"]["edges"]:
            urls = "https://stockx.com/" + datas["node"]["urlKey"]
            print(urls)
            response1 = requests.request("GET", urls, headers=headers)
            soup1 = BeautifulSoup(response1.text, 'html.parser')
            data1 = str(soup1.find("script",{"data-name":"query"})).split("window.__REACT_QUERY_STATE__ = ")[1].strip().split("</script>")[0].replace("}]};","}]}")
            json_data1 = json.loads(data1)

            title = json_data1["queries"][2]["state"]["data"]["product"]["title"]
            primaryTitle = json_data1["queries"][2]["state"]["data"]["product"]["primaryTitle"]
            secondaryTitle = json_data1["queries"][2]["state"]["data"]["product"]["secondaryTitle"]
            condition = json_data1["queries"][2]["state"]["data"]["product"]["condition"]
            primaryCategory = json_data1["queries"][2]["state"]["data"]["product"]["primaryCategory"]
            Style = json_data1["queries"][2]["state"]["data"]["product"]["traits"][0]["value"]
            Colorway = json_data1["queries"][2]["state"]["data"]["product"]["traits"][1]["value"]
            retailPrice = json_data1["queries"][2]["state"]["data"]["product"]["traits"][2]["value"]
            releaseDate = json_data1["queries"][2]["state"]["data"]["product"]["traits"][3]["value"]
            smallImageUrl = json_data1["queries"][2]["state"]["data"]["product"]["media"]["smallImageUrl"]
            brand = json_data1["queries"][2]["state"]["data"]["product"]["brand"]
            model = json_data1["queries"][2]["state"]["data"]["product"]["model"]
            description = str(json_data1["queries"][2]["state"]["data"]["product"]["description"]).replace("<br>","").replace("  ","").replace("\\n","").strip()
            styleId = json_data1["queries"][2]["state"]["data"]["product"]["styleId"]
            currencyCode = json_data1["queries"][2]["queryKey"][1]["variables"]["currencyCode"]
            countryCode = json_data1["queries"][2]["queryKey"][1]["variables"]["countryCode"]
            marketName = json_data1["queries"][2]["queryKey"][1]["variables"]["marketName"]
            lowestAsk = json_data1["queries"][2]["state"]["data"]["product"]["market"]["bidAskData"]["lowestAsk"]
            numberOfAsks = json_data1["queries"][2]["state"]["data"]["product"]["market"]["bidAskData"]["numberOfAsks"]
            highestBid = json_data1["queries"][2]["state"]["data"]["product"]["market"]["bidAskData"]["highestBid"]
            numberOfBids = json_data1["queries"][2]["state"]["data"]["product"]["market"]["bidAskData"]["numberOfBids"]
            annualHigh = json_data1["queries"][2]["state"]["data"]["product"]["market"]["salesInformation"]["annualHigh"]
            annualLow = json_data1["queries"][2]["state"]["data"]["product"]["market"]["salesInformation"]["annualLow"]
            volatility = json_data1["queries"][2]["state"]["data"]["product"]["market"]["salesInformation"]["volatility"]
            pricePremium = json_data1["queries"][2]["state"]["data"]["product"]["market"]["salesInformation"]["pricePremium"]
            lastSale = json_data1["queries"][2]["state"]["data"]["product"]["market"]["salesInformation"]["lastSale"]
            changeValue = json_data1["queries"][2]["state"]["data"]["product"]["market"]["salesInformation"]["changeValue"]
            changePercentage = json_data1["queries"][2]["state"]["data"]["product"]["market"]["salesInformation"]["changePercentage"]
            salesLast72Hours = json_data1["queries"][2]["state"]["data"]["product"]["market"]["salesInformation"]["salesLast72Hours"]
            size_wise_price = []
            count = 0
            while True:
                try:
                    data3 = json_data1["queries"][2]["state"]["data"]["product"]["variants"][count]["sizeChart"]["displayOptions"][0]["size"]
                    data4 = str(json_data1["queries"][2]["state"]["data"]["product"]["variants"][count]["market"]["bidAskData"]["lowestAsk"]).replace("None","Price not confirmed")
                    size_wise_price.append(data3 +": "+ data4)
                except:
                    break
                count += 1
            size_wise_prices = ", ".join(size_wise_price)
            page_url = urls

            store = [title,primaryTitle,secondaryTitle,condition,primaryCategory,Style,Colorway,retailPrice,releaseDate,smallImageUrl,brand,model,description,styleId,currencyCode,countryCode,marketName,lowestAsk,numberOfAsks,highestBid,numberOfBids,annualHigh,annualLow,volatility,pricePremium,lastSale,changeValue,changePercentage,salesLast72Hours,size_wise_prices,page_url]
            yield store
            
def scrape():
    data = fetch_data()
    write_output(data)
scrape()
