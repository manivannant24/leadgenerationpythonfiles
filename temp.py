'''list1=["test1","test2","test3","test4","ding"]
list2=["toto1","test1","test3","toto4"]

def functest(t):
    for l in list2:
        if t == l:
            return cond1
        else:
            return "rien"

for t in list1:
    titi=functest(t)
    print (titi)'''
import requests
r=requests.get("https://www.allamericanclothing.com/SARP.html")
#k=" UPS " 
#j="DHL"
if " UPS "== r.text:
    print("ups")
#elif j==r.text:
 #   print(j)
else:
    print("Cool bro")