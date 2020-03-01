# 库

## random

```python
import random

print(random.randint(1, 100))
```

- 猜数游戏

## time

```python
import time

time.sleep(2) # unit: second

time.time()  # 1523271396.4514377
time.ctime() # 'Mon Apr  9 19:00:25 2018'

time.perf_counter() # twice, end - start, elapse second
```

## turtle

```python
import turtle
import time
 
# 同时设置pencolor=color1, fillcolor=color2
turtle.color("red", "yellow")
 
turtle.begin_fill()
for _ in range(50):
turtle.forward(200)
turtle.left(170)
turtle.end_fill()

turtle.mainloop()
```

```python

import turtle
import time
 
turtle.pensize(5)
turtle.pencolor("yellow")
turtle.fillcolor("red")
 
turtle.begin_fill()
for _ in range(5):
  turtle.forward(200)
  turtle.right(144)
turtle.end_fill()
time.sleep(2)
 
turtle.penup()
turtle.goto(-150,-120)
turtle.color("violet")
turtle.write("Done", font=('Arial', 40, 'normal'))
 
turtle.mainloop()
```

## Pyttsx

```sh
pip3 install pyttsx3
```

```python
import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()
```

