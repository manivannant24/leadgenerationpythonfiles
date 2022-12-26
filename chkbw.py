#open link using firefox browser
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
#username="mani@auditshipment.com"
#password="mani@123"
#username2="ann@auditshipment.com"
#password=""
#url="https://liforme.com/"
#driver=webdriver.Firefox(executable_path=r"C:\Users\swift\Downloads\driver\geckodriver")
#driver.get(url)
#dom="liforme.com"
url="https://www.google.com/search?client=firefox-b-d&ei=AU8FYKr9GLmC4t4P5aq-SA&q=kings&oq=kings&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR1CjEFijEGC3E2gAcAJ4AIABAIgBAJIBAJgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab&ved=0ahUKEwjqgZ2GkKXuAhU5gdgFHWWVDwkQ4dUDCAw&uact=5"
browser=webdriver.Firefox(executable_path=r"C:\Users\swift\Downloads\driver\geckodriver")
#driver.get(url)
#driver.find_element_by_id('q').send_keys(dom)
#driver.find_element_by_id('password').send_keys(password)
#time.sleep(10)
#driver.find_elements_by_class_name("LC20lb DKV0Md").click()
#driver.find_element_by_id('email').send_keys(username2)
#driver.find_element_by_id('verify').click()
#driver.find_element_by_id('basketToggle').click()
browser.get('http://www.google.com')
search = browser.find_element_by_name('q')
search.send_keys("how to search the internet")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results
browser.execute_script("window.scrollTo(0, 873)") 
time.sleep(2)
browser.find_element(By.CLASS_NAME, 'LC20lb DKV0Md').click()
time.sleep(3)
driver.close()