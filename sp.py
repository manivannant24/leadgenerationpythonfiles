try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
    
def method(dummyquery):
    query = str(dummyquery)
    for j in search(query, tld="co.in", num=2, stop=1, pause=2): 
        print(j) 

method(input("Arbor Collective"))