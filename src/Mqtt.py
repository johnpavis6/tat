import paho.mqtt.client as mqtt

client=mqtt.Client()
client.username_pw_set("sangameswarana@wekancode.com", password="e246feec")
client.connect("mqtt.dioty.co",1883,10)

def send(channel,data):
	client.publish(channel,data)
	

