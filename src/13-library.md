# 库 - 编程的百宝箱

## 引言

想象一下,如果你有了一个魔法工具箱,里面有各种各样预先做好的工具:锤子、螺丝刀、扳手、电钻等。当你需要做事情的时候,不需要自己制造这些工具,直接从工具箱里拿来用就可以了!

Python的"库"(Library)就像这个魔法工具箱。里面装满了别人已经写好的、经过测试的代码,我们可以直接拿来使用,而不需要从零开始编写每一个功能。

### 给家长的小贴士

- **为什么需要库?** 就像我们不需要自己制造铅笔一样,编程也不需要从零开始写所有功能。库让编程变得高效和有趣。
- **本章目标** 让孩子了解库的概念,学会使用几个常用的库,并理解如何查找和学习新的库。
- **实践建议** 每个库都有趣味性强的例子,鼓励孩子亲手运行代码并修改参数,观察效果变化。

## 什么是库?

在Python中,库是一组相关功能的集合。有些库是Python自带的(标准库),有些需要额外安装(第三方库)。

### 使用库的基本步骤

使用库通常需要两个步骤:

1. **导入库** - 告诉Python我们要使用哪个库
2. **调用功能** - 使用库提供的函数或对象

```python
# 导入库
import random

# 使用库中的功能
print(random.randint(1, 100))
```

### 导入库的几种方式

```python
# 方式1: 导入整个库
import random
print(random.randint(1, 100))

# 方式2: 给库起一个简短的别名
import random as r
print(r.randint(1, 100))

# 方式3: 只导入库中的某个函数
from random import randint
print(randint(1, 100))

# 方式4: 导入库的所有内容(不推荐,容易造成名称冲突)
from random import *
print(randint(1, 100))
```

### 给家长的小贴士

- **导入方式的选择** 对于初学者,推荐使用方式1(导入整个库),因为这样代码可读性更好,能清楚知道每个函数来自哪个库。
- **命名冲突** 方式4容易导致函数名冲突,不建议孩子使用。

## 字符串操作库

虽然Python的字符串功能不需要额外导入,但这里我们系统地学习一些高级字符串操作,这些在处理文本时非常有用。

### 字符串查找

find()方法可以查找一个字符串在另一个字符串中的位置。

```python
text = input("请输入一些名字(用逗号分隔): ")

# 查找"jerry"的位置
position = text.find("jerry")

if position == -1:
    print("没有找到jerry")
else:
    print(f"在位置 {position} 找到了jerry")
```

**运行示例:**
```
请输入一些名字(用逗号分隔): tom,jerry,mike
在位置 4 找到了jerry
```

### 判断字符串是否包含

使用`in`关键字判断一个字符串是否包含另一个字符串。

```python
text = input("请输入一些名字(用逗号分隔): ")

if "jerry" in text:
    print("jerry在名字列表中")
else:
    print("jerry不在名字列表中")
```

### 字符串替换

replace()方法可以将字符串中的某些内容替换成其他内容。

```python
text = input("请输入一些文字: ")
print("替换前:", text)

# 将"jerry"替换成"JERRY"
new_text = text.replace("jerry", "JERRY")
print("替换后:", new_text)
```

**运行示例:**
```
请输入一些文字: hello jerry, how are you jerry?
替换前: hello jerry, how are you jerry?
替换后: hello JERRY, how are you JERRY?
```

### 字符串分割

split()方法可以将字符串按照指定的分隔符分割成列表。

```python
text = input("请输入一些名字(用逗号分隔): ")
names = text.split(",")

print(f"共有 {len(names)} 个名字:")
for name in names:
    print(f"- {name}")
```

**运行示例:**
```
请输入一些名字(用逗号分隔): tom,jerry,mike,amy
共有 4 个名字:
- tom
- jerry
- mike
- amy
```

### 综合练习:名字处理程序

```python
# 综合使用字符串操作
text = input("请输入一些名字(用逗号分隔): ")

# 1. 检查是否包含某个名字
if "jerry" in text:
    print("✓ 名单中包含jerry")
    # 2. 替换名字的大小写
    text = text.replace("jerry", "JERRY")
    print("✓ 已将jerry改为JERRY")
else:
    print("✗ 名单中不包含jerry")

# 3. 分割字符串
names = text.split(",")
print(f"\n共有 {len(names)} 个名字:")
for i, name in enumerate(names, 1):
    print(f"{i}. {name}")
```

**运行示例:**
```
请输入一些名字(用逗号分隔): tom,jerry,mike,jerry,amy
✓ 名单中包含jerry
✓ 已将jerry改为JERRY

共有 5 个名字:
1. tom
2. JERRY
3. mike
4. JERRY
5. amy
```

### 给家长的小贴士

- **位置从0开始** find()返回的位置是从0开始计数的,这是编程的惯例。
- **-1的含义** find()找不到时返回-1,而不是0,因为0也是一个有效的位置。
- **常见错误** 孩子容易忘记split()的结果是列表,需要用循环来处理。

### 练习1

<details>
<summary>练习1: 文本统计器</summary>

编写一个程序,输入一段文字,统计并显示:
1. 文字的长度
2. 包含多少个"Python"(不区分大小写)
3. 将所有的"Python"替换为"🐍"

**提示:** 使用len()、lower()、replace()函数

</details>

## Random库 - 生成随机数

Random库可以帮我们生成随机数,这对于制作游戏、模拟实验等都很有用。

### 生成随机整数

randint(a, b)函数可以生成a到b之间的随机整数(包含a和b)。

```python
import random

# 生成1到100之间的随机数
secret_number = random.randint(1, 100)
print(f"神秘数字是: {secret_number}")

# 生成1到6之间的随机数(模拟掷骰子)
dice = random.randint(1, 6)
print(f"骰子点数: {dice}")

# 生成1到10之间的随机数
lucky = random.randint(1, 10)
print(f"幸运数字: {lucky}")
```

**运行示例:**
```
神秘数字是: 73
骰子点数: 4
幸运数字: 7
```

### 从列表中随机选择

choice()函数可以从一个列表中随机选择一个元素。

```python
import random

fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]

# 随机选择一个水果
fruit = random.choice(fruits)
print(f"今天吃: {fruit}")

# 随机选择3次
print("\n幸运抽奖:")
for i in range(3):
    prize = random.choice(fruits)
    print(f"第{i+1}次: {prize}")
```

**运行示例:**
```
今天吃: 葡萄

幸运抽奖:
第1次: 西瓜
第2次: 苹果
第3次: 橙子
```

### 打乱列表顺序

shuffle()函数可以随机打乱列表中元素的顺序。

```python
import random

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

print("原始顺序:", cards)

# 打乱顺序
random.shuffle(cards)
print("打乱后:", cards)

# 再次打乱
random.shuffle(cards)
print("再次打乱:", cards)
```

### 综合练习:猜数字游戏

```python
import random

# 电脑随机生成一个1-100的数字
secret = random.randint(1, 100)
attempts = 0

print("=== 猜数字游戏 ===")
print("我已经想好了一个1到100之间的数字,你能在几次内猜中?")

while True:
    guess = int(input("请输入你的猜测(1-100): "))
    attempts += 1

    if guess == secret:
        print(f"🎉 恭喜你!第{attempts}次猜对了!")
        break
    elif guess < secret:
        print("太小了,再大一点!")
    else:
        print("太大了,再小一点!")
```

### 给家长的小贴士

- **随机数的概念** 向孩子解释"随机"意味着每次运行结果可能不同,就像掷骰子一样。
- **游戏化学习** 猜数字游戏是练习循环和条件的绝佳例子,孩子会很有兴趣。
- **调试技巧** 可以让孩子打印出secret_number,先理解程序逻辑,再玩正式游戏。

### 练习2

<details>
<summary>练习2: 石头剪刀布游戏</summary>

编写一个石头剪刀布游戏:
1. 电脑随机选择(石头、剪刀、布)
2. 玩家输入选择
3. 比较并显示结果

**提示:** 用random.choice()和if-elif语句

<details>
<summary>参考答案</summary>

```python
import random

options = ["石头", "剪刀", "布"]

while True:
    # 电脑随机选择
    computer = random.choice(options)

    # 玩家选择
    player = input("请选择(石头/剪刀/布)或输入q退出: ")
    if player == "q":
        break

    if player not in options:
        print("无效的选择!")
        continue

    print(f"电脑出: {computer}")
    print(f"你出: {player}")

    # 判断胜负
    if player == computer:
        print("平局!")
    elif (player == "石头" and computer == "剪刀") or \
         (player == "剪刀" and computer == "布") or \
         (player == "布" and computer == "石头"):
        print("你赢了! 🎉")
    else:
        print("电脑赢了! 😢")
    print()
```

</details>
</details>

## Time库 - 时间和计时

Time库让我们能够处理时间相关的操作,比如暂停程序、计时、获取当前时间等。

### 暂停程序

sleep()函数可以让程序暂停指定的秒数。

```python
import time

print("开始倒计时!")
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("发射! 🚀")

print("\n模拟下载文件...")
for i in range(1, 6):
    print(f"下载中... {i*20}%")
    time.sleep(0.5)
print("下载完成!")
```

### 获取当前时间

time()函数返回当前时间的时间戳(从1970年1月1日开始的秒数)。

```python
import time

# 获取当前时间戳
current_time = time.time()
print(f"当前时间戳: {current_time}")

# 转换为可读格式
readable_time = time.ctime(current_time)
print(f"可读时间: {readable_time}")
```

**运行示例:**
```
当前时间戳: 1736871234.5678901
可读时间: Mon Jan 15 14:32:14 2025
```

### 计时器

perf_counter()函数可以用来精确计时,常用于测量程序运行时间。

```python
import time

# 开始计时
start = time.perf_counter()

# 模拟一些工作
print("开始计算...")
sum_result = 0
for i in range(1, 100000001):
    sum_result += i

# 结束计时
end = time.perf_counter()

# 计算耗时
elapsed = end - start
print(f"1到1亿求和结果: {sum_result}")
print(f"耗时: {elapsed:.2f}秒")
```

**运行示例:**
```
开始计算...
1到1亿求和结果: 5000000050000000
耗时: 4.23秒
```

### 综合练习:速度测试游戏

```python
import time
import random

print("=== 打字速度测试 ===")
print("我会显示一个随机单词,你需要尽快输入它!")

words = ["python", "computer", "programming", "keyboard", "mouse", "screen"]
word = random.choice(words)

print(f"\n请输入: {word}")

# 开始计时
start = time.perf_counter()

user_input = input()

# 结束计时
end = time.perf_counter()
elapsed = end - start

if user_input == word:
    print(f"✓ 正确!耗时: {elapsed:.2f}秒")
    if elapsed < 1:
        print("速度: ⚡⚡⚡ 超级快!")
    elif elapsed < 2:
        print("速度: ⚡⚡ 很快!")
    elif elapsed < 3:
        print("速度: ⚡ 还可以!")
    else:
        print("速度: 🐢 需要练习哦!")
else:
    print("✗ 输入错误!")
```

### 给家长的小贴士

- **时间戳的概念** 向孩子解释时间戳就像给每一刻都编了一个号码,方便计算机计算时间差。
- **暂停的作用** sleep()不只是暂停,还可以用于控制程序的节奏,让孩子观察到程序的执行过程。
- **实际应用** 计时功能可以用于测试程序效率,让孩子理解"优化"的概念。

### 练习3

<details>
<summary>练习3: 反应时间测试</summary>

编写一个测试反应时间的程序:
1. 程序随机等待2-5秒
2. 显示"现在按回车键!"
3. 计算用户按回车键的反应时间

**提示:** 用random.randint()和time.perf_counter()

<details>
<summary>参考答案</summary>

```python
import time
import random

print("=== 反应时间测试 ===")
print("当你看到'现在按回车键!'时,尽快按回车!")
input("准备好了吗?按回车开始...")

# 随机等待2-5秒
wait_time = random.randint(2, 5)
time.sleep(wait_time)

# 记录开始时间
start = time.perf_counter()

# 等待用户按下回车
input("现在按回车键!")

# 记录结束时间
end = time.perf_counter()

# 计算反应时间
reaction = end - start
print(f"\n你的反应时间: {reaction:.3f}秒")

if reaction < 0.3:
    print("神一般的反应! ⚡⚡⚡")
elif reaction < 0.5:
    print("很快! ⚡⚡")
elif reaction < 0.7:
    print("正常水平 ⚡")
else:
    print("有点慢...再接再厉! 🐢")
```

</details>
</details>

## Turtle库 - 图形绘制(复习与扩展)

我们在第6章已经学习了Turtle库的基础,这里我们复习并学习一些高级功能。

### 填充颜色

begin_fill()和end_fill()函数可以让 turtle填充封闭图形的颜色。

```python
import turtle

t = turtle.Turtle()
t.speed(1)

# 设置画笔颜色和填充颜色
# color()可以同时设置两个颜色
t.color("red", "yellow")  # 画笔红色,填充黄色

# 开始填充
t.begin_fill()

# 画一个五角星
for _ in range(5):
    t.forward(200)
    t.right(144)

# 结束填充
t.end_fill()

turtle.mainloop()
```

### 复杂图形: 多角星

```python
import turtle

t = turtle.Turtle()
t.speed(0)

# 画一个50角星
t.color("red", "yellow")
t.begin_fill()

for _ in range(50):
    t.forward(200)
    t.left(170)  # 每次转170度

t.end_fill()

turtle.mainloop()
```

### 在画布上写字

write()函数可以在画布上写字。

```python
import turtle
import time

t = turtle.Turtle()
t.speed(1)

# 设置画笔大小和颜色
t.pensize(5)
t.pencolor("yellow")
t.fillcolor("red")

# 画一个五边形
t.begin_fill()
for _ in range(5):
    t.forward(200)
    t.right(144)
t.end_fill()

# 等待2秒
time.sleep(2)

# 抬起画笔,移动到指定位置
t.penup()
t.goto(-150, -120)

# 设置颜色并写字
t.color("violet")
t.write("Done!", font=('Arial', 40, 'normal'))

turtle.mainloop()
```

### 综合练习: 彩虹五角星

```python
import turtle

t = turtle.Turtle()
t.speed(0)

# 定义彩虹颜色
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# 画多个五角星
for i in range(36):
    t.color(colors[i % 6])  # 循环使用颜色
    t.begin_fill()

    for _ in range(5):
        t.forward(100)
        t.right(144)

    t.end_fill()
    t.right(10)  # 每次旋转10度

turtle.mainloop()
```

### 给家长的小贴士

- **复习与巩固** 这个部分是对第6章内容的复习,如果孩子已经很熟悉,可以快速跳过。
- **颜色循环** `colors[i % 6]`这个表达式是一个重要的技巧,向孩子解释取余运算的作用。
- **创意扩展** 鼓励孩子修改参数(角度、步长、颜色),创造自己的图形艺术。

### 练习4

<details>
<summary>练习4: 花朵图案</summary>

使用Turtle画一朵花:
1. 画多个花瓣(用椭圆或曲线)
2. 每个花瓣旋转一定角度
3. 中心填充黄色,花瓣用粉色

<details>
<summary>参考答案</summary>

```python
import turtle

t = turtle.Turtle()
t.speed(0)

# 画花瓣
for _ in range(12):
    t.color("pink", "pink")
    t.begin_fill()

    # 画一个椭圆花瓣
    for _ in range(2):
        t.circle(50, 90)
        t.circle(10, 90)

    t.end_fill()
    t.right(30)  # 旋转30度

# 画花心
t.penup()
t.goto(0, -20)
t.pendown()
t.color("yellow", "yellow")
t.begin_fill()
t.circle(20)
t.end_fill()

turtle.mainloop()
```

</details>
</details>

## Pyttsx3库 - 文字转语音

Pyttsx3是一个第三方库,可以让电脑"说话",把文字转换成语音。这是一个非常有趣的库!

### 安装Pyttsx3

在使用之前,需要先安装这个库。打开终端(或命令提示符),输入:

```bash
pip3 install pyttsx3
```

### 基本使用

```python
import pyttsx3

# 创建语音引擎
engine = pyttsx3.init()

# 说话
engine.say("Hello World!")
engine.say("你好,我是电脑语音助手!")

# 运行并等待说完
engine.runAndWait()
```

### 设置语速

getProperty()和setProperty()可以获取和设置语音引擎的各种属性。

```python
import pyttsx3

engine = pyttsx3.init()

# 获取当前语速
rate = engine.getProperty('rate')
print(f"当前语速: {rate}")

# 设置新的语速(正常约200,可以设置为125表示慢速)
engine.setProperty('rate', 125)

engine.say("我现在说话的速度变慢了")
engine.runAndWait()
```

### 设置音量

```python
import pyttsx3

engine = pyttsx3.init()

# 获取当前音量(0.0到1.0)
volume = engine.getProperty('volume')
print(f"当前音量: {volume}")

# 设置音量为最大
engine.setProperty('volume', 1.0)

engine.say("我的音量现在是最大的!")
engine.runAndWait()
```

### 设置声音

```python
import pyttsx3

engine = pyttsx3.init()

# 获取可用的声音
voices = engine.getProperty('voices')

print(f"共有 {len(voices)} 种声音:")
for i, voice in voices:
    print(f"声音{i}: {voice.name}")

# 选择声音(voices[0]通常是男声,voices[1]是女声)
engine.setProperty('voice', voices[0].id)  # 男声
# engine.setProperty('voice', voices[1].id)  # 女声

engine.say("你好,我是男声助手")
engine.runAndWait()
```

### 综合练习: 语音计算器

```python
import pyttsx3

engine = pyttsx3.init()

# 设置语速和音量
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

print("=== 语音计算器 ===")
print("输入两个数字,我会用语音告诉你计算结果")

num1 = float(input("第一个数字: "))
num2 = float(input("第二个数字: "))

result = num1 + num2

# 显示结果
print(f"{num1} + {num2} = {result}")

# 语音播报
engine.say(f"{num1}加{num2}等于{result}")
engine.runAndWait()
```

### 给家长的小贴士

- **安装说明** 安装第三方库可能需要一些时间,如果遇到问题,可以检查网络连接或尝试使用国内镜像源。
- **语音功能** 语音功能对孩子很有吸引力,可以用来制作讲故事程序、语音助手等。
- **调试技巧** 如果语音不正常,可以先测试简单程序,再逐步添加功能。

### 练习5

<details>
<summary>练习5: 语音讲故事</summary>

编写一个语音讲故事程序:
1. 预设几个短故事
2. 让用户选择听哪个故事
3. 用语音朗读故事
4. 可以切换男女声

<details>
<summary>参考答案</summary>

```python
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

stories = {
    "1": """
    从前有一只小兔子,它非常爱吃胡萝卜。有一天,它在森林里发现了一片胡萝卜地,
    高兴得跳了起来!它邀请了好朋友小熊一起分享,它们吃得饱饱的,成了最好的朋友。
    """,
    "2": """
    小明过生日那天,爸爸妈妈送给他一台机器人。这个机器人会说话,会跳舞,
    还会帮小明做作业!小明开心极了,每天都和机器人一起学习玩耍。
    """,
    "3": """
    在大海深处,住着一只小美人鱼。她喜欢听海面上的故事,喜欢唱歌。
    有一天,她救了一位王子,并和他成为了好朋友。从此以后,他们一起保护海洋环境。
    """
}

print("=== 语音故事机 ===")
print("1. 小兔子的胡萝卜")
print("2. 小明的机器人")
print("3. 小美人鱼")
print("4. 退出")

while True:
    choice = input("\n请选择故事(1-4): ")

    if choice == "4":
        print("再见!")
        break

    if choice in stories:
        voice_type = input("选择声音(1=男声, 2=女声): ")

        voices = engine.getProperty('voices')
        if voice_type == "1":
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)

        print("\n开始讲故事...\n")
        engine.say(stories[choice])
        engine.runAndWait()
    else:
        print("无效的选择!")
```

</details>
</details>

## 文件操作库

文件操作让我们可以读取和保存数据,这样程序关闭后数据不会丢失。

### 打开和读取文件

open()函数用于打开文件,"r"表示只读模式。

```python
# 打开文件
f = open("story.txt", "r")

# 读取全部内容
content = f.read()
print("文件内容:")
print(content)

# 关闭文件
f.close()
```

### 写入文件

"w"表示写入模式(会覆盖原有内容),"a"表示追加模式(在末尾添加)。

```python
# 写入模式(覆盖)
f = open("diary.txt", "w")
f.write("2025年1月15日 天气: 晴\n")
f.write("今天我学会了Python的文件操作!\n")
f.close()

# 追加模式
f = open("diary.txt", "a")
f.write("感觉很有成就感! 😊\n")
f.close()

# 读取并显示
f = open("diary.txt", "r")
print(f.read())
f.close()
```

### 修改文件

```python
# 打开文件进行读写("r+")
f = open("note.txt", "r+")

# 读取内容
content = f.read()
print("原始内容:")
print(content)

# 移动到文件开头
f.seek(0)

# 清空文件
f.truncate()

# 写入新内容
f.write("更新后的内容\n")
f.write("这是一行新文字\n")

# 关闭文件
f.close()

# 再次读取验证
f = open("note.txt", "r")
print("\n更新后内容:")
print(f.read())
f.close()
```

### 逐行读取

```python
# 打开文件
f = open("students.txt", "r")

# 逐行读取
print("=== 学生名单 ===")
line_number = 1
for line in f:
    # 去除行尾的换行符
    name = line.strip()
    print(f"{line_number}. {name}")
    line_number += 1

f.close()
```

### 给家长的小贴士

- **文件路径** 默认情况下,文件会在当前目录创建。可以教孩子使用绝对路径。
- **文件编码** 如果遇到中文乱码,可以在open()时指定`encoding="utf-8"`。
- **关闭文件** 强调f.close()的重要性,就像用完水龙头要关水一样。

### 练习6

<details>
<summary>练习6: 成绩记录本</summary>

编写一个成绩记录程序:
1. 可以输入科目和成绩
2. 保存到文件
3. 可以查看所有历史记录

<details>
<summary>参考答案</summary>

```python
print("=== 成绩记录本 ===")

while True:
    print("\n1. 记录成绩")
    print("2. 查看历史")
    print("3. 退出")

    choice = input("请选择(1-3): ")

    if choice == "1":
        subject = input("科目: ")
        score = input("成绩: ")

        # 追加到文件
        f = open("scores.txt", "a")
        f.write(f"{subject}: {score}\n")
        f.close()
        print("✓ 已保存!")

    elif choice == "2":
        try:
            f = open("scores.txt", "r")
            print("\n=== 历史成绩 ===")
            print(f.read())
            f.close()
        except FileNotFoundError:
            print("还没有任何记录!")

    elif choice == "3":
        break
```

</details>
</details>

## JSON库 - 数据交换格式

JSON是一种常用的数据格式,Python的json库可以读写JSON文件。

### 什么是JSON

JSON(JavaScript Object Notation)是一种轻量级的数据交换格式,易于人阅读和编写,同时也易于机器解析和生成。

```json
{
    "name": "小明",
    "age": 10,
    "hobbies": ["篮球", "编程", "音乐"]
}
```

### 读取JSON文件

```python
import json

# 读取JSON文件
f = open("student.json", "r")
student = json.load(f)
f.close()

# 使用数据
print(f"姓名: {student['name']}")
print(f"年龄: {student['age']}")
print("爱好:")
for hobby in student['hobbies']:
    print(f"  - {hobby}")
```

### 写入JSON文件

```python
import json

# 准备数据
student = {
    "name": "小红",
    "age": 11,
    "grade": "五年级",
    "hobbies": ["画画", "跳舞", "阅读"]
}

# 写入JSON文件
f = open("student.json", "w")
# indent=2 表示缩进2个空格,让格式更美观
json.dump(student, f, indent=2, ensure_ascii=False)
f.close()

print("JSON文件已创建!")
```

### 修改JSON文件

```python
import json

# 读取JSON文件
f = open("data.json", "r+")
data = json.load(f)

# 修改数据
data['age'] = 12
data['hobbies'].append("游泳")

# 移动到文件开头
f.seek(0)

# 清空文件
f.truncate()

# 写入修改后的数据
json.dump(data, f, indent=2, ensure_ascii=False)
f.close()

print("数据已更新!")
```

### 综合练习: 个人信息管理

```python
import json
import os

filename = "my_info.json"

# 检查文件是否存在
if os.path.exists(filename):
    f = open(filename, "r")
    info = json.load(f)
    f.close()
    print("找到已有信息!")
else:
    info = {}
    print("创建新档案...")

while True:
    print("\n=== 个人信息管理 ===")
    print("1. 查看信息")
    print("2. 修改姓名")
    print("3. 添加爱好")
    print("4. 保存并退出")

    choice = input("请选择(1-4): ")

    if choice == "1":
        print("\n当前信息:")
        for key, value in info.items():
            print(f"{key}: {value}")

    elif choice == "2":
        name = input("请输入姓名: ")
        info['name'] = name
        print("✓ 姓名已更新!")

    elif choice == "3":
        hobby = input("请输入新爱好: ")
        if 'hobbies' not in info:
            info['hobbies'] = []
        info['hobbies'].append(hobby)
        print("✓ 爱好已添加!")

    elif choice == "4":
        f = open(filename, "w")
        json.dump(info, f, indent=2, ensure_ascii=False)
        f.close()
        print("✓ 信息已保存!再见!")
        break
```

### 给家长的小贴士

- **JSON的优势** JSON格式易读、通用,很多网站和API都使用JSON格式交换数据。
- **ensure_ascii=False** 这个参数让中文字符正常显示,而不是显示成Unicode编码。
- **应用场景** 可以用JSON保存游戏进度、配置文件等。

### 练习7

<details>
<summary>练习7: 游戏存档系统</summary>

编写一个简单的游戏存档系统:
1. 保存玩家名字、等级、分数
2. 可以读取存档
3. 可以查看多个存档

<details>
<summary>参考答案</summary>

```python
import json
import os

save_file = "game_saves.json"

def load_saves():
    if os.path.exists(save_file):
        f = open(save_file, "r")
        saves = json.load(f)
        f.close()
        return saves
    else:
        return {}

def save_game(saves, name, level, score):
    saves[name] = {
        "level": level,
        "score": score
    }
    f = open(save_file, "w")
    json.dump(saves, f, indent=2)
    f.close()

saves = load_saves()

while True:
    print("\n=== 游戏存档系统 ===")
    print("1. 创建/更新存档")
    print("2. 读取存档")
    print("3. 查看所有存档")
    print("4. 退出")

    choice = input("请选择(1-4): ")

    if choice == "1":
        name = input("玩家名字: ")
        level = int(input("等级: "))
        score = int(input("分数: "))
        save_game(saves, name, level, score)
        print("✓ 存档已保存!")

    elif choice == "2":
        name = input("要读取的存档名: ")
        if name in saves:
            print(f"\n玩家: {name}")
            print(f"等级: {saves[name]['level']}")
            print(f"分数: {saves[name]['score']}")
        else:
            print("未找到该存档!")

    elif choice == "3":
        if saves:
            print("\n=== 所有存档 ===")
            for name, data in saves.items():
                print(f"{name}: 等级{data['level']}, 分数{data['score']}")
        else:
            print("还没有任何存档!")

    elif choice == "4":
        break
```

</details>
</details>

## 自己开发库

我们不仅可以使用别人写的库,还可以自己创建库!把常用的功能打包成库,可以让代码更简洁、更易维护。

### 创建自己的库

创建一个名为`my_tools.py`的文件:

```python
# my_tools.py - 我的工具库

def calculate_rectangle_area(length, width):
    """计算长方形面积"""
    return length * width

def calculate_rectangle_perimeter(length, width):
    """计算长方形周长"""
    return 2 * (length + width)

def say_hello(name):
    """打招呼函数"""
    return f"你好, {name}!"

def get_grade(score):
    """根据分数返回等级"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
```

### 使用自己的库

在另一个程序中导入并使用:

```python
# main.py
import my_tools

# 使用库中的函数
length = 10
width = 5

area = my_tools.calculate_rectangle_area(length, width)
perimeter = my_tools.calculate_rectangle_perimeter(length, width)

print(f"长方形面积: {area}")
print(f"长方形周长: {perimeter}")

# 问候
greeting = my_tools.say_hello("小明")
print(greeting)

# 成绩等级
score = 85
grade = my_tools.get_grade(score)
print(f"分数{score}对应的等级是: {grade}")
```

### 综合练习: 图形工具库

创建一个`drawing_tools.py`文件:

```python
# drawing_tools.py - 绘图工具库
import turtle

def draw_square(t, size):
    """画正方形"""
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_triangle(t, size):
    """画三角形"""
    for _ in range(3):
        t.forward(size)
        t.right(120)

def draw_polygon(t, sides, size):
    """画多边形"""
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)

def draw_star(t, size, points):
    """画星星"""
    angle = 180 - (180 / points)
    for _ in range(points):
        t.forward(size)
        t.right(angle)
```

使用这个库:

```python
import turtle
import drawing_tools

t = turtle.Turtle()
t.speed(0)

# 使用库中的函数画图
drawing_tools.draw_square(t, 100)
t.penup()
t.goto(150, 0)
t.pendown()

drawing_tools.draw_triangle(t, 100)
t.penup()
t.goto(-150, 0)
t.pendown()

drawing_tools.draw_polygon(t, 6, 80)  # 六边形
t.penup()
t.goto(0, -150)
t.pendown()

drawing_tools.draw_star(t, 100, 5)  # 五角星

turtle.mainloop()
```

### 给家长的小贴士

- **模块化思维** 教孩子把常用的功能整理成库,培养模块化的思维。
- **文件组织** 建议创建一个专门的文件夹存放自定义库。
- **文档注释** 在函数中使用三引号注释,说明函数的用途。

### 练习8

<details>
<summary>练习8: 语音工具库</summary>

创建一个语音工具库`speech_tools.py`,包含以下函数:
1. speak_text(text) - 读出文字
2. speak_number(number) - 读出数字
3. speak_list(items) - 读出列表中的每一项

然后编写一个程序使用这个库。

<details>
<summary>参考答案</summary>

speech_tools.py:
```python
import pyttsx3

def speak_text(text):
    """读出文字"""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def speak_number(number):
    """读出数字"""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(f"数字是 {number}")
    engine.runAndWait()

def speak_list(items):
    """读出列表中的每一项"""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)

    for item in items:
        engine.say(item)
        engine.runAndWait()
```

使用示例:
```python
import speech_tools

# 读文字
speech_tools.speak_text("你好,欢迎使用语音工具库")

# 读数字
speech_tools.speak_number(42)

# 读列表
fruits = ["苹果", "香蕉", "橙子"]
speech_tools.speak_list(fruits)
```

</details>
</details>

## 自学库 - 探索更多可能

Python有海量的第三方库,我们可以根据需要学习使用新的库。

### 如何查找和安装库

1. **查找库** 访问 https://pypi.org 搜索需要的库
2. **安装库** 使用`pip3 install 库名`安装
3. **学习使用** 阅读库的文档和示例代码

### 实践挑战: 音乐播放器

这里给你一个挑战:自己找一个可以播放音乐的Python库,学习它的接口,编写一个简单的音乐播放器。

**推荐库:**
- pygame - 强大的多媒体库
- playsound - 简单的音频播放
- pydub - 音频处理库

**示例步骤:**
1. 使用`pip3 install pygame`安装
2. 在网上搜索"pygame music player example"
3. 学习基本的播放功能
4. 编写自己的播放器程序

### 给家长的小贴士

- **自学能力** 学会查找和使用新库是重要的编程技能。
- **文档阅读** 教孩子如何阅读库的文档,找到需要的函数。
- **试错精神** 鼓励孩子多尝试,不怕犯错,从错误中学习。

## 常见错误和调试

### 错误1: ModuleNotFoundError

```python
import nonexistent_module
```

**错误信息:** `ModuleNotFoundError: No module named 'nonexistent_module'`

**原因:** 库不存在或未安装

**解决方法:**
- 检查库名是否拼写正确
- 使用`pip3 install 库名`安装库

### 错误2: 导入路径错误

```python
import my_tools  # 假设my_tools.py不在当前目录
```

**错误信息:** `ModuleNotFoundError: No module named 'my_tools'`

**原因:** Python找不到自定义库文件

**解决方法:**
- 确保库文件和程序在同一目录
- 或将库文件放在Python能找到的目录中

### 错误3: 文件未关闭

```python
f = open("data.txt", "r")
content = f.read()
# 忘记 f.close()
```

**问题:** 文件可能被锁定,其他程序无法访问

**解决方法:** 使用`with`语句自动关闭文件

```python
with open("data.txt", "r") as f:
    content = f.read()
# 文件会自动关闭
```

### 调试技巧

1. **打印导入的库**
```python
import random
print(random)  # 检查是否成功导入
```

2. **查看库的内容**
```python
import random
print(dir(random))  # 查看库中的所有函数
```

3. **查看函数帮助**
```python
import random
help(random.randint)  # 查看函数说明
```

## 章节小结

### 核心知识点回顾

1. **库的概念** - 库是预先写好的代码集合,可以直接使用
2. **导入库** - 使用`import`语句导入库
3. **常用库** - 学习了random、time、turtle、pyttsx3、json等库
4. **文件操作** - 读取和写入文件
5. **自定义库** - 可以自己创建库
6. **自学新库** - 查找、安装、学习使用新库

### 能力检查表

完成本章学习后,你应该能够:
- [ ] 理解库的概念和作用
- [ ] 正确导入和使用库
- [ ] 使用random库生成随机数
- [ ] 使用time库进行计时和暂停
- [ ] 使用turtle库绘制图形
- [ ] 使用pyttsx3库进行语音播报
- [ ] 进行基本的文件操作
- [ ] 读写JSON文件
- [ ] 创建和使用自定义库

### 下一章预告

本章我们学习了如何使用各种库来扩展程序的功能。下一章,我们将综合运用所学知识,开发一个**命令行程序**,实现一个实用的课表查询系统!

### 挑战练习

1. **抽奖系统** 使用random库创建一个抽奖系统,可以输入参与者名单,随机抽取幸运儿。

2. **语音闹钟** 结合time和pyttsx3库,创建一个定时播报提醒的程序。

3. **图形计算器** 使用turtle库创建一个图形化的计算器界面。

4. **数据管理器** 使用JSON文件创建一个个人数据管理系统,可以增删改查数据。

5. **创意项目** 自学一个新的Python库,用它创建一个有趣的项目!
