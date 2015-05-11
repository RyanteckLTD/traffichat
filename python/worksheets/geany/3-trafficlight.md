<img src = "../../../logonobg.png"/>
#Beginners GPIO - 3
##Making a traffic light

In this worksheet we will be programming the TrafficHAT to act like an pelican crossing light.

**The sequemce is the following:**

1. Green light on
2. Wait for button press
3. Green light off
4. Yellow light on
5. Wait 2 seconds
6. Yellow light off
7. Red light on
9. Buzz the buzzer 10 times
10. Wait 1 second
11. Red light off
12. Blink the yellow light 4 times

And the sequence will be finished.

This tutorial will go through step by step on what to do to create this sequence.

###Setup
To begin we need to first setup our code very much like the previous lessons.

```python
#TrafficHAT
#Pelican Crossing Sequence

import RPi.GPIO as GPIO #This imports the RPi.GPIO Library as IO
import sys #This imports a library to handle errors.
from time import sleep # This imports only the sleep function from time.

#Next we need to setup the Raspberry Pi's GPIO Pins
GPIO.setmode(GPIO.BCM) #This sets the Pi to BCM / GPIO Numbering
```

To setup the outputs we are going to use a different method, first we are going to assign the   GPIO pins to variables.

```python
green = 22
yellow = 23
red = 24
button = 25
buzzer = 5
```
Now we have set the pin numbers to variables we're going to set all of the outputs up using an for loop.

The for loop will run the same code for each variable in the array we set the loop to iterate through.

To do this we use the following code.

```python
outputs = [green,yellow,red,buzzer]

for output in outputs:
    GPIO.setup(output,GPIO.OUT)
```

This will then run the loop and set the variable output to each element in the array as it iterates through them.

To setup the input we use the same code as before. As we only have one input to setup it is quicker to just do this once.

```python
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
```
And then to finish the setup we're going to add the surrounding code that we used before to handle errors and quit successfully.

Don't forget that each section should be indented as shown.

```python
try:
    while True:
        #The rest of the code goes in this loop here.

except KeyboardInterrupt:
    GPIO.cleanup()

except:
    print "Error:", sys.exc_info()[0]
    raise
```

###Build the program

Now the progam is all setup you should be able to build the code using the sequence as discribed at the top.

Here are the lines of code that you have used in the previous worksheets along with some new snippets.

####Controlling an output
```python
GPIO.output(GPIOVARIABLE, STATE)
```
Replace GPIOVARIABLE with the variable of the output you wish to control and STATE with either 1 or 0 for on or off.

####Wait until button is pressed.
```python
while(IO.input(GPIOVARIABLE)):
    pass
```
Replace GPIOVARIABLE with the variable of the button.
The pass command is used to do nothing while the button is not pressed.

####Repeat code
```python
i = 0
while(i<TIMES):
    #Code to repeat here
    i += 1
```
Replace times with the amount of times you wish the code to repeat and put the code you wish to repeat under the code to repeat here comment.

####Sleep / Delay
```python
sleep(seconds)
```
Replacing seconds with the amount of seconds you wish to wait.
