import time
from machine import Pin, I2C, Timer
def error(self):
    i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
    oled_width = 128
    oled_height = 64
    oled = SSD1306_I2C(oled_width, oled_height, i2c)
    y=0
    words="Error Unable to send data /n Press button to retry /n or wait 30 sec"
    while True:
    button.off()
    oled.text(words, 0, y, 1)
    oled.show()
    else:
        oled.fill(0)
        oled.show()
    time.sleep(0.05)
    return