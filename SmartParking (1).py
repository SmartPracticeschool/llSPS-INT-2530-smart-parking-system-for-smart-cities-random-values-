import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
#Provide your IBM Watson Device Credentials
organization = "5v3om3"
deviceType = "raspberrypi"
deviceId = "123456"
authMethod = "token"
authToken = "12345678"

def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)#Commands
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()
# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()
while True:
        slot1=random.randint(0, 200)
        #print(slot1)
        slot2 =random.randint(0, 200)
        #Send slot1 & slot2 to IBM Watson
        data = { 'slot1' : slot1, 'slot2': slot2 }
        #print (data)
        def myOnPublishCallback():
            print ("Published slot1 = %s m" % slot1, "slot2 = %s m" % slot2, "to IBM Watson")
        success = deviceCli.publishEvent("SmartParking", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(2)
        deviceCli.commandCallback = myCommandCallback
# Disconnect the device and application from the cloud
deviceCli.disconnect()
