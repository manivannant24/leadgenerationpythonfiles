#shopify tile extraction
import requests
from bs4 import BeautifulSoup
def getname(texts):
    number=str(texts)
    url="https://apps.shopify.com/tracktor-2/reviews?page="+number+"&rating=1&sort_by=recent"
    page=requests.get(url)
    soup=BeautifulSoup(page.content,'html.parser')
    title=soup.find_all("h3", class_="review-listing-header__text")
    for i in title:
        print(i.text.strip())
n=1
while n<5:
    getname(n)
    n=n+1