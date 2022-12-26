#getting comp name from image - featuredcustomers
from selenium import webdriver
import time


driver = webdriver.Firefox(executable_path=r"C:\Users\swift\Downloads\driver\geckodriver")
driver.get("https://www.shopify.com/plus")

#continue_link = driver.find_element_by_tag_name('a')
i=driver.find_elements_by_tag_name("p").getText()
print(i)
driver.close()  

