
import urllib.request
import time
import board
import busio
import adafruit_am2320
#idx=1 ----------- virtual sensor number
# create the I2C shared bus
i2c = busio.I2C(board.SCL, board.SDA)
am = adafruit_am2320.AM2320(i2c)
while True:
	print("Temperature: ", am.temperature)
	print("Humidity: ", am.relative_humidity)
	ht = urllib.request.urlopen("http://127.0.0.1:8080/json.htm?type=command&param=udevice&idx=1&nvalue=0&svalue="+ str(am.temperature) +";"+ str(am.relative_humidity) +";1")
	time.sleep(10)
ht.close
