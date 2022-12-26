from googlesearch import search
query="shopify "
for j in search(query, tld="co.in", num=1, stop=1, pause=7): 
    print(j)
    if "shopify" in j:
        print("ye proceed")