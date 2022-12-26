#check website have cart or not
try: 
    from googlesearch import search 
except ImportError:
    print("No module named 'google' found") 
def cartchck_domain(enter):
    url=enter
    import requests
    s=requests.get("http://"+url+"/shop")
    st=requests.get("http://"+url+"/store")
    c=requests.get("http://"+url+"/cart/")
    b=requests.get("http://"+url+"/basket")
    r=requests.get("http://"+url)
    query = str(url+' cart')
    for j in search(query, tld="co.in", num=1, stop=1, pause=3):
        maxx = j
        gsl=requests.get(maxx)
        #print(maxx)
    if "Cart"or" cart " in r.text:
        print(url)
        print("YES home")
    if "cart" in c.text:
        print(url)
        print("YES cart")            
    if "cart" in s.text:
        print(url)
        print("YES shop")   
    if "cart" in st.text:
        print(url)
        print("YES store")         
    if "basket" in b.text:
        print(url)
        print("YES basket")            
    if "cart" in gsl.text:
        print(url)
        print("YES-Chk")                       
    else:
        print(url)
        print("NO")

cartchck_domain("balancedwineselections.com/")




