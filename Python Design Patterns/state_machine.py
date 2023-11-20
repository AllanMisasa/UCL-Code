# Example of light bulb class that is a simple state machine

class LightBulb:
    _state = 'OFF'    # initial state of bulb
  
    def onOff(self, switch):
        if switch == 'ON':
            self._state = 'ON'
        elif switch == 'OFF':
            self._state = 'OFF'
        else:
            pass          # if we get wrong input

