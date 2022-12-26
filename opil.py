#job title page  from linkedin
import webbrowser
from selenium import webdriver
from bs4 import BeautifulSoup
import getpass
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pprint
import time
userid="manivannan725@gmail.com"
password="kingbros6"
chrome_path = r'C:\Users\Maruti\Desktop\driver\chromedriver.exe'
driver = webdriver.Chrome(chrome_path)
driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
driver.implicitly_wait(3)
driver.find_element_by_id("username").send_keys(userid)
driver.find_element_by_id("password").send_keys(password)
time.sleep(5)
driver.find_element_by_xpath("//*[@id='app__container']/main/div[2]/form/div[3]/button").click()
#time.sleep(10)
def mul_dom_prof_check(mesg):
    search=mesg
    driver.get("http://www.google.com")
    element = driver.find_element_by_name("q")
    element.send_keys(search+" linkedin")
    element.submit()
    driver.find_element_by_partial_link_text("| LinkedIn").click()
    time.sleep(3)
    #driver.find_element(By.XPATH, '(//h3)[1]/../../a').click()
    #driver.get("https://www.linkedin.com/company/hunterio")
    #driver.find_element_by_partial_link_text("employees on LinkedIn").click()
    driver.find_element_by_partial_link_text(" employees on LinkedIn").click()
    time.sleep(3)
    #driver.find_element_by_xpath("//*[@id='ember452']").click()
    #driver.find_element_by_xpath("//*[@id='ember670']/ul/li[11]/ul/li[3]").send_keys("CEO")
    #content_ofempsize=driver.find_elements_by_xpath("//*[@id='ember396']")
    #for i in content_ofempsize:
    #    print(i.text)
    current_url=str(driver.current_url)
    new_url=current_url.replace("COMPANY_PAGE_CANNED_SEARCH", "FACETED_SEARCH&title=FOUNDER OR CEO OR PRESIDENT")
    driver.get(""+new_url)
    driver.execute_script("window.open('');")
    #time.sleep(3)
    # Switch to the new window
    driver.switch_to.window(driver.window_handles[1])
    #driver.get("http://stackoverflow.com")
    new_url=current_url.replace("COMPANY_PAGE_CANNED_SEARCH", "FACETED_SEARCH&title=OPERATIONS OR OPERATING OR OPERATION")
    driver.get(""+new_url)
    time.sleep(3)
    driver.execute_script("window.open('');")
    #time.sleep(3)
    # Switch to the new window
    driver.switch_to.window(driver.window_handles[2])
    ECOM_URL=current_url.replace("COMPANY_PAGE_CANNED_SEARCH", "FACETED_SEARCH&title=ECOMMERCE OR E-COMMERCE OR COMMERCE")
    driver.get(""+ECOM_URL)
    time.sleep(3)
    driver.execute_script("window.open('');")
n=1   
while n<3:
    mul_dom_prof_check(input("enter dom "))
    time.sleep(25)
    n=n+1


