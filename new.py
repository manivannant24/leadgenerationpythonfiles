# top shop agencies imarketing agencies
import webbrowser
from selenium import webdriver
from bs4 import BeautifulSoup
import getpass
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pprint
import time
import pandas as pd
chrome_path = r'C:\Users\Maruti\Desktop\driver\chromedriver.exe'
driver = webdriver.Chrome(chrome_path)
def countinc(inputs):
    number=str(inputs)
    driver.get("https://clutch.co/agencies/digital?industries=field_pp_if_ecommerce&page="+number)
    src=driver.page_source
    #print(src)
    soup=BeautifulSoup(src,"lxml")
    '''for a in soup.find_all('div', 'company col-md-12 col-xs-12'):
        s=a.find('h3')
        result=s.get_text().strip()
        print(result)  '''
    for g in soup.find_all('div','provider-detail col-md-2 col-xs-12'):
        h=g.find('li')
        #print(h)
        for m in h.find_all('a', href=True):
            print(m['href'])
n=19
while n<31:
    countinc(n)
    n=n+1
