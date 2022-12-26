#check support desk
import requests
def find_desk(msg):
    domain=msg
    url="https://builtwith.com/"+domain
    r= requests.get(url)
    print(domain)
    if 'Zendesk' in r.text:
        print("ZENDESK")
    elif 'zendesk' in r.text:
        print("zendesk")
    elif 'ZENDESK' in r.text:
        print("zendesk")
    if 'GORGIAS' in r.text:
        print("GORGIAS")
    elif 'Gorgias'in r.text:
        print("GORGIAS")
    if 'FRESHDESK' in r.text:
        print("FRESHDESK")
    elif 'Freshdesk'in r.text:
        print('Freshdesk')
    if 'ZOHODESK' in r.text:
        print("ZOHODESK")
    elif 'Zoho Desk' in r.text:
        print("Zoho Desk")
    if 'UVDESK' in r.text:
        print("UVDESK")
    elif 'Uvdesk' in r.text:
        print('Uvdesk')
    elif 'UVdesk' in r.text:
        print("UVdesk")
    if 'SALESFORCE' in r.text:
        print("SALESFORCE")
    elif 'Salesforce' in r.text:
        print('Salesforce')
    elif 'Sales Force' in r.text:
        print('Sales Force')
    else:
        print("****")
find_desk(input('ent url: '))


