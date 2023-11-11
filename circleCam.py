import cv2
import numpy as np
import math
from VehicleData import circleDistance

cap = cv2.VideoCapture(0) # 0 dahili , 1 harici kamera

############ El ile girilecekler ############
focal_length = 3500  # Kameranın odak uzunluğu (mm)
real_radius = 2  # gerçek daire yarıçapı
#############################################

########### Filtreleme parametreleri ###########
num_measurements = 5  # Ölçüm sayısı
buffer_size = 10  # Ölçümlerin saklanacağı tampon boyutu
distances_buffer = []  # Ölçümlerin saklanacağı tampon
filtered_distance = 0  # Filtrelenmiş uzaklık
distanceData = circleDistance() # mesafe sınıfından nesne oluştur
################################################


def detect_circles(frame): # ana fonksiyon
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #filtreleme
    gray = cv2.bilateralFilter(gray, 10,80,95) #filtreleme
    gray = cv2.Canny(gray,75,105) #filtreleme
    
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, minDist=50, param1=100, param2=33, minRadius=10, maxRadius=200) #çember tepit

    if circles is not None: # çember algılanma durumunda bloğa gir
        circles = np.uint16(np.around(circles)) # tam sayı türe dönüştürme

        for circle in circles[0, :]:
            origin_x = 320
            origin_y = 240
            center_x, center_y, radius = circle[0], circle[1], circle[2] # algılanan görüntüde çemberin x,y ve yarıçap değerleri
            distance = calculate_distance(radius) # mesafe hesaplama fonksiyonu 
            distance2 = calculate_distance2(center_x, center_y, origin_x, origin_y)
            if distance2 < 7:
                print("Orijine olan uzaklık: Merkezdesin")
            else:
                print("Orijine olan uzaklık:", distance2)
                
            # Filtreleme işlemi
            update_buffer(distance) # algılanan çember mesafelerini bir listede topla
            update_filtered_distance() # filtrelenen uzaklık değerlerini güncelle

            cv2.circle(frame, (center_x, center_y), radius, (0, 255, 0), 2) # dış sınır
            cv2.circle(frame, (center_x, center_y), 2, (0, 0, 255), 3) # merkez nokta
            cv2.putText(frame, f"Filtered Distance: {filtered_distance:.2f} cm", (center_x, center_y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2) # filtrelenen uzaklığı ekrana yaz
            
            # çemberin bulunduğu bölge numaralarını ata
            if center_x >= frame.shape[1] // 2 and center_y < frame.shape[0] // 2: 
                    distanceData.area = 1
            elif center_x < frame.shape[1] // 2 and center_y < frame.shape[0] // 2:
                    distanceData.area = 2          
            elif center_x < frame.shape[1] // 2 and center_y >= frame.shape[0] // 2:
                    distanceData.area = 3
            elif center_x >= frame.shape[1] // 2 and center_y >= frame.shape[0] // 2:
                    distanceData.area = 4  
            print(f"{distanceData.area}. Bölge")      
                       
    return frame

def calculate_distance(radius):
    distance = (real_radius * focal_length) / (radius *5) # uzaklık formülü
    return distance

def calculate_distance2(center_x, center_y, origin_x=0, origin_y=0):
    return math.sqrt((center_x - origin_x)**2 + (center_y - origin_y)**2) # orjin uzaklığı


def update_buffer(distance):
    distances_buffer.append(distance) 
    if len(distances_buffer) > buffer_size: 
        distances_buffer.pop(0)

def update_filtered_distance():
    global filtered_distance
    if len(distances_buffer) > 0:
        filtered_distance = sum(distances_buffer) / len(distances_buffer)
    else:
        filtered_distance = 0
        
def startCam():
    while True:
                ret, frame = cap.read()
                if ret:
                    frame = detect_circles(frame)
                    height, width, _ = frame.shape # sahpe = yükseklik , genişlik , kanal sayısı
                    half_height = height // 2 # // tam bölme -> 2.5 / 2 değerini 1.25 yerine 1 olarak verir
                    half_width = width // 2                    
                    cv2.putText(frame, 'I', (half_width + half_width // 2, half_height // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 55, 255), 4) # bölgeyi ekrana yaz
                    cv2.putText(frame, 'II', (half_width // 2, half_height // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 55, 255), 4)
                    cv2.putText(frame, 'III', (half_width // 2, half_height + half_height // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 55, 255), 4)
                    cv2.putText(frame, 'IV', (half_width + half_width // 2, half_height + half_height // 2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 55, 255), 4)
                       
                    cv2.line(frame, (frame.shape[1] // 2, 0), (frame.shape[1] // 2, frame.shape[0]), (0, 255, 0), 2) # x ekseni
                    cv2.line(frame, (0, frame.shape[0] // 2), (frame.shape[1], frame.shape[0] // 2), (0, 255, 0), 2) # y ekseni
                                              
                    cv2.imshow('Thorny Skate', frame) # görüntüyü başlat
                    
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        cap.release()
                        cv2.destroyAllWindows()
                        break
                else:
                    break
                
if __name__ == "__main__":
     startCam()
