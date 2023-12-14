#----------------------------------------------------
# GUI to control Servo Motor interfaced with Arduino
#----------------------------------------------------
import tkinter as tk
from tkinter import messagebox
from turtle import speed
from pyfirmata import ArduinoNano, SERVO
from time import sleep
#-------------------------------------------------------------------------
board = ArduinoNano('COM3')
pin = 8
board.digital[pin].mode = SERVO
# Functions --------------------------------------------------------------
def CCW():
    board.digital[3].write(1)
    board.digital[5].write(0)
    endAngle = int(rotationAngle.get())
    speed = int(rotationSpeed.get())
    delay = delaySelect(speed)
    for angle in range(0, endAngle):
        board.digital[pin].write(angle)
        sleep(delay)
    board.digital[3].write(0)
#-----------------------------------------
def CW():
    board.digital[3].write(0)
    board.digital[5].write(1)
    endAngle = int(rotationAngle.get())
    speed = float(rotationSpeed.get())
    delay = delaySelect(speed)
    for angle in range(endAngle, 1, -1):
        board.digital[pin].write(angle)
        sleep(delay)
    board.digital[5].write(0)
#-----------------------------------------
def delaySelect(speed):
    match speed:
        case 1: delay = 0.12
        case 2: delay = 0.09
        case 3: delay = 0.06
        case 4: delay = 0.03
        case 5: delay = 0.01
    return delay
#-----------------------------------------
def aboutMsg():
    messagebox.showinfo("About",
    "Logic Don't Care Software\nServo Motor Ver 1.0\nAugust 2022")
#------------------------------------------------------------------
def quitApp():
    board.exit()
    win.destroy()
# GUI design -------------------------------------------------------------
win = tk.Tk()
win.title("Servo Motor")
win.minsize(290,150)

rotationAngle = tk.Scale(win, bd=5, from_=0, to=180, orient=tk.HORIZONTAL)
rotationAngle.grid(column=2, row=1)
tk.Label(win, text="Angle (0 to 180) ").grid(column=3, row=1)

rotationSpeed = tk.Entry(win, bd=6, width=6)
rotationSpeed.grid(column=2, row=2)
tk.Label(win, text="Speed (1 to 5)").grid(column=3, row=2)

tk.Label(win, text="Counter Clock").grid(column=2, row=3)
CCWBtn = tk.Button(win, bd=5, bg='#89CFF0', text="Rotate", command=CCW)
CCWBtn.grid(column=2, row=4)

tk.Label(win, text="Clock").grid(column=3, row=3)
CWBtn = tk.Button(win, bd=5, bg='#FF7F7F', text="Rotate", command=CW)
CWBtn.grid(column=3, row=4)

aboutBtn = tk.Button(win, bg='yellow', text="About", command=aboutMsg)
aboutBtn.grid(column=1, row=4)

quitBtn = tk.Button(win, bg='red', text="QUIT", command=quitApp)
quitBtn.grid(column=4, row=4)

win.mainloop()