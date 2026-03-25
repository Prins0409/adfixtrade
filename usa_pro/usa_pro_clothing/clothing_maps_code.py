import csv
import requests
from bs4 import BeautifulSoup
import json
from io import open

def write_output(data):
    with open('clothing_maps_data.csv', mode='a', encoding="utf-8", newline="") as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(["location_name","location_review","location_rating","location_type","location_address","location_website","location_contact_no","location_latitude","location_longitude","location_all_reviews"])
        for row in data:
            writer.writerow(row)

def fetch_data():
    proxies = {
        'http': 'http://ronindata-default:7mxrQNQW@proxy.spider.com:8080"'
    }
    for data1 in open("for_clothing_city_country_data.csv",'r',encoding='utf-8'):
        clothing_area = "clothings+in" + str(data1.split(",")[0].replace(" ","+").replace('"',"+"))
        print("++++++++++",clothing_area,"++++++++++")
        for item in [clothing_area]:
            k = item
            url = "https://www.google.co.in/search?tbm=map&authuser=0&hl=en&gl=us&pb=!4m8!1m3!1d10313.249525947202!2d-71.5149869!3d42.015569!3m2!1i1536!2i334!4f13.1!7i20!10b1!12m10!1m1!18b1!2m3!5m1!6e2!20e3!10b1!16b1!17m1!3e1!19m4!2m3!1i360!2i120!4i8!20m57!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m2!1s-BmPY6yVOqDFkPIPn5OdkAc!7e81!24m73!1m23!13m9!2b1!3b1!4b1!6i1!8b1!9b1!14b1!20b1!25b1!18m12!3b1!4b1!5b1!6b1!9b1!12b1!13b1!14b1!15b1!17b1!20b1!21b1!2b1!5m5!2b1!3b1!5b1!6b1!7b1!10m1!8e3!11m1!3e1!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!29b1!30m1!2b1!36b1!39m3!2m2!2i1!3i1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!71b1!72m4!1m2!3b1!5b1!4b1!89b1!26m4!2m3!1i80!2i92!4i8!30m28!1m6!1m2!1i0!2i0!2m2!1i458!2i334!1m6!1m2!1i1486!2i0!2m2!1i1536!2i334!1m6!1m2!1i0!2i0!2m2!1i1536!2i20!1m6!1m2!1i0!2i314!2m2!1i1536!2i334!34m18!2b1!3b1!4b1!6b1!8m6!1b1!3b1!4b1!5b1!6b1!7b1!9b1!12b1!14b1!20b1!23b1!25b1!26b1!37m1!1e81!49m5!3b1!6m1!1b1!7m1!1e3!50m3!2e2!3m1!3b1!67m2!7b1!10b1!69i628&q="+str(k)+"&tch=1&ech=1&psi=-BmPY6yVOqDFkPIPn5OdkAc.1670322683050.1"
            payload={}
            headers = {
            'cookie': 'SEARCH_SAMESITE=CgQI45UB; NID=511=cPtntFTSYiLSMz6vdMtrCJFeGJ5kmHVTY9-z6MxFiHmMQQ4zjhb0csLHE9M7rH7fp59dJGYBKRSrL9yJTiln5JH7Ehhvt2HZoDRQNfveuqB6iz2zCxZjshX1eP-iY7Yg8dtklpRKjqqpZYTXyeaSYMmeBAiPVYGzfOwrsrLDsMnq9T7A5Te9lmbXtTW354nCONwfuL_6ldh8Wh02743YhyPp9nEGPzBmcILEHOq4I7KwSkFqbDN65nzLfuVwUUAOwkEU7quIRlFSGsE54Q; SID=NQj_lj5BoUD48B6-eXGPIVFJLV3OglvC-vyzvpAjYaJc0arsSr5NUQzpj22IR-J1kGV-hQ.; __Secure-1PSID=NQj_lj5BoUD48B6-eXGPIVFJLV3OglvC-vyzvpAjYaJc0arsAag9ijYxnKsNBFeoCjcK6Q.; __Secure-3PSID=NQj_lj5BoUD48B6-eXGPIVFJLV3OglvC-vyzvpAjYaJc0arsmYLiPUn-Vyl0gr6n1URhog.; HSID=A_xbyJ6q9MXD8oHd-; SSID=AUI5aYcqFxaXJ4f8X; APISID=drTXjX7EbVu-KxXK/AClK0wpFC1f2zV03D; SAPISID=hJfKRYt1mB1M4mDd/AJpGh4YKPiQlh35NG; __Secure-1PAPISID=hJfKRYt1mB1M4mDd/AJpGh4YKPiQlh35NG; __Secure-3PAPISID=hJfKRYt1mB1M4mDd/AJpGh4YKPiQlh35NG; AEC=AakniGNIEMOwUnjHIRMDBOjkYdoCHh7JlZMT-JMUvI41_DZtxosEQyY3Wpw; 1P_JAR=2022-12-06-10'
            }
            response = requests.request("GET", url, headers=headers, data=payload, proxies=proxies)
            data = (response.text.replace('/*""*/',''))
            json_data = json.loads(data)
            ii = json_data['d'].replace(")]}'\n",'')
            j = json.loads(ii)[0][1]
            if j[1:] != []:
                for i in j[1:]:
                    try:
                        location_name =(i[14][11])
                    except:
                        location_name = ""
                    try:
                        location_review =(i[14][4][3][1])
                    except:
                        location_review = ""
                    try:
                        location_rating =(i[14][4][7])
                    except:
                        location_rating = ""
                    try:
                        location_type =(i[14][13][0])
                    except:
                        location_type = ""
                    try:
                        location_address =(i[14][18])
                    except:
                        location_address = ""
                    try:
                        location_website =(i[14][7][1])
                    except:
                        location_website = ""
                    try:
                        location_contact_no =(i[14][178][0][0])
                    except:
                        location_contact_no = ""
                    try:
                        location_latitude =(i[14][9][2])
                    except:
                        location_latitude = ""
                    try:
                        location_longitude =(i[14][9][3])
                    except:
                        location_longitude = ""
                    try:
                        place_name =(i[14][11])
                    except:
                        place_name = ""
                    key1 =(i[14][10]).split(":")[0]
                    key2 =(i[14][10]).split(":")[1]
                    name_for_url = place_name.replace(" ","+").replace("'","%27").replace("!","*21")
                    name_for_url1 = place_name.replace(" ","%20").replace("'","%27")
                    name_for_url2 = place_name.replace(" ","+").replace("'","%27").split("+")[0]
                    print(name_for_url)
                    url1 = "https://www.google.co.in/maps/preview/place?authuser=0&hl=en&gl=us&pb=!1m21!1s"+ str(key1) +"%3A"+ str(key2) +"!3m9!1m3!1d10808.874739725166!2d-71.5163471!3d42.0062859!2m0!3m2!1i1536!2i350!4f13.1!4m2!3d"+ str(location_latitude) +"!4d"+ str(location_longitude) +"!15m6!1m5!1s"+ str(key1) +"%3A"+ str(key2) +"!4s%2Fg%2F1tcws4nt!5sChIJ_cZ71NRr5IkRJtcNVLhgh1o!6s13344697267934386159!7s114672003372129408885!6s"+ str(k) +"+"+ name_for_url2 +"!12m4!2m3!1i360!2i120!4i8!13m57!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!14m2!1sZWuQY723NdeD8gLDwqToCA!7e81!15m75!1m25!4e2!13m9!2b1!3b1!4b1!6i1!8b1!9b1!14b1!20b1!25b1!18m13!3b1!4b1!5b1!6b1!9b1!12b1!13b1!14b1!15b1!17b1!20b1!21b1!22b0!2b1!5m5!2b1!3b1!5b1!6b1!7b1!10m1!8e3!11m1!3e1!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!29b1!30m1!2b1!36b1!39m3!2m2!2i1!3i1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!71b1!72m4!1m2!3b1!5b1!4b1!89b1!21m28!1m6!1m2!1i0!2i0!2m2!1i886!2i350!1m6!1m2!1i1486!2i0!2m2!1i1536!2i350!1m6!1m2!1i0!2i0!2m2!1i1536!2i20!1m6!1m2!1i0!2i330!2m2!1i1536!2i350!22m1!1e81!29m0!30m1!3b1!34m2!7b1!10b1!37i628!38sCh9yZXN0YXVyYW50cyBpbiAwMjg5NS0wMDUwIGtheSdzWiEiH3Jlc3RhdXJhbnRzIGluIDAyODk1IDAwNTAga2F5J3OSARNhbWVyaWNhbl9yZXN0YXVyYW50mgEkQ2hkRFNVaE5NRzluUzBWSlEwRm5TVU5YZWpkaGNtbFJSUkFC4AEA!39s"+ name_for_url +"&q="+ name_for_url1                    
                    payload={}
                    headers1 = {
                    'cookie': 'SEARCH_SAMESITE=CgQI45UB; SID=NQj_lj5BoUD48B6-eXGPIVFJLV3OglvC-vyzvpAjYaJc0arsSr5NUQzpj22IR-J1kGV-hQ.; __Secure-1PSID=NQj_lj5BoUD48B6-eXGPIVFJLV3OglvC-vyzvpAjYaJc0arsAag9ijYxnKsNBFeoCjcK6Q.; __Secure-3PSID=NQj_lj5BoUD48B6-eXGPIVFJLV3OglvC-vyzvpAjYaJc0arsmYLiPUn-Vyl0gr6n1URhog.; HSID=A_xbyJ6q9MXD8oHd-; SSID=AUI5aYcqFxaXJ4f8X; APISID=drTXjX7EbVu-KxXK/AClK0wpFC1f2zV03D; SAPISID=hJfKRYt1mB1M4mDd/AJpGh4YKPiQlh35NG; __Secure-1PAPISID=hJfKRYt1mB1M4mDd/AJpGh4YKPiQlh35NG; __Secure-3PAPISID=hJfKRYt1mB1M4mDd/AJpGh4YKPiQlh35NG; OTZ=6801682_34_34__34_; NID=511=E8WhvJOXr6X_8G_WCw-0D7opaZTITKFKo2ApN1Ramu4Cz1J2Xc3IMgiBYK1MJVsMgiMv0LxCY41ZpcKGuXQpsRxzqCGW1qrz5vO7nWcXalpMlC2pSuo4LHwZL7QuFtMZCWTfwYkbdMtFNMnjrNH4IR0RlLr3_rWd0KyeB0XX6osiSoOmmYCxCHKTC8XESv6ggs42nFV8e1Sv3nr5RxEJ1uGpuuwbYMvSgXHluccSJiZzFwW6u_xON3K8ZzH8lojG9v26fBlEjrqUIv3LLQ; 1P_JAR=2022-12-07-10; AEC=AakniGNcFTOc7XFv3c3Ie1gXos535EYChIEo7raHSCo1M_XdrGQ2FBuhW9s'
                    }
                    response1 = requests.request("GET", url1, headers=headers1, data=payload)
                    data1 = (response1.text.replace(")]}'\n",''))
                    json_data1 = json.loads(data1)
                    count = 0
                    location_reviews = []
                    while True:
                        if count == 8:
                            break
                        try:
                            all_reviews = (json_data1[6][52][0][count][3])
                        except:
                            all_reviews = ''
                        location_reviews.append(str(all_reviews))
                        count += 1
                    location_all_reviews = ";".join(location_reviews).replace(";;","")
                    store = []
                    store.append(location_name if location_name else "")
                    store.append(location_review if location_review else "")
                    store.append(location_rating if location_rating else "")
                    store.append(location_type if location_type else "")
                    store.append(location_address if location_address else "")
                    store.append(location_website if location_website else "")
                    store.append(location_contact_no if location_contact_no else "")
                    store.append(location_latitude if location_latitude else "")
                    store.append(location_longitude if location_longitude else "")
                    store.append(location_all_reviews if location_all_reviews else "")
                    yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()