import webbrowser
from selenium import webdriver
from bs4 import BeautifulSoup
import getpass
import requests,random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pprint
import time
userid="manivannan725@gmail.com"
password="kingbros6"
chrome_path = r'C:\Users\Maruti\Desktop\driver\chromedriver.exe'
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fsearch%2Fresults%2Fpeople%2F%3FcurrentCompany%3D%255B%25223506389%2522%255D%26origin%3DCOMPANY_PAGE_CANNED_SEARCH&fromSignIn=true&trk=cold_join_sign_in")
driver.implicitly_wait(3)
driver.find_element_by_id("username").send_keys(userid)
driver.find_element_by_id("password").send_keys(password)
time.sleep(5)
driver.find_element_by_xpath("//*[@id='organic-div']/form/div[3]/button").click()
time.sleep(20)
driver.get("https://www.linkedin.com/search/results/people/?currentCompany=%5B%2226708412%22%5D&origin=COMPANY_PAGE_CANNED_SEARCH")
src=driver.page_source
#print(src)
soup=BeautifulSoup(src,"lxml")
#print(soup)
#link=driver.find_element_by_class_name("app-aware-link")
link=soup.find('div', {'class': 'pv2 artdeco-card ph0 mb2'})#.get_text().strip()
#print(link)
for a in link.find_all('a', href=True):
    print (a['href'])
    urllist= a['href']
'''name_div=soup.find('h1', {'class': 'top-card-layout__title'}).get_text().strip()
print(name_div)
title_div=soup.find('h3', {'class': 'result-card__title'}).get_text().strip()
print(title_div)
location_div=soup.find('h3', {'class': 'top-card-layout__first-subline'}).get_text().strip()
print(location_div[:6])
print(driver.current_url)'''