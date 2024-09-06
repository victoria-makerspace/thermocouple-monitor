# The MIT License (MIT)
# Copyright (c) 2024 Mike Teachman
# https://opensource.org/licenses/MIT

import time
import board
from adafruit_ht16k33 import segments 
import digitalio
import adafruit_max31856
import busio

spi = busio.SPI(clock=board.GP14, MOSI=board.GP15, MISO=board.GP12)
cs = digitalio.DigitalInOut(board.GP13)
cs.direction = digitalio.Direction.OUTPUT
thermocouple = adafruit_max31856.MAX31856(spi, cs)

i2c = busio.I2C(board.GP17, board.GP16)    
display = segments.Seg14x4(i2c)

while True:
    display.print("{:5.1f}".format(thermocouple.temperature))
    time.sleep(0.5)