from bs4 import BeautifulSoup
import time
import pandas as pd
try: 
    from googlesearch import search 
except ImportError:
    print("No module named 'google' found") 
    
def method(dummyquery):
    query = str(dummyquery+'shipping page')
    for j in search(query, tld="co.in", num=1, stop=1, pause=3): 
        maxx = j
        import requests
        r = requests.get(''+maxx)
        if 'USPS' in r.text:
            print(maxx)
            print ('USPS')
            if 'UPS' in r.text:
                print('ups')
        elif 'FedEx' in r.text:
            print(maxx)
            print('FedEx')
            if 'UPS' in r.text:
                print("UPS")
        elif 'UPS' in r.text:
            print(maxx)
            print('UPS')
            if 'DHL' in r.text:
                print('DHL')
        elif 'DHL' in r.text:
            print(maxx)
            print('DHL')
            if 'UPS' in r.text:
                print("ups")
        elif 'DPD' in r.text:
            print(maxx)
            print('DPD')
        elif 'TNT' in r.text:
            print(maxx)
            print('TNT')
        elif 'Parcelforce' in r.text:
            print(maxx)
            print('Parcelforce')
        elif 'Royal Mail' in r.text:
            print(maxx)
            print('Royal Mail')  
        else:
            query = str(dummyquery+' delivery')
            for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
                maxx = j
                import requests
                r = requests.get(''+maxx)
                if 'USPS' in r.text:
                    print(maxx)
                    print ('USPS')
                    if 'UPS' in r.text:
                        print(maxx)
                        print("ups")
                        if 'FedEx' in r.text:
                            print(maxx)
                            print("fedex")
                elif 'FedEx' in r.text:
                    print(maxx)
                    print('FedEx')
                    if 'UPS' in r.text:
                        print(maxx)
                        print("ups")
                elif 'UPS' in r.text:
                    print(maxx)
                    print('UPS')
                    if 'FedEx' in r.text:
                        print(maxx)
                        print("fedex")
                elif 'DHL' in r.text:
                    print(maxx)
                    print('DHL')
                    if 'UPS' in r.text:
                        print(maxx)
                        print("ups")
                elif 'DPD' in r.text:
                    print(maxx)
                    print('DPD')
                elif 'TNT' in r.text:
                    print(maxx)
                    print('TNT')
                elif 'Parcelforce' in r.text:
                    print(maxx)
                    print('Parcelforce')
                elif 'Royal Mail' in r.text:
                    print(maxx)
                    print('Royal Mail')  
                else:
                    query = str(dummyquery+' faq')
                    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
                        maxx = j
                        import requests
                        r = requests.get(''+maxx)
                        if 'USPS' in r.text:
                            print(maxx)
                            print ('USPS')
                            if 'UPS' in r.text:
                                print(maxx)
                                print("ups")
                        elif 'FedEx' in r.text:
                            print('FedEx ')
                            print(maxx)
                            if 'UPS' in r.text:
                                print(maxx)
                                print("ups")
                        elif 'UPS' in r.text:
                            print(maxx)
                            print('UPS')
                            if 'DHL' in r.text:
                                print(maxx)
                                print("DHL")
                        elif 'DHL' in r.text:
                            print(maxx)
                            print('DHL')
                            if 'UPS' in r.text:
                                print(maxx)
                                print("ups")
                        elif 'DPD' in r.text:
                            print(maxx)
                            print('DPD')
                        elif 'TNT' in r.text:
                            print(maxx)
                            print('TNT')
                        elif 'Parcelforce' in r.text:
                            print(maxx)
                            print('Parcelforce')
                        elif 'Royal Mail' in r.text:
                            print(maxx)
                            print('Royal Mail')        
                        else:
                            query = str(dummyquery+' terms')
                            for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
                                maxx = j
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
                                    if "UPS" in r.text:
                                        print(maxx)
                                        print("ups")
                                        if "DHL" in r.text:
                                            print(maxx)
                                            print("dhl")
                                elif 'UPS' in r.text:
                                    print(maxx)
                                    print('UPS')       
                                    if "USPS" in r.text:
                                        print(maxx)
                                        print("USPS")        
                                elif 'DHL' in r.text:
                                    print(maxx)
                                    print('DHL')
                                elif 'DPD' in r.text:
                                    print(maxx)
                                    print('DPD')
                                elif 'TNT' in r.text:
                                    print(maxx)
                                    print('TNT')
                                elif 'Parcelforce' in r.text:
                                    print(maxx)
                                    print('Parcelforce')
                                elif 'Royal Mail' in r.text:
                                    print(maxx)
                                    print('Royal Mail')        
                                else:
                                    query = str(dummyquery+' returns')
                                    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
                                        maxx = j
                                        import requests
                                        r = requests.get(''+maxx)
                                        if 'USPS' in r.text:
                                            print(maxx)
                                            print ('USPS')
                                            if "UPS" in r.text:
                                                print(maxx)
                                                print("ups")
                                                if "DHL" in r.text:
                                                    print(maxx)
                                                    print("dhl")
                                        elif 'FedEx' in r.text:
                                            print(maxx)
                                            print('FedEx ')
                                            if "ups" in r.text:
                                                print(maxx)
                                                print("ups")
                                        elif 'UPS' in r.text:
                                            print(maxx)
                                            print('UPS')
                                            if "USPS" in r.text:
                                                print(maxx)
                                                print("usps")
                                        elif 'DHL' in r.text:
                                            print(maxx)
                                            print('DHL')
                                            if "UPS" in r.text:
                                                print(maxx)
                                                print("ups")
                                        elif 'DPD' in r.text:
                                            print(maxx)
                                            print('DPD')
                                        elif 'TNT' in r.text:
                                            print(maxx)
                                            print('TNT')
                                        elif 'Parcelforce' in r.text:
                                            print(maxx)
                                            print('Parcelforce')
                                        elif 'Royal Mail' in r.text:
                                            print(maxx)
                                            print('Royal Mail') 
                                        else:
                                            query = str(dummyquery+' customer service')
                                            for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
                                                maxx = j
                                                import requests
                                                r = requests.get(''+maxx)
                                                if 'USPS' in r.text:
                                                    print(maxx)
                                                    print ('USPS')
                                                    if 'UPS' in r.text:
                                                        print(maxx)
                                                        print("ups")
                                                        if 'FedEx' in r.text:
                                                            print(maxx)
                                                            print("fedex")
                                                elif 'FedEx' in r.text:
                                                    print(maxx)
                                                    print('FedEx ')
                                                    if "UPS" in r.text:
                                                        print(maxx)
                                                        print("ups")
                                                elif 'UPS' in r.text:
                                                    print(maxx)
                                                    print('UPS')
                                                    if "usps" in r.text:
                                                        print(maxx)
                                                        print("usps")
                                                elif 'DHL' in r.text:
                                                    print(maxx)
                                                    print('DHL')
                                                    if "UPS" in r.text:
                                                        print(maxx)
                                                        print("ups")
                                                elif 'DPD' in r.text:
                                                    print(maxx)
                                                    print('DPD')
                                                elif 'TNT' in r.text:
                                                    print(maxx)
                                                    print('TNT')
                                                elif 'Parcelforce' in r.text:
                                                    print(maxx)
                                                    print('Parcelforce')
                                                elif 'Royal Mail' in r.text:
                                                    print(maxx)
                                                    print('Royal Mail') 
                                                else:
                                                    query = str(dummyquery+' privacy policy')
                                                    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
                                                        maxx = j
                                                        import requests
                                                        r = requests.get(''+maxx)
                                                        if 'USPS' in r.text:
                                                            print(maxx)
                                                            print ('USPS')
                                                            if 'UPS' in r.text:
                                                                print(maxx)
                                                                print("ups")
                                                                if 'FedEx' in r.text:
                                                                    print(maxx)
                                                                    print("fedex")
                                                        elif 'FedEx' in r.text:
                                                            print(maxx)
                                                            print('FedEx ')
                                                            if "UPS" in r.text:
                                                                print(maxx)
                                                                print("ups")
                                                        elif 'UPS' in r.text:
                                                            print(maxx)
                                                            print('UPS')
                                                            if "usps" in r.text:
                                                                print(maxx)
                                                                print("usps")
                                                        elif 'DHL' in r.text:
                                                            print(maxx)
                                                            print('DHL')
                                                            if "UPS" in r.text:
                                                                print(maxx)
                                                                print("ups")
                                                        elif 'DPD' in r.text:
                                                            print(maxx)
                                                            print('DPD')
                                                        elif 'TNT' in r.text:
                                                            print(maxx)
                                                            print('TNT')
                                                        elif 'Parcelforce' in r.text:
                                                            print(maxx)
                                                            print('Parcelforce')
                                                        elif 'Royal Mail' in r.text:
                                                            print(maxx)
                                                            print('Royal Mail') 
                                                        else:
                                                            print(maxx)
                                                            print('i cant find, you may do')
            
method("queeneandbelle.com")
method("quoddy.com")
method("rmwilliams.com")
method("r13denim.com")
method("rachelboston.co.uk")
method("shoprachelzoe.com")
method("rag-bone.com")
method("rastaclat.com")
method("reasonclothing.com")
method("reese-cooper.com")
method("repossi.com")
method("rh-ude.com")
method("richard-james.com")
method("ripndipclothing.com")
method("roberiandfraud.com")
method("rodebjer.com")
method("r-o-k-h.com")
method("roksandailincic.com")
method("rosamosario.com")
method("roughandtumbledesign.com")
method("royaums.com")
method("rxmance.com")
method("salsajeans.com")
method("samanthapleet.com")
method("samsoe.com")
method("sandcopenhagen.com")
method("sarahpacini.com")