# 输入与输出

## 引言

计算机程序就像一个神奇的魔法盒子，它可以接收你的输入（Input），经过处理后，再给你输出（Output）。这一章，我们要学习如何让计算机程序和你"对话"——接收你的指令和信息，然后把结果显示给你。

想象一下，你在玩一个电子游戏：
- **输入**：你按下键盘上的按钮、点击鼠标
- **输出**：屏幕上显示游戏画面、播放音乐、显示分数

我们写程序时，最常用的输入输出方式就是：
- **输入**：通过键盘输入文字或数字
- **输出**：在屏幕上显示文字或数字

## 输出

### 认识 print 函数

在Python中，让程序"说话"的方法叫做 `print`（打印）。`print` 可以把内容显示在屏幕上。

让我们试试看：

```python
print(5)
print("Jerry")  # 双引号中的是字符串，基本按照原样输出
print("Jerry, ", 10, " years old")  # 多个输出，用逗号隔开
print() # 输出空行
print(5 + 3) # 输出计算结果
```

**运行结果：**
```
5
Jerry
Jerry,  10  years old

8
```

**给家长的小贴士**：
- 这里的 `print` 是一个"函数"（function），现在孩子不用理解什么是函数，只需要知道它是一个工具，可以帮我们输出内容
- 双引号 `""` 中的内容叫做"字符串"（string），会原样输出
- 如果没有双引号，Python会把它当作数字或变量来处理
- `#` 后面的是注释，计算机不会执行，只是给人看的说明

### 实践：打印长方形信息

现在我们用 `print` 来展示一个长方形的信息：

```python
print("rectangle")
print("---------------")
print("length   : ", 5)
print("width    : ", 4)
print("area     : ", 5 * 4)
print("perimeter : ", (5 + 4) * 2)
```

**运行结果：**
```
rectangle
---------------
length   :  5
width    :  4
area     :  20
perimeter :  18
```

**想一想**：如果要计算宽为3的长方形，如何修改程序？

**答案**：你需要把所有 `4` 改成 `3`：
```python
print("rectangle")
print("---------------")
print("length   : ", 5)
print("width    : ", 3)  # 改这里
print("area     : ", 5 * 3)  # 改这里
print("perimeter : ", (5 + 3) * 2)  # 改这里
```

但是这样改来改去很麻烦，有没有更好的办法呢？

## 使用变量

### 什么是变量？

**变量**就像是贴了标签的盒子。

想象你的书桌上有很多盒子：
- 每个盒子上都贴着一个标签（名字）
- 你可以在盒子里放东西（值）
- 你可以随时打开盒子，看看里面是什么
- 你也可以随时换掉盒子里的东西

在Python中，我们用 `=` 来给变量"赋值"（给盒子装东西）：
- `=` 的左边是盒子的标签（变量名）
- `=` 的右边是要放进去的东西（值）

```python
l = 5  # 把数字5放进标签为"l"的盒子
w = 4  # 把数字4放进标签为"w"的盒子
```

### 用变量改进长方形程序

现在我们用变量来重写长方形程序：

```python
l = 5  # length（长度）的缩写
w = 4  # width（宽度）的缩写

print("rectangle")
print("---------------")
print("length   : ", l)
print("width    : ", w)
print("area     : ", l * w)
print("perimeter : ", (l + w) * 2)
```

现在，如果你想计算宽为3的长方形，只需要改一个地方：

```python
l = 5
w = 3  # 只需要改这里！

print("rectangle")
print("---------------")
print("length   : ", l)
print("width    : ", w)
print("area     : ", l * w)
print("perimeter : ", (l + w) * 2)
```

### 变量的命名规则

给变量起名字时，要遵守一些规则：

**✅ 可以用：**
- 英文字母（大小写都可以）
- 数字（但不能作为开头）
- 下划线 `_`

**❌ 不能用：**
- 数字开头（如 `1name`）
- 空格或特殊符号（如 `my-name`、`name@`）
- Python的关键字（如 `print`、`input` 等）

**好的变量名例子：**
```python
length = 5  # 用完整的英文单词
width = 4
l = 5  # 用有意义的缩写
w = 4
my_name = "Tom"  # 多个单词用下划线连接
```

**不好的变量名例子：**
```python
a = 5  # 看不出是什么意思
x1 = 5  # 没有意义
```

### 更改变量的值

变量盒子里面的东西可以随时更换：

```python
w = 4
print(w)  # 输出：4

w = 6
print(w)  # 输出：6

w = w + 1
print(w)  # 输出：7（解释：把w的值加1后重新放回w里）
```

**给家长的小贴士**：
- 孩子可能会对 `w = w + 1` 感到困惑，因为在数学中这是不成立的
- 在编程中，`=` 是"赋值"而不是"相等"
- 可以这样解释：把盒子w里的东西拿出来，加1后再放回去

### 练习1：正方形计算器

**任务**：参照上面的长方形程序，写一个计算正方形周长和面积的程序。

对于一个边长为3的正方形，要能输出如下：

```
square
----------------
side : 3
area : 9
perimeter : 12
```

**提示**：
- 正方形只需要一个变量 `side`（边长）
- 面积 = 边长 × 边长
- 周长 = 边长 × 4

<details>
<summary>点击查看答案</summary>

```python
side = 3

print("square")
print("---------------")
print("side : ", side)
print("area : ", side * side)
print("perimeter : ", side * 4)
```

</details>

## 输入

### 认识 input 函数

只有输出还不够，我们希望程序能和用户"对话"。Python中的 `input()` 函数可以让用户通过键盘输入信息。

让我们一步步学习：

#### 最简单的输入

```python
name = input()
print("Hi, ", name)
```

运行这段程序时：
1. 程序会停下来等待（你看不到任何提示）
2. 你输入名字（比如"Tom"）并按回车
3. 程序继续执行，输出 `Hi, Tom`

#### 添加提示信息

```python
print("What is your name?")
name = input()
print("Hi, ", name)
```

这样用户就知道该做什么了！

#### 更简洁的写法

我们可以把提示信息直接放在 `input()` 的括号里：

```python
name = input("What is your name?")
print("Hi, ", name)
```

**给家长的小贴士**：
- 括号里的文字叫做"参数"（parameter），现在孩子不需要理解这个词
- 可以这样解释：把提示信息"交给" input 函数，让它在等待输入时显示出来

#### 让输出更美观

我们可以在问候语前加一个空行：

```python
name = input("What is your name?")
print()  # 输出一个空行
print("Hi, ", name)
```

或者在提示语后加换行符 `\n`：

```python
name = input("What is your name?\n")  # \n 表示换行
print()
print("Hi, ", name)
```

**关于 `\n`**：
- `\n` 是一个特殊符号，表示"换行"（new line）
- `\` 叫做"转义符"，它让后面的 `n` 不再是字母n，而是代表换行

### 输入多个信息

现在我们让程序更聪明一点，询问用户的更多信息：

```python
name = input("What is your name?")
age = input("How old are you?")

print("Haha, you are ", name)
```

**运行示例：**
```
What is your name? Tom
How old are you? 10
Haha, you are  Tom
```

### 练习2：个人信息汇总

**任务**：写一个程序，询问用户的名字和年龄，然后输出一句话介绍他/她。

**期望输出：**
```
What is your name? Tom
How old are you? 10

Haha, you are Tom, you are 10 years old
```

<details>
<summary>点击查看答案</summary>

```python
name = input("What is your name?")
age = input("How old are you?")

print()
print("Haha, you are ", name, ", you are ", age, " years old")
```

</details>

### 更漂亮的输出方式

上面的输出会有很多空格，因为 `print()` 默认会在逗号 `,` 的位置加空格。Python 3.6+ 提供了一种更漂亮的输出方式，叫做 **f-string**（格式化字符串）：

```python
name = input("What is your name?")
age = input("How old are you?")

print(f"Haha, you are {name}, you are {age} years old")
```

**注意**：
- `print()` 前面的字母 `f` 不能忘记！
- `{name}` 和 `{age}` 会自动替换成变量的值
- 这种方式更灵活，你可以自由决定在哪里加空格

**给家长的小贴士**：
- f-string 是 Python 3.6 引入的新特性，现代Python代码推荐使用
- 可以这样解释：字母 f 告诉Python"这里有变量要替换"
- `{}` 就像是一个小窗口，透过它可以看到变量盒子里的内容

## 综合练习：交互式计算器

现在让我们把输入和输出结合起来，做一个真正的交互式程序！

### 练习3：长方形计算器（最终版）

**任务**：写一个程序，询问用户长方形的长和宽，然后输出面积和周长。

**期望输出示例：**
```
rectangle
---------------
length ? 5
width ? 4
area : 20
perimeter : 18
```

<details>
<summary>点击查看答案</summary>

```python
print("rectangle")
print("---------------")

l = int(input("length ? "))
w = int(input("width ? "))

print("area : ", l * w)
print("perimeter : ", (l + w) * 2)
```

**说明**：
- `int(input(...))` 先获取输入，再立即转换成数字
- 这样 `l` 和 `w` 就是数字类型，可以直接进行数学运算
- 关于 `int()` 的详细讲解在下一章

</details>

**给家长的小贴士**：
- 这里出现了一个新问题：`input()` 返回的是"字符串"，不能直接做数学运算
- `int()` 函数可以把字符串转换成数字（integer，整数）
- 这个知识点在第三章会详细讲解
- 如果孩子提出疑问，可以先简单解释：计算机把输入当作文字，需要告诉它"这是数字"

## 本章小结

恭喜你完成了这一章！你已经学会了：

1. **输出**：使用 `print()` 在屏幕上显示内容
2. **变量**：用标签盒子存储和改变数据
3. **输入**：使用 `input()` 获取用户输入
4. **f-string**：用 `{}` 和字母 `f` 美化输出

**重要概念**：
- 变量就像贴了标签的盒子
- `=` 是"赋值"，不是"相等"
- `input()` 得到的是字符串
- `print()` 可以输出多个内容，用逗号隔开

**下节预告**：下一章我们会详细学习"字符串"——文字在计算机中是如何存储和处理的。你会发现，文字也可以做很多有趣的操作！
