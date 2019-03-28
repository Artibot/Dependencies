from time import sleep
from Servo import servo
class Steering(servo):

    def __init__(self, pin, dir = '/sys/class/gpio/', test=True):
        super().__init__(pin=pin, dir=dir, test=test)
        
    
    def set_value(self, angle = 0):
        
        if angle < -5:
            angle = -5
            
        if angle > 5:
            angle = 5
               
        
        self.Set_High_Time(angle*2)

hei = Steering(340, "C:/sys/", True)
hei.Run()

sleep(2)
hei.set_value(3)
sleep(2)
hei.Stop()
del hei