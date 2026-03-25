import requests
import csv
from bs4 import BeautifulSoup
import json

def write_output(data):
	with open('tripadvisor.csv', mode='a', newline="", encoding='utf-8') as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["name","address","street1","street2","city","state","country","postalcode","phone_no","email","website","rating","reviews_count","latitude","longitude","rating_food","rating_service","rating_value","price","varities","image","open_hours","page_url"])
		for row in data:
			writer.writerow(row)

def fetch_data():
  proxies = { 'https' : 'https://brd-customer-c_878f6dc2-zone-zone_priceline_development-country-us:ixuzrn0hwwpw@zproxy.lum-superproxy.io:22225' } 
  for i in range(1, 297):
    j = i * 30
    print(i)
    url = "https://www.tripadvisor.com/RestaurantSearch?Action=PAGE&ajax=1&availSearchEnabled=false&sortOrder=popularity&geo=60763&itags=10591&geobroaden=false&o=a"+str(j)
    headers = {
      'accept': '*/*',
      'accept-encoding': 'gzip, deflate, br',
      'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,gu;q=0.4,de;q=0.3',
      'cookie': 'TADCID=a128-G30Y73V2anZABQCFdpBzzOuRA-9xvCxaMyI13JXyJzkbUqFSQXVb2C73KwBGphgDXD5t3czGJUxP2gaED-ZhJdprbf5jtk; TAUnique=%1%enc%3Au%2FKH8yQEGORQwreYDGyVtOYenWoICPa8vSVstP18WGY%3D; TASSK=enc%3AAHYOXQMt6aP2AOtqfNEvYnOGSbLAsqMLbJRRSnO6Wlp47OmGFH6xC%2FkWC4sUpqS8fL7hEcMVN%2BrgME0vhhX3bjt5hO71EqQRqZL19nmcvTsx1y2S56%2FZ5kyi4p04bvFU9g%3D%3D; ServerPool=B; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; TAReturnTo=%1%%2FRestaurants-g60763-New_York_City_New_York.html; TATrkConsent=eyJvdXQiOiIiLCJpbiI6IkFMTCJ9; _pbjs_userid_consent_data=3524755945110770; _li_dcdm_c=.tripadvisor.com; _lc2_fpi=b140173de591--01gmtd5r0vydcgg72vqwr4aw1z; __gads=ID=a64abf6f536028b9:T=1671628515:S=ALNI_MbIzveR4fDzqZCNXtvPRFYtGNEioA; _lr_sampling_rate=100; _lr_env_src_ats=false; pbjs_li_nonid=%7B%22unifiedId%22%3A%22OIWdHOTuTULRIyCwjS612dP6u1RIlD7Fw3meUg%22%7D; TART=%1%enc%3Ats5cxHjqP8UkgYW1ToyP6uIqQ4B2QCKoF3Yq3hnptfv9H6d0NSAp8uPmIyouRabFh0izmtFali4%3D; PAC=ALyeV4hZBIUTOzZ7rm2AFG68PnuiBn1XIrk75Yx23dE56SKuthBKUyLXysM-o9HJ2vqSBjw3a2ICq6iPG7FsFcGGm8kl8fhrhyQycNjCTG9YOQfL9dmnxnpgIknY9YkKaYMDZSHIqO74K-iNV22oTWmIQ7pDEtgiL9Z3hoCn-qVOYbuSMym60Z_95dsp_Brl5A%3D%3D; TASID=43FDDCC78A9C40DB92A3617D2CA39AE5; _abck=B795C0C63EB090AD23FA3527B4C84858~0~YAAQ23AsMS/jRgmFAQAAK8IVOAkdLL/oa/PHCnfe0DtP1I+fp3uyPgWd9MA45jDCpmbmNNqGjeKPCRN0jc9ACpIxBqd1x+4lEcqriDrEUdetEMNxfS6J8xX92GEory7n43Rxv+53a98S1NzlYgPvd0JAxtPnFLmfIb3mtDFlpwbx1EdER0wzlrHrEVlP87cYK8snZGQ942nXLBfs0OOMWrzjtzzFWQGqP3Oi47KWujHDeOLpmELvXbxpwttAykp2r+NrCpmzCSFSVtvLa5+G/lYQgwjn+ejme2SDufxecNcQBCrvPzR4mHPLi2RuoxSEr63uKWcf9ZMqgYD9bk96XUEeV+DSMSAzc4HiElbG1+odpzCRUttttFcM6tbmN2TRFTRCx04oa3Rys3iIEP4zzjwXInn8tPK9gtX6i8M=~-1~-1~-1; ak_bmsc=37C2559396F9AEB974EA3DFF185C4128~000000000000000000000000000000~YAAQ23AsMTDjRgmFAQAAK8IVOBKT89iwIwNWJwxe5h8rrWqJ8/620MHB0Z7aQXfqDb3LtO5DvdeQNclDE53gPgw7LL92+LLguvyhK5mQ9Xgs8UPOpheBtjOGqe2+6YlSfOAGisgN5FGHoYvnA/sSRWB3LVHC7RMrboUx5aTd4pKN9HdNXu/m2Et4L5aoYrPeTG/5M6PgLP8yLkNQaUieae+uw8Y2bZa+qpHLKxMpNuHG4cgm28FJooHRwKCql4IDyz1KeIyzLZFk7AsRXnquZ7fObeNJcuO3DxdviVbfJu+QevOYZl8sX5HrDE31DR36BBTAMIUVfMc7uHx3YFxMy916Xm9qOTsC9IhdelOQVoe5DI7nbUCQfqrobnDvY1KVraEWxMioz7+hfDh3; bm_sz=0D2A3119824534F2FE03E734FA99CFE2~YAAQ23AsMTHjRgmFAQAAK8IVOBI4rsim9hhegVIVK6c0l+ePtgDHV8QVWiBuNkFlcU2c+pCRj2mJ7aVBferCzzO4uf9XEJ1H/+NevIxesW9aJbvx0iZkOXlAV/7B5kk0N0Z1uVoIMAgboEVoot5ENpywC17TEbQNwj17NsD5rMKFOJ97n53LWhSG5zXxrtezB6c6zGtZYFwuLTjpeAm3PLdrUjhIuLXMYFP4q20/Qe+KyZgwiwkZnR2pWJ4n+frS/odv+ajCHBD/aLfljrYPzOhkkoMUn6OJBMdA1AzTsKlXubzjMlhk3Q==~4339249~4337733; __gpi=UID=00000b9529363c00:T=1671628515:RT=1671683234:S=ALNI_MbMmBHG0_O0ira0QydvlFvT4pNBaw; _lr_retry_request=true; PMC=V2*MS.55*MD.20221221*LD.20221222; SRT=%1%enc%3Ats5cxHjqP8UkgYW1ToyP6uIqQ4B2QCKoF3Yq3hnptfv9H6d0NSAp8uPmIyouRabFh0izmtFali4%3D; roybatty=TNI1625!AOicK%2FmzxT%2F30ghJWTAZL%2Ba2OgjwVZRbV4FLf6GCw%2B54h2SwTM%2Ff3cMVUmSe6qtL7SQgWJZWgrU7rhwCZdIsQ44md5KAdpP8sgcGjAz0GIFOOm9zTnavFWJ8OWPvdK9x9nv1%2BXLubptwBV%2BxTGlqrMtkYiBpZm8SmjIS5jBbv21G%2C1; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Dec+22+2022+10%3A32%3A45+GMT%2B0530+(India+Standard+Time)&version=202209.1.0&isIABGlobal=false&hosts=&consentId=f1a43cd3-a600-4f3d-9d54-26c000b3a8fb&interactionCount=1&landingPath=https%3A%2F%2Fwww.tripadvisor.com%2FRestaurants-g60763-New_York_City_New_York.html&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; __vt=YA2oyRRJrcomlSfNABQCIf6-ytF7QiW7ovfhqc-AvSI5H1KsVNOrNsgb-yxjmi1RpI2Uh5JvVc6D5gvG6dDn7TjOYoBaCOxLagaGLSuGJBS06fi2bKkqgRYwKtC5JjxCvA3HB-EiUXkOwQGkwmh3MR4hl1U; TASession=V2ID.43FDDCC78A9C40DB92A3617D2CA39AE5*SQ.44*LS.Restaurants*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*RT.0*TRA.true*LD.60763*EAU._; TAUD=LA-1671628511543-1*RDD-1-2022_12_21*LG-57089619-2.1.F.*LD-57089620-.....; bm_sv=5E2452C94F45877D685598A3484A35FD~YAAQ23AsMRr5SgmFAQAAVA86OBL/oNLVGp3I0f8LD2Sf/IxqsilNLeA/umD4Z4lR7pXX6fd0qIBI533dmO/mau+HX1XYJRar0bn8aVdOxlqzqNFM/emWJaEUgJiyJhmD7U5GaT08QSeMrWdrMTpFptM40SH8BJTgfjEcxPvDb1PhOJr7BOOUC7LHR+Nt2pY7FUKs96jWlcT84/L/jPR1EQMzBlSPCkG/mdkBd9btE79yh0JFZYece/slUeydzRdB969hsvaNKw==~1; ServerPool=R; TAReturnTo=%1%%2FRestaurants-g60763-New_York_City_New_York.html; TASession=V2ID.43FDDCC78A9C40DB92A3617D2CA39AE5*SQ.45*LS.Restaurants*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*FA.1*DF.0*RT.0*TRA.true*LD.60763*EAU._; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; TAUD=LA-1671628511543-1*RDD-1-2022_12_21*LG-57231141-2.1.F.*LD-57231142-.....; TAUnique=%1%enc%3A34nCenJbfc%2FLDxBs24k%2BMVlK1CyptGY8XfyBM2Zw7d4%3D; _abck=B795C0C63EB090AD23FA3527B4C84858~-1~YAAQ23AsMQ8hSwmFAQAAwCU8OAnIG0Na5BdL2hKRpTkh7Ikhw5lZxfwFRramVLfMPfE4RIOqth4YOl21uZfoLyjOv5E+fpKzF1tLIKTiee6SJ7hJaqCKOw3Tv74+Q0C80ixPGHSM42MbV7xmbKTN4tl3ehtQw6ihowMyjeaX9foR8xI2o95zJNKqCaYPV55hoY7ON9ZZjUBd3Eu64Ic29OiED+wS240rA1TaE55vfVZB2OiIMwmW/xgePVkdfRVj+9fJc/BlkRW+qmRf2eM+FMMkBpTyCiJ4Vm/tK77MS0UTr2SzLNNU7fHm7R0wywjmZRVCZdcd8x6eVFR66k9u0LJ/w9e49yNvGE1cY9T2Zu3v744SiJuYpEd2f5lYwRmPF3KB2CgcWBVcCa7/0L7TIuxyuRTqldWbpmmED3I=~0~-1~-1; bm_sz=A3407F678F4CE798C839D6BFC818547E~YAAQ23AsMZi+SgmFAQAA4/s2OBL3YpciPWNDDhmXzW/HJ1dVNVkvQeCcuXVRxUzR9HiQBVKnlytlfA5sKhwu3IZCba6+0Pt8Xd/WzSKDA10+AIEKQOlrjRFX2bJo2rsIrHPPVx1GIdG2Arn2zAXBGthmf80Kpa6B8KVOG4lwwsq4fpux9HhCbzJmlqWTsTubshsTrpm9dNa7TWjYWAKVneEGpbeoQfJl6+7SRS/TPFP74nBM3T7BL8Aaenc8QDoG8lkNIeplcZlcyXGUdvDhVzKNYXK22j2+D6I5+Wp3vJgjdDJ029wgaw==~4272452~3618629; PAC=AGPSnk5O_jRPsU1IU_dJFcTwx8RF-4z605sEejAH5a8SlTS0yBuXmROjcVB909SYlAUA0GIfm6hRnRXcoMPgQaLQH4lqqVHbmekudjU9GfDndTm9dtpluVCfUS5SdTnNMm0hkLQTxiT4Vi3qEPT6s5_ATdvsvW7EMCZZrhRGy4i1VCaMht4y1STGgikEGueijw%3D%3D; PMC=V2*MS.7*MD.20221222*LD.20221222; SRT=TART_SYNC; TADCID=kmlBVm1SmVIFia53ABQCFdpBzzOuRA-9xvCxaMyI13JbfAnB35PSNzbOvcB9oQgVO35oq41Zh7LlEUNqLTbspwtM_3-lbYIFJMc; TART=%1%enc%3Ayw8QbNuJPjH5YKE4%2FgCqekLPfJE07%2B%2BmaNhn1upGbqwX0cWgOpkUREc9%2BQjM2qJqNox8JbUSTxk%3D; TASID=43FDDCC78A9C40DB92A3617D2CA39AE5; TASSK=enc%3AAJmpc8oDfY8yJOrzXmB1I6w9Y8tVgi%2BYnZxj9p1DTyV0jmis5YCLVfPAoIsCJ79n5xqeSb7m%2BWofM6cGjH56kspNqkMB91n0SQUHHIPCpr%2BLSZIQLMpmQRUGsa3ONGni9g%3D%3D; __vt=BLRWOwb_HppApV5kABQCIf6-ytF7QiW7ovfhqc-AvSI5Av4ju1XNnWJBHoibr2kSftvaWshRj3E-8ngrsjftM2lf4BBeVBOnpLNx3cqQk1WyLaF6i-rWTrwjbPC926cd9RzSmiuo2QUlzGU6k1N3_rgOrLY',
      'referer': 'https://www.tripadvisor.com/Restaurants-g60763-New_York_City_New_York.html',
      'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
      'x-requested-with': 'XMLHttpRequest'
    }
    response = requests.request("GET", url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(response.text, 'html.parser')
    for k in range(j+1, j+31):
      urls = "https://www.tripadvisor.com" + soup.find("div",{"data-test":str(k)+"_list_item"}).find("div",{"class":"zqsLh"}).find("a")["href"]
      print(urls)
      headers1 = {
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'accept-encoding': 'gzip, deflate, br',
      'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,gu;q=0.4,de;q=0.3',
      'cache-control': 'max-age=0',
      'cookie': 'TADCID=a128-G30Y73V2anZABQCFdpBzzOuRA-9xvCxaMyI13JXyJzkbUqFSQXVb2C73KwBGphgDXD5t3czGJUxP2gaED-ZhJdprbf5jtk; TAUnique=%1%enc%3Au%2FKH8yQEGORQwreYDGyVtOYenWoICPa8vSVstP18WGY%3D; TASSK=enc%3AAHYOXQMt6aP2AOtqfNEvYnOGSbLAsqMLbJRRSnO6Wlp47OmGFH6xC%2FkWC4sUpqS8fL7hEcMVN%2BrgME0vhhX3bjt5hO71EqQRqZL19nmcvTsx1y2S56%2FZ5kyi4p04bvFU9g%3D%3D; ServerPool=B; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; TATrkConsent=eyJvdXQiOiIiLCJpbiI6IkFMTCJ9; _pbjs_userid_consent_data=3524755945110770; _li_dcdm_c=.tripadvisor.com; _lc2_fpi=b140173de591--01gmtd5r0vydcgg72vqwr4aw1z; __gads=ID=a64abf6f536028b9:T=1671628515:S=ALNI_MbIzveR4fDzqZCNXtvPRFYtGNEioA; _lr_sampling_rate=100; _lr_env_src_ats=false; pbjs_li_nonid=%7B%22unifiedId%22%3A%22OIWdHOTuTULRIyCwjS612dP6u1RIlD7Fw3meUg%22%7D; TART=%1%enc%3Ats5cxHjqP8UkgYW1ToyP6uIqQ4B2QCKoF3Yq3hnptfv9H6d0NSAp8uPmIyouRabFh0izmtFali4%3D; PAC=ALyeV4hZBIUTOzZ7rm2AFG68PnuiBn1XIrk75Yx23dE56SKuthBKUyLXysM-o9HJ2vqSBjw3a2ICq6iPG7FsFcGGm8kl8fhrhyQycNjCTG9YOQfL9dmnxnpgIknY9YkKaYMDZSHIqO74K-iNV22oTWmIQ7pDEtgiL9Z3hoCn-qVOYbuSMym60Z_95dsp_Brl5A%3D%3D; TASID=43FDDCC78A9C40DB92A3617D2CA39AE5; _abck=B795C0C63EB090AD23FA3527B4C84858~0~YAAQ23AsMS/jRgmFAQAAK8IVOAkdLL/oa/PHCnfe0DtP1I+fp3uyPgWd9MA45jDCpmbmNNqGjeKPCRN0jc9ACpIxBqd1x+4lEcqriDrEUdetEMNxfS6J8xX92GEory7n43Rxv+53a98S1NzlYgPvd0JAxtPnFLmfIb3mtDFlpwbx1EdER0wzlrHrEVlP87cYK8snZGQ942nXLBfs0OOMWrzjtzzFWQGqP3Oi47KWujHDeOLpmELvXbxpwttAykp2r+NrCpmzCSFSVtvLa5+G/lYQgwjn+ejme2SDufxecNcQBCrvPzR4mHPLi2RuoxSEr63uKWcf9ZMqgYD9bk96XUEeV+DSMSAzc4HiElbG1+odpzCRUttttFcM6tbmN2TRFTRCx04oa3Rys3iIEP4zzjwXInn8tPK9gtX6i8M=~-1~-1~-1; ak_bmsc=37C2559396F9AEB974EA3DFF185C4128~000000000000000000000000000000~YAAQ23AsMTDjRgmFAQAAK8IVOBKT89iwIwNWJwxe5h8rrWqJ8/620MHB0Z7aQXfqDb3LtO5DvdeQNclDE53gPgw7LL92+LLguvyhK5mQ9Xgs8UPOpheBtjOGqe2+6YlSfOAGisgN5FGHoYvnA/sSRWB3LVHC7RMrboUx5aTd4pKN9HdNXu/m2Et4L5aoYrPeTG/5M6PgLP8yLkNQaUieae+uw8Y2bZa+qpHLKxMpNuHG4cgm28FJooHRwKCql4IDyz1KeIyzLZFk7AsRXnquZ7fObeNJcuO3DxdviVbfJu+QevOYZl8sX5HrDE31DR36BBTAMIUVfMc7uHx3YFxMy916Xm9qOTsC9IhdelOQVoe5DI7nbUCQfqrobnDvY1KVraEWxMioz7+hfDh3; bm_sz=0D2A3119824534F2FE03E734FA99CFE2~YAAQ23AsMTHjRgmFAQAAK8IVOBI4rsim9hhegVIVK6c0l+ePtgDHV8QVWiBuNkFlcU2c+pCRj2mJ7aVBferCzzO4uf9XEJ1H/+NevIxesW9aJbvx0iZkOXlAV/7B5kk0N0Z1uVoIMAgboEVoot5ENpywC17TEbQNwj17NsD5rMKFOJ97n53LWhSG5zXxrtezB6c6zGtZYFwuLTjpeAm3PLdrUjhIuLXMYFP4q20/Qe+KyZgwiwkZnR2pWJ4n+frS/odv+ajCHBD/aLfljrYPzOhkkoMUn6OJBMdA1AzTsKlXubzjMlhk3Q==~4339249~4337733; __gpi=UID=00000b9529363c00:T=1671628515:RT=1671683234:S=ALNI_MbMmBHG0_O0ira0QydvlFvT4pNBaw; PMC=V2*MS.55*MD.20221221*LD.20221222; SRT=%1%enc%3Ats5cxHjqP8UkgYW1ToyP6uIqQ4B2QCKoF3Yq3hnptfv9H6d0NSAp8uPmIyouRabFh0izmtFali4%3D; _lr_retry_request=true; __vt=S9DZ58FOSWaTktbCABQCIf6-ytF7QiW7ovfhqc-AvSI5VDivqwcWLb2VQINe8jfpCPdA9P4eEqFNXCmnLvJhyPjAGVISoj8_bzwlV-Qqo0YtsLIdTlAxNi6SAZb3XyA5Nky9zt7ooStpLsFR2crI7yB6Xvw; TAReturnTo=%1%%2FRestaurant_Review-g60763-d12425739-Reviews-Piccola_Cucina_Estiatorio-New_York_City_New_York.html; roybatty=TNI1625!AFVfN3FQUoYJy7pso70AYEM9yqOvpj490j1kN%2FyPtOkrCyUs9eOZELqWtcVYpFNg%2FXrF14L6Z6jxb13T5kGEhhfNRWIhQZfoZOtT3GbBfYrrUoJ7dgLH%2FPSC1oDqPjtbjqB8P2rr29%2B%2FOUt8IuqxmvqyJLCClGaih7jhBfx6quQt%2C1; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Dec+22+2022+11%3A32%3A12+GMT%2B0530+(India+Standard+Time)&version=202209.1.0&isIABGlobal=false&hosts=&consentId=f1a43cd3-a600-4f3d-9d54-26c000b3a8fb&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; TASession=V2ID.43FDDCC78A9C40DB92A3617D2CA39AE5*SQ.101*LS.DemandLoadAjax*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*LF.en*FA.1*DF.0*TRA.false*LD.12425739*EAU._; TAUD=LA-1671628511543-1*RDD-1-2022_12_21*LG-60425636-2.1.F.*LD-60425637-.....; bm_sv=5E2452C94F45877D685598A3484A35FD~YAAQ23AsMVSdTgmFAQAAXt9sOBIvEeZ3ab5vx3xYhWo4BTqpiLMwcPFz1TsaGKU/lL9xDWbeOgvK0hIffCJqI91uplYRaupiQd7XRem25uhOGaMasX/mHdzrKxtZGFQ9ENXVZCAc5Zp5D3GcncJJ7zfJGgeHsH7BAVqza7IslUdgBTzi2xqh/e1WeMNKbqqvAOW0SI9U5dUKr+Oa7McjGOS6aG5ESWzGvLxhcETm4ISlhn3I94idKHTeGKQMsGNONhMTd4jrig==~1; CM=%1%PremiumMobSess%2C%2C-1%7Csesswifi%2C%2C-1%7Ct4b-pc%2C%2C-1%7CRCPers%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7Csesstch15%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CCYLPUSess%2C%2C-1%7Ctvsess%2C%2C-1%7CTBPers%2C%2C-1%7Cperstch15%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCCSess%2C%2C-1%7CCYLSess%2C%2C-1%7CPremRetPers%2C%2C-1%7Cpershours%2C%2C-1%7C%24%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CTrayspers%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTADORSess%2C%2C-1%7CMCPPers%2C%2C-1%7Csesshours%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cmdpers%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7Csesslaf%2C%2C-1%7CRestPremRPers%2C%2C-1%7CCYLPUPers%2C%2C-1%7CRevHubRMPers%2C%2C-1%7Cperslaf%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCYLPers%2C%2C-1%7CCCPers%2C%2C-1%7Ctvpers%2C%2C-1%7CTBSess%2C%2C-1%7Cb2bmcsess%2C%2C-1%7Cperswifi%2C%2C-1%7CPremRetSess%2C%2C-1%7CRevHubRMSess%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CMCPSess%2C%2C-1%7CTADORPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CTrayssess%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CPremiumORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CSPORPers%2C%2C-1%7Cbooksticks%2C%2C-1%7Cbookstickp%2C%2C-1%7Cmdsess%2C%2C-1%7C; ServerPool=R; TAReturnTo=%1%%2FRestaurants-g60763-New_York_City_New_York.html; TASession=V2ID.43FDDCC78A9C40DB92A3617D2CA39AE5*SQ.102*LS.DemandLoadAjax*HS.recommended*ES.popularity*DS.5*SAS.popularity*FPS.oldFirst*LF.en*FA.1*DF.0*TRA.false*LD.12425739*EAU._; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; TAUD=LA-1671628511543-1*RDD-1-2022_12_21*LG-60987525-2.1.F.*LD-60987526-.....; TAUnique=%1%enc%3A34nCenJbfc%2FLDxBs24k%2BMVlK1CyptGY8XfyBM2Zw7d4%3D; _abck=B795C0C63EB090AD23FA3527B4C84858~-1~YAAQ2HAsMeRJnxSFAQAAb3R1OAl2Nf1g4YUeoI93buH2i+J+/lCB8+0L8P9vJrcpBhESxWp9ke3m2YLWbvq3NGT5o4m/oiGVS0cSt/Ttw9cse/knZqVkVk0RSP6Eb8Y1IugJ1/g+2jNsTyGoX/QUS8urC5jHCEwJ6cy/US+GMXRBAIWavVjh93Q44ehMubje3X8uD+AQFEz8xQEnOWb0Wo9/Rk9uYQ85qgfc1CVDRd1FcIkPnHQf3QzvoWhIVJzEocPzStdGBiM1mOaCaVbXwuOGBPxZRgJJMkDvcSYb5mEzpKtpVgT+gwololVLn/GMBc5P/A0E/s5/JxaGBMez1BgUrSWtKIeV96ELbBLyWiK6QQbgqdHZLq9fHKdYmqyha+fqlTUsma8q4nG5EDJ7jt8bg820RySuWs2zbus=~0~-1~-1; bm_sz=A3407F678F4CE798C839D6BFC818547E~YAAQ23AsMZi+SgmFAQAA4/s2OBL3YpciPWNDDhmXzW/HJ1dVNVkvQeCcuXVRxUzR9HiQBVKnlytlfA5sKhwu3IZCba6+0Pt8Xd/WzSKDA10+AIEKQOlrjRFX2bJo2rsIrHPPVx1GIdG2Arn2zAXBGthmf80Kpa6B8KVOG4lwwsq4fpux9HhCbzJmlqWTsTubshsTrpm9dNa7TWjYWAKVneEGpbeoQfJl6+7SRS/TPFP74nBM3T7BL8Aaenc8QDoG8lkNIeplcZlcyXGUdvDhVzKNYXK22j2+D6I5+Wp3vJgjdDJ029wgaw==~4272452~3618629; PAC=AGPSnk5O_jRPsU1IU_dJFcTwx8RF-4z605sEejAH5a8SlTS0yBuXmROjcVB909SYlAUA0GIfm6hRnRXcoMPgQaLQH4lqqVHbmekudjU9GfDndTm9dtpluVCfUS5SdTnNMm0hkLQTxiT4Vi3qEPT6s5_ATdvsvW7EMCZZrhRGy4i1VCaMht4y1STGgikEGueijw%3D%3D; PMC=V2*MS.7*MD.20221222*LD.20221222; TADCID=kmlBVm1SmVIFia53ABQCFdpBzzOuRA-9xvCxaMyI13JbfAnB35PSNzbOvcB9oQgVO35oq41Zh7LlEUNqLTbspwtM_3-lbYIFJMc; TART=%1%enc%3Ayw8QbNuJPjH5YKE4%2FgCqekLPfJE07%2B%2BmaNhn1upGbqwX0cWgOpkUREc9%2BQjM2qJqNox8JbUSTxk%3D; TASID=43FDDCC78A9C40DB92A3617D2CA39AE5; TASSK=enc%3AAJmpc8oDfY8yJOrzXmB1I6w9Y8tVgi%2BYnZxj9p1DTyV0jmis5YCLVfPAoIsCJ79n5xqeSb7m%2BWofM6cGjH56kspNqkMB91n0SQUHHIPCpr%2BLSZIQLMpmQRUGsa3ONGni9g%3D%3D',
      'referer': 'https://www.tripadvisor.com/Restaurants-g60763-New_York_City_New_York.html',
      'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
      }
      response1 = requests.request("GET", urls, headers=headers1)
      soup1 = BeautifulSoup(response1.text, 'html.parser')
      location_id = soup1.find("div",{"class":"hidden photo_mosaic_info"})["data-location-id"]
      datas = str(soup1).split("window.__WEB_CONTEXT__={pageManifest:")[1].split("};(this.$WP=this.$WP||[])")[0]
      json_data = json.loads(datas)

      try:
        name = json_data["redux"]["api"]["responses"]["/data/1.0/location/"+str(location_id)]["data"]["name"]
      except:
        name = ''
      try:
        address = json_data["redux"]["api"]["responses"]["/data/1.0/location/"+str(location_id)]["data"]["address"]
      except:
        address = ''
      try:
        street1 = json_data["redux"]["api"]["responses"]["/data/1.0/location/"+str(location_id)]["data"]["address_obj"]["street1"]
      except:
        street1 = ''
      try:
        street2 = str(json_data["redux"]["api"]["responses"]["/data/1.0/location/"+str(location_id)]["data"]["address_obj"]["street2"]).replace("None","")
      except:
        street2 = ''
      try:
        city = json_data["redux"]["api"]["responses"]["/data/1.0/location/"+str(location_id)]["data"]["address_obj"]["city"]
      except:
        city = ''
      try:
        state = json_data["redux"]["api"]["responses"]["/data/1.0/location/"+str(location_id)]["data"]["address_obj"]["state"]
      except:
        state = ''
      try:
        country = json_data["redux"]["api"]["responses"]["/data/1.0/location/"+str(location_id)]["data"]["address_obj"]["country"]
      except:
        country = ''
      try:
        postalcode = json_data["redux"]["api"]["responses"]["/data/1.0/location/"+str(location_id)]["data"]["address_obj"]["postalcode"]
      except:
        postalcode = ''
      try:
        phone_no = json_data["redux"]["api"]["responses"]["/data/1.0/location/"+str(location_id)]["data"]["phone"]
      except:
        phone_no = ''
      try:
        email = json_data["redux"]["api"]["responses"]["/data/1.0/location/"+str(location_id)]["data"]["email"]
      except:
        email = ''
      try:
        website = json_data["redux"]["api"]["responses"]["/data/1.0/location/"+str(location_id)]["data"]["website"]
      except:
        website = ''
      try:
        rating = json_data["redux"]["api"]["responses"]["/data/1.0/location/"+str(location_id)]["data"]["rating"]
      except:
        rating = ''
      try:
        reviews_count = json_data["redux"]["api"]["responses"]["/data/1.0/location/"+str(location_id)]["data"]["num_reviews"]
      except:
        reviews_count = ''
      try:
        latitude = json_data["redux"]["api"]["responses"]["/data/1.0/location/"+str(location_id)]["data"]["latitude"]
      except:
        latitude = ''
      try:
        longitude = json_data["redux"]["api"]["responses"]["/data/1.0/location/"+str(location_id)]["data"]["longitude"]
      except:
        longitude = ''
      try:
        rating_food = str(json_data["redux"]["api"]["responses"]["/data/1.0/restaurant/"+str(location_id)+"/overview"]["data"]["rating"]["ratingQuestions"][0]["name"]) +"rating: "+ str(json_data["redux"]["api"]["responses"]["/data/1.0/restaurant/"+str(location_id)+"/overview"]["data"]["rating"]["ratingQuestions"][0]["rating"])
      except:
        rating_food = ''
      try:
        rating_service = str(json_data["redux"]["api"]["responses"]["/data/1.0/restaurant/"+str(location_id)+"/overview"]["data"]["rating"]["ratingQuestions"][1]["name"]) +"rating: "+ str(json_data["redux"]["api"]["responses"]["/data/1.0/restaurant/"+str(location_id)+"/overview"]["data"]["rating"]["ratingQuestions"][1]["rating"])
      except:
        rating_service = ''
      try:
        rating_value = str(json_data["redux"]["api"]["responses"]["/data/1.0/restaurant/"+str(location_id)+"/overview"]["data"]["rating"]["ratingQuestions"][2]["name"]) +"rating: "+ str(json_data["redux"]["api"]["responses"]["/data/1.0/restaurant/"+str(location_id)+"/overview"]["data"]["rating"]["ratingQuestions"][2]["rating"])
      except:
        rating_value = ''
      try:
        price = json_data["redux"]["api"]["responses"]["/data/1.0/location/"+str(location_id)]["data"]["price"]
      except:
        price = ''
      try:
        image = json_data["redux"]["api"]["responses"]["/data/1.0/location/"+str(location_id)]["data"]["photo"]["images"]["original"]["url"]
      except:
        image = ''
      varity = []
      try:
        for data1 in json_data["redux"]["api"]["responses"]["/data/1.0/location/"+str(location_id)]["data"]["cuisine"]:
          data2 = data1["name"]
          varity.append(data2)
      except:
        varity.append('')
      varities = ", ".join(varity)
      time = []
      try:
        for data3 in json_data["redux"]["api"]["responses"]["/data/1.0/location/"+str(location_id)]["data"]["display_hours"]:
          data4 = data3["days"] +": "+ str(data3["times"]).replace('[',"").replace(']',"").replace('"',"").replace("'","")
          time.append(data4)
      except:
        time.append('')
      open_hours = ", ".join(time)
      print(name)
      page_url = urls

      store =[name,address,street1,street2,city,state,country,postalcode,phone_no,email,website,rating,reviews_count,latitude,longitude,rating_food,rating_service,rating_value,price,varities,image,open_hours,page_url]
      yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()

