#getting comp name from image - featuredcustomers
from selenium import webdriver
import time


driver = webdriver.Firefox(executable_path=r"C:\Users\swift\Downloads\driver\geckodriver")
#driver.get("https://www.featuredcustomers.com/vendor/magento/testimonials/all")
driver.get("https://www.shopify.com/plus/customers")
#continue_link = driver.find_element_by_tag_name('a')
elems = driver.find_elements_by_xpath("//*[@alt]")
for elem in elems:
    print(elem.get_attribute("title"))
time.sleep(4)
driver.close()  

