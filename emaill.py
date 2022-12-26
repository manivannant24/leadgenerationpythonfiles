import requests
def metod(msg):
    mani=msg
    r = requests.get(mani)
    if 'USPS' in r.text:
        #print(maxx)
        print ('USPS')
metod(input("enter domain: "))
