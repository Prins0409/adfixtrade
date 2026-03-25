import time, csv
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import undetected_chromedriver.v2 as uc
from selenium import webdriver


# import undetected_chromedriver as uc
# driver = uc.Chrome()
# driver.get('https://www.verifyemailaddress.org/email-validation')
# exit().

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

# driver = uc.Chrome(use_subprocess=True)
# driver.maximize_window()
driver.get("https://www.verifyemailaddress.org/email-validation")
time.sleep(15)

with open("job_retail_and_CEO.csv",'r',encoding='utf-8') as f:
    read = csv.reader(f)
    for row in read:
        data = row[4]
        if data == '':
            continue
        if data == 'professional_email':
            continue
        valid_invalid = []
        all_mail = []
        if ',' in data:            
            abc = data.split(",")
            for new_data in abc:
                mail = new_data
                print("@@@@@@@@@@@",mail)
                first_name = driver.find_element(By.ID, "email")
                first_name.send_keys(mail)
                print(first_name)

        else:
            all_mail.append(data)
        for new_data in all_mail:
            mail = new_data
            print("@@@@@@@@@@@",mail)
            first_name = driver.find_element(By.ID, "email")
            first_name.send_keys(mail)
            print(first_name)