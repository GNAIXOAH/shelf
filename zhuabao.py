import os
import time
import json
import random
import requests

IBAN = '9781533948861'
VitalSourceAPIKey = 'faab4ead691e451eb230afc98a28e0f2-4089b390-5e4a-4a54-ac5c-6be4f2ea9321-7247'
VitalSourceAccessToken = 't=GwAmAbuEBAAUKFVEGReoCdHdlh1TorgVuqX+P2gOZgAAEC6MmdfHC1Liv4bqrv83MBjwANiI7ml785roDLCQ6ont/jTYsCc99MmlYSzulnms08R0ZMNeMGg6ehtIJgjsIQ4YLUexywKRdouXPeSYvnq0nqozNdgF71diU2pRazBbIOw0Y1yShqeiHy30Y4Wv4KT77WEemlMuJy4PmIgZOX+O3RMe9nnii5Gzn6JKs1VnnqygnHbAk+8fJKArg5F5lE5pSUWcDaejzu7nGI/6vA0hziLnOKBnjkYrX4Gm5apAIj8wR2u0CycH9JMk/nH/qQcxbKTLwVFjY3YlU3iRYRa26EfXAwOUzfn4H/jtVD/Vw3Kh9hZg2bYMEjDMIj6u2ylixx4B&p='
DownloadFolder = os.path.expanduser('/Users/GN0H/Downloads/'+IBAN+'/')

if os.path.exists(DownloadFolder):
    pass
else:
    # try:
        os.mkdir(DownloadFolder)
    # except:
    #     print('Creation of the directory failed')
    #     exit()

while(True):
    try:
        FirstPage = int(input('First page: '))
        LastPage = int(input('Last page: '))
        if (type(FirstPage) != int) or (type(LastPage) != int):
            print('Please enter valid page numbers.\n')
            continue
        elif (FirstPage > LastPage):
            print('First page must be less than last page.\n')
            continue
        else:
            break
    except:
        print('Please enter valid page numbers.\n')

for i in range(int(FirstPage), int(LastPage)+1, 2):
    r = requests.get(
        'https://print.vitalsource.com/print/'+IBAN+'?license_type=download&brand=vitalsource&from='+str(i)+'&to='+str(i+1)+'&appName=VitalSource%20Bookshelf&appVersion=9.0.0&mc=0123456789AB&mn=YourMom',
        headers={
            'X-VitalSource-API-Key': VitalSourceAPIKey,
            'X-VitalSource-Access-Token': VitalSourceAccessToken,
            'Accept': 'application/json',
            'User-Agent': 'Bookshelf-Mac/9.0.0 (MacOS/10.14.6; MacBookPro14,2) vitalsource',
            'Accept-Language': 'en-us'
        }
    )
    js = r.json()

    try:
        print(str(i)+'\t'+js[u'images'][0])
        r = requests.get(
                js[u'images'][0],
                headers={
                    'Accept': '*/*',
                    'Accept-Language': 'en-us',
                    'User-Agent': 'VitalSource%20Bookshelf/1204 CFNetwork/978.1 Darwin/18.7.0 (x86_64)'
                }
            )
        open(DownloadFolder+str(i)+'.png', 'wb').write(r.content)
    except:
        print(str(i)+'\tempty page')

    try:
        print(str(i+1)+'\t'+js[u'images'][1])
        r = requests.get(
                js[u'images'][1],
                headers={
                    'X-VitalSource-API-Key': VitalSourceAPIKey,
                    'X-VitalSource-Access-Token': VitalSourceAccessToken,
                    'Accept': 'application/json',
                    'User-Agent': 'Bookshelf-Mac/9.0.0 (MacOS/10.14.6; MacBookPro14,2) vitalsource',
                    'Accept-Language': 'en-us'
                }
            )
        open(DownloadFolder+str(i+1)+'.png', 'wb').write(r.content)
    except:
        print(str(i+1)+'\tempty page')

    time.sleep(random.randint(1, 10))