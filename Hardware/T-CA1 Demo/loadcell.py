#!/usr/bin/python3
from hx711 import HX711
import RPi.GPIO as GPIO

hx711 = HX711(
    dout_pin=3,
    pd_sck_pin=2
)

while True:
    measures = hx711.get_raw_data()
    print("\n"+(str)(sum(measures)/len(measures)))
    
