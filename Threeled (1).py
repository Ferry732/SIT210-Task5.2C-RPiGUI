from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

ledRed = LED(18)
ledYellow = LED(23)
ledGreen = LED(24)

win = Tk()
win.title("LED Operator")
myFont = tkinter.font.Font(family = 'comicsans', size = 20, weight = "bold")

def ledToggleRed():
    if ledRed.is_lit:
       ledRed.off()
       ledYellow.off()
       ledGreen.off()
       redButton["text"] = "Touch to start LED"
       yellowButton["text"] = "Touch to start LED"
       greenButton["text"] = "Touch to start LED"
    else:
       ledRed.on()
       ledYellow.off()
       ledGreen.off()
       redButton["text"] = "Touch to off"
       yellowButton["text"] = "Touch to start LED"
       greenButton["text"] = "Touch to start LED"
       
def ledToggleYellow():
    if ledYellow.is_lit:
       ledYellow.off()
       ledRed.off()
       ledGreen.off()
       yellowButton["text"] = "Touch to start LED"
       redButton["text"] = "Touch to start LED"
       greenButton["text"] = "Touch to start LED"
    else:
       ledYellow.on()
       ledRed.off()
       ledGreen.off()
       yellowButton["text"] = "Touch to off"
       redButton["text"] = "Touch to start LED"
       greenButton["text"] = "Touch to start LED"
       
def ledToggleGreen():
    if ledGreen.is_lit:
       ledGreen.off()
       ledRed.off()
       ledYellow.off()
       greenButton["text"] = "Touch to start LED"
       redButton["text"] = "Touch to start LED"
       yellowButton["text"] = "Touch to start LED"
    else:
       ledGreen.on()
       ledRed.off()
       ledYellow.off()
       greenButton["text"] = "Touch to off"
       redButton["text"] = "Touch to start LED"
       yellowButton["text"] = "Touch to start LED"

def close():
    RPi.GPIO.cleanup()
    win.destroy() 

##Red
redButton = Radiobutton(win, text= 'Touch to start LED', font = myFont, command = ledToggleRed, bg = 'red', height = 1, width = 20)
redButton.grid(row=0, column=1)

##Yellow
yellowButton = Radiobutton(win, text= 'Touch to start LED', font = myFont, command = ledToggleYellow, bg = 'yellow', height = 1, width = 20)
yellowButton.grid(row=1, column=1)

##Green
greenButton = Radiobutton(win, text= 'Touch to start LED', font = myFont, command = ledToggleGreen, bg = 'green', height = 1, width = 20)
greenButton.grid(row=2, column=1)
##Exit
exitButton = Button(win, text= 'Exit', font = myFont, command = close, bg = 'orange', height = 1, width = 7)
exitButton.grid(row=3, column=1)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()
