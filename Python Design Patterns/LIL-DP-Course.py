# Code from following the introductory  course on https://www.linkedin.com/learning/python-design-patterns-14304845/

'''
Creational patterns - Create objects systematically. 
A flexible pattern, for example used to create different subtypes of objects from the same class. 
Can be used to create at runtime. Takes advantage of polymorphism.
'''

'''
Structural patterns - Establish relationships between software components, fulfilling both functional and nonfunctional requirements. 
Different goals -> different structures. Takes advantage of inheritance.
'''

'''
Behavioural patterns - Object interactions, accomplishing both functional and nonfunctional requirements.
Focus is on defining the protocols between objects when trying to make them cooperate to achieve a common goal.  
Heavy use of methods and their signatures.
'''

'''
Pattern context
- Participants: Classes involved to form a design pattern. The roles needed to accomplish the goal of the design pattern.
- Quality attributes: Nonfunctional requirements. Fulfilling these requirements often affect the overall architecture.
- Forces: Factors or trade-offs to consider when adopting a particular design pattern or trying to fulfill a specific nonfunctional requirement. 
- Consequences: If the rest of the context is not carefully considered and the design patterns are misused, it will have a negative impact on the design.
'''

'''
Factory pattern: Specialized in creating other objects.
Useful when uncertain about what the types of the objects are, or when you have to decide on which classes to use at runtime. 
Flexible and polymorphic, falling under the creational pattern category.
For example, let's say you have to deploy a lot of microcontrollers in different locations. You really enjoy MicroPython, but it gets tedious to write a new boot.py
to connect the ESP32 to the same network, and you have to make them publish some data via MQTT. Also you have to test that they can connect to the network and push data to your
database. If we use the factory design pattern, we can quickly reuse patterns to make this easy to deploy in different areas.
'''
import network
import time

class ESP32CONFIGA:
    def wifi_details(self):
        SSID = 'TF27'
        KEY = 'juggernaut'
        return SSID, KEY
    def mqtt_details(self):
        channel = "/biogas/"

class ESP32CONFIGB:
    def wifi_details(self):
        SSID = 'TF29'
        KEY = 'JanUs'
        return SSID, KEY
    def mqtt_details(self):
        channel = "/monitor/"

class ESPFactory:
    def __init__(self, ESP32=None):
        self._ESP32 = ESP32

    def connect_wifi(self):
        SSID, KEY = self._ESP32.wifi_details() # Load network SSID and KEY from ESP32 config
        station = network.WLAN(network.STA_IF) # Set to wifi mode
        station.active(True) # Set wifi active
        
        def attempt():
            station.connect(SSID, KEY)
            if station.isconnected() == True:
                print('Connected to', SSID)
                return True
            elif station.isconnected() == False:
                print('Did not connect, trying again in 10 seconds...')
                time.sleep(10)
                attempt()

    def test_mqtt(self):
        return True

esp1 = ESP32CONFIGA()