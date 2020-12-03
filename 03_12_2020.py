#!/usr/bin/env python3
from time import sleep
from ev3dev2._platform.brickpi import OUTPUT_B, OUTPUT_C
from ev3dev2.button import Button
from ev3dev2.motor import MoveTank
from ev3dev2.sensor.lego import ColorSensor

btn = Button() # Botão para parar a programação
m1 = OUTPUT_B
m2 = OUTPUT_C

def frente():
    MoveTank(m1, m2)
