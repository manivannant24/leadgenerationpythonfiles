def carrier_find(msg):
    
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module named 'google' found") 
    query=msg
    # to search 
    #query = "A computer science portal"
    
    for j in search(query, tld="co.in", num=1, stop=1, pause=25): 
        #print(j) 
        url=j
        import requests
        page=requests.get(url)
        if "UPS" in page.text:
            print(j)
            print("ups")
            if "DHL" in page.text:
                print("DHL")
            if "FedEx" in page.text:
                print("Fedex")
        elif "FedEx" in page.text:
            print(j)
            print("fedex")
            if "UPS" in page.text:
                print("ups")
            if "DHL" in page.text:
                print("dhl")
        elif "DHL" in page.text:
            print(j)
            print("dhl")
            if "UPS" in page.text:
                print("ups")
            if "FedEx" in page.text:
                print("Fedex")
        elif "DPD" in page.text:
            print(j)
            print("dpd")
        elif "TNT" in page.text:
            print(j)
            print("TNT")
        elif "Parcelforce" in page.text:
            print(j)
            print("parcelforce")
        elif "Royal Mail" in page.text:
            print(j)
            print("royal mail")  
        

for i in carrier_find:
    if i ==ups:
        continue
    print("ups")
carrier_find("theattico.com shipping","theattico.com terms")


