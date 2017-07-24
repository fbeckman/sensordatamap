import json, requests
from time import sleep
import csv
from subprocess import call
import sys

sensorGUID = sys.argv[1]
getdata_url = "https://dweet.io/get/latest/dweet/for/" + sensorGUID

warehouseID = sys.argv[2]
    
while True:
    
    resp = requests.get(url=getdata_url)
    data = json.loads(resp.text)
    print(data)
    thing = data['with'][0]['thing']
    temperature = data['with'][0]['content']['temperature']
    humidity = data['with'][0]['content']['humidity']

    f = open('data.txt', 'w')
    f.write('sensor,WH=' + warehouseID + ',Sensor1=1 c=' + str(temperature) + '\n')
    f.write('sensor,WH=' + warehouseID + ',Sensor1=1 h=' + str(humidity))
    f.close()

    call(["curl", "-XPOST", "http://localhost:8086/write?db=ETAS", "--data-binary", "@data.txt"])    
  
    sleep(10)

