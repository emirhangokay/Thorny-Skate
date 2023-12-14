from VehicleData import Engine
from pymata4 import pymata4
import time

board = pymata4.Pymata4()
engine = Engine(id = 1, pin = 3)
board.set_pin_mode_servo(engine.pin)
class Functions:
     def MotorSpeed(self,clockwise,timex):
          if clockwise == False: 
               for engine.angle in range(180,1,-1): 
                    
                    if engine.angle > 90:
                         continue
                    
                    board.servo_write(engine.pin,engine.angle)
                    print(engine.angle)
                    time.sleep(self.delaySelect(timex)) 
                    
          
          if clockwise == True: 
               
               for engine.angle in range(1,180): 
                    if engine.angle <= 90:
                         continue
                    if self.Speed(clockwise=True,value=1) == engine.angle:
                         break

                    board.servo_write(engine.pin,engine.angle)
                    print(engine.angle)
                    time.sleep(self.delaySelect(timex))       
                      
     def KeepAlive(self,timex):
          for engine.angle in range(0,1): 
               board.servo_write(engine.pin,engine.angle)
               print(engine.angle)
               time.sleep(self.delaySelect(timex))          
                           
     def delaySelect(self,speed):
          match speed:
               case 1: delay = 0.12
               case 2: delay = 0.09
               case 3: delay = 0.06
               case 4: delay = 0.03
               case 5: delay = 0.01
          return delay
     def Speed(self,clockwise,value):
          speed = 0
          if clockwise:
               if value == 1: speed = 94
               elif value == 2: speed = 96
               elif value == 3: speed = 99
               elif value == 4: speed = 102
               elif value == 5: speed = 105
               elif value == 6: speed = 108
               elif value == 7: speed = 111
               elif value == 8: speed = 114
               elif value == 9: speed = 117
               elif value == 10: speed = 130
          return speed
if __name__ == "__main__":
     func = Functions()
     func.KeepAlive(timex=1)
     time.sleep(5)
     func.MotorSpeed(clockwise=True, timex=1)





    



