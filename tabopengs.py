import webbrowser
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
#webbrowser.get(chrome_path).open('http://docs.python.org/')
def tabopen(urls):
    '''tem=urls
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
    print(a)'''
    term= "https://www.google.com/search?q="
    taburl  = urls
    #webbrowser.open(term)
    #webbrowser.get(chrome_path).open(taburl)
    email=" email"
    webbrowser.get(chrome_path).open(term+taburl+email)
    linkedin = " linkedin   "
    webbrowser.get(chrome_path).open(term+taburl+linkedin)
while 1<200:
    tabopen(input("enter dom for tab open: "))

    
    

