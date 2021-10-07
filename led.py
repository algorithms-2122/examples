class Led:
    def __init__(self, pin):
        self.__isOn = False
        self.__pin = pin

    def on(self):
        self.__isOn = True
        return self.__isOn

    def off(self):
        self.__isOn = False
        return self.__isOn

    def toggle(self):
        self.__isOn = not self.__isOn
        return self.__isOn

    def getState(self):
        return self.__isOn

led = Led(1)
print(led.getState())
print(led.on())
print(led.toggle())
otherLed = Led(2)
print(otherLed.getState())
