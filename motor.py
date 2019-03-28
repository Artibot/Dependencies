from Servo import servo
from time import sleep

class Motor(servo):

    def __init__(self, pin, dir = '/sys/class/gpio/', test = False):
        super().__init__(pin=pin, dir=dir, test=test)


    def set_throttle(self, throttle = 0):

        if throttle < 0:
            throttle = 0
        if throttle > 1:
            throttle = 1
        self.Set_High_Time(throttle*10)



pinObject = Motor(340, "C:/sys/", True)
pinObject.Run()

sleep(2)
pinObject.set_throttle(0.6)
sleep(2)
pinObject.Stop()
del pinObject
