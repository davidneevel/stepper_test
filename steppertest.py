from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)



stepDelay = .000001


stepPin = 38
dirPin = 40

GPIO.setup(stepPin,GPIO.OUT)
GPIO.setup(dirPin,GPIO.OUT)

GPIO.output(dirPin, GPIO.LOW)

for x in range(5000):
    GPIO.output(stepPin, GPIO.HIGH)
    sleep(stepDelay)
    
    GPIO.output(stepPin, GPIO.LOW)
    sleep(stepDelay)

GPIO.output(dirPin, GPIO.HIGH)

for x in range(5000):
    GPIO.output(stepPin, GPIO.HIGH)
    sleep(stepDelay)
    
    GPIO.output(stepPin, GPIO.LOW)
    sleep(stepDelay)
