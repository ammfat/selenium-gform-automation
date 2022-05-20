#!/usr/bin/env python

import pandas as pd
from time import sleep
from random import randint
from selenium import webdriver

success, failed = 0, 0
data = pd.read_csv('form_dataset.csv', index_col=0).to_dict('records')

driver_path = "/home/ammfat/Playground/Selenium/automate-siklus-form/chromedriver"
gform_url = "https://docs.google.com/forms/d/e/1FAIpQLScEFqGFlfsOZkNuV_OZtKmY9YQ5EyLboAA8RQXTuVMP7Ac3bg/formResponse"

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_argument("--headless")

for item in data:
    try:
        print(item)
        
        browser = webdriver.Chrome(executable_path=driver_path, options=option)
        browser.get(gform_url)

        # Section 1
        txt_nama = browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        txt_email = browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        txt_nomor =browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        rad_kota = browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[14]/label")
        txt_kota = browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[14]/div/span/div/div/div[1]/input")
        btn_next = browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span")

        txt_nama.send_keys(item['name'])
        sleep(0.5)
        
        txt_email.send_keys(item['email'])
        sleep(0.5)
        
        txt_nomor.send_keys(str(item['phone_number']))
        sleep(0.5)
        
        rad_kota.click()
        sleep(0.5)
        
        txt_kota.send_keys(item['city'])
        sleep(0.5)
        
        btn_next.click()
        sleep(0.5)

        # Section 2
        btn_submit = browser.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span")
        
        btn_submit.click()
        # sleep(0.5)

        browser.close()
        
        success += 1
        sleep_time = randint(3, 5)
        
        print(f"SUCCESS")
        print(f"Going to sleep for {sleep_time} secs...")
        
        sleep(sleep_time)
    
    except Exception as e:
        failed += 1
        print(e)
        
        continue

print("-- STATS --")
print(f"Success\t: {success}")
print(f"Failed\t: {failed}")
