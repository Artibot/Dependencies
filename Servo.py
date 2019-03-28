import threading
from time import sleep

class servo:

    Pin = 0
    Dir = ''
    High_time = 0.0015 # 0.0012----0.0018
    Rate = 0
    thread = ''
    Stopped = True
    Test = False
    
    def __init__(self, pin, dir = '/sys/class/gpio/', test = False):
        self.Pin = pin
        self.Test = test
        self.__export_pin(dir)
        self.thread = threading.Thread(target=self.__set__pwm, args=())
        
        
    def __del__(self):
        self.Stop()
        print("stopped")

    def __export_pin(self, dir):
        f = open(dir + "export", "w+")
        f.write(str(self.Pin))
        f.close()
        ## initialize GPIO
        
        self.Dir = dir + "gpio" + str(self.Pin) + "/"
        f = open(self.Dir + "direction", "w+")
        f.write("out")
        f.close()
        #Set GPIO to output mode

    def __set__value(self, value):
        f = open(self.Dir + "value", "w+")
        f.write(str(value))
        f.close()

    def __set__pwm(self):
        
        if self.Test:
            while(1):
                f = open(self.Dir + "value", "a+")
                f.write(str(self.High_time + self.Rate))
                f.close()
                if self.Stopped:
                    return
        else:
            while(1):
                self.__set__value(1)
                sleep(self.High_time + self.Rate)
                self.__set__value(0)
                sleep(0.02-self.High_time - self.Rate)
                if self.Stopped:
                    return
        
        
    def Run(self):
        self.Stopped = False
        self.thread.start()
        
    def Stop(self):
        self.Stopped = True
        
        
    def Set_High_Time(self, rate):
        if rate > 10:
            rate = 10
        if rate < -10:
            rate = -10
        self.Rate = 0.00003 * rate
        




