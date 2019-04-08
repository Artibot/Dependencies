from Servo import servo
from time import sleep

class Motor:

    Pin = 0
    Dir = ''
    def __init__(self, pin, dir = '/sys/class/gpio/'):
        self.Pin = pin
        self.__export_pin(dir)
        self.Run(0)

    def __export_pin(self, dir):        
        self.Dir = dir + "gpio" + str(self.Pin) + "/"
        f = open(self.Dir + "direction", "w+")
        f.write("out")
        f.close()
        #Set GPIO to output mode
        
        
    def Run(self, value):
        f = open(self.Dir + "value", "w+")
        f.write(str(value))
        f.close()


