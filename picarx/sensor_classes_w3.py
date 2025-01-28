from adc import ADC
from modules import Grayscale_Module

class SENSOR:

    def __init__(self):
        self.pin1 = ADC("A0")
        self.pin2 = ADC("A1")
        self.pin3 = ADC("A2")

        self.gs_mod = Grayscale_Module(pin1,pin2,pin3)
       

    def sensor_read(self):
        sensor_values = self.gs_mod.read()
        return sensor_values
    

class INTERP:

    def __init__(self, sensitivity = 600, polarity = 1, reference = 500):
        
        self.sensitivity = sensitivity
        self.polarity = polarity
        self.reference = reference

    def position(self,sensor_val_list)
        sv = sensor_val_list
        #Compare left and middle:
        ref = self.reference
        Left = sv[0]
        Middle = sv[1]
        Right = sv[2]
        dif1 = Middle - Left
        dif2 = Right - Middle

        if abs(dif1) < sensitivity and abs(dif2) < sensitivity and sv[0] < ref:
            print("Car totally off course")
        elif: abs(dif1) > sensitivity: 
            if abs(dif2) > sensitivity:
                print("Car is centered")
                position = 0
            if abs(dif2) < sensitivity:
                #Car is either on edge case to the right, or is left of center
                if dif1 < 0:
                    print("car is to the left")
                    position = -1
                elif dif1 > 0:
                    print("car at edge case to the right")
                    position = 0.5
        elif abs(dif1) < sensitivity:
            if dif2 > 0:
                print("Car is to the right")
                position = 1
            elif dif2 < 0:
                print("Car at edge case to left")
                position = 0.5




            

      

 






