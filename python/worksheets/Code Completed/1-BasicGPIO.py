#TrafficHAT - Blink LED
#By Your Name Here

import RPi.GPIO as IO
import sys
from time import sleep

try:
    while True:
        IO.output(green,1)
        
except KeyboardInterrupt:
    IO.cleanup()
        
except:
    print "Error:", sys.exc_info()[0]
    raise
    
