import json, requests
from time import sleep
import csv

getdata_url = 'https://dweet.io/get/latest/dweet/for/6f6ce443-341d-473a-b75f-eca547f87728'

with open('c:/temp/measurementdata.csv', 'w') as csvfile:
    fieldnames = ['thing', 'created', 'temperature', 'humidity']
    writer = csv.DictWriter(csvfile, delimiter=';', lineterminator='\n', fieldnames=fieldnames)
    writer.writeheader()
    
    while True:
        resp = requests.get(url=getdata_url)
        data = json.loads(resp.text)
        print(data)
        thing = data['with'][0]['thing']
        created = data['with'][0]['created']
        temperature = data['with'][0]['content']['temperature']
        humidity = data['with'][0]['content']['humidity']

        writer.writerow({'thing': thing, 'created': created, 'temperature' : str(temperature).replace('.', ','), 'humidity' : str(humidity).replace('.', ',')})
        
        sleep(10)
