# 循环语句

## 引言

在前面的章节中,我们学习了顺序语句和条件语句。顺序语句让程序按顺序执行,条件语句让程序根据不同情况做不同决定。

但是,如果需要**重复**做某些事情呢?

想象一下:
- 老师让你把"我要好好学习"这句话写100遍
- 你要帮妈妈数一共有多少颗糖果
- 计算从1加到100的和
- 画一个正方形,要画4条边

这些都需要**重复**执行相同的操作。在Python中,我们用**循环语句**来实现这种功能。

这一章,我们将学习:
- 什么是循环
- while循环(条件循环)
- for循环(计数循环)
- 循环嵌套(循环中的循环)
- break和continue(控制循环)
- 用循环解决实际问题

## 为什么需要循环

让我们先看一个例子:假设我们要打印5次"Python真有趣!"。

### 不用循环的方法

```python
print("Python真有趣!")
print("Python真有趣!")
print("Python真有趣!")
print("Python真有趣!")
print("Python真有趣!")
```

**问题**:
- 需要写很多重复的代码
- 如果要打印100次,会非常麻烦
- 代码容易出错,难以维护

### 用循环的方法

```python
# 用循环打印5次
count = 0
while count < 5:
    print("Python真有趣!")
    count = count + 1
```

**优势**:
- 代码简洁,只写一次
- 想打印多少次都可以,只需修改条件
- 容易维护和修改

> **给家长的小贴士**:
> - 用生活中的例子解释循环:绕操场跑圈、抄写生字、数数
> - 强调循环的好处:省时、省力、不容易出错
> - 可以让孩子想想生活中有哪些"重复"的事情

## while循环:条件循环

`while`循环是**条件循环**,只要条件为True,就一直重复执行代码块。

### while循环的基本语法

```python
while 条件:
    # 条件为True时重复执行的代码
    代码块
```

**语法要点**:
- `while`后面跟着一个条件(布尔表达式)
- 条件后面必须有冒号`:`
- 要执行的代码必须**缩进**
- 当条件为False时,循环结束

### 循环的三个重要元素

1. **初始值**: 循环变量的初始值
2. **条件**: 判断是否继续循环
3. **更新**: 循环变量如何变化

**示例模式**:
```python
# 1. 初始值
count = 0

# 2. 条件
while count < 5:
    print(f"第{count + 1}次: Python真有趣!")

    # 3. 更新循环变量
    count = count + 1

print("循环结束!")
```

**输出结果**:
```
第1次: Python真有趣!
第2次: Python真有趣!
第3次: Python真有趣!
第4次: Python真有趣!
第5次: Python真有趣!
循环结束!
```

> **给家长的小贴士**:
> - 重点讲解"循环变量更新"的重要性
> - 如果忘记更新,会变成"死循环"(无限循环)
> - 可以用"计数器"的概念来解释循环变量
> - 建议画出表格,记录每次循环时变量的值

### 示例1:打印数字

```python
# 打印1到5的数字
count = 1
while count <= 5:
    print(count)
    count = count + 1

print("打印完成!")
```

**输出结果**:
```
1
2
3
4
5
打印完成!
```

### 示例2:累加求和

```python
# 计算1到5的和
total = 0      # 累积变量,保存总和
count = 1      # 计数变量

while count <= 5:
    total = total + count  # 累加
    print(f"加{count}, 当前和:{total}")
    count = count + 1

print(f"1到5的和是:{total}")
```

**输出结果**:
```
加1, 当前和:1
加2, 当前和:3
加3, 当前和:6
加4, 当前和:10
加5, 当前和:15
1到5的和是:15
```

> **给家长的小贴士**:
> - 用"存钱罐"类比累积变量
> - 每次循环往存钱罐里加钱
> - 循环结束时,存钱罐里的钱就是总和
> - 强调初始值的重要性:total要从0开始

### 示例3:打印三角形*

```python
# 打印一个直角三角形
line = 1
while line <= 5:
    # 每行打印line个*
    print("*" * line)
    line = line + 1
```

**输出结果**:
```
*
**
***
****
*****
```

### 练习1:打印一棵圣诞树

**题目**:用while循环打印一棵圣诞树。

要求:
- 树冠:3层,每层*数量递增
- 树干:1层,用|表示

<details>
<summary>👉 点击查看答案</summary>

```python
# 打印圣诞树
# 树冠部分
line = 1
while line <= 3:
    # 打印空格(居中)
    spaces = " " * (3 - line)
    # 打印*
    stars = "*" * (2 * line - 1)
    print(spaces + stars)
    line = line + 1

# 树干部分
print("  |  ")  # 树干
print("  |  ")  # 树干
```

**输出结果**:
```
  *
 ***
*****
  |
  |
```

**简单版本**:
```python
# 简单的圣诞树
line = 1
while line <= 3:
    print("*" * line)
    line = line + 1
print("*")  # 树干
```
</details>

## while循环中嵌套条件

在循环中,我们可以结合条件语句,实现更复杂的逻辑。

### 示例1:打印偶数

```python
# 打印1到10中所有的偶数
count = 1
while count <= 10:
    # 判断是否为偶数
    if count % 2 == 0:
        print(f"{count}是偶数")
    count = count + 1

print("打印完成!")
```

**输出结果**:
```
2是偶数
4是偶数
6是偶数
8是偶数
10是偶数
打印完成!
```

### 示例2:标记特殊数字

```python
# 打印1到10,在3的倍数前加标记
count = 1
while count <= 10:
    # 判断是否为3的倍数
    if count % 3 == 0:
        print(f"[3的倍数] {count}")
    else:
        print(count)
    count = count + 1
```

**输出结果**:
```
1
2
[3的倍数] 3
4
5
[3的倍数] 6
7
8
[3的倍数] 9
10
```

### 示例3:统计奇数和偶数的和

```python
# 计算1到10之间偶数和奇数的和
even_sum = 0   # 偶数和
odd_sum = 0    # 奇数和
count = 1

while count <= 10:
    if count % 2 == 0:
        # 偶数加到even_sum
        even_sum = even_sum + count
        print(f"{count}是偶数, 偶数和:{even_sum}")
    else:
        # 奇数加到odd_sum
        odd_sum = odd_sum + count
        print(f"{count}是奇数, 奇数和:{odd_sum}")
    count = count + 1

print(f"\n偶数和:{even_sum}")
print(f"奇数和:{odd_sum}")
```

**输出结果**:
```
1是奇数, 奇数和:1
2是偶数, 偶数和:2
3是奇数, 奇数和:4
4是偶数, 偶数和:6
5是奇数, 奇数和:9
6是偶数, 偶数和:12
7是奇数, 奇数和:16
8是偶数, 偶数和:20
9是奇数, 奇数和:25
10是偶数, 偶数和:30

偶数和:30
奇数和:25
```

> **给家长的小贴士**:
> - 解释"累加器"的概念
> - 每个累加器都要有自己的初始值
> - 建议画图理解:两个篮子,分别装奇数和偶数
> - 强调print语句在循环中的调试作用

### 练习2:倒三角形

**题目**:用while循环打印倒三角形。

<details>
<summary>👉 点击查看答案</summary>

```python
# 打印倒三角形
line = 5
while line >= 1:
    print("*" * line)
    line = line - 1
```

**输出结果**:
```
*****
****
***
**
*
```
</details>

### 练习3:求能被3整除的数字的乘积

**题目**:计算1到10之间能被3整除的数字的乘积。

<details>
<summary>👉 点击查看答案</summary>

```python
# 计算1到10中能被3整除的数字的乘积
product = 1  # 乘积的初始值是1,不是0!
count = 1

while count <= 10:
    if count % 3 == 0:
        product = product * count
        print(f"乘{count}, 当前乘积:{product}")
    count = count + 1

print(f"乘积是:{product}")
```

**输出结果**:
```
乘3, 当前乘积:3
乘6, 当前乘积:18
乘9, 当前乘积:162
乘积是:162
```

> **重要提示**:
> - 乘积的初始值必须是1,不能是0!
> - 如果初始值是0,乘积永远是0
</details>

## for循环和range函数

`for`循环通常和`range()`函数一起使用,用于**已知循环次数**的情况。

### range函数

`range()`函数生成一个数字序列。

**基本用法**:
```python
# range(开始, 结束, 步长)
# 注意:结束值不包含在内!
```

**示例**:
```python
# range(5): 生成0, 1, 2, 3, 4
for i in range(5):
    print(i)

print("------")

# range(1, 6): 生成1, 2, 3, 4, 5
for i in range(1, 6):
    print(i)

print("------")

# range(1, 10, 2): 生成1, 3, 5, 7, 9 (奇数)
for i in range(1, 10, 2):
    print(i)

print("------")

# range(10, 0, -1): 生成10, 9, 8, 7, 6, 5, 4, 3, 2, 1 (倒数)
for i in range(10, 0, -1):
    print(i)
```

> **给家长的小贴士**:
> - 重点强调"结束值不包含"
> - range(1, 5)生成1, 2, 3, 4,不包括5
> - 用"排队"类比:从1号排到4号,5号不排
> - 步长可以是负数,实现倒序

### for循环的基本语法

```python
for 变量 in range(开始, 结束):
    # 循环体
```

### 示例1:打印数字

```python
# 用for循环打印1到5
for i in range(1, 6):
    print(i)

print("完成!")
```

**输出结果**:
```
1
2
3
4
5
完成!
```

### 示例2:求和

```python
# 用for循环计算1到5的和
total = 0
for i in range(1, 6):
    total = total + i
    print(f"加{i}, 当前和:{total}")

print(f"1到5的和是:{total}")
```

### 示例3:遍历字符串

```python
# 遍历字符串中的每个字符
name = "Python"
for ch in name:
    print(ch)
```

**输出结果**:
```
P
y
t
h
o
n
```

### while vs for:如何选择?

| 特点 | while循环 | for循环 |
|------|----------|---------|
| 使用场景 | 不知道循环次数 | 知道循环次数 |
| 循环条件 | 根据条件判断 | 遍历序列 |
| 需要手动 | 更新循环变量 | 自动更新变量 |
| 例子 | "直到用户输入正确" | "打印1到100" |

**示例对比**:

```python
# while循环版本
count = 1
while count <= 5:
    print(count)
    count = count + 1

print("------")

# for循环版本(更简洁!)
for i in range(1, 6):
    print(i)
```

> **给家长的小贴士**:
> - 如果知道循环次数,优先用for循环
> - for循环更简洁,不容易出错(自动更新变量)
> - while循环更灵活,适合复杂条件
> - 建议让孩子用两种方法写同一个程序,体会区别

## break和continue

在循环中,我们可以用`break`和`continue`来控制循环的执行。

### break:跳出循环

`break`会**立即终止**整个循环。

**示例**:
```python
# 找到第一个能被7整除的数
for i in range(1, 100):
    if i % 7 == 0:
        print(f"找到了!第一个能被7整除的数是:{i}")
        break  # 找到就退出循环

print("程序结束")
```

**输出结果**:
```
找到了!第一个能被7整除的数是:7
程序结束
```

### continue:跳过本次循环

`continue`会**跳过本次循环**,直接进入下一次循环。

**示例**:
```python
# 打印1到10中的奇数(跳过偶数)
for i in range(1, 11):
    if i % 2 == 0:
        continue  # 跳过偶数,不执行后面的print
    print(i)

print("打印完成")
```

**输出结果**:
```
1
3
5
7
9
打印完成
```

### 示例:累加直到和大于等于100

```python
# 计算1+2+3+...,直到和大于等于100
total = 0
count = 1

while True:  # 无限循环
    total = total + count
    print(f"加{count}, 当前和:{total}")

    if total >= 100:
        print(f"和达到{total}, 停止!")
        break  # 达到目标,退出循环

    count = count + 1
```

**输出结果**:
```
加1, 当前和:1
加2, 当前和:3
加3, 当前和:6
...
加13, 当前和:91
加14, 当前和:105
和达到105, 停止!
```

### 示例:QQ登录验证

```python
# 模拟QQ登录
correct_username = "admin"
correct_password = "123456"

while True:
    # 输入用户名和密码
    username = input("请输入用户名:")
    password = input("请输入密码:")

    # 验证
    if username == correct_username and password == correct_password:
        print("登录成功!")
        break  # 登录成功,退出循环
    else:
        print("用户名或密码错误,请重新输入!\n")

print("欢迎进入系统!")
```

> **给家长的小贴士**:
> - `break`就像"紧急出口",随时可以离开循环
> - `continue`就像"跳过",这次不做,继续下一次
> - `while True`是一个无限循环,必须有break才能退出
> - 强调滥用break和continue会让代码难以理解
> - 建议先用普通循环写法,熟练后再用这些控制语句

## 循环嵌套

一个循环内部可以再包含另一个循环,这就是**循环嵌套**。

### 示例1:打印数字矩形

```python
# 打印数字矩形
for i in range(1, 4):  # 外层循环:控制行
    for j in range(1, 4):  # 内层循环:控制列
        print(f"{i}", end=" ")  # end=" "表示不换行
    print()  # 每行结束后换行
```

**输出结果**:
```
1 1 1
2 2 2
3 3 3
```

### 示例2:打印乘法口诀表

```python
# 打印乘法口诀表(9x9)
for i in range(1, 10):  # 行:1到9
    for j in range(1, i + 1):  # 列:1到i
        result = i * j
        print(f"{j}x{i}={result}", end="\t")  # \t是制表符
    print()  # 换行
```

**输出结果**:
```
1x1=1
1x2=2	2x2=4
1x3=3	2x3=6	3x3=9
1x4=4	2x4=8	3x4=12	4x4=16
1x5=5	2x5=10	3x5=15	4x5=20	5x5=25
1x6=6	2x6=12	3x6=18	4x6=24	5x6=30	6x6=36
1x7=7	2x7=14	3x7=21	4x7=28	5x7=35	6x7=42	7x7=49
1x8=8	2x8=16	3x8=24	4x8=32	5x8=40	6x8=48	7x8=56	8x8=64
1x9=9	2x9=18	3x9=27	4x9=36	5x9=45	6x9=54	7x9=63	8x9=72	9x9=81
```

> **给家长的小贴士**:
> - 用"时钟"类比嵌套循环:时针和分针
> - 外层循环执行一次,内层循环执行完整一轮
> - 建议画出执行过程,理解嵌套逻辑
> - 强调缩进的重要性:内层循环要多缩进一层

### 示例3:找出所有三位数

**题目**:用1、2、3、4四个数字,能组成多少个三位数?

```python
# 用1、2、3、4组成三位数
count = 0  # 计数器

print("可以组成的三位数:")

for i in [1, 2, 3, 4]:  # 百位
    for j in [1, 2, 3, 4]:  # 十位
        for k in [1, 2, 3, 4]:  # 个位
            num = i * 100 + j * 10 + k
            print(num, end=" ")
            count = count + 1

            # 每行打印10个
            if count % 10 == 0:
                print()

print(f"\n总共可以组成{count}个三位数")
```

### 示例4:找出无重复数字的三位数

**题目**:用1、2、3、4四个数字,能组成多少个**无重复数字**的三位数?

```python
# 用1、2、3、4组成无重复数字的三位数
count = 0

print("无重复数字的三位数:")

for i in [1, 2, 3, 4]:  # 百位
    for j in [1, 2, 3, 4]:  # 十位
        if j == i:  # 十位和百位不能相同
            continue
        for k in [1, 2, 3, 4]:  # 个位
            if k == i or k == j:  # 个位不能和百位、十位相同
                continue
            num = i * 100 + j * 10 + k
            print(num, end=" ")
            count = count + 1

            # 每行打印10个
            if count % 10 == 0:
                print()

print(f"\n总共可以组成{count}个无重复数字的三位数")
```

**输出结果**:
```
无重复数字的三位数:
123 124 132 134 142 143 213 214 231 234
241 243 312 314 321 324 341 342 412 413
421 423 431 432
总共可以组成24个无重复数字的三位数
```

## 常见循环模式和技巧

### 模式1:计数器模式

```python
# 计数器:统计满足条件的数量
count = 0
for i in range(1, 101):
    if i % 7 == 0:
        count = count + 1

print(f"1到100之间有{count}个数能被7整除")
```

### 模式2:累加器模式

```python
# 累加器:求和
total = 0
for i in range(1, 101):
    total = total + i

print(f"1到100的和是:{total}")
```

### 模式3:累乘器模式

```python
# 累乘器:求阶乘(5! = 5x4x3x2x1)
factorial = 1
for i in range(1, 6):
    factorial = factorial * i

print(f"5的阶乘是:{factorial}")
```

### 模式4:最大值/最小值查找

```python
# 找最大值
numbers = [23, 45, 12, 67, 34, 89, 5]
max_num = numbers[0]  # 假设第一个是最大的

for num in numbers:
    if num > max_num:
        max_num = num

print(f"最大的数是:{max_num}")
```

### 模式5:正序和反序遍历

```python
# 正序遍历
for i in range(1, 6):
    print(i, end=" ")
print()

# 反序遍历
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# 步长为2
for i in range(1, 10, 2):
    print(i, end=" ")
```

> **给家长的小贴士**:
> - 这些模式在编程中非常常见
> - 建议让孩子记住这些基本模式
> - 可以用生活中的例子类比:计数器、存钱罐、找最大数
> - 鼓励孩子用这些模式解决新问题

## 综合练习

### 练习1:打印30以内的自然数

**题目**:分别用while和for循环打印30以内的自然数(包含30)。

<details>
<summary>👉 点击查看答案</summary>

**while版本**:
```python
# while循环
count = 0
while count <= 30:
    print(count, end=" ")
    count = count + 1
```

**for版本**:
```python
# for循环
for i in range(31):  # range(31) = range(0, 31) = 0到30
    print(i, end=" ")
```
</details>

### 练习2:挑水问题

**题目**:一口缸容量有180升,一个和尚每次挑水20升,多少次挑满?

<details>
<summary>👉 点击查看答案</summary>

```python
# 挑水问题
capacity = 180  # 缸的容量
each_time = 20  # 每次挑水量
current = 0     # 当前水量
count = 0       # 挑水次数

while current < capacity:
    current = current + each_time
    count = count + 1
    print(f"第{count}次挑水,当前水量:{current}升")

print(f"需要{count}次才能挑满")
```

**输出结果**:
```
第1次挑水,当前水量:20升
第2次挑水,当前水量:40升
...
第9次挑水,当前水量:180升
需要9次才能挑满
```

**更简洁的写法**:
```python
capacity = 180
each_time = 20

# 用整除计算
times = capacity // each_time

# 如果有余数,需要多挑一次
if capacity % each_time != 0:
    times = times + 1

print(f"需要{times}次才能挑满")
```
</details>

### 练习3:统计学生成绩

**题目**:循环录入Java课的学生成绩,统计分数大于等于80分的学生比例。

<details>
<summary>👉 点击查看答案</summary>

```python
# 统计学生成绩
total_students = int(input("请输入学生人数:"))
pass_count = 0  # 大于等于80分的人数

for i in range(total_students):
    score = int(input(f"请输入第{i + 1}个学生的成绩:"))

    if score >= 80:
        pass_count = pass_count + 1
        print(f"成绩{score}:优秀!")
    else:
        print(f"成绩{score}:继续努力!")

# 计算比例
percentage = (pass_count / total_students) * 100

print(f"\n统计结果:")
print(f"总人数:{total_students}")
print(f"优秀人数:{pass_count}")
print(f"优秀比例:{percentage:.1f}%")
```

**运行示例**:
```
请输入学生人数:5
请输入第1个学生的成绩:85
成绩85:优秀!
请输入第2个学生的成绩:72
成绩72:继续努力!
请输入第3个学生的成绩:90
成绩90:优秀!
请输入第4个学生的成绩:68
成绩68:继续努力!
请输入第5个学生的成绩:82
成绩82:优秀!

统计结果:
总人数:5
优秀人数:3
优秀比例:60.0%
```
</details>

### 练习4:小芳存钱

**题目**:小芳的妈妈每天给她2.5元钱,她都会存起来。从存钱开始,每过5天她就会花去6元钱。请问要到第几天,小芳才可以存满100元钱?

<details>
<summary>👉 点击查看答案</summary>

```python
# 小芳存钱问题
money = 0  # 当前存款
day = 0    # 天数

while money < 100:
    day = day + 1
    money = money + 2.5  # 每天存2.5元
    print(f"第{day}天:存2.5元,当前存款:{money}元")

    # 每5天花6元
    if day % 5 == 0:
        money = money - 6
        print(f"  -> 第{day}天:花6元,剩余存款:{money}元")

print(f"\n第{day}天,小芳存满了100元!")
```

**输出结果**:
```
第1天:存2.5元,当前存款:2.5元
第2天:存2.5元,当前存款:5.0元
第3天:存2.5元,当前存款:7.5元
第4天:存2.5元,当前存款:10.0元
第5天:存2.5元,当前存款:12.5元
  -> 第5天:花6元,剩余存款:6.5元
...
第50天:存2.5元,当前存款:97.5元
第51天:存2.5元,当前存款:100.0元

第51天,小芳存满了100元!
```
</details>

### 练习5:求100以内偶数之和

**题目**:求100以内的偶数之和。

<details>
<summary>👉 点击查看答案</summary>

**方法1:用if判断**:
```python
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total = total + i

print(f"100以内偶数之和:{total}")
```

**方法2:用步长2(更高效)**:
```python
total = 0
for i in range(0, 101, 2):  # 直接生成偶数
    total = total + i

print(f"100以内偶数之和:{total}")
```

**输出结果**:
```
100以内偶数之和:2550
```
</details>

### 练习6:求100以内6的倍数

**题目**:求出100以内的所有6的倍数,以及个数。

<details>
<summary>👉 点击查看答案</summary>

```python
# 求100以内6的倍数
count = 0
print("100以内的6的倍数:")

for i in range(1, 101):
    if i % 6 == 0:
        print(i, end=" ")
        count = count + 1

print(f"\n总共{count}个")
```

**输出结果**:
```
100以内的6的倍数:
6 12 18 24 30 36 42 48 54 60 66 72 78 84 90 96
总共16个
```
</details>

### 练习7:打印数字矩形

**题目**:在控制台输出图形,第一行输出一个1,第二行输出二个2,第n行输出n个n。

<details>
<summary>👉 点击查看答案</summary>

```python
# 打印数字矩形
n = int(input("请输入行数:"))

for i in range(1, n + 1):
    # 打印i个i
    for j in range(i):
        print(i, end=" ")
    print()  # 换行
```

**运行示例**:
```
请输入行数:5
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```
</details>

### 练习8:水仙花数

**题目**:打印所有水仙花数。

**什么是水仙花数?**
- 一个三位数
- 例如153,1³ + 5³ + 3³ = 153
- 即:各位数字的立方和等于它本身

<details>
<summary>👉 点击查看答案</summary>

```python
# 打印水仙花数
print("三位数的水仙花数:")

for num in range(100, 1000):  # 遍历所有三位数
    # 分解百位、十位、个位
    hundreds = num // 100           # 百位
    tens = (num // 10) % 10        # 十位
    ones = num % 10                # 个位

    # 计算各位数字的立方和
    sum_of_cubes = hundreds ** 3 + tens ** 3 + ones ** 3

    # 判断是否为水仙花数
    if sum_of_cubes == num:
        print(num)

print("查找完成!")
```

**输出结果**:
```
三位数的水仙花数:
153
370
371
407
查找完成!
```

> **给家长的小贴士**:
> - 解释"水仙花数"的含义
> - 重点讲解如何分解一个三位数的百位、十位、个位
> - 用除法和取余运算:
>   - 百位 = num // 100
>   - 十位 = (num // 10) % 10
>   - 个位 = num % 10
> - 这是一个经典的编程练习,锻炼数学和编程结合的能力
</details>

### 练习9:交错数列求和

**题目**:计算1 - 2 + 3 - 4 + 5 - ... + 99的结果。

<details>
<summary>👉 点击查看答案</summary>

```python
# 计算交错数列求和: 1 - 2 + 3 - 4 + ... + 99
total = 0

for i in range(1, 100):  # 1到99
    if i % 2 == 1:
        # 奇数相加
        total = total + i
        print(f"+{i}", end=" ")
    else:
        # 偶数相减
        total = total - i
        print(f"-{i}", end=" ")

print(f"\n结果:{total}")
```

**输出结果**:
```
+1 -2 +3 -4 +5 -6 +7 -8 +9 -10 +11 -12 +13 -14 +15 -16 +17 -18 +19 -20 +21 -22 +23 -24 +25 -26 +27 -28 +29 -30 +31 -32 +33 -34 +35 -36 +37 -38 +39 -40 +41 -42 +43 -44 +45 -46 +47 -48 +49 -50 +51 -52 +53 -54 +55 -56 +57 -58 +59 -60 +61 -62 +63 -64 +65 -66 +67 -68 +69 -70 +71 -72 +73 -74 +75 -76 +77 -78 +79 -80 +81 -82 +83 -84 +85 -86 +87 -88 +89 -90 +91 -92 +93 -94 +95 -96 +97 -98 +99
结果:50
```

**更简洁的写法**:
```python
# 方法2:观察规律
# (1-2) + (3-4) + (5-6) + ... + (97-98) + 99
# = -1 + -1 + -1 + ... + -1 + 99
# 共49个-1,最后+99
# = -49 + 99 = 50

# 或者换个角度:
# 1 + 3 + 5 + ... + 99 = 2500 (奇数和)
# 2 + 4 + 6 + ... + 98 = 2450 (偶数和)
# 2500 - 2450 = 50

odd_sum = 0
even_sum = 0

for i in range(1, 100):
    if i % 2 == 1:
        odd_sum = odd_sum + i
    else:
        even_sum = even_sum + i

result = odd_sum - even_sum
print(f"奇数和:{odd_sum}, 偶数和:{even_sum}, 结果:{result}")
```
</details>

### 练习10:猜数字游戏(限制次数)

**题目**:写一个猜数字游戏,猜对了结束,猜不对继续,最多猜9次。

<details>
<summary>👉 点击查看答案</summary>

```python
# 猜数字游戏
import random  # 随机数库

target = random.randint(1, 100)  # 生成1到100的随机数
max_attempts = 9

print("=== 猜数字游戏 ===")
print(f"我已经想好了一个1到100之间的数字,你有{max_attempts}次机会猜!")

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"\n第{attempt}次猜测,请输入你的猜测(1-100):"))

    if guess == target:
        print(f"🎉 恭喜你!第{attempt}次就猜对了!数字是:{target}")
        break  # 猜对了,退出循环
    elif guess < target:
        print(f"太小了!还有{max_attempts - attempt}次机会")
    else:
        print(f"太大了!还有{max_attempts - attempt}次机会")

else:
    # for循环正常结束(没有break)时执行
    print(f"\n😢 很遗憾,你没有猜对。正确答案是:{target}")

print("\n游戏结束!")
```

**运行示例**:
```
=== 猜数字游戏 ===
我已经想好了一个1到100之间的数字,你有9次机会猜!

第1次猜测,请输入你的猜测(1-100):50
太大了!还有8次机会

第2次猜测,请输入你的猜测(1-100):25
太小了!还有7次机会

第3次猜测,请输入你的猜测(1-100):37
太大了!还有6次机会

第4次猜测,请输入你的猜测(1-100):31
🎉 恭喜你!第4次就猜对了!数字是:31

游戏结束!
```

> **给家长的小贴士**:
> - 这是一个综合练习,用到了循环、条件、break、else等
> - `for...else`语法:当for循环正常结束(没有break)时,执行else
> - 可以和孩子一起玩这个游戏,增加趣味性
> - 可以讨论如何用"二分查找"策略提高猜测效率
</details>

### 练习11:求素数

**题目**:输入一个正整数n,判断它是否为素数。

**什么是素数?**
- 只能被1和它本身整除的数
- 例如:2, 3, 5, 7, 11, 13, 17, 19, 23, ...
- 1不是素数
- 2是最小的素数,也是唯一的偶数素数

<details>
<summary>👉 点击查看答案</summary>

```python
# 判断一个数是否为素数
num = int(input("请输入一个正整数:"))

# 处理特殊情况
if num < 2:
    print(f"{num}不是素数")
elif num == 2:
    print(f"{num}是素数")
elif num % 2 == 0:
    print(f"{num}不是素数(能被2整除)")
else:
    # 判断从3到num-1是否有能整除的数
    is_prime = True  # 假设是素数

    for i in range(3, num):
        if num % i == 0:
            is_prime = False
            print(f"{num}不是素数(能被{i}整除)")
            break  # 找到一个因数就够了

    # 如果循环正常结束,说明没有找到因数
    if is_prime:
        print(f"{num}是素数!")
```

**运行示例**:
```
请输入一个正整数:17
17是素数!
```

```
请输入一个正整数:15
15不是素数(能被3整除)
```

**进阶:打印100以内的所有素数**:
```python
# 打印100以内的所有素数
print("100以内的素数:")

for num in range(2, 101):
    if num == 2:
        print(num, end=" ")
        continue

    if num % 2 == 0:
        continue

    # 判断是否为素数
    is_prime = True
    for i in range(3, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
```

**输出结果**:
```
100以内的素数:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
```

> **给家长的小贴士**:
> - 素数判断是一个经典算法问题
> - 可以优化:只需要判断到√n,不需要到n-1
> - 这是密码学的基础( RSA加密算法用到素数)
> - 可以和孩子讨论为什么素数很重要
</details>

## 用循环简化Turtle图形

还记得第6章我们用Turtle画图形吗？当时我们用顺序语句，每个边都要写一遍代码。现在学完循环后，我们可以大大简化这些代码！

### 回顾：第6章的画图代码

在第6章，我们画正方形时是这样的：

```python
import turtle

t = turtle.Turtle()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

turtle.done()
```

**问题**：这段代码重复了4次相同的内容！如果我们想画正六边形、正八边形，代码会变得很长。

### 用循环改进：画正n边形

现在我们可以用循环来简化：

```python
import turtle

t = turtle.Turtle()

# 画正方形（4条边）
for i in range(4):
    t.forward(100)
    t.left(90)

turtle.done()
```

**优势**：
- 代码从8行减少到3行！
- 如果要画正六边形，只需要改数字：
  ```python
  for i in range(6):
      t.forward(100)
      t.left(60)  # 360 ÷ 6 = 60度
  ```

> **👨‍🏫 给家长的Tips**
>
> 这是一个绝佳的教学时机！
> - 让孩子对比两种写法的代码行数
> - 问孩子："哪种写法更简单？如果我要画正12边形呢？"
> - 引导孩子理解：循环就是让计算机帮我们重复做相同的事
> - 强调：程序员很"懒"，总在想办法让代码更简洁

### 练习1：改写长方形画法

**第6章的代码**（顺序语句）：
```python
length = 150
width = 80

t.forward(length)
t.left(90)
t.forward(width)
t.left(90)
t.forward(length)
t.left(90)
t.forward(width)
t.left(90)
```

**用循环改进**：
```python
length = 150
width = 80

for i in range(2):  # 重复2次
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.left(90)
```

代码从10行减少到5行！

### 练习2：改写五边形

**第6章的代码**：
```python
side = 100
angle = 360 / 5  # 72度

t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
t.forward(side)
t.left(angle)
```

**用循环改进**：
```python
side = 100
angle = 360 / 5

for i in range(5):
    t.forward(side)
    t.left(angle)
```

代码从11行减少到3行！

### 练习3：改写五角星

**第6章的代码**：
```python
t.pencolor("gold")
t.fillcolor("orange")
t.begin_fill()

t.forward(200)
t.right(144)
t.forward(200)
t.right(144)
t.forward(200)
t.right(144)
t.forward(200)
t.right(144)
t.forward(200)
t.right(144)

t.end_fill()
```

**用循环改进**：
```python
t.pencolor("gold")
t.fillcolor("orange")
t.begin_fill()

for i in range(5):
    t.forward(200)
    t.right(144)

t.end_fill()
```

### 挑战项目：用循环画复杂图形

现在你掌握了循环，可以尝试画更复杂的图形了！

#### 项目1：彩色多边形螺旋

```python
import turtle

t = turtle.Turtle()
t.speed(0)  # 最快速度

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# 画36个逐渐变大的正方形
for i in range(36):
    t.pencolor(colors[i % 6])  # 循环使用6种颜色
    t.forward(50 + i * 5)      # 每次边长增加
    t.left(90)                 # 转向
    t.forward(50 + i * 5)
    t.left(90)
    t.forward(50 + i * 5)
    t.left(90)
    t.forward(50 + i * 5)
    t.left(90)
    t.left(10)  # 每次多转10度，形成螺旋

turtle.done()
```

#### 项目2：花朵（第6章留下的挑战）

在第6章，我们说花朵练习要等学完循环再做。现在可以了！

```python
import turtle

t = turtle.Turtle()
t.speed(10)

colors = ["red", "orange", "yellow", "pink", "purple", "blue"]

# 画6个花瓣
for i in range(6):
    t.color(colors[i])
    t.begin_fill()

    # 画椭圆（通过多次小角度转向实现）
    for j in range(36):
        t.forward(20)
        t.left(10)
    t.left(60)  # 转到下一个花瓣

    t.end_fill()

# 画花心
t.penup()
t.goto(0, -10)
t.pendown()
t.color("green")
t.begin_fill()
t.circle(20)
t.end_fill()

turtle.done()
```

> **👨‍🏫 给家长的Tips**
>
> 这个花朵项目使用了**嵌套循环**：
> - 外层循环：画6个花瓣
> - 内层循环：每个花瓣由36条短线段组成
> - 这是循环的高级应用，让孩子看到循环的威力
> - 可以让孩子修改参数（如花瓣数量、颜色），观察变化

### 练习4：创意画图

用循环发挥你的创意！

**想法**：
- 用循环画一排五角星（10个，位置不同）
- 用循环画同心圆（10个圆，半径逐渐增大）
- 用循环画一个"图案生成器"（旋转对称图形）

**示例：旋转的五角星**

```python
import turtle

t = turtle.Turtle()
t.speed(0)

# 画12个旋转的五角星
for i in range(12):
    t.pencolor("gold")
    t.begin_fill()

    for j in range(5):
        t.forward(100)
        t.right(144)

    t.end_fill()
    t.right(30)  # 旋转30度（360 ÷ 12 = 30）

turtle.done()
```

### 总结：循环的威力

通过对比第6章和现在的代码，我们发现：

| 图形 | 第6章（顺序语句） | 现在（循环） | 减少行数 |
|------|-------------------|--------------|---------|
| 正方形 | 8行 | 3行 | 减少5行 |
| 五边形 | 11行 | 3行 | 减少8行 |
| 五角星 | 11行 | 3行 | 减少8行 |
| 花朵 | 不现实 | 15行 | 不可想象 |

**循环的优势**：
1. **代码更短**：从几十行减少到几行
2. **更易修改**：想画正12边形？只改一个数字
3. **更易阅读**：代码意图更清晰
4. **减少错误**：不用重复写相同的代码

> **👨‍🏫 给家长的Tips**
>
> 这个对比非常重要！
> - 让孩子真切感受到循环的价值
> - 回顾第6章时留下的"伏笔"，现在终于"解密"了
> - 告诉孩子："这就是为什么我们要学循环——让代码更简洁、更强大"
> - 鼓励孩子用循环改写之前的所有画图代码


## 变量的作用域

在循环中定义的变量,在循环外面可以使用吗?

### 示例:循环变量的作用域

```python
# 循环变量的作用域
for i in range(1, 6):
    print(f"循环内:i = {i}")

print(f"循环外:i = {i}")  # 可以访问i!

# 但是,如果循环一次都没执行呢?
for j in range(0):  # range(0)是空的
    print(f"循环内:j = {j}")

# print(f"循环外:j = {j}")  # 错误!j不存在
```

**输出结果**:
```
循环内:i = 1
循环内:i = 2
循环内:i = 3
循环内:i = 4
循环内:i = 5
循环外:i = 5
```

> **给家长的小贴士**:
> - Python中,for循环的变量在循环外仍然可以访问
> - 但是,如果循环一次都没执行,变量就不存在
> - 建议:在循环外定义好所有需要的变量
> - 这样代码更清晰,不容易出错

## 循环和分支互相嵌套

### 示例:求和或求乘积

**题目**:要求用户输入一个正整数n,然后问用户计算求和还是求乘积。如果用户输入求和,则输出1+2+...+n的结果;用户输入求乘积,则输出1×2×...×n的结果。

<details>
<summary>👉 点击查看答案</summary>

```python
# 求和或求乘积
n = int(input("请输入一个正整数n:"))
choice = input("请选择计算方式(求和/求乘积):")

if choice == "求和":
    # 计算求和
    total = 0
    for i in range(1, n + 1):
        total = total + i
    print(f"1+2+...+{n} = {total}")

elif choice == "求乘积":
    # 计算求乘积
    product = 1
    for i in range(1, n + 1):
        product = product * i
    print(f"1×2×...×{n} = {product}")

else:
    print("Error!!! 输入不正确")
```

**运行示例**:
```
请输入一个正整数n:5
请选择计算方式(求和/求乘积):求和
1+2+...+5 = 15
```

```
请输入一个正整数n:5
请选择计算方式(求和/求乘积):求乘积
1×2×...×5 = 120
```
</details>

## 常见错误和调试

### 错误1:忘记更新循环变量

```python
# 错误:死循环
count = 0
while count < 5:
    print(count)
    # 忘记了 count = count + 1

# 正确
count = 0
while count < 5:
    print(count)
    count = count + 1  # 更新循环变量!
```

### 错误2:循环条件错误

```python
# 错误:永远不会执行
count = 5
while count > 10:  # 5 > 10是False
    print(count)

# 正确
count = 5
while count < 10:  # 5 < 10是True
    print(count)
    count = count + 1
```

### 错误3:off-by-one错误

```python
# 常见错误:想打印1到10,但只打印到9
for i in range(1, 10):  # 错误!range(1, 10)是1到9
    print(i)

# 正确
for i in range(1, 11):  # 正确!range(1, 11)是1到10
    print(i)
```

### 错误4:缩进错误

```python
# 错误:缩进不一致
for i in range(5):
  print(i)  # 2个空格
    print(i * 2)  # 4个空格

# 正确:缩进一致
for i in range(5):
    print(i)
    print(i * 2)
```

### 调试技巧

1. **使用print语句**:
```python
for i in range(1, 6):
    print(f"调试:i = {i}")  # 调试信息
    total = total + i
    print(f"调试:total = {total}")  # 调试信息
```

2. **画表格追踪变量**:
| 循环次数 | i | total |
|---------|---|-------|
| 第1次 | 1 | 1 |
| 第2次 | 2 | 3 |
| 第3次 | 3 | 6 |

3. **简化问题**:
   - 先用小的数字测试(比如1到5,而不是1到100)
   - 确认逻辑正确后再扩大范围

4. **检查边界条件**:
   - 0会怎样?
   - 1会怎样?
   - 最大值会怎样?

> **给家长的小贴士**:
> - 教孩子学会看错误信息
> - 鼓励孩子用print调试
> - 建议先在纸上画出执行过程
> - 强调"从小到大"测试策略

## 章节小结

### 我们学到了什么

1. **循环的概念**:重复执行某些操作
2. **while循环**:条件循环,适合不知道循环次数的情况
3. **for循环**:计数循环,适合知道循环次数的情况
4. **range()函数**:生成数字序列
5. **break和continue**:控制循环的执行
6. **循环嵌套**:循环中的循环
7. **常见模式**:计数器、累加器、累乘器、最大值查找

### 重要语法回顾

| 循环类型 | 语法 | 用途 |
|---------|------|------|
| while | `while 条件:` | 条件循环 |
| for | `for i in range():` | 计数循环 |
| break | `break` | 跳出循环 |
| continue | `continue` | 跳过本次 |

### 循环的三个要素

1. **初始值**:循环变量的起点
2. **条件**:判断是否继续循环
3. **更新**:循环变量如何变化

### 编程技巧

1. **避免死循环**:记得更新循环变量
2. **注意边界**:range(1, 5)是1到4,不包括5
3. **缩进正确**:循环体要统一缩进
4. **简化测试**:先用小数字测试,确认逻辑后再扩大
5. **调试方法**:用print输出中间结果

### 下一步

在下一章(第9章),我们将学习**流程图**,用图形化的方式表示程序的执行流程。流程图能帮助我们更好地理解程序的逻辑!

### 挑战练习

1. **必做**:
   - 用for循环计算1到1000的和
   - 打印所有三位数中,个位、十位、百位都相同的数字(如111, 222, 333)
   - 用while循环实现:输入密码,直到输入正确为止

2. **选做**:
   - 打印"斐波那契数列"的前20项(1, 1, 2, 3, 5, 8, 13, ...)
   - 计算阶乘:n! = 1×2×3×...×n
   - 打印"杨辉三角"的前10行

3. **挑战**:
   - 用循环实现"九九乘法表"的倒三角版本
   - 找出所有"完全数":一个数等于它的所有真因数之和(如6=1+2+3)
   - 实现"猜数字"游戏,并在猜测次数上设置难度级别

4. **综合项目**:
   - 写一个简单的计算器,可以循环计算,直到用户选择退出
   - 写一个成绩管理系统,可以录入、查询、统计成绩
   - 用Turtle库和循环,画一个螺旋图形

加油!你已经掌握了让程序重复工作的能力!🎉
