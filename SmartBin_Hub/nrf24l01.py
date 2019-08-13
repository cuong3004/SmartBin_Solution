from RF24 import *
import time

class NRF24L01:
    def __init__(self):
        self.radio = RF24(22, 0)
        self.pipes = [0xF0F0F0F0E1, 0xF0F0F0F0D2]

        self.radio.begin()
        self.radio.enableDynamicPayloads()
        self.radio.setRetries(5,15)

        self.radio.openWritingPipe(self.pipes[0])
        self.radio.openReadingPipe(1, self.pipes[1])

        self.radio.powerUp()
    
    def write(self, data):
        self.radio.write(data)
