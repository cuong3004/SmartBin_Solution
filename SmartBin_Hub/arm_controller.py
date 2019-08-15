import pigpio

class ArmController:
	
	def __init__(self):
		self.pi = pigpio.pi()
	
	def _setGpio(self, pin, pulse_width):
		self.pi.set_servo_pulsewidth(pin, pulse_width)
		
