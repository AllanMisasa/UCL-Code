'''Virker kun på et WiFi 5 eller lavere 2.4Ghz netværk
Jeg kunne lave et på min Oneplus 8 Pro ved at vælge 2.4Ghz
på hotspotindstillinger, og slå WiFi 6 fra.
'''

ssid = 'indsæt ssid her'
password = 'indsæt password her'

def do_connect(ssid, password):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

do_connect(ssid, password)

# Her installerer vi nødvendig lora firmware
import mip
mip.install("lora-sync")
mip.install("lora-sx126x")