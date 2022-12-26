#import regex
tem="https://www.imsolutions.co.za/"
if "https://www." in tem:
    a=tem.replace("https://www.","")
    print(a)
elif "http://www." in tem:
    a=tem.replace("http://www.","")
    print(a)
elif "http://" in tem:
    a=tem.replace("http://","")
    print(a)
elif "https://" in tem:
    a=tem.replace("https://","")
    print(a)