import webbrowser
from selenium import webdriver
from bs4 import BeautifulSoup
import getpass
import requests,random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pprint
import time
#userid="manivannan725@gmail.com"
#password="kingbros6"
chrome_path = r'C:\Users\Maruti\Desktop\driver\chromedriver.exe'
driver = webdriver.Chrome(chrome_path)
'''driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
driver.implicitly_wait(3)
driver.find_element_by_id("username").send_keys(userid)
driver.find_element_by_id("password").send_keys(password)
time.sleep(5)
driver.find_element_by_xpath("//*[@id='app__container']/main/div[2]/form/div[3]/button").click()'''
#time.sleep(10)
driver.get("https://clutch.co/agencies/digital?industries=field_pp_if_ecommerce&page=8")
src=driver.page_source
soup=BeautifulSoup(src,"lxml")
#print(soup)
name_div=soup.find('div', {'class': 'company col-md-12 col-xs-12'}).get_text().strip()
for i in soup.find_all(name_div):
    print(name_div)
'''title_div=soup.find('h3', {'class': 'result-card__title'}).get_text().strip()
print(title_div)
location_div=soup.find('h3', {'class': 'top-card-layout__first-subline'}).get_text().strip()
print(location_div[:6])
print(driver.current_url)'''