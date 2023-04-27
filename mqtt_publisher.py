import paho.mqtt.client as mqtt
import time
import random

# create a client instance
client = mqtt.Client()

# connect to the broker
client.connect("broker.hivemq.com", 1883, 60)

# loop forever and publish sensor data
while True:
    temperature = random.randint(0, 100) # TODO: Replace it with your Sensor value
    humidity = random.randint(0, 100)    # TODO: Replace it with your Sensor value
    client.publish("melvin/mqttExample/temperature", temperature)
    client.publish("melvin/mqttExample/humidity", humidity)
    print("Publishing-->melvin/mqttExample/temperature: ", temperature)
    print("Publishing-->melvin/mqttExamplehumidity: ", humidity)
    time.sleep(1)