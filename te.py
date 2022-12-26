import requests
r = requests.get('https://liforme.com/pages/shipping-and-returns')

if 'UPS' in r.text:
    print ('UPS')
elif 'FedEx' or 'FEDEX' or 'fedex' in r.text:
    print ('FedEx')
elif 'DPD' or 'dpd' or 'Dpd' in r.text:
    print ('DPD')
elif 'TNT' in r.text:
    print ('TNT')
elif 'DHL' or 'dhl' or 'Dhl' in r.text:
    print ('DHL')
elif 'usps' or 'USPS' in r.text:
    print ('usps')
elif 'Parcelforce ' or 'Royal Mail' in r.text:
    print ('Parcelforce OR Royal Mail ')
else:
    print('No shipping Carriers found   ')