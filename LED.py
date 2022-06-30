from machine import Pin
import time


class Led:
    # private attributes
    __pin_number = 0
    __blink_frequency = 0.0

    # constructor
    def __init__(self, pin_number, blink_frequency):
        self.__pin_number = pin_number
        self.__blink_frequency = blink_frequency

    def turn_on(self):
        led = Pin(self.__pin_number, Pin.OUT)
        led(1)

    def turn_off(self):
        led = Pin(self.__pin_number, Pin.OUT, )
        led(0)

    def blink(self):
        while True:
            led = Pin(self.__pin_number, Pin.OUT)
            led(self.__blink_frequency)
            time.sleep(1)
            led(0)
            time.sleep(1)
