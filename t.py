from bs4 import BeautifulSoup
import requests
def title_find(mes):
    numbers = mes
    url = 'https://apps.shopify.com/klaviyo-email-marketing/reviews?page='+numbers+'&rating=5'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    Title = soup.find_all('h3',class_='review-listing-header__text') 
    for i in Title:
        print(i.text)
    #print(page.prettify)
number=1
while number <2:
    title_find(number)
    number=number+1