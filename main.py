import Functions
import circleCam
import time
from threading import Thread # eş zamanlı işlem

engine = Functions.engine
Functions.Functions.KeepAlive()
time.sleep(2)
cam_thread = Thread(target=circleCam.startCam)
cam_thread.start()
while True:
    print(circleCam.filtered_distance)
    print("--")
    print(engine.speed)
    print("-----------------------------")
    if circleCam.filtered_distance >= 20 and engine.speed < 10:
        Functions.Functions.Start()
    elif circleCam.filtered_distance < 20 and engine.speed > 10 :
        Functions.Functions.Stop()
    time.sleep(0.00001)
   
