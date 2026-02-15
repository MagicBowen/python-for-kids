# 库 - 编程的百宝箱 🎁

## 引言

想象一下,如果你玩乐高积木时,每个零件都要自己亲手制造,那该多累啊!幸运的是,乐高公司已经为你准备好了成千上万种积木零件:车轮、窗户、门、人偶等。你只需要从零件盒里拿出需要的零件,就能拼搭出城堡、汽车、飞机等各种各样的作品!

Python的"库"(Library)就像这个乐高零件盒。里面装满了别人已经写好的、经过测试的代码,我们可以直接拿来使用,而不需要从零开始编写每一个功能。这正是编程的精髓之一:**站在巨人的肩膀上**,用更少的代码做更多的事情!

### 给家长的小贴士 💡

- **为什么需要库?** 就像我们不需要自己制造铅笔、橡皮一样,编程也不需要从零开始写所有功能。库让编程变得高效、有趣且专业化。
- **本章目标** 让孩子了解库的概念,学会使用几个常用的库,并理解如何查找和学习新的库。
- **编程思想** 通过学习库,培养孩子的"代码复用"思维——理解为什么重复造轮子是低效的,而善用已有工具是聪明的做法。
- **实践建议** 每个库都有趣味性强的例子,鼓励孩子亲手运行代码并修改参数,观察效果变化。

## 什么是库?

在Python中,库是一组相关功能的集合。有些库是Python自带的(标准库),有些需要额外安装(第三方库)。

### 生活类比:工具箱的智慧 🔧

库的概念在生活中随处可见:

- **工具箱** → 里面有锤子、螺丝刀、扳手等,你不需要自己制造这些工具
- **材料包** → 做手工时,纸、胶水、剪刀等材料都准备好了
- **乐高积木** → 各种预制的零件,可以直接拼搭作品
- **调料架** → 做菜时,盐、糖、酱油等调料都已准备好

**编程中的库也是一样的道理!** 别人已经把常用功能写好了,我们只需要"导入"就能使用。

```python
# 这就像从工具箱里拿出"随机数生成器"这个工具
import random

# 然后直接使用它
number = random.randint(1, 100)
```

### 编程思想:代码复用 ♻️

在编程中,有一个重要的原则叫做**DRY**(Don't Repeat Yourself,不要重复自己)。库就是这个原则的最佳实践:

- **避免重复劳动** → 不用每次都写相同的功能
- **提高效率** → 把时间花在创造新功能上
- **减少错误** → 使用经过测试的代码,比自己写更可靠
- **便于维护** → 库会持续更新和改进

### 给家长的小贴士 💡

- **模块化思维** 库体现了"模块化"的编程思想——把复杂问题分解成可复用的小模块。这种思维方式不仅能应用于编程,也能应用于解决日常问题。
- **分工协作** 现实中的大型软件是由成百上千的程序员协作开发的,每个人负责不同的模块(库),最后组合成完整的系统。这就像建造大厦,不同工种的人负责不同的工作。
- **教学建议** 可以和孩子讨论生活中的"复用"例子,比如:预制菜、模板、复印等,帮助孩子理解"复用"的价值。

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
# 方式1: 导入整个库(推荐给初学者)
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

### 给家长的小贴士 💡

- **导入方式的选择** 对于初学者,推荐使用方式1(导入整个库),因为这样代码可读性更好,能清楚知道每个函数来自哪个库。
- **命名冲突** 方式4容易导致函数名冲突,不建议孩子使用。举例说明:如果两个库都有叫`read()`的函数,就会产生混淆。
- **可读性优先** 在学习阶段,代码清晰易懂比简洁更重要。鼓励孩子写出容易理解的代码。

## 库与计算机系统的关系 💻

### 系统库 vs 第三方库

Python的库可以分为两大类:

#### 1. 标准库(系统库)

这些是Python自带的库,安装Python后就可以直接使用:

- **random** - 生成随机数
- **time** - 时间和计时
- **json** - JSON数据格式
- **math** - 数学函数(正弦、余弦、平方根等)
- **os** - 操作系统功能(文件、目录等)

**类比**: 就像手机出厂时预装的应用程序(计算器、日历、时钟等)。

#### 2. 第三方库

这些是由社区开发者编写的库,需要额外安装:

- **pyttsx3** - 文字转语音
- **pygame** - 游戏开发
- **turtle** - 图形绘制(有些Python发行版自带)
- **pandas** - 数据分析
- **requests** - 网络请求

**类比**: 就像从应用商店下载的额外应用程序(游戏、社交软件等)。

### 库与计算机硬件的协作

当我们使用库时,实际上是在指挥计算机的各个部件协同工作:

```
┌─────────────────────────────────────┐
│         你的程序                    │
│  import random                     │
│  number = random.randint(1, 100)   │
└────────────┬────────────────────────┘
             │ 调用
             ↓
┌─────────────────────────────────────┐
│      Random库(代码)                 │
│  包含生成随机数的算法                │
└────────────┬────────────────────────┘
             │ 使用
             ↓
┌─────────┬───┴────┬─────────┬───────┐
│   CPU   │  内存  │   时钟   │ 系统时间│
│ 执行算法│ 存储数据│ 提供种子│ 随机源 │
└─────────┴────────┴─────────┴───────┘
```

**给家长的小贴士 💡**

- **"随机"的本质** 可以告诉孩子,计算机中的"随机数"其实不是真正随机的,而是根据一个"种子"(通常是当前时间)通过数学公式计算出来的。这就像"如果知道种子,就能预测结果",所以叫"伪随机数"。
- **硬件协作** 每个库的函数最终都会转换成CPU指令,指挥硬件工作。让孩子理解"代码→CPU指令→硬件执行"这个流程。
- **系统资源** 有些库会消耗系统资源(内存、CPU时间),比如图形库需要显卡支持。这是很好的"成本意识"教育机会。

### 库的"生态系统" 🌿

Python有庞大的库生态系统,这得益于:

- **开源社区** → 全世界的程序员共同贡献代码
- **包管理工具** → pip工具让安装库变得简单
- **文档和教程** → 每个库都有详细的使用说明
- **持续更新** → 库会不断改进和修复bug

这就像一个巨大的"工具共享社区",每个人都可以使用别人的工具,也可以贡献自己的工具!

### 给家长的小贴士 💡

- **开源精神** 可以向孩子介绍"开源"的概念——代码共享、互相帮助、共同进步。这是现代软件行业的重要文化。
- **社区协作** 大型项目通常由世界各地的人协作开发,通过互联网共享代码。这能培养孩子的全球视野和协作意识。
- **学习资源** 教会孩子如何搜索和利用社区资源(文档、论坛、教程)是重要的自学能力。

## Random库 - 生成随机数 🎲

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

### 数学练习:概率实验 📊

我们可以用random库来做数学中的概率实验!

```python
import random

print("=== 抛硬币实验 ===")
heads = 0  # 正面次数
tails = 0  # 反面次数
total = 1000  # 抛1000次

for i in range(total):
    # 随机选择0或1,0代表正面,1代表反面
    result = random.randint(0, 1)
    if result == 0:
        heads += 1
    else:
        tails += 1

print(f"抛硬币{total}次的结果:")
print(f"正面(0): {heads}次, 比例: {heads/total*100:.1f}%")
print(f"反面(1): {tails}次, 比例: {tails/total*100:.1f}%")
print(f"\n理论上,正面和反面应该各占50%")
print(f"实验结果与理论的差异: {abs(heads - tails)/total*100:.1f}%")
```

**运行示例:**
```
=== 抛硬币实验 ===
抛硬币1000次的结果:
正面(0): 503次, 比例: 50.3%
反面(1): 497次, 比例: 49.7%

理论上,正面和反面应该各占50%
实验结果与理论的差异: 0.6%
```

**给家长的小贴士 💡**

- **概率与统计** 这个实验很好地展示了"大数定律":当试验次数足够多时,实验结果会趋近于理论概率。
- **数学联系** 可以和孩子讨论:为什么是1000次而不是10次?实验次数越多,结果越接近50%。
- **扩展思考** 可以让孩子修改程序,尝试掷骰子实验,看看每个数字出现的概率是否接近1/6。

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

### 给家长的小贴士 💡

- **随机数的概念** 向孩子解释"随机"意味着每次运行结果可能不同,就像掷骰子一样。
- **游戏化学习** 猜数字游戏是练习循环和条件的绝佳例子,孩子会很有兴趣。
- **调试技巧** 可以让孩子打印出secret_number,先理解程序逻辑,再玩正式游戏。

### 练习1

<details>
<summary>练习1: 石头剪刀布游戏</summary>

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

## Time库 - 时间和计时 ⏰

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

### 数学联系:时间计算 🧮

时间计算是很好的数学练习!

```python
import time

# 记录开始时间
start = time.time()

# 做一些计算(比如计算1到10000的和)
total = 0
for i in range(1, 10001):
    total += i

# 记录结束时间
end = time.time()

# 计算耗时
elapsed = end - start

print(f"1到10000的和: {total}")
print(f"计算耗时: {elapsed:.6f}秒")

# 数学问题:如果计算1到100000的和,需要多久?
print("\n让我们试试计算1到100000的和...")

start = time.time()
total = 0
for i in range(1, 100001):
    total += i
end = time.time()

elapsed = end - start
print(f"计算耗时: {elapsed:.6f}秒")

# 思考题:耗时增加了大约多少倍?
print("\n思考:计算量增加了10倍,耗时增加了多少倍?")
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

# 数学问题:CPU每秒能执行多少次加法?
operations = 100000000 / elapsed
print(f"\nCPU每秒大约执行了 {operations:.0f} 次加法运算")
```

**运行示例:**
```
开始计算...
1到1亿求和结果: 5000000050000000
耗时: 4.23秒

CPU每秒大约执行了 23640662 次加法运算
```

### 给家长的小贴士 💡

- **CPU性能概念** 通过计时,让孩子理解CPU的速度——每秒能执行几千万次简单运算!这能培养对计算机性能的直观认识。
- **时间戳的概念** 向孩子解释时间戳就像给每一刻都编了一个号码,方便计算机计算时间差。
- **实际应用** 计时功能可以用于测试程序效率,让孩子理解"优化"的概念——同样的功能,代码写得更好,运行更快。

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

### 练习2

<details>
<summary>练习2: 反应时间测试</summary>

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

## Turtle库 - 图形绘制(复习与扩展) 🐢

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

### 数学练习:多角星的几何计算 📐

画多角星需要计算角度,这是很好的几何练习!

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

**数学思考题:**
- 如果画n角星,每次应该转多少度?
- 提示:360度 × (n-2) / n 是正n边形的内角
- 星形的角度是:180 - (360 / n)

### 几何知识复习

```python
import turtle

def draw_polygon(t, sides, size):
    """画正多边形"""
    # 计算外角
    angle = 360 / sides
    print(f"画{sides}边形,每次转{angle}度")

    for _ in range(sides):
        t.forward(size)
        t.right(angle)

t = turtle.Turtle()
t.speed(1)

# 画各种多边形
draw_polygon(t, 3, 100)  # 三角形
t.penup()
t.goto(150, 0)
t.pendown()

draw_polygon(t, 4, 100)  # 正方形
t.penup()
t.goto(-150, 0)
t.pendown()

draw_polygon(t, 5, 100)  # 五边形
t.penup()
t.goto(0, -150)
t.pendown()

draw_polygon(t, 6, 100)  # 六边形
t.penup()
t.goto(0, 150)
t.pendown()

draw_polygon(t, 8, 80)   # 八边形

turtle.mainloop()
```

**给家长的小贴士 💡**

- **几何与编程** 这是将编程与数学几何完美结合的例子!鼓励孩子计算不同多边形的角度。
- **数学公式复习**:
  - 三角形内角和 = 180度
  - 四边形内角和 = 360度
  - n边形内角和 = (n-2) × 180度
  - 正n边形每个外角 = 360度 / n
- **探索精神** 鼓励孩子尝试不同的参数,观察图形的变化,这是科学探索的精神!

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

### 给家长的小贴士 💡

- **复习与巩固** 这个部分是对第6章内容的复习,如果孩子已经很熟悉,可以快速跳过。
- **颜色循环** `colors[i % 6]`这个表达式是一个重要的技巧,向孩子解释取余运算的作用。
- **创意扩展** 鼓励孩子修改参数(角度、步长、颜色),创造自己的图形艺术。

### 练习3

<details>
<summary>练习3: 花朵图案</summary>

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

## 文件操作库 - 数据的持久化 💾

文件操作让我们可以读取和保存数据,这样程序关闭后数据不会丢失。

### 为什么需要文件?

想象一下,如果你写的日记每次合上本子后,字迹就消失了,那该多糟糕!文件就是计算机的"日记本",让数据可以永久保存。

```python
# 没有文件:数据在内存中,程序关闭就丢失
score = 100  # 程序关闭后,这个数据就不见了

# 有了文件:数据保存在硬盘上,程序关闭后数据还在
f = open("score.txt", "w")
f.write("100")
f.close()
# 即使关闭程序,数据仍然保存在文件中
```

### 文件与计算机硬件 🖥️

```
┌─────────────────────────────────────┐
│         你的程序                    │
│  读取/保存数据                       │
└────────────┬────────────────────────┘
             │
             ↓
┌─────────────────────────────────────┐
│         文件系统                     │
│  管理文件的存储和组织                │
└────────────┬────────────────────────┘
             │
             ↓
┌─────────────────────────────────────┐
│          硬盘存储                   │
│  永久保存数据(磁道、扇区)             │
└─────────────────────────────────────┘
```

**给家长的小贴士 💡**

- **内存 vs 硬盘** 可以这样解释:
  - **内存** = 书桌 → 工作时放东西,速度快但断电后数据消失
  - **硬盘** = 文件柜 → 长期存储,速度慢但断电后数据还在
- **持久化** 向孩子解释"持久化"就是"让数据长期保存"的意思。
- **文件编码** 简单提一下文件是用0和1存储的,不同的编码方式(如UTF-8)决定如何表示字符。

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

### 数学应用:成绩统计 📊

```python
# 假设我们有一个成绩文件
# 创建示例文件
f = open("scores.txt", "w")
f.write("85\n")
f.write("92\n")
f.write("78\n")
f.write("95\n")
f.write("88\n")
f.close()

# 读取并统计
f = open("scores.txt", "r")
scores = []

for line in f:
    score = int(line.strip())
    scores.append(score)

f.close()

# 计算统计数据
total = sum(scores)
count = len(scores)
average = total / count
highest = max(scores)
lowest = min(scores)

print(f"成绩统计:")
print(f"总人数: {count}")
print(f"总分: {total}")
print(f"平均分: {average:.1f}")
print(f"最高分: {highest}")
print(f"最低分: {lowest}")
```

### 给家长的小贴士 💡

- **文件路径** 默认情况下,文件会在当前目录创建。可以教孩子使用绝对路径。
- **文件编码** 如果遇到中文乱码,可以在open()时指定`encoding="utf-8"`。
- **关闭文件** 强调f.close()的重要性,就像用完水龙头要关水一样。
- **更好的写法** 可以介绍`with`语句,它会自动关闭文件:

```python
# 推荐的写法:自动关闭文件
with open("data.txt", "r") as f:
    content = f.read()
# 文件会自动关闭,即使发生错误也是如此
```

### 练习4

<details>
<summary>练习4: 成绩记录本</summary>

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

## JSON库 - 数据交换格式 📋

JSON是一种常用的数据格式,Python的json库可以读写JSON文件。

### 什么是JSON?

JSON(JavaScript Object Notation)是一种轻量级的数据交换格式,易于人阅读和编写,同时也易于机器解析和生成。

```json
{
    "name": "小明",
    "age": 10,
    "hobbies": ["篮球", "编程", "音乐"]
}
```

**生活类比:**
- JSON就像**乐高组装说明书** → 用统一格式描述如何组装
- 就像**简历模板** → 用统一格式记录个人信息
- 就像**配置表** → 记录软件的各种设置

### JSON与数据结构 📊

JSON完美对应Python的数据结构:

```python
# Python字典 → JSON对象
person = {
    "name": "小明",
    "age": 10
}

# Python列表 → JSON数组
hobbies = ["篮球", "编程", "音乐"]

# Python字符串/数字/布尔值 → JSON对应类型
name = "小明"
age = 10
is_student = True
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

### 数学应用:成绩统计系统 📈

```python
import json

# 保存班级成绩
class_data = {
    "class_name": "五年级1班",
    "students": [
        {"name": "小明", "scores": {"数学": 95, "语文": 88, "英语": 92}},
        {"name": "小红", "scores": {"数学": 89, "语文": 95, "英语": 90}},
        {"name": "小刚", "scores": {"数学": 92, "语文": 85, "英语": 88}}
    ]
}

# 保存到文件
f = open("class_scores.json", "w", encoding="utf-8")
json.dump(class_data, f, indent=2, ensure_ascii=False)
f.close()

# 读取并统计
f = open("class_scores.json", "r", encoding="utf-8")
data = json.load(f)
f.close()

print(f"班级: {data['class_name']}")
print(f"学生人数: {len(data['students'])}")

# 计算班级平均分
math_total = 0
chinese_total = 0
english_total = 0

for student in data['students']:
    scores = student['scores']
    math_total += scores['数学']
    chinese_total += scores['语文']
    english_total += scores['英语']

count = len(data['students'])
print(f"\n班级平均分:")
print(f"数学: {math_total/count:.1f}")
print(f"语文: {chinese_total/count:.1f}")
print(f"英语: {english_total/count:.1f}")
```

### 给家长的小贴士 💡

- **JSON的优势** JSON格式易读、通用,很多网站和API都使用JSON格式交换数据。
- **ensure_ascii=False** 这个参数让中文字符正常显示,而不是显示成Unicode编码。
- **应用场景** 可以用JSON保存游戏进度、配置文件等。
- **数据结构映射** 这是一个很好的机会,向孩子展示现实中的数据如何用编程结构来表示。

### 练习5

<details>
<summary>练习5: 个人信息管理</summary>

编写一个个人信息管理系统:
1. 可以查看信息
2. 可以修改姓名
3. 可以添加爱好
4. 保存到JSON文件

<details>
<summary>参考答案</summary>

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

</details>
</details>

## 自己开发库 - 模块化编程 🧩

我们不仅可以使用别人写的库,还可以自己创建库!把常用的功能打包成库,可以让代码更简洁、更易维护。

### 为什么要自己写库?

**代码复用的思想**:

```python
# 没有库:每次都要重复写相同的代码
def calculate_rectangle_area(length, width):
    return length * width

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

# 在多个程序中重复复制这些代码... 😞

# 有了库:写一次,到处使用
import my_tools
area = my_tools.calculate_rectangle_area(10, 5)  # 😊
```

**好处**:
- ✅ 不用重复写代码
- ✅ 代码更简洁
- ✅ 更新时只改一个地方
- ✅ 可以分享给别人使用

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

### 数学工具库示例 🧮

创建一个`math_tools.py`文件:

```python
# math_tools.py - 数学工具库

def calculate_average(numbers):
    """计算平均数"""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    """计算中位数"""
    if len(numbers) == 0:
        return 0

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    middle = n // 2

    if n % 2 == 0:
        # 偶数个元素,取中间两个的平均值
        return (sorted_numbers[middle-1] + sorted_numbers[middle]) / 2
    else:
        # 奇数个元素,取中间的值
        return sorted_numbers[middle]

def is_prime(n):
    """判断是否为质数"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def calculate_factorial(n):
    """计算阶乘"""
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

使用这个数学工具库:

```python
import math_tools

# 测试平均数
scores = [85, 92, 78, 95, 88]
avg = math_tools.calculate_average(scores)
print(f"平均分: {avg}")

# 测试中位数
median = math_tools.calculate_median(scores)
print(f"中位数: {median}")

# 测试质数判断
print(f"17是质数吗? {math_tools.is_prime(17)}")
print(f"18是质数吗? {math_tools.is_prime(18)}")

# 测试阶乘
print(f"5的阶乘: {math_tools.calculate_factorial(5)}")
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

### 给家长的小贴士 💡

- **模块化思维** 教孩子把常用的功能整理成库,培养模块化的思维。
- **文件组织** 建议创建一个专门的文件夹存放自定义库。
- **文档注释** 在函数中使用三引号注释,说明函数的用途。
- **函数命名** 鼓励孩子使用清晰的函数名,让别人一看就知道函数是做什么的。
- **编程规范** 这是培养良好编程习惯的好机会,比如:
  - 一个函数只做一件事
  - 函数名要描述性
  - 添加注释说明

### 练习6

<details>
<summary>练习6: 语音工具库</summary>

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

## 自学库 - 探索更多可能 🔍

Python有海量的第三方库,我们可以根据需要学习使用新的库。

### 如何查找和安装库

1. **查找库** 访问 https://pypi.org 搜索需要的库
2. **安装库** 使用`pip3 install 库名`安装
3. **学习使用** 阅读库的文档和示例代码

### 学会阅读文档 📖

这是程序员最重要的技能之一!

**文档通常包含:**
- **安装说明** → 如何安装库
- **快速开始** → 最简单的使用示例
- **API参考** → 所有函数的详细说明
- **示例代码** → 完整的使用案例
- **常见问题** → FAQ

**阅读文档的技巧:**
1. 先看"快速开始",跑通最简单的例子
2. 再看示例代码,理解如何使用
3. 遇到问题时查API参考
4. 最后查看FAQ或搜索问题

### 给家长的小贴士 💡

- **自学能力** 学会查找和使用新库是重要的编程技能。
- **文档阅读** 教孩子如何阅读库的文档,找到需要的函数。
- **试错精神** 鼓励孩子多尝试,不怕犯错,从错误中学习。
- **搜索引擎** 教会孩子如何有效地搜索问题,比如:
  - "python 库名 教程"
  - "python 库名 example"
  - "python how to 使用某个功能"
- **社区资源** 介绍一些学习资源:
  - Stack Overflow - 问答社区
  - GitHub - 查看开源项目
  - B站/YouTube - 视频教程

### 实践挑战:探索新库

这里给你一个挑战:自己找一个可以播放音乐的Python库,学习它的接口,编写一个简单的音乐播放器。

**推荐库:**
- **pygame** - 强大的多媒体库
- **playsound** - 简单的音频播放
- **pydub** - 音频处理库

**示例步骤:**
1. 使用`pip3 install pygame`安装
2. 在网上搜索"pygame music player example"
3. 学习基本的播放功能
4. 编写自己的播放器程序

**学习过程记录:**
```
[ ] 1. 安装库
[ ] 2. 查看官方文档
[ ] 3. 运行示例代码
[ ] 4. 理解代码原理
[ ] 5. 修改和扩展功能
[ ] 6. 完成自己的项目
```

### 常见错误和调试 🔧

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

1. **库的概念** 🎁
   - 库是预先写好的代码集合,可以直接使用
   - 就像工具箱、乐高积木、材料包
   - 体现了"代码复用"和"模块化"的编程思想

2. **导入库** 📥
   - 使用`import`语句导入库
   - 有多种导入方式,推荐初学者使用`import 库名`

3. **常用库** 🛠️
   - random - 生成随机数
   - time - 时间和计时
   - turtle - 图形绘制
   - json - JSON数据格式

4. **文件操作** 💾
   - 读取和写入文件
   - 文件是数据的持久化存储
   - 理解内存和硬盘的区别

5. **库与计算机系统** 💻
   - 标准库 vs 第三方库
   - 库与硬件的协作关系
   - 开源社区和代码共享精神

6. **自定义库** 🧩
   - 可以自己创建库
   - 提高代码复用性
   - 培养模块化思维

7. **自学能力** 🔍
   - 如何查找和安装新库
   - 如何阅读文档
   - 从错误中学习

### 能力检查表 ✅

完成本章学习后,你应该能够:
- [ ] 理解库的概念和作用
- [ ] 正确导入和使用库
- [ ] 使用random库生成随机数
- [ ] 使用time库进行计时和暂停
- [ ] 使用turtle库绘制图形
- [ ] 进行基本的文件操作
- [ ] 读写JSON文件
- [ ] 创建和使用自定义库
- [ ] 理解库与计算机硬件的关系
- [ ] 会查找和学习新的库

### 编程思想总结 💡

通过学习库,我们掌握了重要的编程思想:

- **代码复用** → 不要重复造轮子,善用已有工具
- **模块化** → 把复杂问题分解成可复用的小模块
- **分工协作** → 大型项目由多人分工完成,各自负责不同的库
- **开源精神** → 代码共享,互相帮助,共同进步
- **持续学习** → 技术在不断进步,要学会查找和探索新工具

### 数学知识点回顾 📚

本章融入的数学知识:
- **概率统计** → 抛硬币实验、随机数分布
- **几何计算** → 多边形角度、图形绘制
- **数据分析** → 平均数、中位数、方差
- **时间计算** → 时间戳、时间差
- **函数概念** → 数学函数 vs 编程函数

### 计算机知识回顾 💻

本章融入的计算机知识:
- **内存 vs 硬盘** → 临时存储 vs 永久存储
- **文件系统** → 文件的组织和管理
- **CPU性能** → 通过计时理解运算速度
- **随机数原理** → 种子和伪随机数
- **开源生态** → 社区协作和代码共享

### 下一章预告 ➡️

本章我们学习了如何使用各种库来扩展程序的功能,理解了代码复用和模块化的重要思想。

下一章,我们将综合运用所学知识,开发一个**命令行程序**,实现一个实用的课表查询系统!我们将深入学习:
- 如何设计一个完整的程序
- 如何处理复杂的用户交互
- 如何组织和管理大量数据
- 文件系统在程序中的应用

### 挑战练习 🎯

1. **抽奖系统** 🎰
   使用random库创建一个抽奖系统,可以输入参与者名单,随机抽取幸运儿。
   - 提示:用列表存储名单,用random.choice()抽取

2. **语音闹钟** ⏰
   结合time和pyttsx3库,创建一个定时播报提醒的程序。
   - 提示:用time.sleep()等待,用pyttsx3播报

3. **图形计算器** 🖥️
   使用turtle库创建一个图形化的计算器界面。
   - 提示:用turtle画按钮,处理用户输入

4. **数据管理器** 📊
   使用JSON文件创建一个个人数据管理系统,可以增删改查数据。
   - 提示:用字典存储数据,用json.dump/load保存读取

5. **创意项目** ⭐
   自学一个新的Python库,用它创建一个有趣的项目!
   - 推荐方向:
     - ** Arcade** - 游戏开发库
     - ** Pillow** - 图像处理库
     - **requests** - 网络请求库
     - ** Beautiful Soup** - 网页爬虫库

---

**恭喜你完成了第13章的学习!** 🎉

你已经掌握了使用库这一重要技能,这会让你的编程之旅更加高效和有趣!继续保持好奇心和探索精神,下一章见! 👋
