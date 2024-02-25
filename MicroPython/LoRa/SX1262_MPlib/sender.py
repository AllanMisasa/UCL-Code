# MicroPython lora simple_rxtx example - synchronous API version
# MIT license; Copyright (c) 2023 Angus Gratton
import time
from machine import Pin, SPI
from lora import SX1262
#from antenna_switch import MyAntennaSwitch

def get_modem():
    lora_cfg = { 'freq_khz': 868000, # 868000 for europæisk 868Mhz bånd
                 'sf': 7, # Spreading factor
                 'coding_rate': 8, # 4/5 coding
                 'bw': '125', # båndbredde
                 #'ant_sw': MyAntennaSwitch(25)
                 }   
    
    '''
    HSPI: id=1 - SCK 14, MOSI 13, MISO 12
    VSPI: id=2 - SCK 18, MOSI 23, MISO 19
    Resten af koden er baseret på VSPI
    '''
    spi = SPI(1, baudrate=2000_000, sck=Pin(14), mosi=Pin(13), miso=Pin(12)) # Required.
    cs = Pin(5) # Required

    return SX1262(spi, cs,
                 busy=Pin(2),  # Required
                 dio1=Pin(21),   # Optional, recommended
                 dio2_rf_sw=True,
                 dio3_tcxo_millivolts=1600, # Else try 3300
                 reset=Pin(15),  # Optional, recommended
                 lora_cfg=lora_cfg)

def main():
    print("Initializing...")
    modem = get_modem()

    while True:
        print("Sending...")

        modem.send(b"F")

        print("Sent!")
        #modem.send("hello".encode())
        #modem.send("hello".encode(), time.ticks_add(time.ticks_ms(), 250))
        print("Receiving...")
        rx = modem.recv(timeout_ms=5000)
        if rx:
            print(f"Received: {rx!r}")
        else:
            print("Timeout!")
        time.sleep(2)


if __name__ == "__main__":
    main()