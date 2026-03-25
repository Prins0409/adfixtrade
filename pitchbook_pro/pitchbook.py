import requests
import json
import csv

def write_output(data):
	with open('pitchBooks_technology.csv', mode='w',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["stock_full_data","stocks_highlights","company_general_information","primary_contact_information","primary_office_information","alternate_office_information","industry_vertical","market_analysis","similar_companies","investors","investor_lead_partners","filings"])
		for row in data:
			writer.writerow(row)
k = 0
while True:
    def fetch_data():
        url = "https://my.pitchbook.com/web-api/advanced-search-api/tables/s214138797.peer_group.data_set/data?page="+str(k)+"&pageSize=250&recentUpdatesMode=false"
        payload = "page="+str(k)+"&pageSize=250&recentUpdatesMode=false"
        headers = {
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5,gu;q=0.4,de;q=0.3',
        'content-length': '0',
        'cookie': '_dy_csc_ses=t; _dy_c_exps=; _dycnst=dg; _dyid=6282521675120590578; _dyjsession=cae877a1153d7b609dd5b6f570a6f629; _dycst=dk.w.c.ws.; _gcl_au=1.1.1325594438.1665220339; _biz_uid=81eb08b730614abdfe4daec17110ab71; fpid=e8685a3cc360f33c0e650cd237ec2cda; _mkto_trk=id:942-MYM-356&token:_mch-pitchbook.com-1665220339867-91219; _fbp=fb.1.1665220340056.1276083760; __adroll_fpc=104735905872ede13ce0b113ae7393ea-1665220340418; drift_aid=0e0642ca-3d93-4e66-bef3-d458bbfd38b5; driftt_aid=0e0642ca-3d93-4e66-bef3-d458bbfd38b5; pxcts=6662b57f-46e9-11ed-951e-504a5747526b; _pxvid=5e830ac5-46e9-11ed-be12-6d73624a7077; _dyfs=1665220384730; place_id=19dc7cff-02d9-44b3-84c4-d42c91d06a60; fs_cid=1.0; dy_fs_page=my.pitchbook.com%2Floginaction.do%3Faction%3Dlogin; _gid=GA1.2.1285602917.1665408183; liveagent_oref=https://my.pitchbook.com/loginAction.do?action=login; liveagent_sid=b583ebec-d35d-47bc-a1b6-dae55b7e8162; liveagent_vc=2; liveagent_ptid=b583ebec-d35d-47bc-a1b6-dae55b7e8162; _dy_c_att_exps=; _hjSessionUser_77093=eyJpZCI6ImRjOWY0ZWE5LWNiNmItNWI2Ni1hMzYxLWNiNjViNGU0ZmU0NCIsImNyZWF0ZWQiOjE2NjUyMjAzMzk5MDEsImV4aXN0aW5nIjp0cnVlfQ==; _biz_flagsA=%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%2C%22Frm%22%3A%221%22%2C%22Mkto%22%3A%221%22%7D; _pxhd=klsEg5YzPwj3mwCsU/-MltQ5cx9eESK7OtNWpYNmkjMVOmPAqIRUGwo63nqJyXsTmihOqkDs3L/qM2PeUlMG5Q==:i1L/sfa1VyYpLRGzNiYlIrrTB3fVEcRC2an4vQNvUwm7r6watdEq4qCoFioReumnE9i1OmFoZ1HXlc2KpZgbierrv/viVm6m53k6i6zRInE=; _dy_geo=IN.AS.IN_GJ.IN_GJ_Surat; _dy_df_geo=India..Surat; _biz_sid=1671ad; _dy_toffset=0; fs_uid=#CMR2P#4656749815238656:6194699438886912:::#cc674b79#/1696756406; sourceType=DIRECT; sourceUrl=https%3A%2F%2Fmy.pitchbook.com%2Flogout; DriftPlaybook=A; highDensity=true; _hjSession_77093=eyJpZCI6ImJmNWNmNmZiLTQ3M2ItNDFhZS1hMjYyLTZmNTMxNDYxZWEwMiIsImNyZWF0ZWQiOjE2NjU1OTc1MDg2MTksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _uetsid=7a230de04a5711edab6a8bf6144d7202; _uetvid=4fd9bdf046e911ed8c963353fa6b7605; __ar_v4=2HN5SB32U5B7RKLIF5GUQE%3A20221007%3A3%7C5S2POJ2OE5GPZNGPI6HCQ6%3A20221007%3A3%7CABSQS3OE7JFQRP56UD4C6C%3A20221007%3A3; _clck=1d9q2so|1|f5n|0; _clsk=zj36qa|1665597511466|1|1|j.clarity.ms/collect; _ga_DS3177N6CK=GS1.1.1665597508.4.0.1665597511.57.0.0; _ga=GA1.2.207862471.1665220339; _dy_ses_load_seq=94617%3A1665598062413; _dy_soct=417895.725550.1665592281*372970.622086.1665598062; _dy_lu_ses=cae877a1153d7b609dd5b6f570a6f629%3A1665598062701; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; _pxff_rf=1; _biz_nA=61; _biz_pendingA=%5B%5D; SESSION=59b5cb95-a0d1-45a5-a455-050cdacf45ec; _pxff_tm=1; _px3=391fd487f3d3c1264a07688b467efbdb7c24b32514c3ef7b5f2e84ebdc641361:Kg8ebFO8aux2rR/SX4LYiQJXExJcwvkaTQP0/Uln7YpIv0OrIdG5xM9DmJfaKXaHgMjf135h8lPjmw6UDvUreQ==:1000:PFCsQYzkbX8ba6ZhoCTrhn8+IhIRa7/pHVxbV1hJ7VyzsOS0Y+cCx52r5JIJBk21M4frW/TPagi9+kV5IROzt9fRfb3V01FTtij72FgDoOg8xiLJFKa9wpxbPaLooO3fi9FAcsKhM9bcpDpLiNwuv981azHdPjJ1+bM7Q2pZYR5XmRW222561F1D9GpFBI+a+WhpdYyB+JPfLAHMoyFwsw==',
        'origin': 'https://my.pitchbook.com',
        'referer': 'https://my.pitchbook.com/search-results/s214138797/peer_group',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'Content-Type': 'text/plain'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        json_data = json.loads(response.text)
        json_datas = json_data['dataRows']
        for data in json_datas:
            stock_prices = data['columnValues']['StockPrice']
            stock_price = []
            for stock_value in stock_prices:
                stock_price.append("stock value: " + str(stock_value['value']))
            
            stock_date = data['columnValues']['ReportedDate']
            asOfdate = []
            for stock_dates in stock_date:
                asOfdate.append(", as of date: " + str(stock_dates['asOfdate']))

            market_caps = data['columnValues']['marketCapBasic']
            market_cap = []
            for stock_market_caps in market_caps:
                market_cap.append(", market cap: " + str(stock_market_caps['value']))
            
            enterprise_values = data['columnValues']['enterpriseValue_PG']
            enterprise_value = []
            for stock_enterprise_value in enterprise_values:
                enterprise_value.append(", enterprise value: " + str(stock_enterprise_value['value']))
            
            grossMargin_TTM_values = data['columnValues']['grossMargin_TTM']
            grossMargin_TTM = []
            for grossMargin_TTM_value in grossMargin_TTM_values:
                grossMargin_TTM.append(", gross margin_TTM: " + str(grossMargin_TTM_value['value']))
            
            EBITDAMargin_TTM_values = data['columnValues']['EBITDAMargin_TTM']
            EBITDAMargin_TTM = []
            for EBITDAMargin_TTM_value in EBITDAMargin_TTM_values:
                EBITDAMargin_TTM.append(", EBITDA margin_TTM: " + str(EBITDAMargin_TTM_value['value']))
            
            priceEarnings_values = data['columnValues']['priceEarnings']
            priceEarnings = []
            for priceEarnings_value in priceEarnings_values:
                priceEarnings.append(", price earnings: " + str(priceEarnings_value['value']))
            
            priceBook_values = data['columnValues']['priceBook']
            priceBook = []
            for priceBook_value in priceBook_values:
                priceBook.append(", price book: " + str(priceBook_value['value']))
            
            enterpriseValueEBITDA_values = data['columnValues']['enterpriseValueEBITDA']
            enterpriseValueEBITDA = []
            for enterpriseValueEBITDA_value in enterpriseValueEBITDA_values:
                enterpriseValueEBITDA.append(", enterprise value EBITDA: " + str(enterpriseValueEBITDA_value['value']))
            
            activeCoverage_values = data['columnValues']['activeCoverage']
            columnValueType = []
            accessStatus = []
            activeCoverage = columnValueType + accessStatus
            for activeCoverage_value in activeCoverage_values:
                activeCoverage.append(", column value type: " + str(activeCoverage_value['columnValueType']) + ", access status: " +  str(activeCoverage_value['accessStatus']))
            
            latestStockAnalystNote_values = data['columnValues']['latestStockAnalystNote']
            columnValueType = []
            accessStatus = []
            latestStockAnalystNote = columnValueType + accessStatus
            for latestStockAnalystNote_value in latestStockAnalystNote_values:
                latestStockAnalystNote.append(", latest stock analyst note: " + str(latestStockAnalystNote_value['columnValueType']) + ", latest stock values: " + str(latestStockAnalystNote_value['accessStatus']))
            
            latestCashFlowModel_values = data['columnValues']['latestCashFlowModel']
            columnValueType = []
            accessStatus = []
            latestCashFlowModel = columnValueType + accessStatus
            for latestCashFlowModel_value in latestCashFlowModel_values:
                latestCashFlowModel.append(", latest cash flow model: " + str(latestCashFlowModel_value['columnValueType']) + ", latest cash flow model value: " +  str(latestCashFlowModel_value['accessStatus']))
            
            morningstarRating_values = data['columnValues']['morningstarRating']
            columnValueType = []
            accessStatus = []
            morningstarRating = columnValueType + accessStatus
            for morningstarRating_value in morningstarRating_values:
                morningstarRating.append(", morningstar rating: " + str(morningstarRating_value['columnValueType']) + ", morning star rating value: " + str(morningstarRating_value['accessStatus']))

            gecsIndustry_values = data['columnValues']['gecsIndustry']
            gecsIndustry = []
            for gecsIndustry_value in gecsIndustry_values:
                gecsIndustry.append(", gecs industry: " + str(gecsIndustry_value['value']))
            
            hqCountry_values = data['columnValues']['hqCountry']
            hqCountry = []
            for hqCountry_value in hqCountry_values:
                hqCountry.append(", hq country: " + str(hqCountry_value['value']))
            
            pbid_for_url_values = data['columnValues']['companyName']
            page_url = []
            for pbid_for_url_value in pbid_for_url_values:
                page_url.append(", page url: " + "https://my.pitchbook.com/profile/"+ str(pbid_for_url_value['pbId']) +"/company/profile")

            if page_url == None:
                break
            page_urls = "https://my.pitchbook.com/profile/"+ data['pbId'] +"/company/profile"
            print(page_urls)
            yield_data_1 = stock_price + asOfdate + market_cap + enterprise_value + grossMargin_TTM + EBITDAMargin_TTM + priceEarnings + priceBook + enterpriseValueEBITDA + activeCoverage + latestStockAnalystNote + latestCashFlowModel + morningstarRating + gecsIndustry + hqCountry + page_url

            url1 = "https://my.pitchbook.com/web-api/profiles/"+ data['pbId'] +"/company/insights?exchangeId=TSX&exchangeSymbol=ONE"
            payload1 = "exchangeId=TSX&exchangeSymbol=ONE"
            response1 = requests.request("GET", url1, headers=headers, data=payload1)
            json_data1 = json.loads(response1.text)
            try:
                json_datas1 = json_data1['items']
            except:
                json_datas1 = ''

            for data1 in json_datas1:
                highlights = data1['highlight']
                if highlights == "INDUSTRY_VERTICAL":
                    try:
                        descriptions = data1['primaryIndustry']['description']
                    except:
                        descriptions = ''
                    description = []
                    description.append(descriptions)
            yield_data_2 = description
            
            url2 = "https://my.pitchbook.com/web-api/profiles/"+ data['pbId'] +"/company/general-info?shareClass=0P00005RWB"
            payload2 = "shareClass=0P00005RWB"
            response2 = requests.request("GET", url2, headers=headers, data=payload2)
            json_data2 = json.loads(response2.text)
            try:
                full_descriptions = json_data2['description'] + "," + json_data2['financingStatusNote']
            except:
                full_descriptions = ''
            try:
                website = ", Website: " + json_data2['website']
            except:
                website = ''
            try:
                entities = json_data2['types']
            except:
                entities = ''
            entity_type = ", Entity: " + "; ".join(entities)
            try:
                official_name = ", OfficialName: " + json_data2['officialName']
            except:
                official_name = ''
            try:
                business_status = ", businessStatus: " + json_data2['businessStatus']
            except:
                business_status = ''
            try:
                ownership_status = ", ownershipStatus: " + json_data2['ownershipStatus']
            except:
                ownership_status = ''
            try:
                financing_status = ", financingStatus: " + json_data2['financingStatus']
            except:
                financing_status = ''
            try:
                date_founded = ", dateFounded: " + json_data2['dateFounded']
            except:
                date_founded = ''
            try:
                domicile = ", domicile: " + json_data2['domicile']
            except:
                domicile = ''
            try:
                universe = json_data2['universes']
            except:
                universe = ''
            universes = ", Universe: " + "; ".join(universe)
            try:
                employee_history = ", employeeHistory: " + str(json_data2['employeeHistory'])
            except:
                employee_history = ''

            full_description = []
            full_description.append(full_descriptions + website + entity_type + official_name + business_status + ownership_status + financing_status + date_founded + domicile + universes + employee_history)
            yield_data_3 = full_descriptions + website + entity_type + official_name + business_status + ownership_status + financing_status + date_founded + domicile + universes + employee_history

            url3 = "https://my.pitchbook.com/web-api/profiles/"+ data['pbId'] +"/company/contact-info"
            response3 = requests.request("GET", url3, headers=headers)
            json_data3 = json.loads(response3.text)
            try:
                first_name = json_data3['primaryContact']['firstName']
            except:
                first_name = ''
            try:
                last_name = json_data3['primaryContact']['lastName']
            except:
                last_name = ''
            full_name = "Full name: " + first_name +" "+ last_name
            try:
                position = ", Position: " + json_data3['primaryContact']['primaryPosition']
            except:
                position = ''
            try:
                mail_id = ", Mail id: " + json_data3['primaryContact']['contactInfo']['email']
            except:
                mail_id = ''
            try:
                phone_no = ", Phone no: " + json_data3['primaryContact']['contactInfo']['phone']
            except:
                phone_no = ''
            try:
                linkedInLink_id = ", LinkedIn id: " + json_data3['primaryContact']['contactInfo']['linkedInLink']
            except:
                linkedInLink_id = ''
            primary_contact = []
            primary_contact.append(full_name + position + mail_id + phone_no + linkedInLink_id)
            yield_data_4 = full_name + position + mail_id + phone_no + linkedInLink_id

            full_address = "Full address: " + str(json_data3['primaryOffice']['address'])
            try:
                email_id = ", email Id: " + json_data3['primaryOffice']['email']
            except:
                email_id = ''
            try:
                phone_number = ", phone Number: " + json_data3['primaryOffice']['phone']
            except:
                phone_number = ''
            try:
                fax = ", fax: " + json_data3['primaryOffice']['fax']
            except:
                fax = ''
            try:
                country_city = ", country: " + json_data3['primaryOffice']['country'] + ", city: "  + json_data3['primaryOffice']['name']
            except:
                country_city = ''
            primary_office = []
            primary_office.append(full_address + email_id + phone_number + fax + country_city)
            yield_data_5 = full_address + email_id + phone_number + fax + country_city
            
            try:
                alternate_office_data = json_data3['alternateOffices']
            except:
                alternate_office_data = ''
            alternate_office_full_address = ''
            email_id_alt = ''
            phone_number_alt = ''
            fax_alt = ''
            country_city_alt = ''
            for all_datta in alternate_office_data:
                alternate_office_full_address = "Full address: " + str(all_datta['address'])
                try:
                    email_id_alt = ", Mail id: " + all_datta['email']
                except:
                    email_id_alt = ''
                try:
                    phone_number_alt = ", phone Number: " + all_datta['phone']
                except:
                    phone_number_alt = ''
                try:
                    fax_alt = ", fax: " + all_datta['fax']
                except:
                    fax_alt = ''
                try:
                    country_city_alt = ", country: " + all_datta['country'] + ", city: "  + all_datta['name']
                except:
                    country_city_alt = ''
            alternate_office = []
            alternate_office.append(alternate_office_full_address + email_id_alt + phone_number_alt + fax_alt + country_city_alt)
            yield_data_6 = alternate_office_full_address + email_id_alt + phone_number_alt + fax_alt + country_city_alt
            
            url4 = "https://my.pitchbook.com/web-api/profiles/"+ data['pbId'] +"/company/industry-vertical"
            response4 = requests.request("GET", url4, headers=headers)
            json_data4 = json.loads(response4.text)
            
            industry_data = json_data4['industries']
            all_industry_description = []
            for description in industry_data:
                all_industry_description.append("Industries description: " + str(description['description']))

            try:
                verticals_data = json_data4['verticals']
            except:
                verticals_data = ''
            all_verticals_description = []
            for description1 in verticals_data:
                all_verticals_description.append("Verticals description: " + str(description1['description']))
            
            keywords_data = json_data4['keywords']
            all_keywords_description = []
            for description2 in keywords_data:
                all_keywords_description.append("Keywords description: " + str(description2['keyword']))
            
            all_gecs_sector = "Gecs sector: " + str(json_data4['gecsSector'])
            all_gecs_industry = "Gecs industry: " + str(json_data4['gecsIndustry']['description'])

            try:
                all_naics_sectors = json_data4['naicsSectors']
            except:
                all_naics_sectors = ''
            all_naics_sectors_description = []
            for description3 in all_naics_sectors:
                all_naics_sectors_description.append("Total " + str(description3['code']) +" naics sectors:- "+ str(description3['description']))
            
            try:
                all_naics_industries = json_data4['naicsIndustries']
            except:
                all_naics_industries = ''
            all_naics_industries_description = []
            for description4 in all_naics_industries:
                all_naics_industries_description.append("Total " + str(description4['code']) +" naics industries:- "+ str(description4['description']))
            yield_data_7 = str(all_industry_description) + str(all_verticals_description) + str(all_keywords_description) + str(all_gecs_sector) + str(all_gecs_industry) + str(all_naics_sectors_description) + str(all_naics_industries_description)

            url5 = "https://my.pitchbook.com/web-api/profiles/"+ data['pbId'] +"/company/market-analysis?searchType=MARKET_MAP"
            response5 = requests.request("GET", url5, headers=headers)
            json_data5 = json.loads(response5.text)
            
            try:
                trends_company_spaces_data = json_data5['trendsCompanySpaces']
            except:
                trends_company_spaces_data = ''
            space_name = []
            companies_count = []
            for description5 in trends_company_spaces_data:
                space_name.append("space name: " + str(description5['spaceName']))
                companies_count.append("companies count: " + str(description5['companiesCount']))
            try:
                company_spaces_data = json_data5['publishedSearchData']
            except:
                company_spaces_data = ''
            company_spaces_title = []
            company_spaces_description = []
            for description6 in company_spaces_data:
                company_spaces_title.append("company spaces title: " + str(description6['title']))
                try:
                    company_spaces_description.append("company spaces description: " + str(description6['description']))
                except:
                    continue
            yield_data_8 = space_name + companies_count + company_spaces_title + company_spaces_description

            url6 = "https://my.pitchbook.com/web-api/profiles/"+ data['pbId'] +"/company/similar-companies?count=5"
            response6 = requests.request("GET", url6, headers=headers)
            json_data6 = json.loads(response6.text)

            all_datas = json_data6['items']
            name_of_similar_companies = []
            similar_companies_competitor = []
            companies_financing_status = []
            companies_location = []
            primary_industry_code = []
            founded_year = []
            lastFinancing_date_and_type = []
            company_amount = []
            for companies in all_datas:
                name_of_similar_companies.append(companies['company']['name'])
                similar_companies_competitor.append(companies['competitor'])
                companies_financing_status.append(companies['companyType'])
                try:
                    companies_location.append(companies['location'])
                except:
                    companies_location.append('')  
                primary_industry_code.append(companies['primaryIndustryCode'])
                try:
                    founded_year.append(companies['foundedYear'])
                except:
                    founded_year.append('')
                try:
                    lastFinancing_date_and_type.append(companies['lastFinancingDate'] +'/'+ companies['lastFinancingType'])
                except:
                    lastFinancing_date_and_type.append('')
                try:
                    company_amount.append(companies['raisedToDate']['amount'])
                except:
                    company_amount.append('')
            yield_data_9 = name_of_similar_companies + similar_companies_competitor + companies_financing_status + companies_location + primary_industry_code + founded_year + lastFinancing_date_and_type + company_amount

            url7 = "https://my.pitchbook.com/web-api/profiles/"+ data['pbId'] +"/company/investors/PENDING_BUY_SIDE?page=1&pageSize=10"
            response7 = requests.request("GET", url7, headers=headers)
            json_data7 = json.loads(response7.text)

            try:
                all_the_data = json_data7['content']
            except:
                all_the_data = ''
            name_of_investors = []
            type_of_investors = []
            for investors in all_the_data:
                name_of_investors.append(investors['investor']['name'])
                type_of_investors.append(investors['investorType'])
            related_deals = []
            deal_amount = []
            deal_as_of_date = []
            type_of_investor = []
            investor_contact = []
            investor_contact_no = []
            investor_contact_email = []
            investor_contact_linkedin = []
            for investor_deals in all_the_data:
                all_the_datas = investor_deals['rounds']
                for related_deal in all_the_datas:
                    try:
                        related_deals.append(str(related_deal['roundInfo']['number']) +"/"+ related_deal['roundInfo']['type'])
                    except:
                        related_deals = ''
                    try:
                        deal_amount.append(related_deal['roundInfo']['amount']['amount'])
                    except:
                        deal_amount = ''
                    try:
                        deal_as_of_date.append(related_deal['roundInfo']['amount']['asOfDate'])
                    except:
                        deal_as_of_date = ''
                    try:
                        type_of_investor.append(related_deal['roundStatus'])
                    except:
                        type_of_investor = ''
                    try:
                        investor_contact.append(related_deal['leadPartner']['firstName']+" "+related_deal['leadPartner']['lastName'])
                    except:
                        investor_contact = ''
                    try:
                        investor_contact_no.append(related_deal['leadPartner']['contactInfo']['phone'])
                    except:
                        investor_contact_no = ''
                    try:
                        investor_contact_email.append(related_deal['leadPartner']['contactInfo']['email'])
                    except:
                        investor_contact_email = ''
                    try:
                        investor_contact_linkedin.append(related_deal['leadPartner']['contactInfo']['linkedInLink'])
                    except:
                        investor_contact_linkedin = ''
            yield_data_10 = related_deals + deal_amount + deal_as_of_date + type_of_investor + investor_contact + investor_contact_no + investor_contact_email + investor_contact_linkedin

            url8 = "https://my.pitchbook.com/web-api/profiles/"+ data['pbId'] +"/company/investor-lead-partners?page=1&pageSize=10"
            response8 = requests.request("GET", url8, headers=headers)
            json_data8 = json.loads(response8.text)

            try:
                lead_partners_data = json_data8['content']
            except:
                lead_partners_data = ''
            name_of_lead_partners = []
            total_deals = []
            title_of_lead_partners = []
            related_deals_lead_partners = []
            partners_deal_as_of_date = []
            partners_deal_amount = []
            deal_complete_or_not = []
            partners_contact_no = []
            partners_contact_email = []
            partners_contact_linkedin = []
            for partners in lead_partners_data:
                try:
                    name_of_lead_partners.append(partners['person']['firstName']+" "+partners['person']['lastName'])
                except:
                    name_of_lead_partners = ''
                try:
                    total_deals.append(partners['personDealsNumber'])
                except:
                    total_deals = ''
                try:
                    title_of_lead_partners.append(partners['personTitle'])
                except:
                    title_of_lead_partners = ''
                try:
                    related_deals_lead_partners.append(str(partners['recentDeal']['number']) +"/"+ partners['recentDeal']['type'])
                except:
                    related_deals_lead_partners = ''
                try:
                    partners_deal_as_of_date.append(partners['recentDeal']['date'])
                except:
                    partners_deal_as_of_date = ''
                try:
                    partners_deal_amount.append(partners['recentDeal']['amount']['amount'])
                except:
                    partners_deal_amount = ''
                try:
                    deal_complete_or_not.append(partners['recentDeal']['status'])
                except:
                    deal_complete_or_not = ''
                try:
                    partners_contact_no.append(partners['person']['contactInfo']['phone'])
                except:
                    partners_contact_no = ''
                try:
                    partners_contact_email.append(partners['person']['contactInfo']['email'])
                except:
                    partners_contact_email = ''
                try:
                    partners_contact_linkedin.append(partners['person']['contactInfo']['linkedInLink'])
                except:
                    partners_contact_linkedin = ''
            yield_data_11 = str(name_of_lead_partners) + str(total_deals) + str(title_of_lead_partners) + str(related_deals_lead_partners) + str(partners_deal_as_of_date) + str(partners_deal_amount) + str(deal_complete_or_not) + str(partners_contact_no) + str(partners_contact_email) + str(partners_contact_linkedin)

            filled_date = []
            filled_title = []
            filled_country = []
            filled_language = []
            filled_type = []
            filled_cikId = []
            for i in range(1,100):
                if data['pbId']==None:
                    url9 = "https://my.pitchbook.com/web-api/filings/api/filings/public-company/"+ data['pbId'] +"/tab/ALL?page="+str(i)+"&pageSize=10"
                    response9 = requests.request("GET", url9, headers=headers)
                    json_data9 = json.loads(response9.text)

                    fillings_data = json_data9['filings']
                    for filled_datas in fillings_data:
                        try:
                            filled_date.append(filled_datas['filedDate'])
                        except:
                            filled_date.append('')
                    try:
                        filled_title.append(filled_datas['title'])
                    except:
                        filled_title = ''
                    try:
                        filled_country.append(filled_datas['filingCountry'])
                    except:
                        filled_country = ''
                    try:
                        filled_language.append(filled_datas['language'])
                    except:
                        filled_language = ''
                    try:
                        filled_type.append(filled_datas['type'])
                    except:
                        filled_type = ''
                    try:
                        filled_cikId.append(filled_datas['cikId'])
                    except:
                        filled_cikId = ''
            yield_data_12 = filled_date + filled_title + filled_country + filled_language + filled_type + filled_cikId
            store =[str(yield_data_1),str(yield_data_2),str(yield_data_3),str(yield_data_4),str(yield_data_5),str(yield_data_6),str(yield_data_7),str(yield_data_8),str(yield_data_9),str(yield_data_10),str(yield_data_11),str(yield_data_12)]
            yield store
    k += 1
    def scrape():
        data = fetch_data()
        write_output(data)
    scrape()
