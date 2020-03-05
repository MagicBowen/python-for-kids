import random
import pyttsx3

engine = pyttsx3.init()

def say(str):
    engine.say(str)
    engine.runAndWait()

 
target = random.randint(1,100)
count = 0


say("游戏开始！")
say("我想了一个1到100之间的数字，你猜猜是多少？")

while True:
    number = int(input())
    if number <= 0 or number > 100:
        say("别逗了，{0}不符合要求，请输入1到100之间的数字".format(number))
    elif number < target:
        say("不对哦，比{0}大一些，请再猜一次吧！".format(number))
    elif number > target:
        say("不对哦，比{0}小一些，请再猜一次吧！".format(number))
    else:
        say("哇哦，太棒了，你猜对了，就是{0}！".format(number))
        break
    count = count + 1

say("游戏结束啦，你一共猜了{0}次，希望下次更厉害哦！".format(count + 1))

engine.stop()
