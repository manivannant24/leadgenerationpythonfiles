#open link using firefox browser
#from selenium import webdriver
#username=input("lms search: ")
#url="http://partners.auditshipment.com/AuditLeadmanagement/admin/search"
#driver=webdriver.Firefox(executable_path=r"C:\Users\swift\Downloads\driver\geckodriver")
#driver=webdriver.Chrome(executable_path=r"C:\\Users\swift\Desktop\kings\chromedriver")
#driver.get(url)
#driver.find_element_by_id('domainsearchval').send_keys(username)
#driver.find_element_by_id('password').send_keys(password)
#driver.find_element_by_id('searchdomain').click()
#driver.find_element_by_id('email').send_keys(username2)
#driver.find_element_by_id('verify').click()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_setup_selenium(driver_name):
    options = Options()
    options.headless = True
    return {
        'executable_path': '/usr/bin/chromedriver',
        'chrome_options': options,
    }
#username=input("lms search: ")
url="http://partners.auditshipment.com/AuditLeadmanagement/admin/search"
#driver=webdriver.Firefox(executable_path=r"C:\Users\swift\Downloads\driver\geckodriver")
driver=webdriver.Chrome(executable_path=r"C:\\Users\swift\Desktop\kings\chromedriver")
driver.get(url)
pytest_setup_selenium("mani")

