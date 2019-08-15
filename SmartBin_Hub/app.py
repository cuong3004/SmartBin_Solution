import json
import time

from mqtt_service import MqttService
from nrf24l01 import NRF24L01
from arm_controller import ArmController

from config import *

rf24 = NRF24L01()
mqtt = MqttService()
arm = ArmController()

current_object_id = 0

def on_mqtt_message(client, userdata, message):
    global current_object_id
    
    json_str = str(message.payload.decode("utf-8"))
    data = json.loads(json_str)
    
    print(data)
    
    if data['id'] == current_object_id:
        return
    
    current_object_id = data['id']
    
    rf24.write(bytes(str(data['id']), 'utf8') + b'1')
    if data['id'] == 1:
        arm.moveToTrashBin1()
    elif data['id'] == 2:
        arm.moveToTrashBin2()
    elif data['id'] == 3:
        arm.moveToTrashBin3()
     
    time.sleep(0.5)
    
    arm.originState()
    
    rf24.write(bytes(str(data['id']), 'utf8') + b'0')
    
    
if __name__ == '__main__':
    mqtt.subscribe(on_mqtt_message)
    
    mqtt.client.loop_forever()
    
    
    