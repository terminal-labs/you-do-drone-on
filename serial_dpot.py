## MCP4131 docs: http://dlnmh9ip6v2uc.cloudfront.net/datasheets/Components/General%20IC/22060b.pdf
## some codes: http://electronics.stackexchange.com/questions/94479/digital-potentiometer-mcp4131-with-raspberry-pi

import sys
import time
import RPi.GPIO as GPIO

SPI_CS_PIN = 17
SPI_SDISDO_PIN = 22 # mosi
SPI_CLK_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(SPI_CS_PIN, GPIO.OUT)
GPIO.output(SPI_CS_PIN, False)
GPIO.setup(SPI_CLK_PIN, GPIO.OUT)
GPIO.setup(SPI_SDISDO_PIN, GPIO.OUT)

def set_value(value):
    b = '{0:016b}'.format(value)
    for x in range(0, 16):
        print 'x:' + str(x) + ' -> ' + str(b[x])
        GPIO.output(SPI_SDISDO_PIN, int(b[x]))

        GPIO.output(SPI_CLK_PIN, True)
        GPIO.output(SPI_CLK_PIN, False)
level = 0
try:
    while True:
        print 'level:' + str(level)
        set_value(level)
        level = int(raw_input('enter level\n'))
except KeyboardInterrupt:
    set_value(128)
    GPIO.cleanup()

# try:
#     while True:
#         for level in range(0, 256):
# #        for level in range(0, 40):
#             print 'level:' + str(level)
#             set_value(level)
#             time.sleep(0.25)

#         for level in range(255, -1, -1):
# #        for level in range(40, -1 , -1):
#             print 'level:' + str(level)
#             set_value(level)
#             time.sleep(0.25)
# except KeyboardInterrupt:
#     set_value(128)
#     GPIO.cleanup()
