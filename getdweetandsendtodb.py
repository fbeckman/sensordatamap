import json, requests
from time import sleep
import csv

getdata_url = "https://dweet.io/get/latest/dweet/for/1907ac6b-6a37-40b3-afa8-e6bcf12348c0"
influxdb_url = "http://localhost:8086/write?db=ETAS' --databinary @c:/temp/data.txt"
    
while True:
    
    resp = requests.get(url=getdata_url)
    data = json.loads(resp.text)
    print(data)
    thing = data['with'][0]['thing']
    temperature = data['with'][0]['content']['temperature']
    humidity = data['with'][0]['content']['humidity']

    f = open('c:/temp/data.txt', 'w')
    f.write('sensor,WH=Vaihingen,Sensor1=' + thing + ' c=' + str(temperature) + '\n')
    f.write('sensor,WH=Vaihingen,Sensor1=' + thing + ' h=' + str(humidity))
    f.close()

    r = requests.post(influxdb_url)
   
    sleep(10)
