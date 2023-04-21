import time
import os
import subprocess
import datetime

### 樹梅派2 : 接收另一個樹莓派傳來的訊號，並啟動微型抽水馬達

order = 'mosquitto_sub -h 192.168.0.13 -t test'
pi = subprocess.Popen(order,shell=True,stdout=subprocess.PIPE)
os.system('sudo uhubctl -l 1-1 -p 2 -a off')
print('start to detect')

while True:
	os.system('sudo uhubctl -l 1-1 -p 2 -a off')
	for i in iter(pi.stdout.readline,'b'):
		if i == b'There have a cat\n':
			print('open the power')
			os.system('sudo uhubctl -l 1-1 -p 2 -a on')
			content = str(datetime.datetime.now())
			with open('drink_water.txt','a') as f:
				f.write(content)
				f.write('\n')
			time.sleep(10)
		else:
			print('There is no cat')
			os.system('sudo uhubctl -l 1-1 -p 2 -a off')
