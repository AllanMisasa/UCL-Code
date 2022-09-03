'''import machine
import time
pin = 15
led = machine.Pin(pin1, machine.Pin.OUT)
led.low()
time.sleep(5)
led.high()
time.sleep(5)
frequency = 5000
pwm = machine.PWM(machine.Pin(15), frequency)
while True:
    for duty_cycle in range(0, 1023):
        pwm.duty(duty_cycle)
        time.sleep(0.005)'''

import time
from machine import Pin
led = Pin(2, Pin.OUT)  # create LED object from pin2,Set Pin2 to output

while True:
    led.value(1)  # Set led turn on
    time.sleep(0.5)
    led.value(0)  # Set led turn off
    time.sleep(0.5)
