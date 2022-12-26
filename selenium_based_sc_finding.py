#selenium based sc finding
import time
import requests
def site(url):
    try:
        a=requests.get(url)
    except requests.exceptions.ConnectionError:
        #print(f"URL {url} not reachable")
        print("snr")
    else:
        ass=a.status_code
        if ass>200:
            print("error")
        if ass==200:
        #print("it is ok")
            if "Buy this domain" in a.text:
                print("buy this domain")
            elif "hugedomains.com" in a.text:
                print("not active")
            else:
                print("active")
                from selenium import webdriver
                from selenium.webdriver.common.keys import Keys
                from selenium.webdriver.common.by import By
                chrome_path = r'C:\Users\Maruti\Desktop\driver\chromedriver.exe'
                driver = webdriver.Chrome(chrome_path)
                driver.get(url)
                time.sleep(6)
                links=driver.find_elements_by_tag_name("a")
                for i in links:
                    print(i)
                #time.sleep(3)
site("https://int.hismileteeth.com/")


