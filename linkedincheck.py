from selenium import webdriver 
 
# to open Firefox web browser and maximize the window 
browser = webdriver.Firefox(executable_path='<Path>/geckodriver.exe') 
browser.maximize_window() 
 
#connect to the specific URL 
browser.get("http://192.168.1.1:8090/httpclient.html") 
 
assert browser.page_source.find("Cyberoam Captive Portal") 