import RPi.GPIO as GPIO
import time
dcmot = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(dcmot, GPIO.OUT)
pwm = GPIO.PWM(dcmot, 100)
pwm.start(0)
try:
  while True:
    for dc in range(3.3,0):
      pwm.ChangeDutyCycle(dc)
      print(dc)
      time.sleep(0.5)
except KeyboardInterrupt:
  print("bye")
GPIO.cleanup()
