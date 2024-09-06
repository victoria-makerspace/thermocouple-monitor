# Thermocouple Monitor
This repository describes the components needed to make a thermocouple monitor

<img src="images/thermocouple-connection.jpeg" width="600">


## Schematic
The [schematic](schematic/thermocouple-measurement-unit.pdf) shows the point-to-point wiring needed on the Perma-Proto breadboard.  

## Connectors

Two female-to-female connectors are used to connect the 

## 3D printed enclosure
The enclosure design is a derivative of the [3DP case for an Adafruit half-size Perma-Proto Half-Sized breadboard](https://www.printables.com/model/37200-perma-proto-feather-case).  The [7 or 14 Segment Display Panel Mount](https://www.printables.com/en/model/628477-7-or-14-segment-display-panel-mount) is also a 3D print. 

The modifications include:
1. side hole to plug usb cable into Raspberry Pi Pico
1. top hole to fit a bezel for the HT16K33 Backpack PCB
1. mount for the Adafruit Universal Thermocouple Amplifier MAX31856 Breakout
1. strain relief for thermocouple cable

3D print files are found [here](/3dp)

<img src="images/inside.jpeg" width="600">
<img src="images/outside.jpeg" width="600">


## CircuitPython Code
A few lines of CircuitPython [code](code/code.py) is used to read the temperature values from thermocouple board and display the values on the display.  The code uses two Adafruit CircuitPython libraries:
1. adafruit_ht16k33
1. adafruit_max31856

These two libraries need to loaded into the CircuitPython filesystem on the Raspberry Pi Pico.
