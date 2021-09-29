# now on github!
import RPi.GPIO as GPIO # importing GPIO library
from time import sleep # import sleep

GPIO.setmode(GPIO.BCM) # define ports using BCM

green = 4 # green light
GPIO.setup(green, GPIO.OUT)
blue = 5 # blue light
GPIO.setup(blue, GPIO.OUT)
yellow = 21 # yellow light
GPIO.setup(yellow, GPIO.OUT)

button1, button2 = 12, 16
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)

pwm1 = GPIO.PWM(green, 100)
pwm2 = GPIO.PWM(blue, 100)

try:

  # Define a threaded callback function:
  def myCallback(button):
    print("Pushed button detected")
    if button == button1:
      pwm1.start(0) # initiate PWM at 0% duty cycle
      for dc in range(101): # loop duty cycle from 0 to 100
        pwm1.ChangeDutyCycle(dc) # set duty cycle
        sleep(0.005)
      for dc in range(100, -1, -1): # loop duty cycle from 0 to 100
        pwm1.ChangeDutyCycle(dc) # set duty cycle
        sleep(0.005)
      pwm1.stop()
    elif button == button2:
      pwm2.start(0) # initiate PWM at 0% duty cycle
      for dc in range(101): # loop duty cycle from 0 to 100
        pwm2.ChangeDutyCycle(dc) # set duty cycle
        sleep(0.005)
      for dc in range(100, -1, -1): # loop duty cycle from 0 to 100
        pwm2.ChangeDutyCycle(dc) # set duty cycle
        sleep(0.005)
      pwm2.stop()     

  # Execute myCallback() if port 1 goes HIGH:
  GPIO.add_event_detect(button1, GPIO.RISING, callback=myCallback, bouncetime=500)
  GPIO.add_event_detect(button2, GPIO.RISING, callback=myCallback, bouncetime=500)

  while True:
    GPIO.output(yellow,0)
    sleep(1)
    GPIO.output(yellow,1)
    sleep(1)
  
except KeyboardInterrupt: 
  print('\nExiting')
except Exception as e: # catch all other errors
  print('\n', e)

GPIO.cleanup()