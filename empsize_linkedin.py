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
def empsizefinder(mesg):
    given=str(mesg)
    '''driver.get("http://www.google.com")
    element = driver.find_element_by_name("q")
    element.send_keys(search+" linkedin")
    element.submit()
    driver.find_element_by_partial_link_text("| LinkedIn").click()
    turl=driver.current_url
    print(turl)'''
    from googlesearch import search 
    query = str(given+' linkedin')
    for j in search(query, tld="co.in", num=1, stop=1, pause=7): 
        print(j)
    a=j
    if '/about' in a:
        urlss=print(str(a))
        print("ok")
    elif '?originalSubdomain=in' in a:
        new=a.replace('?originalSubdomain=in', 'about')
        urlss=print(str(new))
        print("remove uw")
    else:
        urlss=print(str(a+'/about'))
        print("add")
        print(type(urlss))
    #urlss="https://www.linkedin.com/company/lounge-underwear/about"
    print(urlss)
    url=(urlss)
    driver.get(url)
    src=driver.page_source
    soup=BeautifulSoup(src,"lxml")
    empsize=soup.find('dl', {'class': 'overflow-hidden'})
    #empsizetext=empsize.text()
    empvar=empsize.get_text()
    #print(emptextvalue.strip())
    #print(driver.current_url)
    #empvar=empsize
    if '2-10 employees' in empvar:
        print("2-10 employees")
    elif'11-50 employees' in empvar:
        print("11-50 employees")
    elif'51-200 employees' in empvar:
        print("51-200 employees")
    elif'201-500 employees' in empvar:
        print("201-500 employees")
    elif'501-1000 employees' in empvar:
        print("501-1000 employees")
    elif'1001-5000 employees' in empvar:
        print("1001-5000 employees")
    elif'5001-10,000 employees' in empvar:
        print("5001-10,000 employees")
    elif'10,001+ employees' in empvar:
        print("10,001+ employees")
    else:
        print("no")
#empsizefinder("pipecandy.com")
empsizefinder("loungeunderwear.com")