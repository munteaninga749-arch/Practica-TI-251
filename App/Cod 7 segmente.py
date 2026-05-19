from machine import Pin
from time import sleep

A=Pin(5,Pin.OUT)    #D1
B=Pin(4,Pin.OUT)    #D2
C=Pin(0,Pin.OUT)    #D3
D=Pin(2,Pin.OUT)    #D4
P=Pin(14,Pin.OUT)  #D5
E=Pin(12,Pin.OUT)   #D6
F=Pin(13,Pin.OUT)   #D7
G=Pin(16,Pin.OUT)   #D0

seg=[A,B,C,D,E,F,G]

cifre=[
[0,0,0,0,0,0,1],
[1,0,0,1,1,1,1],
[0,0,1,0,0,1,0],
[0,0,0,0,1,1,0],
[1,0,0,1,1,0,0],
[0,1,0,0,1,0,0],
[0,1,0,0,0,0,0],
[0,0,0,1,1,1,1],
[0,0,0,0,0,0,0],
[0,0,0,0,1,0,0]
]

while True:
    for n in range(10):
        for i in range(7):
            seg[i].value(cifre[n][i])
        sleep(1)
