# code modified, tweaked and tailored from code by bertwert 
# on RPi forum thread topic 91796
import RPi.GPIO as GPIO
import time
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
    


#GPIO.output(three, 0)



for loop in range(0,7):
    GPIO.output(segments[loop], num['7'][loop])
    


