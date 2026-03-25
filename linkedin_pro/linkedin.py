import json
import os
import warnings
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from random import randint
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.linkedin.com/login')
print ("Opened website")
warnings.simplefilter(action='ignore', category=FutureWarning)
currentDirectory = os.getcwd()  
sleep(2)

usr='poonamdhiyar@gmail.com'
pwd='8154942368'
sleep(5)
username_box = driver.find_element(By.XPATH,'//*[@id="username"]')
username_box.send_keys(usr)
print ("Email Id entered")
sleep(10)
  
password_box = driver.find_element(By.XPATH,'//*[@id="password"]')
password_box.send_keys(pwd)
print ("Password entered")
sleep(5) 
login_box = driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
login_box.click()
sleep(10)

def write_output(data):
    with open('linkedin_63k6.csv', mode='a',newline="",encoding='utf-8') as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        # Header
        writer.writerow(['Links','url','Company name','Number of employees','Address','Valid','Website','Category'])
        # Body
        for row in data:
            writer.writerow(row)

def fetch_data():
    data = ['https://www.linkedin.com/company/81607676/about/', 'https://www.linkedin.com/company/5354637/about/', 'https://www.linkedin.com/company/86327603/about/']

    for count,zipps in enumerate(data):
        url = zipps
        driver.get(url)
        sleep(randint(5,10))
        pageSource = driver.page_source
        fileToWrite = open(str(count)+"page_source.html", "w", encoding="utf-8")
        fileToWrite.write(pageSource)
        fileToWrite.close()
        file = open(str(count)+"page_source.html", "r",encoding= "utf-8")
        f = file.read()

        try:
            json_data = '{"data":{"viewerPermissions":'+f.split('{"data":{"viewerPermissions":')[1].split('</code>')[0]
            js_dt = json.loads(json_data)
        except:
            store =[url,driver.current_url,'','','','','','']
            yield store
            continue
        try:
            indu = js_dt['data']['industryUrns'][0]
            for i in js_dt['included']:
                if i['entityUrn'] == indu:
                    industry = i['name'].replace("amp;","").strip()
        except:
            industry = ''
        try:
            name = js_dt['data']['name']
        except:
            name = ''
        try:
            employe = js_dt['data']['employeeCount']
        except:
            employe = ''
        try:
            website = js_dt['data']['websiteUrl']
        except:
            website = ''
        try:
            line1 = js_dt['data']['headquarter']['address']['line1']
        except:
            line1 = ''
        try:
            line2 = js_dt['data']['headquarter']['address']['line2']
        except:
            line2 = ''
        try:
            line3 = js_dt['data']['headquarter']['address']['line3']
        except:
            line3 = ''
        try:
            city = js_dt['data']['headquarter']['address']['city']
        except:
            city = ''
        try:
            postalcode = js_dt['data']['headquarter']['address']['postalCode']
        except:
            postalcode = ''
        try:
            country = js_dt['data']['headquarter']['address']['country']
        except:
            country = ''
        address = line1 + ' ' + line2 + ' '+ line3 +' ' + city + ' ' +  postalcode + ' ' +  country
        store =[url,driver.current_url,name,employe,address,'',website,industry]
        yield store
        # count += 1
def scrape():
    data = fetch_data()
    write_output(data)
scrape()
    # fileToRead = open("page_source.html", "r")
    # print(fileToRead.read())
    # fileToRead.close()
# driver.quit()
# exit()
# def write_output(data):
#     with open('19.csv', mode='a',newline='') as output_file:
#         writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

#         # Header
#         writer.writerow(["profile_link","years_experience","founder_experience","tech_product_experience","senior_in_small_company","tech_experience","product_in_small_company","too_senior","perfect_profiles"])
#         # Body
#         for row in data:
#             writer.writerow(row)



# def fetch_data():
#     founder_titles = ["founder", "cofounder", "co-founder"]
#     product_titles = ["product manager", "senior product manager", "sr. product manager",
#     "principal product manager", "group product manager", "product lead"]
#     senior_titles = ["product director", "director of product", "vice president", "vp", "vp of product",
#     "head of product", "chief product officer", "cpo", "ceo","senior director of product"]
#     tech_companies = ["google", "facebook", "instagram", "whatsapp", "meta", "amazon",
#     "microsoft", "apple", "uber", "lyft", "stripe", "slack", "palantir", "spotify", "airbnb", "snapchat",
#     "square", "dropbox", "twitter", "intuit", "shopify", "instacart", "netflix", "youtube" ]

#     too_senior = False or True
#     senior_in_small_company = 0
#     founder_experience = 0
#     tech_product_experience = 0
#     tech_experience = 0
#     product_in_small_company = 0
#     perfect_profiles = 0
#     years_experience = 0
#     pos = ["Product Manager","Fellow - On Deck Angel (ODA5)","Cofounder & Angel Investor","Startup Advisor, Angel Investor, Weekend Hacker","Product Manager","Startup Mentor","Head of Product","Cofounder, CEO","AlumAlum","Employee","CofounderCofounder","President of Student Council","Legal Assistant","Assistant Project Manager"]
#     pos = ["Principal Product TPM","Staff / Director, Product TPM","Board Member","Founder","Developer Platform & Products","Director of Product & Ecosystem","Product Lead","Co-Founder and Board Member","Senior Manager, Mobile Products","Product TPM","Strategic Partner Programs Manager, Google Apps (now G Suite)","Business Instructor","Systems Engineer","Project Manager","Researcher in Space Sciences Lab"]
#     pos = ["Director of Product Management","Founder","Product Management","Product Management","Customer Engagement","Solution Architecture","Program Management"]
#     pos = ["Product Lead, Shopping","Sr. Director of Product","Director","Product Management","Senior Product Manager","Product Manager","Student","Sr. Product Manager Intern","Product Manager","Business Development, SMB Business","Co-Founder","Program Manager"]
#     pos = ["Product","Adjunct Lecturer","Product","Product","Self Employed","TED Resident, Speaker, TED/BMW 'Next Visionary' Program Mentor","Manager, Business Development","Graduate Student Research Assistant"]
#     pos = ["Founder","Product Manager","Product Manager","Product Lead","Product Manager","AssociateAssociate","Senior Associate Consultant","Founder, Director of Product","Analyst, Strategic Portfolio Solutions Group"]
#     pos = ["Sr. Director of Product, Creators & Reels","Director of Product, Creators & Reels","Director of Product, Creators","Chief Product Officer","Vice President Of Product","Director of Product","Senior Product Manager","Senior Product Manager"]
#     pos = ["Founder & CEO","Founder & CEO","Product Manager","Morgan Stanley Ambassador","Investment Banking Analyst"]
#     pos = ["Senior Product Manager","Music Producer","Senior Product Manager, Creator Experience","Product Manager, Dropbox Paper","Product Specialist, Dropbox Paper","Rotation Program","Product Engineer","User Operations Engineering Intern","Undergraduate Physics Mentor","Cofounder & Developer","Assistant Debate Coach","Software Development Intern","Research Fellow","Research Assistant","Graphic Design Intern"]
#     pos = ["Co-Founder","Product Manager","Senior Product Manager - Technical","Head of Product and Operations","Growth & Operations","Trader"]
#     pos = ["Product Manager, Shop Pay","Growth Strategist","Co-Founder","Digital Strategist","Digital Specialist","Technical Coordinator"]
#     pos = ["Director of Product, Shop","Board Member","CPO & Co-Founder (acquired by Shopify)","Digital Art Director & Partner","Co-Founder (acquired by Identity Works)"]
#     pos = ["Founder, Host","Senior Product Manager","Product Manager","Product Growth Manager","Board Member","President"]
#     pos = ["Product Manager","Venture Scout","Co-founder, Director","Co-founder, CEO","Venture Fellow","Summer Investment Analyst","Vice President","Software Engineer Intern","Software Engineer Intern","Software Engineer Intern","Shelter Summer Camp Counselor and Development Office Intern","Development Office Intern"]
#     pos = ["Product Manager","Product Manager","Product Manager","Product Manager","Associate Product Manager - Technology Rotational Program","Collegiate Leader in Environmental Health"]
#     pos = ["Co-founder & CEO","Head of Product, Next Billion Users","Group Product Manager, Next Billion Users","Career Coach","Head of Products - Messaging & Groups","VP of Product","Product Strategy/Development Consultant","Director of Product/Head of Social","Founder & CEO","Product, Marketing and Business Development (Internship)","Manager, Product & Design - Online Product Advertising","Manager, Search Experience Product Management","Technical Product/Program Manager","Program Manager"]
#     pos = ["Director, Facebook Growth","Co-Founder, Head of Product","Associate Principal","Founder/CEO"]
#     pos = ["Product Manager","Advisor","Lecturer","Designer in Residence","Founder","Entrepreneur in Residence","Designer Fund Guild","Mobile Product Lead","Co Founder","Co Founder","Product Manager","Business Factors","Design Researcher","Merchandise Planner","Merchandise Planner","Distribution Analyst","AnalystAnalyst","Intern"]
#     pos = ["CEO / Cofounder / Head of Product","Product Management","Head of Product, Machine Learning","Head of Product","CEO / Cofounder / Head of Product","Swaps Trader"]
#     comps = ["Google","On Deck","Backed By Blue (B3)","Lapin Ventures","Facebook","The Jewish Entrepreneur","VestaVesta","ParachuteParachute","AngelPadAngelPad","MakeSpace.com","Storage Bucket, LLC","Sy Syms School of Business","Cahill Gordon & Reindel","Compliance Inc."]
#     comps = ["Slack","Slack","Interserve","Karibu (www.gokaribu.com)","Airbnb","Planet","Planet","Global Cycle Solutions (GCS)","Twitter","Twitter","Google","meet - Middle East Entrepreneurs of Tomorrow","Raytheon Company","Development Alternatives","Cornell University"]
#     comps = ["LegalZoom","Beaze","Google","Amazon Web Services","Launch Consulting Group","Catalysis","Microsoft"]
#     comps = ["Instagram","1stdibs","1stdibs","1stdibs","1stdibs","Harvard Business School","Amazon","ZipDial","ZipDial","Lila Horn, LLC","Grameen Financial Services Pvt. Ltd."]
#     comps = ["Skillshare","Stanford University","LinkedIn","SpotifySpotify","Self Employed - Freelancer","TED Conferences","Sesame Workshop","MIT Media Lab · Part-time"]
#     comps = ["Bloom Community App","Instagram","MetaMeta","FaireFaire","Oculus VR","SignalFire · Full-time","Bain & Company","ThermeleonThermeleon","Goldman Sachs"]
#     comps = ["Instagram","Instagram","Instagram","TuneIn","TuneIn","TuneIn","BillShrink/TrueAxis (acquired by MasterCard)","imeem (acquired by myspace)"]
#     comps = ["MerryMint · Full-time","SnackWallaSnackWalla","Kiwi Crate","New York-Presbyterian Hospital","Morgan Stanley"]
#     comps = ["Instagram · Full-time","Independent · Self-employed","Patreon · Full-time","Dropbox","Dropbox","Dropbox","HubLogix","Dropbox","Emory University","cooperat.es","Alpharetta High School Raider Debate Team","Travelport","Department of Veterans Affairs","Emory University","Appen Newspapers"]
#     comps = ["Drunk Fruit","Instagram","TwitchTwitch","Payout.com","Ribbon","Consolidated Trading"]
#     comps = ["ShopifyShopify","Hootsuite","Civic Tech Vancouver","Vega","JIBE eCommerce","Vancouver Short Film Festival"]
#     comps = ["Shopify","Identity Works","Tictail","Identity Works","Super Strikers"]
#     comps = ["Hello Metaverse","Roblox · Full-time","Facebook","Shopify","Nspire Innovation Network","Nspire Innovation Network"]
#     comps = ["Meta · Full-time","Grishin Robotics","Envision Accelerator","Anchor","Rough Draft Ventures","Insight Partners","InnovationFWDInnovationFWD","Instagram","Facebook","OkCupid","Coalition for the Homeless, Inc.","Coalition for the Homeless, Inc."]
#     comps = ["Meta · Full-time","Instagram · Full-time","Dropbox","Optoro","Optoro","Centers for Disease Control and Prevention"]
#     comps = ["AllTakes · Full-time","YouTube · Full-time","Google · Full-time","Harvard Business School · Part-time","LinkedIn","Weddington Way","Independent Consultant","BloomReach","CleverBootzCleverBootz","threadsy","Amazon.com","Amazon.com","Amazon.com","Expedia, Inc."]
#     comps = ["Facebook","Blackwattle Co","Port Jackson Partners","Prosple"]
#     comps = ["Instagram · Full-time","FidoCure","Hasso Plattner Institute of Design at Stanford ( d.school )","Hasso Plattner Institute of Design at Stanford ( d.school )","BacktickBacktick","Foundation Capital","Designer Fund","TripAdvisor","Tiny Post","ListCharming","MUBI (The Auteurs)","IDEO","d.light","GUESS?, Inc.","Gap Inc.","Gap Inc.","Wells Fargo","World Bank Group"]
#     comps = ["Fidap","Google","Bloomberg LP","KGS-Alpha Capital Markets, L.P. (acquired)","Dentity","HSBC"]
#     start_year_first_job = 2007
#     profile_link = ''
#     for index, comp in enumerate(comps):
#         compapy = comp.lower()
#         # # print(compapy)
#         # .replace("sr. product manager","senior product manager").split(",")[0].split("&")[0].split("and")[0].replace("assistant",'').replace("Intern",'').replace("Staff / ",'').replace("TPM",'').replace("sr.",'').strip()
#         title = pos[index].lower().replace("sr.",'senior').replace(" intern",'')
#         # print(title)
#         if compapy in tech_companies:
#             # print(compapy)
#             if title in senior_titles:
#                 too_senior = True
#             elif title in product_titles:
#                 tech_product_experience += 1 
#             else:
#                 tech_experience += 1
#         else:
#             if title in founder_titles:
#                 founder_experience += 1
#             elif title in senior_titles:
#                 senior_in_small_company += 1 
#             elif title in product_titles:
#                 product_in_small_company += 1

#     years_experience = 2022 - start_year_first_job
#     dd = founder_experience + tech_product_experience
#     if  years_experience >5 and years_experience < 25 and  dd != 0:
        

#         if founder_experience != 0 and tech_product_experience != 0 and too_senior == False:
#             perfect_profiles += 1 
#         # yield [profile_link, years_experience,founder_experience,tech_product_experience,senior_in_small_company,tech_experience,product_in_small_company,too_senior,perfect_profiles]
#         # dd = f'too_senior : {too_senior}  senior_in_small_company : {senior_in_small_company} founder_experience : {founder_experience} tech_product_experience : {tech_product_experience} tech_experience : {tech_experience} product_in_small_company : {product_in_small_company}'
#         # print(dd)
    
# # fetch_data()
# def scrape():
#     data = fetch_data()
#     write_output(data)
# scrape()    



