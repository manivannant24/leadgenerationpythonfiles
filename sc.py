import time
import sys

def carrier_find(msg):

    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
    query=msg
    # to search 
    #query = "A computer science portal"
    
    for j in search(query, tld="co.in", num=1, stop=1, pause=5): 
        #print(j) 
        url=j
        import requests
        page=requests.get(url)
        if "UPS" in page.text:
            print("ups", j)
            sys.exit()
            if "DHL" in page.text:
                print("DHL")
            if "FedEx" in page.text:
                print("Fedex")
        elif "FedEx" in page.text:
            print("fedex",j)
            sys.exit()
            if "UPS" in page.text:
                print("ups")
            if "DHL" in page.text:
                print("dhl")
        elif "DHL" in page.text:
            print("dhl",j)
            sys.exit()
            if "UPS" in page.text:
                print("ups")
            if "FedEx" in page.text:
                print("Fedex")
        elif "DPD" in page.text:
            print("dpd", j)
            sys.exit()
        elif "TNT" in page.text:
            print("TNT", j)
            sys.exit()
        elif "Parcelforce" in page.text:
            print("parcelforce", j)
            sys.exit()
        elif "Royal Mail" in page.text:
            print("royal mail", j) 
        
'''a="giglio.com"
my_list = [(carrier_find(a+" faq"))]
time.sleep(10)'''

#a="aureliebidermann.com"
def mani(msgs):
    a=msgs
    my_list = [(carrier_find(a+" shipping page")),(carrier_find(a+" delivery")),(carrier_find(a+" faq")),(carrier_find(a+" customer service")),(carrier_find(a+" terms")),(carrier_find(a+" returns")),(carrier_find(a+" privacy policy"))  ]
#a="aureliebidermann.com"
mani("dtlr.com")
mani("dailysale.com")
time.sleep(5)
mani("smokecartel.com")
time.sleep(5)
mani("calpaktravel.com")
mani("novelkeys.xyz")
