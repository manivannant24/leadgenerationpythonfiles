from bs4 import BeautifulSoup
import requests
url="https://c-qp.com/shipping-info/"
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
#a=soup.find_all()
if ' UPS ' in page.text:
    print('a')
else:
    print("b")