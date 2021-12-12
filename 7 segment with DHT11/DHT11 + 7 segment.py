import RPi.GPIO as GPIO
import time
from time import sleep
import datetime
import dht11


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#location + numbers on BOARD
top = 23
topRight = 7
bottomRight = 16
bottom = 24
bottomLeft = 26
topLeft = 19
middle = 12
dot = 22
 
# GPIO ports for the 7seg pins
segments =  (top,topRight,bottomRight,bottom,bottomLeft,topLeft,middle,dot)
 
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 1)

one = 15
two = 13
three = 11
four = 18

# GPIO ports for the digit 0-3 pins 
digits = (one,two,three,four)
 
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)



 
num = {' ':(1,1,1,1,1,1,1),
    '0':(0,0,0,0,0,0,1),
    '1':(1,0,0,1,1,1,1),
    '2':(0,0,1,0,0,1,0),
    '3':(0,0,0,0,1,1,0),
    '4':(1,0,0,1,1,0,0),
    '5':(0,1,0,0,1,0,0),
    '6':(0,1,0,0,0,0,0),
    '7':(0,0,0,1,1,1,1),
    '8':(0,0,0,0,0,0,0),
    '9':(0,0,0,0,1,0,0)}
    
led = 12
button = 11
temp = 13
led2 = 15

GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(led,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)

instance = dht11.DHT11(pin=temp)

turnedON=True
GPIO.output(led,False)
GPIO.output(led2,True)


while(1):
    result = instance.read()
    if GPIO.input(button)==0: 
        if(turnedON == True):
            print ('LED = ON')
            GPIO.output(led,False)
            GPIO.output(led2,True)
            turnedON=False
            sleep(0.5)
        else:
            print ('LED = OFF')
            GPIO.output(led,True)
            GPIO.output(led2,False)
            turnedON=True
            sleep(0.5)

    if (turnedON == False):       
        if result.is_valid():
            print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)
    
    

    



    
        
            
        

