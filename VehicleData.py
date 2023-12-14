class Engine:
    def __init__(self,id =0,speed=0,time=0,pin=0,angle=0,active = False):
        self.id = id
        self.speed = speed
        self.angle = angle
        self.time = time
        self.pin = pin
        self.active = active
class circleDistance:
    def __init__(self,distance=0,area = 5) :
        self.distance = distance
        self.area = area # 0 merkez, 1,2,3,4 bölge , 5 boş 