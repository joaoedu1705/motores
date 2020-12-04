#!/usr/bin/env python3

from time import sleep
from ev3dev2._platform.brickpi import OUTPUT_B, OUTPUT_C
from ev3dev2.button import Button
from ev3dev2.motor import MoveTank
from ev3dev2.sensor.lego import ColorSensor
from simple_pid import PID

#VARIÁVEIS DO MOTOR [
btn = Button() # Botão para parar a programação
m1 = OUTPUT_B #Motor 1
m2 = OUTPUT_C #Motor 2
mt = MoveTank(m1, m2) #Os dois motores juntos
# ]

#VARIÁVEIS PARA O SENSOR [
cs = ColorSensor()
#  ]

#VARIÁVEIS PARA O PID [
#pid = PID(1, 0.1, 0.05, setpoint=1) #Função do PID
#output = pid()
#pid.sample_time = 0.01  # update every 0.01 seconds
#pid.setpoint = 10 #Organizar o PID
#pid.Ki = 1.0 #Valor do Ki
#pid.tunings = (1.0, 0.2, 0.4)
#  ]

#SETAR O BOTÃO
if (btn == 1):
    break

#Função para o robô ir para frente
def frente():
    mt.on_for_seconds(speed = 50, seconds=3)
    sleep(1)

def tras():
    mt.on_for_seconds(speed=-50, seconds=3)
    sleep(1)

#while True:
    control = pid(v) #Faz com que sempre seja encontrado uma saída
    v = controlled_system.update(control) #Modifica o valor de acordo com o número da variárel anterior
    output = pid(current_value)

for i in range(3):
    frente()
