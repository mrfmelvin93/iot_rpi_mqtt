import paho.mqtt.client as mqtt

# create a client instance
client = mqtt.Client()

# define a callback for the message received event
def on_message(client, userdata, message):
    print("Subscribing-->"+ message.topic, message.payload)

# connect to the broker
client.connect("broker.hivemq.com", 1883, 60)

# subscribe to the sensor data topics
client.subscribe("melvin/mqttExample/temperature")
client.subscribe("melvin/mqttExample/humidity")

# set the callback for the message received event
client.on_message = on_message

# loop forever and wait for messages
client.loop_forever()
