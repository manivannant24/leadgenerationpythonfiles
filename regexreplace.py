a="https://www.linkedin.com/company/lounge-underwear/"
if '/about' in a:
    urlss=print(a)
elif '?originalSubdomain=in' in a:
    new=a.replace('?originalSubdomain=in', 'about')
    urlss=print(str(new))
else:
    print(a+'/about')
#urlss="https://www.linkedin.com/company/lounge-underwear/about"
#driver.get(urlss)