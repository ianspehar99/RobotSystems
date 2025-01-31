from robot_hat import ADC
from robot_hat import Grayscale_Module
from picarx_improved import Picarx


class SENSOR(Picarx):

    def __init__(self):
        super().__init__()

    def sensor_read(self):
        sensor_values = self.get_grayscale_data()
        return sensor_values
    

class INTERP(Picarx):

    def __init__(self, sensitivity = 300, polarity = 1, reference = 1000):
        #If line is darker than background, use default polarity
        #If line is lighter, set polarity to 0
        super().__init__()

        
        self.sensitivity = sensitivity
        self.polarity = polarity
        self.reference = self.set_grayscale_reference()

    def get_position(self,sensor_val_list):
        sensitivity = self.sensitivity
        sv = sensor_val_list
        #Reverse everything if polarity switched
        if self.polarity == 0:
            sv = sv*-1
        #Compare left and middle:
        ref = self.reference
        Left = sv[0]
        Middle = sv[1]
        Right = sv[2]
        dif1 = Middle - Left
        dif2 = Right - Middle
        position = None
        if abs(dif1) < sensitivity and abs(dif2) < sensitivity and sv[0] < ref:
            print("Car totally off course")
            position = 2
        elif abs(dif1) > sensitivity: 
            if abs(dif2) > sensitivity:
                print("Car is centered")
                position = 0
            if abs(dif2) < sensitivity:
                #Car is either on edge case to the right, or is left of center
                if dif1 < 0:
                    print("car is to the left")
                    position = -1*(dif1/sensitivity)
                elif dif1 > 0:
                    print("car at edge case to the right")
                    position = 0.5*(dif1/sensitivity)
        elif abs(dif1) < sensitivity:
            if dif2 > 0:
                print("Car is to the right")
                position = 1*(dif2/sensitivity)
            elif dif2 < 0:
                print("Car at edge case to left")
                position = 0.5*(dif2/sensitivity)
        return position
    

class CONTROL(Picarx):

    def __init__(self, scale_factor = 10):
        #Negative to correct the offset
        self.scale_factor = -1*scale_factor
        super().__init__()

    def correct_car(self,offset):
        servo_angle = offset*self.scale_factor
        self.set_dir_servo_angle(servo_angle)






            

      

 






