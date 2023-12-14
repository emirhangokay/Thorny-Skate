from pymata4 import pymata4

board = pymata4.Pymata4(baud_rate=9600)

# Potansiyometre için kullanılacak pin numarası
potentiometer_pin = 0  # Örnek olarak A0 pinini kullanıyoruz

# Potansiyometre değerini okumak için gerekli fonksiyon
def read_potentiometer():
    # Potansiyometre değerini oku (Analog okuma yapılır)
    pot_value = board.analog_read(potentiometer_pin)
    print(f"Potansiyometre değeri: {pot_value}")

board.start()

try:
    while True:
        read_potentiometer()

except KeyboardInterrupt:
    board.shutdown()
