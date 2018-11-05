from time import sleep
from json import dumps
import Mqtt as mqtt
import Calculator as calc
import Camera as cam
import Location as loc

def start(id,latitude,longitude):
	dist=0
	th=1000
	prev_loc=loc.generate_random_data(latitude, longitude, 1)
	while(True):
		curr_loc=loc.generate_random_data(latitude, longitude, 1)
		dist+=calc.distance(prev_loc,curr_loc)
		data={'tracking_id':'wekancode','driver_id':id,'type':1}
		data.update(curr_loc)
		mqtt.send("/sangameswarana@wekancode.com/wekancode",dumps(data))
		print("wekancode",dumps(data),dist)
		prev_loc=curr_loc
		if(dist>=th):
			dist=dist-th
			#cam.take_photo()
		sleep(2)
