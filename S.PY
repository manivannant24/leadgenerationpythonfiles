#from bs4 import BeautifulSoup
try: 
    from googlesearch import search 
except ImportError:
    print("No module named 'google' found") 
    
def method(dummyquery):
    query = str(dummyquery)
    
    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
       #print(j)
        maxx = j
        #print(maxx)
        import requests
        r = requests.get(''+maxx)
    if 'USPS' in r.text:
        #print(maxx)
        print ('USPS')
            #if 'DHL' in r.text:
             #   print(maxx)
              #  print('FedEx ')
method("https://us.boohoo.com/customer-service#folder-cs-folder-orders")





