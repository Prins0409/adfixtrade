import csv
from html.parser import HTMLParser
from itertools import count
from tkinter import N
from bs4 import BeautifulSoup
from numpy import empty
import requests
import json
from pymongo import MongoClient
from bson.json_util import dumps

def write_output(data):
	with open('linkedin_usa_all_title_profiles.csv', mode='a',newline="", encoding="utf-8") as output_file:
		writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		writer.writerow(["full_name","phone_numbers","mobile_phone","emails","industry","job_company_name","job_title","work_email","location_country","full_address"])
		for row in data:
			writer.writerow(row)
CONNECTION_STRING = "mongodb://admin:12345@3.144.224.78:27017/?authSource=admin&readPreference=primary&directConnection=true&ssl=false"
client = MongoClient(CONNECTION_STRING)
dbname = client['admin']
collection_name = dbname["56"]

def fetch_data():
    item_details = json.loads(dumps(list(collection_name.find({},{'full_name':1,"phone_numbers":1,"mobile_phone":1,"emails":1,"industry":1,"job_company_name":1,"job_title":1,"work_email":1,"location_country":1,"full_address":1,"location_street_address":1,"location_locality":1,"location_region":1,"location_postal_code":1}))))
    for item in item_details:
        if item['location_country'] != None:
            if "united states" in item['location_country'].lower() or "usa" == item['location_country'].lower() or "us" == item['location_country'].lower():
                if item['job_title'] != None:
                    if "ceo" == item['job_title'].lower() or "Ceo" == item['job_title'].lower() or "CEO" == item['job_title'].lower() or "founder" in item['job_title'].lower() or "owner" in item['job_title'].lower() or "president" in item['job_title'].lower() or "director" in item['job_title'].lower() or "chairperson" in item['job_title'].lower() or "principal" in item['job_title'].lower() or "managing director" in item['job_title'].lower() or "managing-director" in item['job_title'].lower() or "administrator" in item['job_title'].lower() or "proprietor" in item['job_title'].lower():
                        if item['industry'] != None:
                            if "transportaion" in item['industry'].lower() or "professional-services" in item['industry'].lower() or "professional services" in item['industry'].lower() or "professional-service" in item['industry'].lower() or "professional service" in item['industry'].lower() or "professionalservices" in item['industry'].lower() or "professionalservice" in item['industry'].lower() or "construction" in item['industry'].lower() or "technology" in item['industry'].lower() or "retail" in item['industry'].lower():
                                location_street_address = ''
                                if item['location_street_address'] != None:
                                    location_street_address = str(item['location_street_address']).replace("None",'')
                                location_locality = ''
                                if item['location_locality']:
                                    if len(location_street_address) == 0:
                                        location_locality = str(item['location_locality']).replace("None",'')
                                    else:
                                        location_locality = ', '+ str(item['location_locality']).replace("None",'')
                                location_region = ''
                                if item['location_region']:
                                    if len(location_locality) == 0 and len(location_locality)==0:
                                        location_region = str(item['location_region']).replace("None",'')
                                    else:
                                        location_region = ", "+str(item['location_region']).replace("None",'')
                                location_postal_code = ''
                                if item['location_postal_code']:
                                    if str(len(location_street_address)) == 0 and len(location_locality) == 0 and len(location_locality)==0:
                                        location_postal_code =  str(item['location_postal_code']).replace("None",'')
                                    else:
                                        location_postal_code = ', '+ str(item['location_postal_code']).replace("None",'')
                                full_address =   location_street_address + location_locality +location_region + location_postal_code
                                full_name = str(item['full_name']).replace("None",'')
                                phone_numbers = str(item['phone_numbers']).replace("None",'')
                                mobile_phone = str(item['mobile_phone']).replace("None",'')
                                emails = str(item['emails']).replace("None",'')
                                industry = str(item['industry']).replace("None",'')
                                job_company_name = str(item['job_company_name']).replace("None",'')
                                job_title = str(item['job_title']).replace("None",'')
                                work_email = str(item['work_email']).replace("None",'')
                                location_country = str(item['location_country']).replace("None",'')
                                print(full_name)
                                store =[full_name,phone_numbers,mobile_phone,emails,industry,job_company_name,job_title,work_email,location_country,full_address.strip()]
                                yield store
def scrape():
    data = fetch_data()
    write_output(data)
scrape()