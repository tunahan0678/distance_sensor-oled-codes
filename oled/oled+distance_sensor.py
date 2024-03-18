from machine import Pin, SoftI2C
from hcsr04 import HCSR04
import ssd1306
from time import sleep


i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)



oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
    distance = sensor.distance_cm()
    oled.text(f'Distance: {distance} cm',0 ,0)
    sleep(0.2)
    oled.show()

        
oled.show() 
