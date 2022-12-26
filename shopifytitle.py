from bs4 import BeautifulSoup
import requests
url = 'https://www.featuredcustomers.com/vendor/magento/case-studies/all'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#Title = soup.find_all('div',class_='featuredBox case-studies-premium') 
Title=img_src=soup.find("img")["src"]

for i in Title:
    print(i.text)

