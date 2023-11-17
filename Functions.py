from VehicleData import Engine
from pymata4 import pymata4
import time

board = pymata4.Pymata4()
engine = Engine(id = 1, pin = 3)
board.set_pin_mode_servo(engine.pin)

class Functions:
    def KeepAlive():       # ilk nabız
         for engine.speed in range(0,10):
                board.servo_write(engine.pin,engine.speed)
                time.sleep(0.0001)
                engine.active = True
                
    def Start():
               for engine.speed in range(10,32): ## 22 start 32 max 90 diğer tur 32 stop
                    board.servo_write(engine.pin,engine.speed)
                    time.sleep(0.0001)
    def Stop(): 
               for j in range (engine.speed,0,-1):
                    board.servo_write(engine.pin,j)
                    time.sleep(0.0001)
                    engine.speed = j
                    engine.active = False
if __name__ == "__main__":
    Functions.KeepAlive()
    time.sleep(4)
    Functions.Start()
    time.sleep(4)
    Functions.Stop()




    



