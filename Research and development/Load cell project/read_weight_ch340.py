import os
import serial
import logging
from time import sleep

logging.basicConfig(level=logging.DEBUG)

ser = serial.Serial('/dev/ttyUSB0', '9600', timeout=2)
logging.debug(os.system("python3 -m serial.tools.list_ports"))

while True:
#ser.write('your command\r\n'.encode('ascii'))  # convert to ASCII before sending it
    buf = ser.read(100)  # read 100 bytes
    print(buf.decode('ascii'))
    sleep(0.1)