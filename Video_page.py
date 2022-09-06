# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# import chromedriver_binary
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import random
import datetime
# import openpyxl
from csv import writer
# import itertools
# import pprint

from subprocess import CREATE_NO_WINDOW
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
from oauth2client.service_account import ServiceAccountCredentials 
import gspread
# import json
import requests
import csv
# import random

#########API#########################
# scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
 
# # 秘密鍵（JSONファイル）のファイル名を入力
# credentials = ServiceAccountCredentials.from_json_keyfile_name('intec-336107-22dc7ac3620e.json', scope)
# gc = gspread.authorize(credentials)
# workbook = gc.open_by_key('1oPxiU3MQieypLLTiOgiC4_btYGmRaTx6h8deoZW6vO')
# worksheet = workbook.worksheet('output')

# worksheet.update('A2:EL2',[basic_data])



##chormeのオプションを指定####################################################################
options = webdriver.ChromeOptions()
#options.add_argument("--headless")# ヘッドレスで起動するオプションを指定
options.page_load_strategy = 'normal'
# options.add_argument("--disable-gpu")

#options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--use-fake-ui-for-media-stream")
# options.add_argument('--hide-scrollbars')
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
#options.add_argument("--blink-settings=imagesEnabled=false")
options.add_argument("--start-maximized")
# options.add_experimental_option('excludeSwitches', ['enable-logging'])


# CHROMEDRIVER = 'C:\\Users\\user\\Desktop\\python\\ポートフォリオ\\chromedriver.exe'
chrome_service = fs.Service()
# chrome_service = fs.Service(executable_path=CHROMEDRIVER)
# driver = webdriver.Chrome(options=options,service=chrome_service)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)#CMP_URLにアクセスする。
##chormeのオプションを指定
options = webdriver.ChromeOptions()
#options.add_argument("--headless")# ヘッドレスで起動するオプションを指定
options.page_load_strategy = 'normal'
options.add_argument("--disable-gpu")

#options.add_argument("--disable-dev-shm-usage")
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument('--hide-scrollbars')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
#options.add_argument("--blink-settings=imagesEnabled=false")
options.add_argument("--start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])


# CHROMEDRIVER = 'C:\\Users\\user\\Desktop\\python\\ポートフォリオ\\chromedriver.exe'
chrome_service = fs.Service()
# chrome_service = fs.Service(executable_path=CHROMEDRIVER)
# driver = webdriver.Chrome(options=options,service=chrome_service)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(2)

#keyword.csvからvideoidを取得する
Video_ID = ''
Video_IDs = []

with open('keyword.csv') as f:
    reader = csv.reader(f)
    
    for row in reader:
        Video_IDs.append(row[2])