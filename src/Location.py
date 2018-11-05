import random

def generate_random_data(lat, lon, num_rows):
	locs=[]
	for _ in range(0,num_rows):
		hex1 = '%012x' % random.randrange(16**12)
		flt = float(random.randint(0,100))
		dec_lat = random.random()/700
		dec_lon = random.random()/700
		locs.append({'lng':lon+dec_lon, 'lat':lat+dec_lat})
	return locs[0]