############################code by KANISHK MAHOR###########################



import paho.mqtt.client as mqtt
import os         #used to use os cmds from python

file=open("/proc/loadavg","r") # opening the file and getting the loadavg

for line in file:
    field=line.split(" ")
    one=field[0]               #one gets the load for 1 minute
    five=field[1]              #one gets the load for 5 minute
    ten=field[2]               #one gets the load for 10 minute

file.close()
def on_connect(client, userdata, flags, rc):
    print("Connected")
    
#load1, load2, load3 = os.getloadavg()  getting load avg by simply using getloadavg()


client=mqtt.Client()    
client.will_set("client/dead","client_disconnected",retain=False) #will used for getting if the publisher abruptly disconnect or not.
client.connect("192.168.7x.xxx",1883,60)  #enter your system ip port =1883(default port for mqtt) 

client.on_connect=on_connect          # calling the on connect function

client.publish("room/load/1m",one)    #get 1m load
client.publish("room/load/5m",five)   #get 5m load
client.publish("room/load/10m",ten)   #get 10m load

client.loop_forever()                 #loop for continous running

client.disconnect()                   #disconnect the client normally

