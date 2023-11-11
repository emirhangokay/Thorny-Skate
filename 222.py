import cv2
import numpy as np

ref_diameter = 5.0
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=100, param1=50, param2=30, minRadius=10, maxRadius=100)
    

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        
        for (x, y, r) in circles:
            # Çemberi çizme
            cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
            
            # Uzaklığı hesaplama
            diameter = 2 * r
            distance = (ref_diameter * cap.get(3)) / diameter  # Uzaklık hesaplaması
            
            # Uzaklığı görüntüye yazdırma
            cv2.putText(frame, f"{distance:.2f} cm", (x - r, y - r - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    # Görüntüyü gösterme
    cv2.imshow("TS | Cam", frame)
    
    # 'q' tuşuna basıldığında döngüyü sonlandırma
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video akışını ve pencereleri serbest bırakma
cap.release()
cv2.destroyAllWindows()
