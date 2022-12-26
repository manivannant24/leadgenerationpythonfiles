import requests
#url="http://ocado.com"
def site(url):
    try:
        a=requests.get(url)
    except requests.exceptions.ConnectionError:
        #print(f"URL {url} not reachable")
        print("snr")
    else:
        ass=a.status_code
        if ass>200:
            print("error")
        if ass==200:
        #print("it is ok")
            if "Buy this domain" in a.text:
                print("buy this domain")
            elif "hugedomains.com" in a.text:
                print("not active")
            else:
                print("active")
        

site("http://"+"heyhoney.com")
site("http://"+"chasingpaper.com")
'''site("http://"+"chillsacks.com")
site("http://"+"classicshaving.com")
site("http://"+"cloveandhallow.com")
site("http://"+"clubhub.com")
site("http://"+"cocoandbreezy.com")
site("http://"+"internetwines.com")
site("http://"+"concreteminerals.com")
site("http://"+"coogi.com")'''
