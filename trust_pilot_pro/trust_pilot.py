import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime

def write_output(data):
	with open('trust_pilot.csv', mode='a', newline="", encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["page_url","reviewers_name","reviewers_country","reviewers_published_date","reviewers_title","reviewers_review","reviewers_rating","company_name","company_total_review","reviewers_trust_score","company_website","company_all_over_rating_star","current_timestamp"])
		for row in data:
			writer.writerow(row)

def fetch_data():
    proxies = { 'https' : 'https://brd-customer-c_878f6dc2-zone-zone_priceline_development-country-us:ixuzrn0hwwpw@zproxy.lum-superproxy.io:22225' } 
    for i in range(1,12):
        print(i)
        url = "https://www.trustpilot.com/categories/real_estate_agents?page="+str(i)
        headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "cookie": "TP.uuid=7b739693-c0e3-48db-ba7b-dd1fc8453241; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_391767=eyJpZCI6ImRkOTdiYjkwLTM0YjAtNDU5NC05ZWIxLTgwNWFlN2VjZDU4ZSIsImNyZWF0ZWQiOjE2NzExNjgwNzQzNDUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; ajs_anonymous_id=505ae155-ccb5-4c3a-be74-2a41f589ac66; amplitude_idundefinedtrustpilot.com=eyJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOm51bGwsImxhc3RFdmVudFRpbWUiOm51bGwsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjowfQ==; _gcl_au=1.1.1430519724.1671168075; _hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7ImFtcGxpdHVkZV9kZXZpY2VfaWQiOiI1MWE2YzYxNi00OTc4LTQ0MTctODQ0MC0yNWIzZjMzZDI2NDZSIiwic2VnbWVudF9hbm9ueW1vdXNfaWQiOiI1MDVhZTE1NS1jY2I1LTRjM2EtYmU3NC0yYTQxZjU4OWFjNjYiLCJzZWdtZW50X3VzZXJfaWQiOm51bGx9LCJ1c2VySWQiOm51bGx9; _ga=GA1.1.1376748295.1671168076; _fbp=fb.1.1671168075769.1645594485; _biz_sid=210667; _biz_uid=81eb08b730614abdfe4daec17110ab71; _biz_flagsA=%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; OptanonAlertBoxClosed=2022-12-16T05:21:17.705Z; _csrf=AzxgIRwHA3bSpk-aLVZ3I3qG; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Dec+16+2022+10%3A52%3A37+GMT%2B0530+(India+Standard+Time)&version=6.28.0&isIABGlobal=false&hosts=&consentId=44161268-072f-4690-9959-6f4fb793e80e&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=IN%3BGJ&AwaitingReconsent=false; _hjSessionUser_391767=eyJpZCI6IjkwMzRiZDM4LTdjMzctNTg5Ny1iOGZlLTRiZDQ2ZmFkMTBkMSIsImNyZWF0ZWQiOjE2NzExNjgwNzQyNjgsImV4aXN0aW5nIjp0cnVlfQ==; _biz_nA=5; _biz_pendingA=%5B%5D; amplitude_id_67f7b7e6c8cb1b558b0c5bda2f747b07trustpilot.com=eyJkZXZpY2VJZCI6IjUxYTZjNjE2LTQ5NzgtNDQxNy04NDQwLTI1YjNmMzNkMjY0NlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY3MTE2ODA3NDkwMCwibGFzdEV2ZW50VGltZSI6MTY3MTE2ODE2NTUzOCwiZXZlbnRJZCI6OCwiaWRlbnRpZnlJZCI6MSwic2VxdWVuY2VOdW1iZXIiOjl9; _ga_11HBWMC274=GS1.1.1671168075.1.1.1671168170.0.0.0; _ga_MD2Z7JEPWG=GS1.1.1671168075.1.1.1671168170.0.0.0",
        "if-none-match": "m97ts410cragch",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        response = requests.request("GET", url, headers=headers, proxies=proxies)
        soup = BeautifulSoup(response.text, 'html.parser')
        for data in soup.find_all("div",{"class":"paper_paper__1PY90 paper_outline__lwsUX card_card__lQWDv card_noPadding__D8PcU styles_wrapper__2JOo2"}):
            sub_url = "https://www.trustpilot.com" + data.find("a")["href"]
            headers1 = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "cookie": "TP.uuid=7b739693-c0e3-48db-ba7b-dd1fc8453241; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_391767=eyJpZCI6ImRkOTdiYjkwLTM0YjAtNDU5NC05ZWIxLTgwNWFlN2VjZDU4ZSIsImNyZWF0ZWQiOjE2NzExNjgwNzQzNDUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; ajs_anonymous_id=505ae155-ccb5-4c3a-be74-2a41f589ac66; amplitude_idundefinedtrustpilot.com=eyJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOm51bGwsImxhc3RFdmVudFRpbWUiOm51bGwsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjowfQ==; _gcl_au=1.1.1430519724.1671168075; _hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7ImFtcGxpdHVkZV9kZXZpY2VfaWQiOiI1MWE2YzYxNi00OTc4LTQ0MTctODQ0MC0yNWIzZjMzZDI2NDZSIiwic2VnbWVudF9hbm9ueW1vdXNfaWQiOiI1MDVhZTE1NS1jY2I1LTRjM2EtYmU3NC0yYTQxZjU4OWFjNjYiLCJzZWdtZW50X3VzZXJfaWQiOm51bGx9LCJ1c2VySWQiOm51bGx9; _ga=GA1.1.1376748295.1671168076; _fbp=fb.1.1671168075769.1645594485; _biz_sid=210667; _biz_uid=81eb08b730614abdfe4daec17110ab71; _biz_flagsA=%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; OptanonAlertBoxClosed=2022-12-16T05:21:17.705Z; _csrf=AzxgIRwHA3bSpk-aLVZ3I3qG; _hjSessionUser_391767=eyJpZCI6IjkwMzRiZDM4LTdjMzctNTg5Ny1iOGZlLTRiZDQ2ZmFkMTBkMSIsImNyZWF0ZWQiOjE2NzExNjgwNzQyNjgsImV4aXN0aW5nIjp0cnVlfQ==; _tt_enable_cookie=1; _ttp=GWbs3fSa8NdMpf1gzg7lrD68yVW; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Dec+16+2022+11%3A25%3A09+GMT%2B0530+(India+Standard+Time)&version=6.28.0&isIABGlobal=false&hosts=&consentId=44161268-072f-4690-9959-6f4fb793e80e&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=IN%3BGJ&AwaitingReconsent=false; _biz_nA=10; amplitude_id_67f7b7e6c8cb1b558b0c5bda2f747b07trustpilot.com=eyJkZXZpY2VJZCI6IjUxYTZjNjE2LTQ5NzgtNDQxNy04NDQwLTI1YjNmMzNkMjY0NlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY3MTE2ODA3NDkwMCwibGFzdEV2ZW50VGltZSI6MTY3MTE3MDE3MTkzNCwiZXZlbnRJZCI6NDcsImlkZW50aWZ5SWQiOjMsInNlcXVlbmNlTnVtYmVyIjo1MH0=; _ga_11HBWMC274=GS1.1.1671168075.1.1.1671170172.0.0.0; _ga_MD2Z7JEPWG=GS1.1.1671168075.1.1.1671170172.0.0.0; _biz_pendingA=%5B%5D",
            "if-none-match": "nfd1abzbmk8sgp",
            "referer": "https://www.trustpilot.com/categories/real_estate_agents",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
            }
            response1 = requests.request("GET", sub_url, headers=headers1)
            soup1 = BeautifulSoup(response1.text, 'html.parser')
            try:
                datas = int(soup1.find("nav",{"class":"pagination_pagination___F1qS"}).find("a",{"name":"pagination-button-last"})["href"].split("page=")[1])
            except:
                numbers = []
                for datta in soup1.find("nav",{"class":"pagination_pagination___F1qS"}).find_all("a"):
                    datta2 = datta["aria-label"]
                    numbers.append(datta2)
                datas = int(" ".join(numbers).replace("Next page","").strip()[-1])
            for j in range(1, datas+1):
                final_all_page_url = sub_url + "?page=" + str(j)
                print(final_all_page_url)
                headers2 = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "cookie": "TP.uuid=7b739693-c0e3-48db-ba7b-dd1fc8453241; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_391767=eyJpZCI6ImRkOTdiYjkwLTM0YjAtNDU5NC05ZWIxLTgwNWFlN2VjZDU4ZSIsImNyZWF0ZWQiOjE2NzExNjgwNzQzNDUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; ajs_anonymous_id=505ae155-ccb5-4c3a-be74-2a41f589ac66; amplitude_idundefinedtrustpilot.com=eyJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOm51bGwsImxhc3RFdmVudFRpbWUiOm51bGwsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjowfQ==; _gcl_au=1.1.1430519724.1671168075; _hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7ImFtcGxpdHVkZV9kZXZpY2VfaWQiOiI1MWE2YzYxNi00OTc4LTQ0MTctODQ0MC0yNWIzZjMzZDI2NDZSIiwic2VnbWVudF9hbm9ueW1vdXNfaWQiOiI1MDVhZTE1NS1jY2I1LTRjM2EtYmU3NC0yYTQxZjU4OWFjNjYiLCJzZWdtZW50X3VzZXJfaWQiOm51bGx9LCJ1c2VySWQiOm51bGx9; _ga=GA1.1.1376748295.1671168076; _fbp=fb.1.1671168075769.1645594485; _biz_sid=210667; _biz_uid=81eb08b730614abdfe4daec17110ab71; _biz_flagsA=%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; OptanonAlertBoxClosed=2022-12-16T05:21:17.705Z; _csrf=AzxgIRwHA3bSpk-aLVZ3I3qG; _hjSessionUser_391767=eyJpZCI6IjkwMzRiZDM4LTdjMzctNTg5Ny1iOGZlLTRiZDQ2ZmFkMTBkMSIsImNyZWF0ZWQiOjE2NzExNjgwNzQyNjgsImV4aXN0aW5nIjp0cnVlfQ==; _tt_enable_cookie=1; _ttp=GWbs3fSa8NdMpf1gzg7lrD68yVW; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Dec+16+2022+11%3A25%3A09+GMT%2B0530+(India+Standard+Time)&version=6.28.0&isIABGlobal=false&hosts=&consentId=44161268-072f-4690-9959-6f4fb793e80e&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=IN%3BGJ&AwaitingReconsent=false; _biz_nA=10; amplitude_id_67f7b7e6c8cb1b558b0c5bda2f747b07trustpilot.com=eyJkZXZpY2VJZCI6IjUxYTZjNjE2LTQ5NzgtNDQxNy04NDQwLTI1YjNmMzNkMjY0NlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTY3MTE2ODA3NDkwMCwibGFzdEV2ZW50VGltZSI6MTY3MTE3MDE3MTkzNCwiZXZlbnRJZCI6NDcsImlkZW50aWZ5SWQiOjMsInNlcXVlbmNlTnVtYmVyIjo1MH0=; _ga_11HBWMC274=GS1.1.1671168075.1.1.1671170172.0.0.0; _ga_MD2Z7JEPWG=GS1.1.1671168075.1.1.1671170172.0.0.0; _biz_pendingA=%5B%5D",
                "if-none-match": "nfd1abzbmk8sgp",
                "referer": "https://www.trustpilot.com/categories/real_estate_agents",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
                }
                response2 = requests.request("GET", final_all_page_url, headers=headers2)
                soup2 = BeautifulSoup(response2.text, 'html.parser')
                for reviewers_data in soup2.find_all("div",{"class":"styles_cardWrapper__LcCPA styles_show__HUXRb styles_reviewCard__9HxJJ"}):
                    reviewers_name = reviewers_data.find("span",{"class":"typography_heading-xxs__QKBS8 typography_appearance-default__AAY17"}).text.strip()
                    reviewers_country = reviewers_data.find("div",{"class":"typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l styles_detailsIcon__Fo_ua"}).text.strip()
                    reviewers_published_date = reviewers_data.find("div",{"class":"typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l styles_datesWrapper__RCEKH"}).find("time")["datetime"]
                    reviewers_title = reviewers_data.find("h2",{"class":"typography_heading-s__f7029 typography_appearance-default__AAY17"}).text.strip()
                    try:
                        reviewers_review = reviewers_data.find("p",{"class":"typography_body-l__KUYFJ typography_appearance-default__AAY17 typography_color-black__5LYEn"}).text.strip()
                    except:
                        reviewers_review = ''
                    reviewers_trust_score = soup2.find("div",{"class":"star-rating_starRating__4rrcf star-rating_medium__iN6Ty"}).find("img")["alt"].replace("TrustScore ", "").replace(" out of 5", "")
                    reviewers_rating = reviewers_data.find("div",{"class":"star-rating_starRating__4rrcf star-rating_medium__iN6Ty"}).find("img")["alt"].replace("Rated ", "").replace(" out of 5 stars", "")
                    if "TrustScore" in reviewers_rating:
                        continue
                    company_name = soup2.find("span",{"class":"typography_display-s__qOjh6 typography_appearance-default__AAY17 title_displayName__TtDDM"}).text.strip()
                    company_total_review = soup2.find("span",{"class":"typography_body-l__KUYFJ typography_appearance-subtle__8_H2l styles_text__W4hWi"}).text.strip().replace("Excellent", "").replace("•", "").strip()
                    try:
                        company_website = soup2.find("span",{"class":"styles_smartEllipsisContainer__US5DI"}).text.strip()
                    except:
                        company_website = soup2.find("div",{"class":"styles_header__7nPK9"}).find("span").text.strip()
                    if "www" in str(company_website):
                        company_website = "https://" + company_website
                    else:
                        company_website = "https://www." + company_website
                    company_all_over_rating_star = soup2.find("div",{"class":"styles_rating__uyC6m styles_clickable__uWsnU styles_rating__NPyeH"}).find("p",{"class":"typography_body-l__KUYFJ typography_appearance-subtle__8_H2l"}).text.strip()
                    now = datetime.now()
                    current_timestamp = now.strftime("%y-%m-%dT%H:%M:%SZ")
                    page_url = final_all_page_url
                    store =[page_url,reviewers_name,reviewers_country,reviewers_published_date,reviewers_title,reviewers_review,reviewers_rating,company_name,company_total_review,reviewers_trust_score,company_website,company_all_over_rating_star,current_timestamp]
                    yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()
