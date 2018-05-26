import sys
print(sys.path)
import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIGsag=23
TRIGsol=22
ECHOsag=24
ECHOsol=27


print "HC-SR04 mesafe sensoru"

GPIO.setup(TRIGsag,GPIO.OUT)
GPIO.setup(ECHOsag,GPIO.IN)
GPIO.setup(TRIGsol,GPIO.OUT)
GPIO.setup(ECHOsol,GPIO.IN)


sayilar="12"
for sayac in sayilar:
 if(int(sayac)==1):
  print "1. sensor"
  GPIO.output(TRIGsag,False)
  print  "Olculuyor..."
  time.sleep(2)
  
  GPIO.output(TRIGsag,True)
  time.sleep(0.00001)
  GPIO. output(TRIGsag,False)
  
  while GPIO.input(ECHOsag)==0:
   pulse_start = time.time()
   
  while GPIO.input(ECHOsag)==1:
   pulse_end = time.time()
   
  pulse_duration = pulse_end - pulse_start
  
  distance = pulse_duration * 17150
  distance = round(distance, 2)
  
  if distance > 2 and distance < 400:
   print "Mesafe:",distance - 0.5,"cm"
  else:
   print "Menzil asildi"
 GPIO.output(TRIGsag,True)


 
 if(int(sayac)==2):
  print "2. sensor"
  GPIO.output(TRIGsol,False)
  print  "Olculuyor..."
  time.sleep(2)
  
  GPIO.output(TRIGsol,True)
  time.sleep(0.00001)
  GPIO. output(TRIGsol,False)
  
  while GPIO.input(ECHOsol)==0:
   pulse_start = time.time() 
   
   
  while GPIO.input(ECHOsol)==1:
   pulse_end = time.time() 
   
  pulse_duration = pulse_end - pulse_start
  
  distance = pulse_duration * 17150
  distance = round(distance, 2)
  
  if distance > 2 and distance < 400:
   print "Mesafe:",distance - 0.5,"cm"
  else:
   print "Menzil asildi"
  GPIO.output(TRIGsol,True)






