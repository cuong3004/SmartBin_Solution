import pigpio
from time import sleep

from config import *

class ArmController:
    
    def __init__(self):
        self.pi = pigpio.pi()
        
        self.servoPos = {}
        self.servoPos[str(SERVO1)] = 0
        self.servoPos[str(SERVO2)] = 0
        self.servoPos[str(SERVO3)] = 0
        self.servoPos[str(SERVO4)] = 0
        
        self.originState()
    
    def _setGpio(self, pin, pulse_width):
        self.pi.set_servo_pulsewidth(pin, pulse_width)
        sleep_time = abs(self.servoPos[str(pin)] - pulse_width) / 1000 * 0.5
        sleep(sleep_time)
        self.servoPos[str(pin)] = pulse_width
        self.pi.set_servo_pulsewidth(pin, 0)
        
    def originState(self):
        self._setGpio(SERVO4, 800)
        self._setGpio(SERVO3, 1500)
        self._setGpio(SERVO2, 800)
        self._setGpio(SERVO1, 1500)
        
        
    def moveToTrashBin1(self):
        self._setGpio(SERVO1, 1000)
        self._setGpio(SERVO3, 1500)
        self._setGpio(SERVO2, 1500)
        self._setGpio(SERVO4, 800)
        sleep(0.5)
        self._setGpio(SERVO4, 1500)
        sleep(0.2)
        self._setGpio(SERVO4, 800)
            
    def moveToTrashBin2(self):
        self._setGpio(SERVO1, 1500)
        self._setGpio(SERVO3, 1500)
        self._setGpio(SERVO2, 1500)
        self._setGpio(SERVO4, 800)
        sleep(0.5)
        self._setGpio(SERVO4, 1500)
        sleep(0.2)
        self._setGpio(SERVO4, 800)
        
    def moveToTrashBin3(self):
        self._setGpio(SERVO1, 2000)
        self._setGpio(SERVO3, 1500)
        self._setGpio(SERVO2, 1500)
        self._setGpio(SERVO4, 800)
        sleep(0.5)
        self._setGpio(SERVO4, 1500)
        sleep(0.2)
        self._setGpio(SERVO4, 800)