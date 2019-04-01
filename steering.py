from time import sleep
from Servo import servo
class Steering(servo):

    def __init__(self, pin, dir = '/sys/class/gpio/', test=False):
        super().__init__(pin=pin, dir=dir, test=test)
        
    
    def set_angle(self, angle = 0):
        
        if angle < -1:
            angle = -1
            
        if angle > 1:
            angle = 1
               
        
        self.Set_High_Time(angle*38)

 
hei = Steering(388)
hei.Run()
angle = -1
while 1: 
	hei.set_angle(angle)
	sleep(3)
	angle = -angle
hei.Stop()
del hei

