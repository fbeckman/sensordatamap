import json, requests
from subprocess import call
import sys

sensorGUID = sys.argv[1]
warehouseID = sys.argv[2]
geohash = sys.argv[3]
getdata_url = "https://dweet.io/get/latest/dweet/for/" + sensorGUID
    
try:
	resp = requests.get(url=getdata_url)
	data = json.loads(resp.text)
	thing = data['with'][0]['thing']
	temperature = data['with'][0]['content']['temperature']
	humidity = data['with'][0]['content']['humidity']
	call(["curl", "-XPOST", "http://localhost:8086/write?db=logger", "--data-binary", "sensor,WH=" + warehouseID + ",Sensor1=1,geohash=" + geohash + " c=" + str(temperature) + ",h=" + str(humidity)])    
except:
	print("Unexpected error:", sys.exc_info()[0])