#!/usr/bin/env python
# Serial Test
import time
import serial
serial = serial.Serial(
    port='/dev/serial0',
    baudrate = 57600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1)
serial.flush()
serial.write(str.encode("mot help\n"))
strList = serial.readlines()
for i in strList:
    print(i)
