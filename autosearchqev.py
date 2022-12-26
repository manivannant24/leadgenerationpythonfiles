import time
try: 
    from googlesearch import search 
except ImportError:
    print("No module named 'google' found") 

dummyquery="king.com "
n=0
while n<7:
    cars = ["delivery", "faq", "terms","returns","customer service","privacy policy","shipping page"]
    query = str(dummyquery+cars[n])  
    print(query) 
    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
        maxx = j
        print(maxx)
        import requests
        r = requests.get(''+maxx)
        if 'USPS' in r.text:
            print(maxx)
            print ('USPS')
            if 'UPS' in r.text:
                print('ups')
                break
        elif 'FedEx' in r.text:
            print(maxx)
            print('FedEx')
            if 'UPS' in r.text:
                print("UPS")
                break
        elif 'UPS' in r.text:
            print(maxx)
            print('UPS')
            if 'DHL' in r.text:
                print('DHL')
                break
        elif 'DHL' in r.text:
            print(maxx)
            print('DHL')
            if 'UPS' in r.text:
                print("ups")
                break
        elif 'DPD' in r.text:
            print(maxx)
            print('DPD')
            break
        elif 'TNT' in r.text:
            print(maxx)
            print('TNT')
            break
        elif 'Parcelforce' in r.text:
            print(maxx)
            print('Parcelforce')
            break
        elif 'Royal Mail' in r.text:
            print(maxx)
            print('Royal Mail')  
            break
        n=n+1
    
#method("neweracap.co.uk")