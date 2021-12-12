import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

led = 12

GPIO.setup(led, GPIO.OUT)
GPIO.output(led, True)
time.sleep(2)
GPIO.output(led, False)


