# 第17章 程序设计 - 如何写出好程序

## 引言：从"能运行"到"写得好"

想象一下，有两个同学都写了一个"猜数字"游戏程序：

**同学A的程序**：
```python
import random
n=random.randint(1,100)
while True:
    g=int(input("?"))
    if g>n:print("大")
    elif g<n:print("小")
    else:print("对");break
```

**同学B的程序**：
```python
import random

# 猜数字游戏
# 目标：猜一个1-100之间的随机数

secret_number = random.randint(1, 100)
guess_count = 0

print("=== 猜数字游戏 ===")
print("我已经想好了一个1到100之间的数字")
print("你能猜到它是多少吗？")

while True:
    guess = input("请输入你的猜测（输入q退出）：")

    # 允许用户退出
    if guess == 'q':
        print(f"游戏结束！正确答案是：{secret_number}")
        break

    # 验证输入
    if not guess.isdigit():
        print("请输入一个有效的数字！")
        continue

    guess_count += 1
    guess = int(guess)

    # 比较大小
    if guess > secret_number:
        print(f"{guess} 太大了！再试试")
    elif guess < secret_number:
        print(f"{guess} 太小了！再试试")
    else:
        print(f"恭喜你！{guess} 就是正确答案！")
        print(f"你总共猜了 {guess_count} 次")
        break
```

### 两个程序的对比

| 对比项 | 同学A的程序 | 同学B的程序 |
|--------|------------|------------|
| **能否运行** | ✅ 能运行 | ✅ 能运行 |
| **变量命名** | ❌ n, g（看不懂） | ✅ secret_number, guess（清晰） |
| **注释** | ❌ 没有注释 | ✅ 有注释说明 |
| **用户体验** | ❌ 提示不清楚 | ✅ 友好的提示 |
| **错误处理** | ❌ 输入非数字会崩溃 | ✅ 验证输入，可以退出 |
| **代码格式** | ❌ 一行多语句 | ✅ 格式清晰 |

**问题**：如果你是老师，你会给哪个程序更高的分数？

**答案**：当然是同学B！虽然两个程序都能"运行"，但同学B的程序：
- 更容易理解和修改
- 更健壮（不容易出错）
- 用户体验更好

### 什么是"好程序"?

**好程序**不仅要**能运行**，还要：

1. **正确性** - 能正确解决问题
2. **可读性** - 别人能看懂你的代码
3. **可维护性** - 容易修改和扩展
4. **健壮性** - 不容易出错
5. **效率** - 运行速度快，占用资源少

### 为什么要学习"程序设计"?

你可能在想：*"我写的程序能运行不就行了吗？为什么要学这些?"*

**答案是**：

1. **让代码更容易理解**
   - 过了一个月，你自己都看不懂自己写的代码
   - 别人看你的代码像看"天书"

2. **让代码更容易修改**
   - 需求变化时，不用重写整个程序
   - 可以轻松添加新功能

3. **减少程序错误**
   - 好的设计让错误更少
   - 出错了也更容易找到

4. **为大型程序做准备**
   - 写10行的程序，随便写写也行
   - 写100行、1000行的程序，就需要好的设计方法

5. **成为一名优秀的程序员**
   - 初级程序员：能写出能运行的代码
   - 高级程序员：能写出优雅、健壮的代码

### 本章学习路线

```
第1步：如何评价一个程序的好坏
   ↓
第2步：变量设计的原则
   ↓
第3步：程序设计的一般方法
   ↓
第4步：综合实践：用设计方法重写程序
   ↓
第5步：常见错误和调试技巧
```

**给家长的小贴士**：这一章是理论性较强的章节，但非常重要。建议家长：
- 用"写作文"类比程序设计：作文不仅要通顺，还要有结构、有逻辑
- 鼓励孩子对比自己之前的程序，找出可以改进的地方
- 强调"好习惯"的重要性：现在养成好习惯，以后写程序会更轻松
- 可以让孩子"代码审查"家长写的程序，找出问题

---

## 17.1 如何评价一个程序的好坏

### 程序评价的五个维度

我们可以从以下五个维度评价一个程序：

#### 1. 正确性（Correctness）

**定义**：程序是否正确地解决了问题。

**如何判断**：
- 输入合法数据，输出结果是否正确？
- 边界情况是否正确？（例如：空列表、0、负数）
- 错误输入是否妥善处理？

**举例**：

写一个"计算平均分"的程序：

❌ **不正确的版本**：
```python
scores = [80, 90, 85]
average = sum(scores) / 3  # 假设固定3个科目
print(average)
```

问题：如果列表不是3个科目，结果就错了！

✅ **正确的版本**：
```python
def calculate_average(scores):
    if not scores:  # 处理空列表
        return 0
    return sum(scores) / len(scores)

# 测试各种情况
print(calculate_average([80, 90, 85]))      # 正常情况
print(calculate_average([]))                 # 空列表
print(calculate_average([100]))               # 一个元素
```

**给家长的小贴士**：教导孩子"测试思维"
- 编写程序后，要主动测试各种情况
- 询问："如果输入是空的会怎样？" "如果是负数会怎样？"
- 这能培养孩子的严谨思维

#### 2. 可读性（Readability）

**定义**：程序是否容易被人类理解。

**评价标准**：
- ✅ 变量名能说明用途
- ✅ 有适当的注释
- ✅ 代码格式整齐
- ✅ 逻辑清晰

**举例对比**：

❌ **可读性差的代码**：
```python
a=10
b=20
c=a*b
print(c)
```

问题：a、b、c是什么意思？

✅ **可读性好的代码**：
```python
length = 10      # 长方形的长
width = 20       # 长方形的宽
area = length * width  # 计算面积
print(f"面积是：{area}")
```

**可读性的三个黄金法则**：

1. **好命名**
   ```python
   # ❌ 差的命名
   x = 10
   s = "hello"
   flg = True

   # ✅ 好的命名
   age = 10
   user_name = "hello"
   is_valid = True
   ```

2. **好注释**
   ```python
   # ❌ 没有注释
   s = s.replace(" ", "")

   # ✅ 有注释
   # 去除用户名中的所有空格
   user_name = user_name.replace(" ", "")
   ```

3. **好格式**
   ```python
   # ❌ 格式混乱
   if x>0:x=x+1;print(x)

   # ✅ 格式清晰
   if x > 0:
       x = x + 1
       print(x)
   ```

**给家长的小贴士**：鼓励孩子"像讲故事一样写代码"
- 变量名要像一个"好标题"
- 注释要像"故事说明"
- 代码要像"分段清晰的文章"

#### 3. 可维护性（Maintainability）

**定义**：程序是否容易被修改和扩展。

**问题场景**：
- 需求变化时，是否需要大改代码？
- 修复一个bug，会不会引入新的bug？
- 能否轻松添加新功能？

**举例**：

❌ **可维护性差的代码**：
```python
# 硬编码的值，难以修改
price = 100
tax = price * 0.13  # 税率13%写死在代码里
total = price + tax
print(total)
```

问题：如果税率改成15%，要修改所有地方！

✅ **可维护性好的代码**：
```python
# 使用常量，易于修改
TAX_RATE = 0.13  # 税率集中定义

def calculate_total(price):
    """计算含税总价"""
    tax = price * TAX_RATE
    return price + tax

print(calculate_total(100))
print(calculate_total(200))
```

优势：修改税率只需要改一行！

**可维护性的技巧**：

1. **避免重复代码（DRY原则）**
   ```python
   # ❌ 重复代码
   area1 = length1 * width1
   area2 = length2 * width2
   area3 = length3 * width3

   # ✅ 使用函数
   def calculate_area(length, width):
       return length * width

   area1 = calculate_area(length1, width1)
   area2 = calculate_area(length2, width2)
   area3 = calculate_area(length3, width3)
   ```

2. **使用函数封装**
   ```python
   # ❌ 所有代码堆在一起
   a = 10
   b = 20
   print(a + b)
   c = 30
   d = 40
   print(c + d)

   # ✅ 封装成函数
   def add_and_print(x, y):
       print(x + y)

   add_and_print(10, 20)
   add_and_print(30, 40)
   ```

**给家长的小贴士**：
- 用"乐高积木"比喻函数：每块积木（函数）做好后，可以重复使用
- 当孩子写类似的代码时，提醒："这能不能做成一个函数？"

#### 4. 健壮性（Robustness）

**定义**：程序是否能处理各种异常情况，不容易崩溃。

**问题场景**：
- 用户输入错误时，程序是否崩溃？
- 数据不完整时，程序是否继续运行？
- 出现错误时，是否有友好的提示？

**举例**：

❌ **不健壮的代码**：
```python
age = int(input("请输入年龄："))
print(f"你明年{age + 1}岁")
```

问题：如果用户输入"abc"，程序崩溃！

✅ **健壮的代码**：
```python
while True:
    age_input = input("请输入年龄：")

    # 验证输入是否为数字
    if not age_input.isdigit():
        print("请输入一个有效的数字！")
        continue

    age = int(age_input)

    # 验证年龄范围
    if age < 0 or age > 150:
        print("年龄应该在0-150之间！")
        continue

    print(f"你明年{age + 1}岁")
    break
```

**健壮性的三个原则**：

1. **永远不要相信用户输入**
   ```python
   # 假设用户可能输入任何东西
   user_input = input("请输入数字：")

   # 先验证再使用
   if user_input.isdigit():
       number = int(user_input)
       # 使用这个数字
   else:
       print("输入无效！")
   ```

2. **处理边界情况**
   ```python
   # 边界情况：空列表
   scores = []
   if scores:  # 先检查是否为空
       average = sum(scores) / len(scores)
   else:
       print("没有成绩数据")
   ```

3. **提供有用的错误信息**
   ```python
   # ❌ 无用的错误信息
   print("错误")

   # ✅ 有用的错误信息
   print("错误：文件不存在，请检查文件名是否正确")
   ```

**给家长的小贴士**：
- 和孩子玩"找茬游戏"：让孩子想方设法"破坏"程序
- 问孩子："如果你故意输入错误，程序会怎样？"
- 这能培养孩子的"防御性编程"思维

#### 5. 效率（Efficiency）

**定义**：程序运行的速度和占用的资源。

**对于初学者**：
- 不要过度优化
- "先让它能运行，再让它运行得更快"
- 可读性比效率更重要

**什么时候需要考虑效率**：
- 数据量很大时（例如：处理10000条数据）
- 程序运行很慢时
- 使用有限的资源（例如：内存）

**简单优化技巧**：

1. **避免重复计算**
   ```python
   # ❌ 重复计算
   for i in range(1000):
       result = sum(very_large_list) * i  # 每次循环都重新计算

   # ✅ 只计算一次
   total = sum(very_large_list)
   for i in range(1000):
       result = total * i
   ```

2. **选择合适的数据结构**
   ```python
   # 如果需要频繁查找，用字典而不是列表

   # ❌ 用列表查找（慢）
   students_list = ["Alice", "Bob", "Charlie"]
   if "Bob" in students_list:  # 需要遍历整个列表
       print("找到Bob")

   # ✅ 用字典查找（快）
   students_dict = {"Alice": 1, "Bob": 2, "Charlie": 3}
   if "Bob" in students_dict:  # 直接查找
       print("找到Bob")
   ```

**给家长的小贴士**：
- 告诉孩子："就像写作文，先写完，再润色"
- 对于初学者，**可读性 > 效率**
- 如果程序运行速度能接受，就不需要优化

### 综合评价案例

让我们用五个维度评价一个完整的程序：

**题目**：写一个"学生成绩管理"程序

**版本A：基础版**
```python
scores = []
while True:
    s = input("输入成绩（q退出）：")
    if s == 'q':
        break
    scores.append(int(s))
print(sum(scores)/len(scores))
```

**版本B：改进版**
```python
def calculate_average(scores):
    """计算平均分"""
    if not scores:
        return 0
    return sum(scores) / len(scores)

def get_valid_score(prompt):
    """获取有效的成绩输入"""
    while True:
        user_input = input(prompt)

        if user_input.lower() == 'q':
            return None

        # 验证输入
        if not user_input.isdigit():
            print("请输入一个有效的数字！")
            continue

        score = int(user_input)

        # 验证范围
        if score < 0 or score > 100:
            print("成绩应该在0-100之间！")
            continue

        return score

def main():
    """主程序"""
    print("=== 学生成绩管理系统 ===")

    scores = []
    while True:
        score = get_valid_score("请输入成绩（0-100，输入q退出）：")

        if score is None:
            break

        scores.append(score)

    if scores:
        average = calculate_average(scores)
        highest = max(scores)
        lowest = min(scores)

        print(f"\n=== 成绩统计 ===")
        print(f"学生人数：{len(scores)}")
        print(f"平均分：{average:.2f}")
        print(f"最高分：{highest}")
        print(f"最低分：{lowest}")
    else:
        print("没有输入成绩数据")

if __name__ == "__main__":
    main()
```

**评价对比**：

| 维度 | 版本A | 版本B |
|------|-------|-------|
| **正确性** | ✅ 基本正确 | ✅ 完全正确（处理空列表） |
| **可读性** | ❌ 变量名s不明确 | ✅ 变量名清晰，有注释 |
| **可维护性** | ❌ 代码重复，难扩展 | ✅ 使用函数，易扩展 |
| **健壮性** | ❌ 输入非数字会崩溃 | ✅ 验证输入和范围 |
| **效率** | ✅ 效率可以接受 | ✅ 效率可以接受 |

**结论**：版本B是一个更好的程序！

### 练习1：评价以下程序

请用五个维度评价以下程序，指出优点和缺点：

```python
# 计算圆的面积
r = float(input("请输入半径："))
area = 3.14 * r * r
print(area)
```

<details>
<summary>📝 查看评价</summary>

**评价结果**：

1. **正确性**：⭐⭐⭐⭐
   - ✅ 计算公式正确
   - ⚠️ π只用3.14，精度不够

2. **可读性**：⭐⭐⭐
   - ✅ 变量名r和area还算清晰
   - ❌ 没有注释
   - ❌ 输出没有说明

3. **可维护性**：⭐⭐⭐
   - ⚠️ π的值硬编码
   - ✅ 逻辑简单，容易理解

4. **健壮性**：⭐
   - ❌ 没有检查半径是否为负数
   - ❌ 输入非数字会崩溃

5. **效率**：⭐⭐⭐⭐⭐
   - ✅ 简单计算，效率很高

**改进建议**：
```python
import math

def calculate_circle_area(radius):
    """计算圆的面积"""
    if radius <= 0:
        raise ValueError("半径必须大于0")
    return math.pi * radius * radius

try:
    radius = float(input("请输入圆的半径："))
    area = calculate_circle_area(radius)
    print(f"半径为 {radius} 的圆的面积是：{area:.2f}")
except ValueError as e:
    print(f"输入错误：{e}")
```
</details>

---

## 17.2 变量的设计

### 为什么变量设计很重要？

**变量**是程序中最基本的"存储单元"。变量设计得好坏，直接影响程序的质量。

**比喻**：
- 变量就像收纳箱
- 好的变量设计：每个箱子贴上清晰的标签，只放一种物品
- 坏的变量设计：箱子没有标签，什么都混在一起

### 变量设计的三个原则

#### 原则1：职责明确（Single Responsibility）

**核心思想**：一个变量只承担一个职责。

❌ **不好的例子**：
```python
# x既用来存储输入，又用来存储计算结果
x = input("请输入数字：")
x = int(x) * 2
print(x)
```

问题：x的职责不清晰，容易混淆。

✅ **好的例子**：
```python
# 每个变量职责明确
user_input = input("请输入数字：")
number = int(user_input)
doubled_number = number * 2
print(doubled_number)
```

**比喻**：
- 像整理房间，一个抽屉只放一种东西
- "袜子抽屉"只放袜子，"内衣抽屉"只放内衣

#### 原则2：命名规范（Meaningful Names）

**核心思想**：变量名要能"自解释"，让人一看就知道它存的是什么。

**命名规范**：

1. **使用有意义的英文名词**
   ```python
   # ❌ 不好的命名
   a = 10
   x = "hello"
   f1 = 3.14

   # ✅ 好的命名
   age = 10
   user_name = "hello"
   pi = 3.14
   ```

2. **使用完整单词，不要过度缩写**
   ```python
   # ❌ 过度缩写
   s = "hello"  # s是什么？
   nm = "Alice"  # nm是name吗？
   cnt = 0       # cnt是count吗？

   # ✅ 完整单词
   name = "hello"
   username = "Alice"
   count = 0
   ```

3. **使用下划线分隔多个单词（snake_case）**
   ```python
   # ❌ 不符合Python风格
   userName = "Alice"
   StudentAge = 10

   # ✅ Python风格（snake_case）
   user_name = "Alice"
   student_age = 10
   ```

4. **布尔变量用is/has/can开头**
   ```python
   # ✅ 清晰的布尔命名
   is_valid = True
   has_permission = False
   can_edit = True
   is_empty = False

   # ❌ 不清晰的布尔命名
   valid = True
   permission = False
   edit = True
   ```

5. **集合类型用复数名词**
   ```python
   # ✅ 清晰的集合命名
   students = ["Alice", "Bob", "Charlie"]
   scores = [80, 90, 85]
   books = ["书1", "书2", "书3"]

   # ❌ 不清晰的集合命名
   student_list = ["Alice", "Bob", "Charlie"]
   score_array = [80, 90, 85]
   ```

**命名禁忌**：
- ❌ 使用单个字母（除了循环变量i, j, k）
- ❌ 使用拼音（如xingming）
- ❌ 使用中文（Python3支持但不推荐）
- ❌ 使用关键字（如if, for, while）
- ❌ 使用特殊字符（如@, #, $）

**给家长的小贴士**：
- 像教孩子写作文"起标题"一样，教孩子给变量起名
- 鼓励孩子使用"能看懂的英文"，而不是"a", "b", "c"
- 可以建议孩子准备一个"变量命名词典"，记录常用的英文单词

#### 原则3：作用域最小化（Minimize Scope）

**核心思想**：变量的作用范围越小越好。

**什么是作用域**：
- 变量能被访问的代码范围
- 在函数内部定义的变量，只能在函数内部使用
- 在函数外部定义的变量，可以在整个程序中使用

**为什么作用域要小**：
- 减少变量被意外修改的风险
- 让程序更容易理解
- 降低代码的耦合度

❌ **不好的例子**：
```python
# 全局变量，任何地方都能修改
counter = 0

def increment():
    global counter
    counter = counter + 1

def decrement():
    global counter
    counter = counter - 1

increment()
decrement()
print(counter)
```

问题：counter是全局变量，任何函数都能修改，容易出错。

✅ **好的例子**：
```python
def process_numbers(numbers):
    """局部变量，作用域在函数内"""
    counter = 0
    total = 0

    for num in numbers:
        counter += 1
        total += num

    average = total / counter
    return average

result = process_numbers([10, 20, 30])
print(result)
```

**作用域最小化的技巧**：

1. **优先使用局部变量**
   ```python
   # ✅ 好的做法：变量定义在需要的地方
   def calculate_rectangle_area(length, width):
       area = length * width  # 局部变量
       return area
   ```

2. **避免全局变量**
   ```python
   # ❌ 不好：使用全局变量
   TAX_RATE = 0.13

   def calculate_tax(price):
       return price * TAX_RATE

   # ✅ 更好：作为参数传递
   def calculate_tax(price, tax_rate):
       return price * tax_rate
   ```

3. **循环变量的作用域**
   ```python
   # ✅ 好的做法：循环变量只在循环中使用
   for i in range(10):
       print(i)
   # i在循环外就没有意义了
   ```

**给家长的小贴士**：
- 用"隐私"的概念比喻作用域
- "就像你的日记本，只有你自己能看，别人不能随便翻"
- 变量也是一样，尽量让它"私有"，不要让所有人都能访问

### 变量设计的实战案例

**案例**：设计一个"学生成绩统计"程序

**需求**：
- 输入多个学生的成绩
- 计算平均分、最高分、最低分
- 统计及格人数

**设计1：不好的变量设计**
```python
# ❌ 变量命名不清晰
a = []
while True:
    b = input("输入成绩：")
    if b == 'q':
        break
    a.append(int(b))

c = sum(a) / len(a)
d = max(a)
e = min(a)
f = 0
for g in a:
    if g >= 60:
        f = f + 1

print(c, d, e, f)
```

**问题**：
- a, b, c, d, e, f, g这些变量名完全没有意义
- 看代码完全不知道在做什么

**设计2：改进的变量设计**
```python
# ✅ 变量命名清晰，职责明确
scores = []           # 存储所有成绩
passing_score = 60    # 及格分数线

while True:
    user_input = input("请输入成绩（输入q退出）：")
    if user_input == 'q':
        break
    score = int(user_input)
    scores.append(score)

if scores:
    average_score = sum(scores) / len(scores)  # 平均分
    highest_score = max(scores)                 # 最高分
    lowest_score = min(scores)                  # 最低分

    passing_count = 0  # 及格人数
    for score in scores:
        if score >= passing_score:
            passing_count += 1

    print(f"平均分：{average_score:.2f}")
    print(f"最高分：{highest_score}")
    print(f"最低分：{lowest_score}")
    print(f"及格人数：{passing_count}/{len(scores)}")
```

**优点**：
- 每个变量的职责都很明确
- 变量名能"自解释"
- 代码易于理解和维护

### 练习2：改进变量设计

请改进以下程序的变量设计：

```python
x = input("请输入学生姓名：")
y = int(input("请输入语文成绩："))
z = int(input("请输入数学成绩："))
w = int(input("请输入英语成绩："))
v = y + z + w
u = v / 3
print(f"{x}的总分是{v}，平均分是{u}")
```

<details>
<summary>📝 查看改进方案</summary>

```python
# ✅ 改进后的版本
student_name = input("请输入学生姓名：")
chinese_score = int(input("请输入语文成绩："))
math_score = int(input("请输入数学成绩："))
english_score = int(input("请输入英语成绩："))

total_score = chinese_score + math_score + english_score
average_score = total_score / 3

print(f"{student_name}的总分是{total_score}，平均分是{average_score:.2f}")
```

**改进点**：
- x → student_name：明确表示学生姓名
- y, z, w → chinese_score, math_score, english_score：分别表示各科成绩
- v → total_score：总分
- u → average_score：平均分
- 添加:.2f格式化平均分输出
</details>

---

## 17.3 程序设计的一般方法

### 从"想到哪里写到哪里"到"系统化设计"

**初学者的做法**：
```
看到题目 → 直接开始写代码 → 边写边想 → 不断修改
```

**程序员的做法**：
```
分析需求 → 设计方案 → 编写代码 → 测试调试 → 优化改进
```

**比喻**：
- 初学者：像没有地图就开车，开到哪算哪
- 程序员：先规划路线，再出发

### 程序设计的五个步骤

#### 第1步：明确需求（Understand Requirements）

**核心问题**：
- 程序要解决什么问题？
- 输入是什么？输出是什么？
- 有哪些特殊要求？

**方法**：
1. **列出输入和输出**
   ```python
   题目：写一个猜数字游戏

   输入：
   - 用户猜测的数字

   输出：
   - "太大了"、"太小了"、"正确"的提示
   - 猜测次数统计
   ```

2. **明确功能要求**
   ```python
   功能要求：
   1. 生成1-100之间的随机数
   2. 用户可以多次猜测
   3. 每次猜测后给出提示
   4. 猜中后显示猜测次数
   5. 允许用户中途退出
   ```

3. **确定边界条件**
   ```python
   边界情况：
   - 用户输入的不是数字怎么办？
   - 用户输入的数字超出范围怎么办？
   - 用户一直猜不中怎么办？
   ```

**给家长的小贴士**：
- 让孩子把需求"说出来"或"写下来"
- 问孩子："这个程序要做什么？输入是什么？输出是什么？"
- 这能培养孩子的"需求分析"能力

#### 第2步：设计输入输出（Design Input/Output）

**核心问题**：
- 用户如何输入数据？
- 程序如何展示结果？

**方法**：

1. **设计输入格式**
   ```python
   # 猜数字游戏的输入设计

   方案1：简单输入
   请输入你的猜测：50

   方案2：带提示的输入
   猜数字游戏（1-100）
   第1次猜测，请输入数字：50
   （输入q退出）

   选择方案2，更友好！
   ```

2. **设计输出格式**
   ```python
   # 猜数字游戏的输出设计

   方案1：简单输出
   太大了
   太小了
   正确

   方案2：详细输出
   ===== 猜数字游戏 =====
   第1次猜测：50
   提示：太大了！
   你已经猜了1次

   选择方案2，用户体验更好！
   ```

**输入输出设计的原则**：
- ✅ 提示信息清晰
- ✅ 输入格式简单
- ✅ 输出结果直观
- ✅ 提供退出选项

#### 第3步：设计主要步骤（Design Main Steps）

**核心问题**：
- 程序的主要步骤是什么？
- 用什么控制结构？

**方法**：使用**伪代码**（Pseudocode）

**什么是伪代码**：
- 介于自然语言和编程语言之间的描述
- 不需要语法正确
- 重点是把逻辑说清楚

**举例**：猜数字游戏的伪代码

```python
# 伪代码：猜数字游戏

1. 生成一个1-100的随机数
2. 初始化猜测次数为0
3. 循环：
   3.1 提示用户输入猜测
   3.2 如果用户输入q，退出循环
   3.3 验证输入是否为有效数字
   3.4 猜测次数加1
   3.5 比较猜测和目标数字
       如果猜中：显示恭喜，退出循环
       如果太大：提示"太大"
       如果太小：提示"太小"
4. 显示游戏结果
```

**流程图表示**：

```
    开始
      ↓
生成随机数
      ↓
  初始化次数
      ↓
  ┌─────────┐
  │  循环   │←──────┐
  └─────────┘       │
      ↓             │
  获取用户输入      │
      ↓             │
  输入q? → 结束     │
      ↓ 否          │
  验证输入          │
      ↓             │
  次数+1            │
      ↓             │
  比较大小          │
      ↓             │
  猜中? → 是 → 结束  │
      ↓ 否          │
  提示大小 ─────────┘
```

#### 第4步：设计数据结构（Design Data Structures）

**核心问题**：
- 用什么变量存储数据？
- 用什么数据结构（列表、字典等）？

**方法**：

1. **列出需要的变量**
   ```python
   # 猜数字游戏需要的变量

   secret_number     # 目标数字（整数）
   guess_count       # 猜测次数（整数）
   user_input        # 用户输入（字符串）
   guess             # 猜测的数字（整数）
   is_correct        # 是否猜中（布尔值）
   ```

2. **确定数据结构**
   ```python
   # 简单情况：用基本变量
   secret_number = 50
   guess_count = 0

   # 复杂情况：用列表或字典
   # 如果要记录所有猜测历史
   guess_history = [50, 25, 37, 42]

   # 如果要记录多个玩家的成绩
   player_scores = {
       "小明": 5,
       "小红": 7
   }
   ```

**数据结构选择原则**：
- 数据量小 → 用基本变量
- 数据有顺序 → 用列表
- 数据需要查找 → 用字典

#### 第5步：设计验证方法（Design Verification）

**核心问题**：
- 如何验证程序是否正确？
- 需要测试哪些情况？

**方法**：

1. **设计测试用例**
   ```python
   # 猜数字游戏的测试用例

   测试用例1：正常情况
   - 目标数字：50
   - 猜测：30, 60, 40, 55, 45, 50
   - 预期输出：太小、太大、太小、太大、太小、正确

   测试用例2：边界情况
   - 目标数字：1
   - 猜测：0, 2, 1
   - 预期输出：无效、太大、正确

   测试用例3：错误输入
   - 目标数字：50
   - 猜测：abc, 50
   - 预期输出：提示输入有效数字、正确

   测试用例4：中途退出
   - 目标数字：50
   - 猜测：q
   - 预期输出：显示游戏结束和答案
   ```

2. **验证方法**
   ```python
   # 方法1：手工验证
   print("目标数字是：50")  # 调试输出
   # 手动输入各种测试数据

   # 方法2：自动测试
   def test_guess_number():
       # 模拟测试
       assert compare_guess(50, 30) == "太小"
       assert compare_guess(50, 60) == "太大"
       assert compare_guess(50, 50) == "正确"
       print("所有测试通过！")
   ```

### 综合案例：完整的设计过程

**题目**：设计一个"成绩管理系统"

#### 第1步：明确需求

```
功能需求：
1. 添加学生成绩
2. 查询学生成绩
3. 计算班级平均分
4. 找出最高分和最低分
5. 显示所有成绩

输入：
- 命令选择（1-5）
- 学生姓名
- 成绩分数

输出：
- 操作结果
- 成绩列表
- 统计信息
```

#### 第2步：设计输入输出

```python
# 输入设计
========== 成绩管理系统 ==========
1. 添加成绩
2. 查询成绩
3. 统计信息
4. 显示所有成绩
5. 退出
请选择操作（1-5）：_

# 输出设计
✓ 成绩添加成功！
✓ 查询结果：小明的成绩是85分

=== 班级统计 ===
学生人数：30
平均分：82.5
最高分：98（小红）
最低分：45（小刚）
```

#### 第3步：设计主要步骤（伪代码）

```python
# 伪代码

main:
    初始化成绩字典
    循环：
        显示菜单
        获取用户选择
        根据选择执行操作：
            1 → add_score()
            2 → query_score()
            3 → show_statistics()
            4 → show_all_scores()
            5 → 退出程序
        如果选择无效，提示错误

add_score:
    输入学生姓名
    输入成绩分数
    验证成绩范围（0-100）
    添加到字典
    显示成功消息

query_score:
    输入学生姓名
    在字典中查找
    如果找到，显示成绩
    如果没找到，提示不存在

show_statistics:
    如果字典为空，提示无数据
    否则：
        计算平均分
        找最高分
        找最低分
        显示统计结果
```

#### 第4步：设计数据结构

```python
# 数据结构设计

# 主数据结构：用字典存储成绩
# key: 学生姓名（字符串）
# value: 成绩分数（整数）
scores = {
    "小明": 85,
    "小红": 92,
    "小刚": 78
}

# 辅助变量
command = ""        # 用户命令
student_name = ""   # 学生姓名
score = 0          # 成绩分数
```

#### 第5步：设计验证方法

```python
# 测试用例

测试1：添加成绩
输入：小明，85
预期：添加成功，scores中有{"小明": 85}

测试2：查询成绩
输入：小明
预期：显示"小明的成绩是85分"

测试3：无效成绩
输入：小刚，150
预期：提示"成绩应该在0-100之间"

测试4：查询不存在的学生
输入：小华
预期：提示"找不到该学生"

测试5：统计信息
输入：scores = {"小明":85, "小红":92, "小刚":78}
预期：平均分=85，最高=92，最低=78
```

#### 完整代码实现

```python
def display_menu():
    """显示菜单"""
    print("\n========== 成绩管理系统 ==========")
    print("1. 添加成绩")
    print("2. 查询成绩")
    print("3. 统计信息")
    print("4. 显示所有成绩")
    print("5. 退出")
    print("=" * 30)

def add_score(scores):
    """添加成绩"""
    name = input("请输入学生姓名：")
    score_str = input("请输入成绩（0-100）：")

    # 验证输入
    if not score_str.isdigit():
        print("错误：请输入有效的数字！")
        return

    score = int(score_str)

    # 验证范围
    if score < 0 or score > 100:
        print("错误：成绩应该在0-100之间！")
        return

    # 添加成绩
    scores[name] = score
    print(f"✓ 成功添加{name}的成绩：{score}分")

def query_score(scores):
    """查询成绩"""
    name = input("请输入要查询的学生姓名：")

    if name in scores:
        print(f"✓ {name}的成绩是{scores[name]}分")
    else:
        print(f"✗ 找不到学生：{name}")

def show_statistics(scores):
    """显示统计信息"""
    if not scores:
        print("✗ 还没有成绩数据！")
        return

    score_list = list(scores.values())
    average = sum(score_list) / len(score_list)
    highest = max(score_list)
    lowest = min(score_list)

    # 找出最高分和最低分的学生
    highest_students = [name for name, score in scores.items() if score == highest]
    lowest_students = [name for name, score in scores.items() if score == lowest]

    print("\n=== 班级统计 ===")
    print(f"学生人数：{len(scores)}")
    print(f"平均分：{average:.2f}")
    print(f"最高分：{highest}分（{', '.join(highest_students)}）")
    print(f"最低分：{lowest}分（{', '.join(lowest_students)}）")

def show_all_scores(scores):
    """显示所有成绩"""
    if not scores:
        print("✗ 还没有成绩数据！")
        return

    print("\n=== 所有成绩 ===")
    for name, score in scores.items():
        print(f"{name}：{score}分")

def main():
    """主程序"""
    scores = {}  # 存储成绩的字典

    while True:
        display_menu()
        command = input("请选择操作（1-5）：")

        if command == "1":
            add_score(scores)
        elif command == "2":
            query_score(scores)
        elif command == "3":
            show_statistics(scores)
        elif command == "4":
            show_all_scores(scores)
        elif command == "5":
            print("感谢使用成绩管理系统！")
            break
        else:
            print("✗ 无效的选择，请输入1-5之间的数字！")

if __name__ == "__main__":
    main()
```

### 练习3：设计程序

按照上述五个步骤，设计一个"图书馆借阅系统"。

**需求**：
- 添加图书（书名、作者）
- 借阅图书（记录借阅人）
- 归还图书
- 查询图书状态
- 显示所有图书

请写出：
1. 需求分析
2. 输入输出设计
3. 主要步骤（伪代码）
4. 数据结构设计
5. 测试用例

<details>
<summary>📝 查看设计参考</summary>

```python
# 1. 需求分析

功能需求：
- 添加图书：输入书名和作者，添加到图书馆
- 借阅图书：输入书名和借阅人，记录借阅
- 归还图书：输入书名，清除借阅信息
- 查询图书：输入书名，显示图书状态（在馆/借出）
- 显示所有图书：列出所有图书及状态

# 2. 输入输出设计

========== 图书馆管理系统 ==========
1. 添加图书
2. 借阅图书
3. 归还图书
4. 查询图书
5. 显示所有图书
6. 退出
请选择操作（1-6）：_

# 3. 主要步骤（伪代码）

main:
    初始化图书字典
    循环：
        显示菜单
        获取用户选择
        根据选择执行操作
        如果选择6，退出程序

add_book:
    输入书名
    输入作者
    添加到字典
    标记为"在馆"

borrow_book:
    输入书名
    输入借阅人
    如果图书在馆：
        标记为"借出"
        记录借阅人
    否则：
        提示图书已借出

return_book:
    输入书名
    如果图书已借出：
        标记为"在馆"
        清除借阅人
    否则：
        提示图书在馆

query_book:
    输入书名
    如果图书存在：
        显示书名、作者、状态
        如果已借出，显示借阅人
    否则：
        提示图书不存在

# 4. 数据结构设计

books = {
    "书名": {
        "author": "作者名",
        "borrower": "借阅人",  # None表示在馆
        "is_borrowed": False   # False表示在馆
    }
}

# 5. 测试用例

测试1：添加图书
输入：Python编程，小明
预期：成功添加，状态为"在馆"

测试2：借阅图书
输入：Python编程，小红
预期：成功借阅，借阅人为"小红"

测试3：重复借阅
输入：Python编程，小刚
预期：提示"图书已被小红借出"

测试4：归还图书
输入：Python编程
预期：成功归还，状态为"在馆"

测试5：查询不存在的图书
输入：Java编程
预期：提示"图书不存在"
```
</details>

---

## 17.4 综合实践：重写之前的程序

现在我们已经学习了程序设计的理论，让我们用这些知识来改进之前写过的程序！

### 案例1：改进"猜数字游戏"

**回顾**：你在第8章学过猜数字游戏

**原始版本**（可能的样子）：
```python
import random

n = random.randint(1, 100)
c = 0

while True:
    g = input("请输入数字：")
    if g == 'q':
        break

    g = int(g)
    c = c + 1

    if g > n:
        print("太大了")
    elif g < n:
        print("太小")
    else:
        print("对了")
        break

print(c)
```

**问题分析**：
- ❌ 变量命名不清晰（n, c, g）
- ❌ 没有输入验证
- ❌ 没有注释
- ❌ 用户提示不友好
- ❌ 输出格式简陋

**改进版本**：
```python
import random

def guess_number_game():
    """猜数字游戏 - 猜一个1到100之间的随机数"""

    print("=== 猜数字游戏 ===")
    print("我已经想好了一个1到100之间的数字")
    print("你能猜到它是多少吗？")
    print("(输入q可以随时退出)\n")

    # 生成随机数
    secret_number = random.randint(1, 100)
    guess_count = 0
    guess_history = []  # 记录猜测历史

    while True:
        # 获取用户输入
        user_input = input(f"第{guess_count + 1}次猜测，请输入数字：")

        # 检查是否退出
        if user_input.lower() == 'q':
            print(f"\n游戏结束！正确答案是：{secret_number}")
            return

        # 验证输入
        if not user_input.isdigit():
            print("请输入一个有效的数字！\n")
            continue

        guess = int(user_input)

        # 验证范围
        if guess < 1 or guess > 100:
            print("请输入1到100之间的数字！\n")
            continue

        # 记录猜测
        guess_count += 1
        guess_history.append(guess)

        # 比较大小
        if guess > secret_number:
            print(f"{guess} 太大了！")
        elif guess < secret_number:
            print(f"{guess} 太小了！")
        else:
            print(f"\n🎉 恭喜你！{guess} 就是正确答案！")
            print(f"你总共猜了 {guess_count} 次")

            # 显示猜测历史
            if guess_count > 1:
                print(f"猜测历史：{guess_history}")
            break

        # 提供提示
        print()

if __name__ == "__main__":
    guess_number_game()
```

**改进点**：
- ✅ 清晰的函数名和变量名
- ✅ 完整的文档字符串
- ✅ 输入验证（数字、范围）
- ✅ 友好的用户界面
- ✅ 猜测历史记录
- ✅ 退出功能
- ✅ 格式化输出

### 案例2：改进"计算器程序"

**原始版本**（可能的样子）：
```python
n1 = int(input("第1个数："))
n2 = int(input("第2个数："))
op = input("运算符：")

if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "*":
    print(n1 * n2)
elif op == "/":
    print(n1 / n2)
```

**问题分析**：
- ❌ 没有除零检查
- ❌ 没有输入验证
- ❌ 没有循环功能
- ❌ 输出简陋

**改进版本**：
```python
def calculator():
    """简单计算器 - 支持加减乘除运算"""

    print("=== 简单计算器 ===")
    print("支持的运算：+ - * /")
    print("输入q退出\n")

    while True:
        try:
            # 获取第一个数字
            num1_str = input("请输入第一个数字：")
            if num1_str.lower() == 'q':
                break

            num1 = float(num1_str)

            # 获取运算符
            operator = input("请输入运算符（+ - * /）：")
            if operator not in ['+', '-', '*', '/']:
                print("无效的运算符！请输入 + - * /\n")
                continue

            # 获取第二个数字
            num2_str = input("请输入第二个数字：")
            num2 = float(num2_str)

            # 计算结果
            result = None
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                # 除零检查
                if num2 == 0:
                    print("错误：不能除以零！\n")
                    continue
                result = num1 / num2

            # 显示结果
            print(f"结果：{num1} {operator} {num2} = {result}\n")

        except ValueError:
            print("错误：请输入有效的数字！\n")

if __name__ == "__main__":
    calculator()
```

**改进点**：
- ✅ 支持小数计算（使用float）
- ✅ 除零检查
- ✅ 输入验证（try-except）
- ✅ 循环功能
- ✅ 格式化输出
- ✅ 退出功能

### 练习4：改进你自己的程序

从你之前写过的程序中选择一个（例如：
- 长方形计算器（第2章）
- 温度转换器（第4章）
- 水仙花数程序（第8章）
- 课表查询系统（第14章）

按照以下步骤进行改进：

1. **评价原始程序**
   - 用五个维度评价
   - 列出所有问题

2. **设计改进方案**
   - 改进变量命名
   - 添加输入验证
   - 改进用户界面
   - 添加错误处理

3. **重写程序**
   - 应用本章学到的知识
   - 使用函数封装
   - 添加注释

4. **测试程序**
   - 设计测试用例
   - 验证各种情况

---

## 17.5 常见错误和调试

### 常见的程序设计错误

#### 错误1：过早优化（Premature Optimization）

**表现**：
- 还没让程序运行起来，就开始考虑"怎么让它更快"
- 为了"效率"牺牲了可读性

**例子**：
```python
# ❌ 过早优化的例子
# 为了节省一行代码，牺牲了可读性
result = (lambda x: x * x)(int(input("输入数字：")))
print(result)

# ✅ 先让它能运行，再考虑优化
user_input = input("输入数字：")
number = int(user_input)
result = number * number
print(result)
```

**建议**：
- "Make it work, make it right, make it fast"
- 先让它能运行，再让它运行正确，最后才考虑让它运行得快
- 对于初学者，可读性 > 效率

#### 错误2：过度设计（Over-Engineering）

**表现**：
- 为简单的问题设计复杂的解决方案
- "用大炮打蚊子"

**例子**：
```python
# ❌ 过度设计的例子
# 一个简单的加法程序，却用了复杂的架构

class NumberAdder:
    """数字加加器类"""
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def calculate_sum(self):
        return sum(self.numbers)

def main():
    adder = NumberAdder()
    adder.add_number(10)
    adder.add_number(20)
    result = adder.calculate_sum()
    print(result)

main()

# ✅ 简单直接的设计
num1 = 10
num2 = 20
result = num1 + num2
print(result)
```

**建议**：
- 简单问题用简单方案
- 只在需要时才引入复杂结构
- KISS原则：Keep It Simple, Stupid

#### 错误3：重复代码（Code Duplication）

**表现**：
- 相同的代码在程序中出现多次
- 不知道如何使用函数

**例子**：
```python
# ❌ 重复代码
area1 = length1 * width1
area2 = length2 * width2
area3 = length3 * width3
area4 = length4 * width4

# ✅ 使用函数
def calculate_area(length, width):
    return length * width

area1 = calculate_area(length1, width1)
area2 = calculate_area(length2, width2)
area3 = calculate_area(length3, width3)
area4 = calculate_area(length4, width4)
```

**建议**：
- 遵循DRY原则：Don't Repeat Yourself
- 相同的代码出现3次，就该考虑用函数

#### 错误4：魔法数字（Magic Numbers）

**表现**：
- 代码中出现没有解释的数字
- 不知道这些数字是什么意思

**例子**：
```python
# ❌ 魔法数字
area = 3.14159 * radius * radius
if score >= 60:
    print("及格")

# ✅ 使用命名常量
PI = 3.14159
PASSING_SCORE = 60

area = PI * radius * radius
if score >= PASSING_SCORE:
    print("及格")
```

**建议**：
- 给重要的数字起个名字
- 使用全大写字母命名常量
- 常量定义在程序开头

#### 错误5：忽略错误处理（No Error Handling）

**表现**：
- 假设用户总是输入正确
- 程序遇到错误就崩溃

**例子**：
```python
# ❌ 没有错误处理
age = int(input("请输入年龄："))
print(f"你明年{age + 1}岁")

# ✅ 添加错误处理
try:
    age = int(input("请输入年龄："))
    if age < 0 or age > 150:
        print("年龄应该在0-150之间")
    else:
        print(f"你明年{age + 1}岁")
except ValueError:
    print("请输入有效的数字！")
```

**建议**：
- 永远不要相信用户输入
- 使用try-except捕获异常
- 验证输入的有效性

### 调试技巧

#### 技巧1：使用print调试

**方法**：在关键位置打印变量值

```python
def calculate_average(scores):
    print(f"[DEBUG] scores = {scores}")  # 调试输出

    if not scores:
        print("[DEBUG] Empty list!")
        return 0

    total = sum(scores)
    print(f"[DEBUG] total = {total}")  # 调试输出

    count = len(scores)
    print(f"[DEBUG] count = {count}")  # 调试输出

    average = total / count
    print(f"[DEBUG] average = {average}")  # 调试输出

    return average
```

**优点**：
- 简单直接
- 不需要额外工具
- 适合快速定位问题

**缺点**：
- 需要手动添加和删除
- 调试完成后要清理代码

**给家长的小贴士**：
- 教导孩子："不知道哪里出错，就打印出来看看"
- 建议使用统一的格式，如`[DEBUG]`
- 调试完成后记得删除或注释掉

#### 技巧2：逐步测试

**方法**：不要等程序全部写完才测试，每写一段就测试

```python
# 第1步：测试基本功能
def calculate_area(length, width):
    return length * width

# 立即测试
print(calculate_area(10, 20))  # 应该输出200

# 第2步：添加输入验证
def calculate_area(length, width):
    if length <= 0 or width <= 0:
        return 0
    return length * width

# 再次测试
print(calculate_area(10, 20))    # 200
print(calculate_area(-10, 20))  # 0

# 第3步：添加文档和优化
def calculate_area(length, width):
    """计算长方形面积

    Args:
        length: 长度
        width: 宽度

    Returns:
        面积，如果输入无效则返回0
    """
    if length <= 0 or width <= 0:
        return 0
    return length * width
```

**优点**：
- 问题容易定位
- 每一步都是正确的
- 积累成就感

**给家长的小贴士**：
- 鼓励孩子"写一点，测一点"
- 不要等到全部写完才运行
- 这能培养孩子的"增量开发"习惯

#### 技巧3：使用断言（Assertion）

**方法**：用assert语句检查假设

```python
def calculate_average(scores):
    """计算平均分"""
    assert isinstance(scores, list), "scores必须是列表"
    assert len(scores) > 0, "scores不能为空"

    total = sum(scores)
    assert total >= 0, "总分不能为负数"

    average = total / len(scores)
    assert 0 <= average <= 100, f"平均分{average}超出范围"

    return average

# 测试
print(calculate_average([80, 90, 85]))  # 正常
# print(calculate_average([]))          # 触发断言错误
```

**优点**：
- 能快速发现逻辑错误
- 文档化代码的假设
- 调试后可以选择禁用

**使用场景**：
- 检查函数的输入
- 验证计算结果
- 确保不变式成立

#### 技巧4：简化问题

**方法**：遇到复杂问题时，先用简单版本复现

```python
# 复杂版本：计算n个班级的平均分
def calculate_all_classes_average(students):
    result = {}
    for class_name, class_students in students.items():
        # 复杂的计算...
        pass

# 简化版本：先计算一个班级
def calculate_one_class_average(scores):
    return sum(scores) / len(scores)

# 测试简化版本
print(calculate_one_class_average([80, 90, 85]))  # 确保正确

# 再逐步扩展到复杂版本
```

**优点**：
- 降低问题复杂度
- 容易找到问题所在
- 逐步构建解决方案

**给家长的小贴士**：
- 告诉孩子："太复杂了就先简化"
- 从最简单的情况开始
- 这能培养孩子的"问题分解"能力

---

## 17.6 本章小结

### 核心知识点回顾

#### 1. 程序评价的五个维度

| 维度 | 评价标准 | 重要性 |
|------|---------|--------|
| **正确性** | 能否正确解决问题 | ⭐⭐⭐⭐⭐ |
| **可读性** | 是否容易理解 | ⭐⭐⭐⭐ |
| **可维护性** | 是否容易修改 | ⭐⭐⭐⭐ |
| **健壮性** | 是否容易出错 | ⭐⭐⭐⭐ |
| **效率** | 是否运行快速 | ⭐⭐⭐ |

#### 2. 变量设计的三个原则

1. **职责明确**：一个变量只承担一个职责
2. **命名规范**：变量名要能"自解释"
3. **作用域最小化**：变量的作用范围越小越好

#### 3. 程序设计的五个步骤

```
第1步：明确需求（做什么）
   ↓
第2步：设计输入输出（怎么交互）
   ↓
第3步：设计主要步骤（怎么做）
   ↓
第4步：设计数据结构（用什么数据）
   ↓
第5步：设计验证方法（怎么验证）
```

#### 4. 常见错误

- ❌ 过早优化
- ❌ 过度设计
- ❌ 重复代码
- ❌ 魔法数字
- ❌ 忽略错误处理

#### 5. 调试技巧

- ✅ 使用print调试
- ✅ 逐步测试
- ✅ 使用断言
- ✅ 简化问题

### 能力检查表

完成本章学习后，请检查你是否具备以下能力：

- [ ] 能用五个维度评价一个程序的好坏
- [ ] 能设计职责明确、命名规范的变量
- [ ] 能按照五个步骤设计程序
- [ ] 能使用伪代码和流程图设计算法
- [ ] 能改进自己之前写的程序
- [ ] 能识别和避免常见的程序设计错误
- [ ] 能使用调试技巧定位问题

### 给家长的小贴士：如何培养孩子的程序设计能力

#### 1. 从小程序开始

**不要**：一开始就要求孩子写出"完美"的程序

**应该**：
- 先让程序能运行
- 再逐步改进
- 最后追求完美

**比喻**：学写作文
- 小学1年级：写通顺句子
- 小学3年级：写完整段落
- 小学6年级：写完整文章
- 不能要求1年级学生写出6年级水平的作文

#### 2. 培养评价能力

**活动建议**：
- 让孩子"代码审查"：找出家长写的程序的问题
- 对比两个程序：哪个更好？为什么？
- 重构练习：改进之前写的程序

**目的**：
- 培养"批判性思维"
- 学会识别"好代码"和"坏代码"
- 建立"质量意识"

#### 3. 强调设计过程

**不要**：看到题目就让孩子直接写代码

**应该**：
- 先讨论：这个程序要做什么？
- 再设计：用什么数据结构？什么算法？
- 最后实现：编写代码
- 测试验证：是否正确？

**比喻**：
- 建房子：先设计图纸，再施工
- 写作文：先列提纲，再写作
- 编程也是一样：先设计，再编程

#### 4. 鼓励持续改进

**活动建议**：
- 定期回顾：这周写的程序，下周再看，能不能改进？
- 版本对比：版本1、版本2、版本3，哪个最好？
- 最佳实践：总结好的做法，形成"编程规范"

**目的**：
- 培养"精益求精"的态度
- 学会从"能运行"到"写得好"
- 建立"持续改进"的习惯

---

## 17.7 挑战练习

### 挑战1：代码审查 ⭐⭐

审查以下程序，找出所有问题并改进：

```python
a = input("名字")
b = int(input("年龄"))
c = int(input("成绩"))
if c >= 60:
    print("及格")
else:
    print("不及格")
print(c / b)
```

**要求**：
1. 用五个维度评价
2. 指出所有问题
3. 重写程序
4. 说明改进点

<details>
<summary>📝 查看参考答案</summary>

**评价结果**：

| 维度 | 评分 | 问题 |
|------|------|------|
| 正确性 | ⭐⭐⭐ | 基本正确，但除法可能有问题 |
| 可读性 | ⭐ | 变量名不清晰，无注释 |
| 可维护性 | ⭐⭐ | 无函数封装 |
| 健壮性 | ⭐ | 无输入验证 |
| 效率 | ⭐⭐⭐⭐ | 效率可以接受 |

**问题列表**：
1. 变量名a, b, c不清晰
2. 没有提示信息
3. 没有输入验证
4. 成绩除以年龄没有意义（可能是bug）
5. 没有注释
6. 没有函数封装

**改进版本**：
```python
def print_student_status():
    """打印学生状态"""

    # 获取学生信息
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄：")
    score = input("请输入学生成绩：")

    # 验证输入
    if not age.isdigit() or not score.isdigit():
        print("错误：年龄和成绩必须是数字！")
        return

    age = int(age)
    score = int(score)

    # 验证范围
    if age < 0 or age > 150:
        print("错误：年龄应该在0-150之间！")
        return

    if score < 0 or score > 100:
        print("错误：成绩应该在0-100之间！")
        return

    # 判断是否及格
    if score >= 60:
        status = "及格"
    else:
        status = "不及格"

    # 输出结果
    print(f"\n=== 学生信息 ===")
    print(f"姓名：{name}")
    print(f"年龄：{age}岁")
    print(f"成绩：{score}分")
    print(f"状态：{status}")

if __name__ == "__main__":
    print_student_status()
```

**改进点**：
- ✅ 清晰的变量命名
- ✅ 完整的输入提示
- ✅ 输入验证（数字、范围）
- ✅ 格式化输出
- ✅ 函数封装
- ✅ 注释说明
</details>

### 挑战2：重构程序 ⭐⭐⭐

重构以下程序，应用本章学到的知识：

```python
l = 10
w = 20
h = 5
s1 = l * w
s2 = l * h
s3 = w * h
print(s1, s2, s3)
print(s1 + s2 + s3)
```

**要求**：
1. 给变量起好名字
2. 添加注释
3. 封装成函数
4. 添加输入验证
5. 改进输出格式

<details>
<summary>📝 查看参考答案</summary>

```python
def calculate_surface_area(length, width, height):
    """计算长方体的表面积

    Args:
        length: 长度
        width: 宽度
        height: 高度

    Returns:
        表面积
    """
    # 计算三个面的面积
    area1 = length * width   # 顶面和底面
    area2 = length * height  # 前面和后面
    area3 = width * height   # 左面和右面

    # 表面积 = 2 × (三个面的面积之和)
    surface_area = 2 * (area1 + area2 + area3)

    return surface_area

def get_positive_number(prompt):
    """获取一个正数

    Args:
        prompt: 输入提示

    Returns:
        用户输入的正数
    """
    while True:
        user_input = input(prompt)

        if not user_input.isdigit():
            print("请输入一个有效的数字！")
            continue

        number = float(user_input)

        if number <= 0:
            print("请输入一个大于0的数字！")
            continue

        return number

def main():
    """主程序"""
    print("=== 长方体表面积计算器 ===")

    # 获取长宽高
    length = get_positive_number("请输入长度：")
    width = get_positive_number("请输入宽度：")
    height = get_positive_number("请输入高度：")

    # 计算表面积
    surface_area = calculate_surface_area(length, width, height)

    # 显示结果
    print(f"\n=== 计算结果 ===")
    print(f"长方体尺寸：{length} × {width} × {height}")
    print(f"表面积：{surface_area:.2f}")

if __name__ == "__main__":
    main()
```
</details>

### 挑战3：设计程序 ⭐⭐⭐⭐

按照程序设计的五个步骤，设计一个"密码强度检查器"：

**功能需求**：
- 输入密码
- 检查密码强度（弱/中/强）
- 显示改进建议
- 直到输入强密码为止

**要求**：
1. 完成五个步骤的设计
2. 实现完整程序
3. 编写测试用例
4. 提供改进建议

**强度判断标准**：
- 弱：长度<8或只有数字或只有字母
- 中：长度>=8且包含数字和字母
- 强：长度>=12且包含数字、字母和特殊字符

<details>
<summary>📝 查看参考答案</summary>

**第1步：明确需求**

```
功能需求：
1. 输入密码
2. 检查密码强度
3. 显示强度等级
4. 提供改进建议
5. 循环直到输入强密码

输入：
- 密码（字符串）

输出：
- 强度等级（弱/中/强）
- 改进建议

边界情况：
- 空字符串
- 只有数字
- 只有字母
- 包含特殊字符
```

**第2步：设计输入输出**

```python
=== 密码强度检查器 ===
请输入密码：******

强度：弱
建议：
- 密码长度至少8位
- 包含数字和字母
- 包含特殊字符

请重新输入密码：******

强度：强
✓ 密码符合要求！
```

**第3步：设计主要步骤（伪代码）**

```python
main:
    循环：
        输入密码
        检查强度
        显示强度和建议
        如果是强密码：
            退出循环

check_password_strength:
    如果长度<8：
        返回"弱"
    如果只有数字或只有字母：
        返回"弱"
    如果长度>=8且包含数字和字母：
        返回"中"
    如果长度>=12且包含数字、字母和特殊字符：
        返回"强"

get_suggestions:
    根据密码的问题提供建议
    - 如果太短，建议增加长度
    - 如果只有数字，建议添加字母
    - 如果只有字母，建议添加数字
    - 如果没有特殊字符，建议添加特殊字符
```

**第4步：设计数据结构**

```python
password = ""           # 密码（字符串）
length = 0             # 长度（整数）
has_digit = False      # 包含数字（布尔）
has_letter = False     # 包含字母（布尔）
has_special = False    # 包含特殊字符（布尔）
strength = ""          # 强度（字符串）
suggestions = []       # 建议列表
```

**第5步：设计验证方法**

```python
测试用例1：弱密码
输入：123
预期：弱（太短）

测试用例2：弱密码
输入：abcdefg
预期：弱（太短且只有字母）

测试用例3：弱密码
输入：12345678
预期：弱（只有数字）

测试用例4：中等密码
输入：abc12345
预期：中

测试用例5：强密码
输入：abc123!@#XYZ
预期：强
```

**完整实现**：

```python
def check_password_strength(password):
    """检查密码强度

    Args:
        password: 要检查的密码

    Returns:
        (strength, suggestions): 强度等级和建议列表
    """
    suggestions = []

    # 检查长度
    if len(password) < 8:
        suggestions.append("密码长度至少8位")
        return "弱", suggestions

    # 检查是否包含数字
    has_digit = any(char.isdigit() for char in password)

    # 检查是否包含字母
    has_letter = any(char.isalpha() for char in password)

    # 检查是否包含特殊字符
    has_special = any(not char.isalnum() for char in password)

    # 判断强度
    if not has_digit or not has_letter:
        suggestions.append("密码应同时包含数字和字母")
        if not has_digit:
            suggestions.append("建议添加数字")
        if not has_letter:
            suggestions.append("建议添加字母")
        return "弱", suggestions

    if len(password) >= 12 and has_special:
        suggestions.append("密码很安全！")
        return "强", suggestions

    if len(password) >= 8 and has_digit and has_letter:
        suggestions.append("建议增加到12位以上")
        suggestions.append("建议添加特殊字符（如!@#）")
        return "中", suggestions

    return "弱", ["密码不符合要求"]

def password_strength_checker():
    """密码强度检查器主程序"""
    print("=== 密码强度检查器 ===")
    print("密码要求：")
    print("- 长度至少8位")
    print("- 包含数字和字母")
    print("- 强密码要求12位以上且包含特殊字符")
    print()

    while True:
        password = input("请输入密码（输入q退出）：")

        if password.lower() == 'q':
            print("已退出")
            break

        if not password:
            print("密码不能为空！\n")
            continue

        # 检查强度
        strength, suggestions = check_password_strength(password)

        # 显示结果
        print(f"\n强度：{strength}")

        if strength == "强":
            print("✓ " + "\n✓ ".join(suggestions))
            print()
            break
        else:
            print("建议：")
            for suggestion in suggestions:
                print(f"- {suggestion}")
            print()

def test_password_checker():
    """测试密码强度检查器"""
    test_cases = [
        ("123", "弱"),
        ("abcdefg", "弱"),
        ("12345678", "弱"),
        ("abc12345", "中"),
        ("abc123!@#XYZ", "强"),
    ]

    print("=== 测试密码强度检查器 ===")
    for password, expected in test_cases:
        strength, _ = check_password_strength(password)
        status = "✓" if strength == expected else "✗"
        print(f"{status} '{password}' -> {strength} (期望: {expected})")

if __name__ == "__main__":
    # 运行测试
    test_password_checker()
    print()

    # 运行主程序
    password_strength_checker()
```
</details>

### 挑战4：改进你自己的程序 ⭐⭐⭐⭐⭐

选择你之前写过的一个程序（例如：课表查询系统、猜数字游戏、水仙花数等），按照以下步骤进行改进：

1. **评价原始程序**
   - 用五个维度评价
   - 列出所有问题

2. **设计改进方案**
   - 改进变量命名
   - 添加输入验证
   - 改进用户界面
   - 添加错误处理
   - 使用函数封装

3. **重写程序**
   - 应用本章学到的知识
   - 添加注释
   - 改进结构

4. **对比版本**
   - 列出改进前后的对比
- 说明改进理由

5. **编写测试**
   - 设计测试用例
   - 验证各种情况
