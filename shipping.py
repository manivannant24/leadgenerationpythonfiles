import time
try: 
    from googlesearch import search 
except ImportError:
    print("No module named 'google' found") 
    
def method(dummyquery):
  
    n=1
    while n<8:
        searching='s'+str(n)
        s1=' delivery'                
        s2=' faq'                             
        s3=' terms'                                                    
        s4=' returns'
        s5=' customer service'                                                                        
        s6=' privacy policy'
        s7=' shipping page'
        
        query = str(dummyquery+searching)   
        
    
    for j in search(query, tld="co.in", num=1, stop=1, pause=5): 
        maxx = j
        print(maxx)

        import requests
        r = requests.get(''+maxx)
        if 'USPS' in r.text:
            print(maxx)
            print ('USPS')
        if "UPS" in r.text:
            print(maxx)
            print("UPS")
        if"DHL" in r.text:
            print(maxx)
            print("dhl")
        elif 'FedEx' in r.text:
            print(maxx)
            print('FedEx ')
        n=n+1
    
method("neweracap.co.uk")











