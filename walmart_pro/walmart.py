import requests
import csv
from bs4 import BeautifulSoup
import json

def write_output(data):
	with open('walmart.csv', mode='a', newline="", encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name","sku","product_code","image","description","model","brand","manufacture_number","category","price","old_price","currency","price_display","rating","review_count","colors_type","size_wise_price","color_wise_price","page_url"])
		for row in data:
			writer.writerow(row)

def fetch_data():
    proxies = { 'https' : 'https://brd-customer-c_878f6dc2-zone-zone_priceline_development-country-us:ixuzrn0hwwpw@zproxy.lum-superproxy.io:22225' } 
    for i in range(1, 26):
        print(i)
        url = "https://www.walmart.com/browse/clothing/men/5438_133197?povid=ApparelNav_MENS_Mens_CP_LHN_Cat_MensShopAll&page="+str(i)+"&affinityOverride=default"
        headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'cookie': 'wmtboid=1672203151-5186715456-17656903680-55177824; _pxhd=c5677e57ce95ec53d47847298482396e4069fac06f8feeab907511a2b57da263:6fd886a7-866b-11ed-a307-796652464248; bm_mi=AC8DFC898445A792FD3709FCC2876961~YAAQ7YwsMVQcXxuFAQAA/CgTVxLjHKyjVem8suIulpyFmk36DdenPJTwGYzhecR0Y+Y5bC8LC9f9zI1snySHad3izuHUUXfmhnA/pTAkHneKnjl7UArSSc0szNsgKKKomPD7OY0bis0mf28qPzKvd61SzOXFM7ReBSql7N/vN13ooUFAGtwYFuDe0sQEgIIDTzJ/90vdu4E8qPDdrQii9sL9v4AZNA4o/B9zg25IaFsWd4R443DLNwXwCoGlyO6rODDYl6MBUnEDDXU98pO94UWUv9jt/6A7QWvuJ9A0+wU8E7UJp25kj/gEniI4WWbHPVraWAY=~1; pxcts=70506e1c-866b-11ed-984f-6c46554b4c48; _pxvid=6fd886a7-866b-11ed-a307-796652464248; auth=MTAyOTYyMDE4pB1jYI%2FHvbm3WI6ekUtOgebyEaixf%2FH02NbRyM1ET0o7%2FllCD1WB7edIqJ752TD%2FJCsZnXTRn5DD3j5GGt0eF3L8XeyvgC%2FI3DRtaPu4mBtGTQhviV0OCArrCCk3TVsb767wuZloTfhm7Wk2Kcjygt6CFmh5hT8BoAhiLFQG8TPDrU%2FNue5miT6rjX6uE2zZh6SDkppm6NgXxw%2Fh8MokafKn14E9dv3f8EiS%2F4IG770UMk70P8glgOEpLOprhDfMM%2FFHGZ2dCNmxWrdkwqEKroRE6tEzF8UHG5mZg9CQrKntlvfRv1xR5lKtfmPlEJ9Nl3auMV5Vn0VJomjlNu1kMJx%2FPlBJ9SDzvYmNZl2UtiDrWfPVO2ipZNMVx9v2EZnC5GKksFL2XtzTImVevB2I9ZE5WBBdZBCyKnCQAR7o6eg%3D; ACID=c7aec169-9aed-4080-b91d-7d6b6e4187f8; hasACID=true; locDataV3=eyJpc0RlZmF1bHRlZCI6dHJ1ZSwiaW50ZW50IjoiU0hJUFBJTkciLCJwaWNrdXAiOlt7ImJ1SWQiOiIwIiwibm9kZUlkIjoiMzA4MSIsImRpc3BsYXlOYW1lIjoiU2FjcmFtZW50byBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5NTgyOSIsImFkZHJlc3NMaW5lMSI6Ijg5MTUgR2VyYmVyIFJvYWQiLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6Ijk1ODI5LTAwMDAifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjM4LjQ4MjY3NywibG9uZ2l0dWRlIjotMTIxLjM2OTAyNn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJ1blNjaGVkdWxlZEVuYWJsZWQiOnRydWUsImh1Yk5vZGVJZCI6IjMwODEiLCJzdG9yZUhycyI6IjA2OjAwLTIzOjAwIiwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiUElDS1VQX0NVUkJTSURFIiwiUElDS1VQX0lOU1RPUkUiXX1dLCJzaGlwcGluZ0FkZHJlc3MiOnsibGF0aXR1ZGUiOjM4LjQ4MjY3NywibG9uZ2l0dWRlIjotMTIxLjM2OTAyNiwicG9zdGFsQ29kZSI6Ijk1ODI5IiwiY2l0eSI6IlNhY3JhbWVudG8iLCJzdGF0ZSI6IkNBIiwiY291bnRyeUNvZGUiOiJVUyIsImxvY2F0aW9uQWNjdXJhY3kiOiJsb3ciLCJnaWZ0QWRkcmVzcyI6ZmFsc2V9LCJhc3NvcnRtZW50Ijp7Im5vZGVJZCI6IjMwODEiLCJkaXNwbGF5TmFtZSI6IlNhY3JhbWVudG8gU3VwZXJjZW50ZXIiLCJhY2Nlc3NQb2ludHMiOm51bGwsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbXSwiaW50ZW50IjoiUElDS1VQIiwic2NoZWR1bGVFbmFibGVkIjpmYWxzZX0sImRlbGl2ZXJ5Ijp7ImJ1SWQiOiIwIiwibm9kZUlkIjoiMzA4MSIsImRpc3BsYXlOYW1lIjoiU2FjcmFtZW50byBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiI5NTgyOSIsImFkZHJlc3NMaW5lMSI6Ijg5MTUgR2VyYmVyIFJvYWQiLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6Ijk1ODI5LTAwMDAifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjM4LjQ4MjY3NywibG9uZ2l0dWRlIjotMTIxLjM2OTAyNn0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJ1blNjaGVkdWxlZEVuYWJsZWQiOnRydWUsImFjY2Vzc1BvaW50cyI6W3siYWNjZXNzVHlwZSI6IkRFTElWRVJZX0FERFJFU1MifV0sImh1Yk5vZGVJZCI6IjMwODEiLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6WyJERUxJVkVSWV9BRERSRVNTIl19LCJpbnN0b3JlIjpmYWxzZSwicmVmcmVzaEF0IjoxNjcyMjI0NzYzNTQyLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6YzdhZWMxNjktOWFlZC00MDgwLWI5MWQtN2Q2YjZlNDE4N2Y4In0%3D; assortmentStoreId=3081; hasLocData=1; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsInN0b3JlSW50ZW50IjoiUElDS1VQIiwibWVyZ2VGbGFnIjpmYWxzZSwiaXNEZWZhdWx0ZWQiOnRydWUsInN0b3JlU2VsZWN0aW9uVHlwZSI6IkRFRkFVTFRFRCIsInBpY2t1cCI6eyJub2RlSWQiOiIzMDgxIiwidGltZXN0YW1wIjoxNjcyMjAzMTYzNTM4fSwic2hpcHBpbmdBZGRyZXNzIjp7ImlkIjpudWxsLCJ0aW1lc3RhbXAiOjE2NzIyMDMxNjM1MzgsImNyZWF0ZVRpbWVzdGFtcCI6bnVsbCwidHlwZSI6InBhcnRpYWwtbG9jYXRpb24iLCJnaWZ0QWRkcmVzcyI6ZmFsc2UsInBvc3RhbENvZGUiOiI5NTgyOSIsImNpdHkiOiJTYWNyYW1lbnRvIiwic3RhdGUiOiJDQSIsImRlbGl2ZXJ5U3RvcmVMaXN0IjpbeyJub2RlSWQiOiIzMDgxIiwidHlwZSI6IkRFTElWRVJZIn1dfSwicG9zdGFsQ29kZSI6eyJ0aW1lc3RhbXAiOjE2NzIyMDMxNjM1MzgsImJhc2UiOiI5NTgyOSJ9LCJtcCI6W10sInZhbGlkYXRlS2V5IjoicHJvZDp2MjpjN2FlYzE2OS05YWVkLTQwODAtYjkxZC03ZDZiNmU0MTg3ZjgifQ%3D%3D; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_SFOU-100=; vtc=Wbgyz2u6CpenSRkIHrCiQY; bstc=Wbgyz2u6CpenSRkIHrCiQY; mobileweb=0; xpth=x-o-mverified%2Bfalse; xpa=9DCwR|BciIR|O-Nuy|kvhAJ|szAbx|tTQ2Y; exp-ck=szAbx3tTQ2Y1; ak_bmsc=35C1A05CF789B5D526FBD92DFFFB942F~000000000000000000000000000000~YAAQxYwsMR3vJiCFAQAA91sTVxKIamv18se6K2uuzabR6HxAl7XDI6iG3QJwhpW4BnM8MV0SP7Q7InNxAoLQ2GoZkeZrk6QzKeRlRmMSx5QZwG83AXIT70K0gX7v1P07dorCfbGINYzyM7IgQi+VQNVWyEIWagerNvrEo+r/DBLRWRiDwzPouAY63R1+W+AvFbclkZnCYSMugscyTSigTKGO95rA9bzDzIFsS0fZnSMEHWlyby2j17o7g6V9Gkvzhj5g1SK3j15qwDfXn8irYbd6pXFKno7q/H8XuMu6bRk2HRY8xuR6GL8DOA5yR0nBwKHMRdFNJhGF1gtWRxBccCT9Qhh8UfShe4kzeruKWNS6QYZ6uKbQntJ/+ki6M5Aej/zFvD/nkPEIZwfzKePV4KjcskCyhG+nN9vfz//HC3QO; TBV=7; _astc=b0c230d64c3acf633495b624ad8d8f9a; adblocked=false; xptc=assortmentStoreId%2B3081; xpm=1%2B1672203166%2BWbgyz2u6CpenSRkIHrCiQY~%2B0; _sp_ses.ad94=*; _sp_id.ad94=c7b74352-1663-4360-9432-99e2216eec8b.1672203299.1.1672203330.1672203299.63231db6-d275-4546-af01-e3bb453bd3f5; AID=wmlspartner%3D0%3Areflectorid%3D0000000000000000000000%3Alastupd%3D1672203508859; xptwj=rq:a3049a3c5252a4fcd727:yuY6Bsa81iIfNyPcokqsgOL2gSAoT2z+6zOo6654Vt4OyX5PtzF/SRoAOflpXGE1g0Qb6aIXGT/dU6VOKC6xxKd0ZzBgcoQZQGC0ZbpODT6AET5Xb8gxOCM=; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1672203511000@firstcreate:1672203163490"; akavpau_p2=1672204112~id=29521f2166a5c6fc5442b40efcd5efe6; xptwg=3159709672:1E39716D16F64E0:4DA137D:BCB80D3A:DC181E5D:F72F97C5:; TS012768cf=01ea83a631697361ae827f423b858b111b13a5d741c88bf06a4732335af22095a7aa7638a6e11ff500b65957a9e1b9f282bc40582e; TS01a90220=01ea83a631697361ae827f423b858b111b13a5d741c88bf06a4732335af22095a7aa7638a6e11ff500b65957a9e1b9f282bc40582e; TS2a5e0c5c027=0889f137dcab2000776c2734e49e07ad601a1d8af7886997428bd35669c0729d61d6f64ed08c777f08b55c5ff411300047a8a19cb2e1c417bdf65d8a997cca81a5a2720d967097f26a148ee77ab7bbf6162595a730cbe42eceb9f56e9c75e9e5; bm_sv=1E595216486E5AD5F63EBA2D08BF2566~YAAQvYwsMSz9yhuFAQAA8agYVxJExz79QlVftRnvskNzFOh9zfcYk8vah7HDKjTufXKUNcRqadN8ED10HwwXYma3wsg38Pgq0YlFoZZHa9lpaWq2P0FjInSQQdJ8bKQdyXTOOcKMKypqSbfbOPqy6ygoEFC8wlZESDxv0VzZ7TGPvONvJGrIK/0UeqWjznSolU+DziBFKbLmIo/u/ub2gafhvkVgwWhjeOaxwt+Ux3GBUW3TukY7ZY6t3xoUg76CPW8=~1; _px3=545702e16d7f3481f2e57649da95ccbfd3baab798bfbe953083ebb2704586d18:0gphqDODGL+H5h5ktQXDC4YEFogpi10+01YGVQAUQXHwSiquMwJd+wEt4IKN9D2tpUKdhHtOToAtK+Vv+PClYQ==:1000:YLRMqt93Fe3aN6WZw9rNuZgUB9b7OLoRHFaJP3egQ+zoUINK60NeO6cx6Z4FHOBcNKOxC1/rXLCTdtVUe1R1nvkkyTHA1lPrdUPlwBa65FSax8L0g4ox/h6dtw3eRyno0JRNUj+RozZ55xddUYsdYawJBMDKUupiFvqMwwv7Vd/BbXQcZXL3P6CO3/z/Gf6qlCW7eZJuSzwlhZm5xtjtRg==',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
        response = requests.request("GET", url, headers=headers, proxies=proxies)
        soup = BeautifulSoup(response.text, 'html.parser')
        datas = str(soup.find("script",{"type":"application/json"})).split('application/json">')[1].split("</script>")[0]
        json_data = json.loads(datas)

        for data in json_data["props"]["pageProps"]["initialData"]["searchResult"]["itemStacks"][0]["items"]:
            try:
                urls = "https://www.walmart.com" + data["canonicalUrl"]
            except:
                continue
            page_url = urls
            print(page_url)

            response1 = requests.request("GET", page_url, headers=headers)
            soup1 = BeautifulSoup(response1.text, 'html.parser')
            data1 = str(soup1.find("script",{"type":"application/json"})).split('application/json">')[1].split("</script>")[0]
            json_data1 = json.loads(data1)
            # open("test.txt",'w',encoding='utf-8').write(str(data1))

            try:
                name = json_data1["props"]["pageProps"]["initialData"]["data"]["contentLayout"]["modules"][2]["configs"]["ad"]["adsContext"]["productName"]
            except:
                name = json_data1["props"]["pageProps"]["initialData"]["data"]["contentLayout"]["modules"][1]["configs"]["ad"]["adsContext"]["productName"]
            try:
                sku = json_data1["props"]["pageProps"]["initialData"]["data"]["contentLayout"]["modules"][2]["configs"]["ad"]["pageContext"]["itemContext"]["itemId"]
            except:
                sku = json_data1["props"]["pageProps"]["initialData"]["data"]["contentLayout"]["modules"][1]["configs"]["ad"]["pageContext"]["itemContext"]["itemId"]
            product_code = json_data1["props"]["pageProps"]["initialData"]["data"]["product"]["upc"]
            image = json_data1["props"]["pageProps"]["initialData"]["data"]["product"]["imageInfo"]["allImages"][0]["url"]
            description = json_data1["props"]["pageProps"]["initialData"]["data"]["product"]["shortDescription"].replace("<b>","").replace("</b>","").replace("<br />","")
            model = json_data1["props"]["pageProps"]["initialData"]["data"]["product"]["model"]
            try:
                brand = json_data1["props"]["pageProps"]["initialData"]["data"]["contentLayout"]["modules"][2]["configs"]["ad"]["pageContext"]["itemContext"]["brand"]
            except:
                brand = json_data1["props"]["pageProps"]["initialData"]["data"]["contentLayout"]["modules"][1]["configs"]["ad"]["pageContext"]["itemContext"]["brand"]
            try:
                manufacture_number = json_data1["props"]["pageProps"]["initialData"]["data"]["contentLayout"]["modules"][2]["configs"]["ad"]["pageContext"]["itemContext"]["manufactureNumber"]
            except:
                manufacture_number = json_data1["props"]["pageProps"]["initialData"]["data"]["contentLayout"]["modules"][1]["configs"]["ad"]["pageContext"]["itemContext"]["manufactureNumber"]
            try:
                category = json_data1["props"]["pageProps"]["initialData"]["data"]["contentLayout"]["modules"][2]["configs"]["ad"]["adsContext"]["categoryName"].replace("/",", ")
            except:
                category = json_data1["props"]["pageProps"]["initialData"]["data"]["contentLayout"]["modules"][1]["configs"]["ad"]["adsContext"]["categoryName"].replace("/",", ")
            price = json_data1["props"]["pageProps"]["initialData"]["data"]["product"]["priceInfo"]["currentPrice"]["price"]
            try:
                old_price = json_data1["props"]["pageProps"]["initialData"]["data"]["product"]["priceInfo"]["wasPrice"]["priceString"]
            except:
                old_price = ''
            currency = json_data1["props"]["pageProps"]["initialData"]["data"]["product"]["priceInfo"]["currentPrice"]["currencyUnit"]
            price_display = json_data1["props"]["pageProps"]["initialData"]["data"]["product"]["priceInfo"]["currentPrice"]["priceDisplay"].replace("Now","").strip()
            rating = json_data1["props"]["pageProps"]["initialData"]["data"]["product"]["averageRating"]
            review_count = json_data1["props"]["pageProps"]["initialData"]["data"]["reviews"]["totalReviewCount"]
            color = []
            try:
                for data2 in json_data1["props"]["pageProps"]["initialData"]["data"]["product"]["variantCriteria"][0]["variantList"]:
                    data3 = data2["name"]
                    color.append(data3)
            except:
                color.append('')
            colors_type  = ", ".join(color)
            size = []
            try:
                for data4 in json_data1["props"]["pageProps"]["initialData"]["data"]["product"]["variantCriteria"][1]["variantList"]:
                    data5 = data4["name"]
                    size.append(data5)
            except:
                size.append('')
            size_type  = ", ".join(size)
            all_price = []
            for data6 in json_data1["props"]["pageProps"]["initialData"]["data"]["product"]["variants"]:
                data7 = data6["priceInfo"]["currentPrice"]["variantPriceString"]
                all_price.append(data7)
            size_and_price = []
            if size_type != '': 
                for (a, b) in zip(size, all_price):
                    data8 = str(a +": "+ b)
                    size_and_price.append(data8)
            else:
                size_and_price.append('')
            size_wise_price  = ", ".join(size_and_price)
            color_and_price = []
            for data9 in soup1.find("div",{"class":"flex flex-wrap nl2"}).find_all("span",{"class":"w_iUH7"}):
                data10 = data9.text.replace("selected,",":").replace(",",":").strip()
                color_and_price.append(data10)
            color_wise_price = ", ".join(color_and_price)

            store =[name,sku,product_code,image,description,model,brand,manufacture_number,category,price,old_price,currency,price_display,rating,review_count,colors_type,size_wise_price,color_wise_price,page_url]
            yield store
            
def scrape():
    data = fetch_data()
    write_output(data)
scrape()
