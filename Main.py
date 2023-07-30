from pyfirmata import Arduino, SERVO, util
from tkinter import *
from time import *

board = Arduino("COM3")

Mpin1 = 4 #base
Mpin2 = 7 #motor 1
Mpin3 = 8 #motor 2
Mpin4 = 11 #hand

board.digital[Mpin1].mode = SERVO
board.digital[Mpin2].mode = SERVO
board.digital[Mpin3].mode = SERVO
board.digital[Mpin4].mode = SERVO

board.digital[Mpin1].write(90)
board.digital[Mpin2].write(90)
board.digital[Mpin3].write(90)
board.digital[Mpin4].write(80)
#app

def RM1(val):
    board.digital[Mpin1].write(val)
def RM2(val):
    board.digital[Mpin2].write(val)
def RM3(val):
    board.digital[Mpin3].write(val)
def RM4(val):
    board.digital[Mpin4].write(val)

app = Tk()
app.title("Saint Gabriel's college")

title = Label(app, text="Saint Gabriel's college", font=("Ariel", 25))
title.pack(side="top")

v1 = IntVar(value=90)
slide1 = Scale(app, length="300", label="Base motor", orient=HORIZONTAL, variable=v1, command=RM1, from_=1, to=180)
slide1.pack(anchor="center")

v2 = IntVar(value=90)
slide2 = Scale(app, length="300", label="Back | Go", orient=HORIZONTAL, variable=v2, command=RM2, from_=1, to=180)
slide2.pack(anchor="center")

v3 = IntVar(value=90)
slide3 = Scale(app, length="300", label="Down | Up", orient=HORIZONTAL, variable=v3, command=RM3, from_=1, to=180)
slide3.pack(anchor="center")

v4 = IntVar(value=80)
slide4 = Scale(app, length="300", label="Hand motor", orient=HORIZONTAL, variable=v4, command=RM4, from_=1, to=80)
slide4.pack(anchor="center")

def resett():
    slide1.set(90)
    slide2.set(90)
    slide3.set(90)
    slide4.set(80)

reset = Button(app, bg="red", command=lambda:resett(), text="reset all")
reset.pack(side="bottom")

def tt():
    slide1.set(90)


resetssa = Button(app, bg="yellow", command=lambda:tt(), text="reset base")
resetssa.pack(side="right")

def x():
    slide2.set(118)
def y():
    slide3.set(105)
def yy():
    slide3.set(120)
def yyy():
    slide3.set(135)

def xg():
    slide2.set(125)
def yg():
    slide3.set(86)

oneX = Button(app, bg="blue", command=lambda:x(), text="X")
oneX.pack(side="left")

oney = Button(app, bg="blue", command=lambda:y(), text="Y1")
oney.pack(side="left")
twoy = Button(app, bg="blue", command=lambda:yy(), text="Y2")
twoy.pack(side="left")
threey = Button(app, bg="blue", command=lambda:yyy(), text="Y3")
threey.pack(side="left")

g1 = Button(app, bg="blue", command=lambda:xg(), text="xg")
g1.pack(side="right")
g2 = Button(app, bg="blue", command=lambda:yg(), text="yx")
g2.pack(side="right")

app.geometry("500x400")
app.mainloop()