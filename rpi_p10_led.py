import requests
import serial
import time
#|
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJRCI6IjQ0ZTNiYmRmLTI1NjAtNDdjOC1iNTM5LWFjMWJjYzRmOTUwZiIsIk5hbWUiOiJHVEsgQy5FLlQuUCBTb2NpZXR5In0.KArANyWtSIsS2qBgFfovAmBfZCY-tmpnJCVkErgqUeU"
url = "https://analyzeriot.el.r.appspot.com/api/analyzer/water"

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.flush()

while True:
	try:
		resp = requests.get(url, headers={"content-type":"application/json", "Authorization": "Bearer " + token}).json()
		serial_data = resp['data']['cod'] + ":" + resp['data']['bod'] + ":" + resp['data']['tss'] + ":" + resp['data']['ph']
		ser.write(serial_data.encode())
		time.sleep(300)
	except:
		pass
