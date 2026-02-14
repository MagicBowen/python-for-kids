# 第11章 数据结构：字典

## 引言

想象一下，你在学校里有一个储物柜。每个储物柜都有一个编号，你可以在里面放东西。要用储物柜，你需要记住你的柜子号码，这样就能快速找到你的东西。

在Python中，有一种和储物柜很像的数据结构，叫做"字典"（Dictionary）。字典让我们能够用"钥匙"（key）来找到对应的"值"（value），就像用储物柜的号码来找到里面的东西一样。

**给家长的小贴士**：可以用"电话簿"、"字典查词"、"储物柜"等生活中的例子来类比字典，帮助孩子理解"键-值"对的概念。

---

## 什么是字典

字典是Python中的一种数据结构，它存储的是"键-值"对（key-value pairs）。

### 键和值的概念

- **键（key）**：就像储物柜的编号，用来唯一标识一个值
- **值（value）**：就像储物柜里放的东西，是我们真正想要存储的数据

比如，我们想存储几个同学的身高：

```python
# 创建一个字典
heights = {"小明": 150, "小红": 145, "小华": 152}

# 访问字典中的值
print(heights["小明"])  # 输出: 150
```

在这个例子中：
- "小明"、"小红"、"小华" 是键（key）
- 150、145、152 是值（value）
- 整个 `{"小明": 150, "小红": 145, "小华": 152}` 叫做"键-值对"

### 字典与列表的区别

| 特点 | 列表 | 字典 |
|------|------|------|
| 索引 | 数字索引（0, 1, 2...） | 任意不可变类型的键 |
| 访问 | `list[0]` | `dict["key"]` |
| 顺序 | 有序 | 无序（Python 3.7+有序） |
| 用途 | 按顺序存储数据 | 按键值对存储数据 |

**给家长的小贴士**：可以告诉孩子，列表像是一排编号的盒子，你必须记住号码才能找到东西；而字典像是给每个盒子贴了标签，你可以直接通过标签找到东西。

---

## 创建字典

### 方法一：直接创建

```python
# 创建一个空字典
empty_dict = {}

# 创建一个有内容的字典
student = {"name": "小明", "age": 12, "grade": 6}
```

### 方法二：使用dict()函数

```python
# 使用dict()函数创建
student = dict(name="小明", age=12, grade=6)

print(student)
# 输出: {'name': '小明', 'age': 12, 'grade': 6}
```

**给家长的小贴士**：这两种方法创建的字典是一样的，第一种方法更常用，特别是在处理复杂数据结构时。

---

## 访问字典中的值

### 使用键访问值

```python
scores = {"语文": 95, "数学": 98, "英语": 88}

# 访问语文成绩
print(scores["语文"])  # 输出: 95

# 访问数学成绩
print(scores["数学"])  # 输出: 98
```

### 处理键不存在的情况

如果我们访问一个不存在的键，程序会报错：

```python
scores = {"语文": 95, "数学": 98, "英语": 88}

# 这行代码会报错！KeyError
print(scores["科学"])
```

为了避免这种情况，我们有两种方法：

#### 方法1：使用in检查键是否存在

```python
scores = {"语文": 95, "数学": 98, "英语": 88}

subject = "科学"
if subject in scores:
    print(scores[subject])
else:
    print(f"没有{subject}这门课的成绩")
```

#### 方法2：使用get()方法

```python
scores = {"语文": 95, "数学": 98, "英语": 88}

# 使用get方法，如果键不存在，返回None
print(scores.get("科学"))  # 输出: None

# 使用get方法，如果键不存在，返回默认值
print(scores.get("科学", "没有这门课"))  # 输出: 没有这门课
```

**给家长的小贴士**：`get()`方法更安全，建议孩子养成使用`get()`的习惯，特别是在处理用户输入时。

---

## 添加和修改字典元素

### 添加新的键值对

```python
# 创建一个空字典
phone_book = {}

# 添加新的联系人
phone_book["小明"] = "123-4567"
phone_book["小红"] = "234-5678"

print(phone_book)
# 输出: {'小明': '123-4567', '小红': '234-5678'}
```

### 修改现有的值

```python
scores = {"语文": 95, "数学": 98, "英语": 88}

# 修改语文成绩
scores["语文"] = 99

print(scores)
# 输出: {'语文': 99, '数学': 98, '英语': 88}
```

**给家长的小贴士**：在Python中，添加新元素和修改现有元素的语法是一样的。如果键不存在，就是添加；如果键已存在，就是修改。

---

## 删除字典元素

### 方法1：使用del语句

```python
scores = {"语文": 95, "数学": 98, "英语": 88}

# 删除语文成绩
del scores["语文"]

print(scores)
# 输出: {'数学': 98, '英语': 88}
```

### 方法2：使用pop()方法

```python
scores = {"语文": 95, "数学": 98, "英语": 88}

# 删除并返回数学成绩
math_score = scores.pop("数学")
print(math_score)  # 输出: 98
print(scores)       # 输出: {'语文': 95, '英语': 88}
```

### 方法3：使用popitem()方法

```python
scores = {"语文": 95, "数学": 98, "英语": 88}

# 删除并返回最后一个键值对（Python 3.7+）
last_item = scores.popitem()
print(last_item)  # 输出: ('英语', 88)
print(scores)     # 输出: {'语文': 95, '数学': 98}
```

**给家长的小贴士**：提醒孩子，`del`语句直接删除，不会返回值；`pop()`方法会返回被删除的值，可以在需要使用这个值的时候使用。

---

## 字典的常用操作

### 获取所有键、所有值、所有键值对

```python
scores = {"语文": 95, "数学": 98, "英语": 88}

# 获取所有键
print(scores.keys())    # 输出: dict_keys(['语文', '数学', '英语'])

# 获取所有值
print(scores.values())  # 输出: dict_values([95, 98, 88])

# 获取所有键值对
print(scores.items())   # 输出: dict_items([('语文', 95), ('数学', 98), ('英语', 88)])
```

### 获取字典的长度

```python
scores = {"语文": 95, "数学": 98, "英语": 88}

print(len(scores))  # 输出: 3
```

### 检查键是否存在

```python
scores = {"语文": 95, "数学": 98, "英语": 88}

# 使用in检查
print("语文" in scores)   # 输出: True
print("科学" in scores)   # 输出: False

# 使用not in检查
print("语文" not in scores)  # 输出: False
```

### 清空字典

```python
scores = {"语文": 95, "数学": 98, "英语": 88}

# 清空字典
scores.clear()

print(scores)  # 输出: {}
```

**给家长的小贴士**：`keys()`、`values()`、`items()`返回的是视图对象，不是列表。如果需要列表，可以用`list()`转换：`list(scores.keys())`

---

## 遍历字典

### 遍历所有键

```python
scores = {"语文": 95, "数学": 98, "英语": 88}

# 方法1：直接遍历字典（遍历的是键）
for subject in scores:
    print(subject)

# 输出:
# 语文
# 数学
# 英语

# 方法2：使用keys()方法（更明确）
for subject in scores.keys():
    print(subject)
```

### 遍历所有值

```python
scores = {"语文": 95, "数学": 98, "英语": 88}

for score in scores.values():
    print(score)

# 输出:
# 95
# 98
# 88
```

### 遍历所有键值对

```python
scores = {"语文": 95, "数学": 98, "英语": 88}

# 使用items()方法同时获取键和值
for subject, score in scores.items():
    print(f"{subject}: {score}分")

# 输出:
# 语文: 95分
# 数学: 98分
# 英语: 88分
```

**给家长的小贴士**：最常用的是`items()`方法，因为它能同时获取键和值，代码更简洁。

---

## 字典的常用方法

### update()方法 - 更新字典

```python
# 原字典
scores = {"语文": 95, "数学": 98}

# 新数据
new_scores = {"英语": 88, "数学": 100}

# 用new_scores更新scores
scores.update(new_scores)

print(scores)
# 输出: {'语文': 95, '数学': 100, '英语': 88}
```

### setdefault()方法 - 设置默认值

```python
scores = {"语文": 95, "数学": 98}

# 如果"英语"不存在，设置默认值85
english_score = scores.setdefault("英语", 85)
print(english_score)  # 输出: 85
print(scores)         # 输出: {'语文': 95, '数学': 98, '英语': 85}

# 如果"数学"已存在，不会修改
math_score = scores.setdefault("数学", 0)
print(math_score)     # 输出: 98
print(scores)         # 输出: {'语文': 95, '数学': 98, '英语': 85}
```

### fromkeys()方法 - 创建相同值的字典

```python
# 创建一个字典，所有值都是0
subjects = ["语文", "数学", "英语"]
scores = dict.fromkeys(subjects, 0)

print(scores)
# 输出: {'语文': 0, '数学': 0, '英语': 0}
```

### copy()方法 - 复制字典

```python
original = {"语文": 95, "数学": 98}

# 浅复制
copied = original.copy()

# 修改复制的字典
copied["英语"] = 88

print(original)  # 输出: {'语文': 95, '数学': 98}
print(copied)    # 输出: {'语文': 95, '数学': 98, '英语': 88}
```

**给家长的小贴士**：`copy()`方法很重要，因为它创建了一个独立的副本，不会影响原字典。直接赋值`new_dict = old_dict`只是创建了一个引用。

---

## 字典的键的要求

字典的键必须满足以下要求：

1. **键必须是不可变类型**：
   - 可以是：整数、浮点数、字符串、元组
   - 不能是：列表、字典

2. **键必须是唯一的**：
   - 如果有重复的键，后面的值会覆盖前面的值

```python
# 正确的键
dict1 = {1: "one", 2.5: "two point five", "hello": "world", (1, 2): "tuple key"}

# 错误的键（会报错）
# dict2 = {[1, 2]: "list key"}  # TypeError: 列表不能作为键

# 重复的键（后面的值会覆盖前面的）
dict3 = {"name": "小明", "name": "小红"}
print(dict3)  # 输出: {'name': '小红'}
```

**给家长的小贴士**：可以用"门牌号"来类比，门牌号是固定的、唯一的，就像字典的键。如果两个储物柜号码相同，就会造成混乱。

---

## 嵌套字典

字典的值可以是任意类型，包括另一个字典。这就是"嵌套字典"。

### 简单的嵌套字典

```python
# 存储学生信息
student = {
    "name": "小明",
    "age": 12,
    "address": {
        "city": "北京",
        "district": "朝阳区"
    }
}

# 访问嵌套字典
print(student["address"]["city"])  # 输出: 北京
```

### 复杂的嵌套字典

```python
# 存储多个学生的信息
students = {
    "001": {
        "name": "小明",
        "age": 12,
        "scores": {"语文": 95, "数学": 98}
    },
    "002": {
        "name": "小红",
        "age": 11,
        "scores": {"语文": 92, "数学": 99}
    }
}

# 访问小红的数学成绩
print(students["002"]["scores"]["数学"])  # 输出: 99
```

### 字典和列表的嵌套

```python
# 课程表：字典 + 列表的嵌套
schedule = {
    "星期一": ["语文", "数学", "英语"],
    "星期二": ["数学", "科学", "体育"],
    "星期三": ["语文", "美术", "音乐"]
}

# 访问星期二第二节课
print(schedule["星期二"][1])  # 输出: 科学
```

### 复杂的嵌套结构

```python
# 更复杂的课程表：多层嵌套
courses = {
    "MON": {
        "morning": ["数学", "英语", "绘画"],
        "afternoon": ["音乐", "体育"]
    },
    "TUE": {
        "morning": ["科学", "数学", "体育"],
        "afternoon": ["英语"]
    }
}

# 访问星期一上午第二节课
print(courses["MON"]["morning"][1])  # 输出: 英语

# 查看星期一下午课程的类型
print(type(courses["MON"]["afternoon"]))  # 输出: <class 'list'>

# 查看星期一上午第二节课的类型
print(type(courses["MON"]["morning"][1]))  # 输出: <class 'str'>
```

**给家长的小贴士**：嵌套结构理解起来比较困难，建议用"俄罗斯套娃"或"多层盒子"的类比。访问嵌套数据就像一层层打开盒子，每次只打开一层。

---

## 字典的排序

### 按键排序

```python
scores = {"语文": 95, "数学": 98, "英语": 88}

# 按键排序
sorted_keys = sorted(scores.keys())
print(sorted_keys)  # 输出: ['数学', '英语', '语文']

# 按排序后的顺序遍历
for subject in sorted_keys:
    print(f"{subject}: {scores[subject]}")

# 输出:
# 数学: 98
# 英语: 88
# 语文: 95
```

### 按值排序

```python
scores = {"语文": 95, "数学": 98, "英语": 88}

# 按值排序（从低到高）
sorted_items = sorted(scores.items(), key=lambda x: x[1])
print(sorted_items)  # 输出: [('英语', 88), ('语文', 95), ('数学', 98)]

# 按值排序（从高到低）
sorted_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(sorted_items)  # 输出: [('数学', 98), ('语文', 95), ('英语', 88)]
```

**给家长的小贴士**：lambda表达式对孩子来说比较抽象，可以简单地解释为"告诉Python按什么排序"。对于初学者，可以先跳过这个部分。

---

## 字典的应用案例

### 案例1：制作简单的翻译器

```python
# 英汉词典
dictionary = {
    "hello": "你好",
    "world": "世界",
    "python": "蟒蛇",
    "computer": "电脑"
}

# 翻译功能
word = input("请输入要翻译的英文单词: ")
translation = dictionary.get(word.lower(), "词典里没有这个单词")

print(f"翻译结果: {translation}")
```

### 案例2：统计字符出现次数

```python
# 统计字符串中每个字符出现的次数
text = "hello world"

# 创建空字典
char_count = {}

# 遍历字符串
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)
# 输出: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

### 案例3：制作简单的投票系统

```python
# 投票系统
votes = {}

while True:
    name = input("请输入要投票的同学的名字（输入'结束'退出）: ")

    if name == "结束":
        break

    # 使用get()方法，如果不存在则从0开始计数
    votes[name] = votes.get(name, 0) + 1
    print(f"{name}的票数: {votes[name]}")

# 输出最终结果
print("\n投票结果:")
for name, count in votes.items():
    print(f"{name}: {count}票")
```

### 案例4：学生成绩管理系统

```python
# 学生成绩管理系统
students = {}

while True:
    print("\n===== 成绩管理系统 =====")
    print("1. 添加学生")
    print("2. 查询学生")
    print("3. 显示所有学生")
    print("4. 退出")

    choice = input("请选择操作 (1-4): ")

    if choice == "1":
        # 添加学生
        name = input("请输入学生姓名: ")
        score = int(input("请输入学生成绩: "))
        students[name] = score
        print(f"已添加: {name}, 成绩: {score}")

    elif choice == "2":
        # 查询学生
        name = input("请输入要查询的学生姓名: ")
        if name in students:
            print(f"{name}的成绩是: {students[name]}")
        else:
            print("没有找到该学生")

    elif choice == "3":
        # 显示所有学生
        if students:
            print("\n所有学生成绩:")
            for name, score in students.items():
                print(f"{name}: {score}分")
        else:
            print("还没有添加学生")

    elif choice == "4":
        print("再见！")
        break

    else:
        print("无效的选择，请重新输入")
```

**给家长的小贴士**：这些案例都是很好的综合练习，可以让孩子自己尝试实现，然后再和示例代码对比，找出差异。

---

## 实践练习

### 练习1：简单的电话簿

创建一个电话簿程序，支持以下功能：
1. 添加联系人（姓名和电话）
2. 查询联系人
3. 显示所有联系人
4. 删除联系人

<details>
<summary>查看答案</summary>

```python
# 电话簿程序
phone_book = {}

while True:
    print("\n===== 电话簿 =====")
    print("1. 添加联系人")
    print("2. 查询联系人")
    print("3. 显示所有联系人")
    print("4. 删除联系人")
    print("5. 退出")

    choice = input("请选择操作 (1-5): ")

    if choice == "1":
        # 添加联系人
        name = input("请输入姓名: ")
        phone = input("请输入电话: ")
        phone_book[name] = phone
        print(f"已添加: {name}")

    elif choice == "2":
        # 查询联系人
        name = input("请输入要查询的姓名: ")
        if name in phone_book:
            print(f"{name}的电话: {phone_book[name]}")
        else:
            print("没有找到该联系人")

    elif choice == "3":
        # 显示所有联系人
        if phone_book:
            print("\n所有联系人:")
            for name, phone in phone_book.items():
                print(f"{name}: {phone}")
        else:
            print("电话簿是空的")

    elif choice == "4":
        # 删除联系人
        name = input("请输入要删除的联系人姓名: ")
        if name in phone_book:
            del phone_book[name]
            print(f"已删除: {name}")
        else:
            print("没有找到该联系人")

    elif choice == "5":
        print("再见！")
        break

    else:
        print("无效的选择，请重新输入")
```
</details>

### 练习2：单词统计器

编写一个程序，统计一段文本中每个单词出现的次数。

<details>
<summary>查看答案</summary>

```python
# 单词统计器
text = input("请输入一段文本: ")

# 分割成单词
words = text.split()

# 统计词频
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# 输出结果
print("\n单词出现次数:")
for word, count in sorted(word_count.items()):
    print(f"{word}: {count}次")
```
</details>

### 练习3：制作课程表

创建一个程序，管理一周的课程表。

<details>
<summary>查看答案</summary>

```python
# 课程表管理
schedule = {}

weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五"]

# 初始化课程表
for day in weekdays:
    schedule[day] = []

while True:
    print("\n===== 课程表管理 =====")
    print("1. 添加课程")
    print("2. 查看课程表")
    print("3. 退出")

    choice = input("请选择操作 (1-3): ")

    if choice == "1":
        # 添加课程
        for i, day in enumerate(weekdays):
            print(f"{i+1}. {day}")

        day_choice = int(input("请选择星期几 (1-5): ")) - 1
        course = input("请输入课程名称: ")
        schedule[weekdays[day_choice]].append(course)
        print(f"已添加: {weekdays[day_choice]} - {course}")

    elif choice == "2":
        # 查看课程表
        print("\n=== 本周课程表 ===")
        for day in weekdays:
            courses = schedule[day]
            if courses:
                courses_str = "、".join(courses)
                print(f"{day}: {courses_str}")
            else:
                print(f"{day}: 无课程")

    elif choice == "3":
        print("再见！")
        break

    else:
        print("无效的选择，请重新输入")
```
</details>

### 练习4：计算平均成绩

创建一个程序，管理多个学生的成绩，并计算平均分。

<details>
<summary>查看答案</summary>

```python
# 成绩管理系统
students = {}

while True:
    print("\n===== 成绩管理 =====")
    print("1. 添加学生成绩")
    print("2. 查看学生成绩")
    print("3. 查看班级平均分")
    print("4. 退出")

    choice = input("请选择操作 (1-4): ")

    if choice == "1":
        # 添加学生
        name = input("请输入学生姓名: ")
        score = float(input("请输入成绩: "))
        students[name] = score
        print(f"已添加: {name}")

    elif choice == "2":
        # 查看成绩
        if students:
            print("\n所有学生成绩:")
            for name, score in students.items():
                print(f"{name}: {score}分")
        else:
            print("还没有添加学生")

    elif choice == "3":
        # 计算平均分
        if students:
            average = sum(students.values()) / len(students)
            print(f"班级平均分: {average:.2f}")
        else:
            print("还没有添加学生")

    elif choice == "4":
        print("再见！")
        break

    else:
        print("无效的选择，请重新输入")
```
</details>

### 练习5：简单的加密解密程序

创建一个简单的凯撒密码加密解密程序。

<details>
<summary>查看答案</summary>

```python
# 凯撒密码加密解密
def create_cipher(shift):
    """创建密码本"""
    cipher = {}
    for i in range(26):
        original = chr(ord('a') + i)
        encrypted = chr(ord('a') + (i + shift) % 26)
        cipher[original] = encrypted
        cipher[original.upper()] = encrypted.upper()
    return cipher

def encrypt(text, cipher):
    """加密"""
    result = []
    for char in text:
        if char in cipher:
            result.append(cipher[char])
        else:
            result.append(char)
    return ''.join(result)

def decrypt(text, cipher):
    """解密"""
    # 创建反向密码本
    reverse_cipher = {v: k for k, v in cipher.items()}
    return encrypt(text, reverse_cipher)

# 主程序
shift = int(input("请输入偏移量 (1-25): "))
cipher = create_cipher(shift)

while True:
    print("\n===== 加密解密系统 =====")
    print("1. 加密")
    print("2. 解密")
    print("3. 退出")

    choice = input("请选择操作 (1-3): ")

    if choice == "1":
        text = input("请输入要加密的文本: ")
        encrypted = encrypt(text, cipher)
        print(f"加密结果: {encrypted}")

    elif choice == "2":
        text = input("请输入要解密的文本: ")
        decrypted = decrypt(text, cipher)
        print(f"解密结果: {decrypted}")

    elif choice == "3":
        print("再见！")
        break

    else:
        print("无效的选择，请重新输入")
```
</details>

---

## 综合应用：人员信息管理系统

结合前面学的知识，我们创建一个完整的人员信息管理系统：

```python
# 人员信息管理系统
people = {}

def add_person():
    """添加人员"""
    name = input("请输入姓名: ")
    age = input("请输入年龄: ")
    phone = input("请输入电话: ")

    people[name] = {
        "age": age,
        "phone": phone
    }
    print(f"已添加: {name}")

def find_person():
    """查找人员"""
    name = input("请输入要查找的姓名: ")
    if name in people:
        info = people[name]
        print(f"姓名: {name}")
        print(f"年龄: {info['age']}")
        print(f"电话: {info['phone']}")
    else:
        print("没有找到该人员")

def list_all():
    """列出所有人员"""
    if people:
        print("\n所有人员信息:")
        print("-" * 40)
        for name, info in people.items():
            print(f"姓名: {name}")
            print(f"年龄: {info['age']}")
            print(f"电话: {info['phone']}")
            print("-" * 40)
    else:
        print("还没有添加人员")

def delete_person():
    """删除人员"""
    name = input("请输入要删除的人员姓名: ")
    if name in people:
        del people[name]
        print(f"已删除: {name}")
    else:
        print("没有找到该人员")

# 主菜单
while True:
    print("\n===== 人员信息管理系统 =====")
    print("1. 添加人员")
    print("2. 查找人员")
    print("3. 列出所有人员")
    print("4. 删除人员")
    print("5. 退出")

    choice = input("请选择操作 (1-5): ")

    if choice == "1":
        add_person()
    elif choice == "2":
        find_person()
    elif choice == "3":
        list_all()
    elif choice == "4":
        delete_person()
    elif choice == "5":
        print("再见！")
        break
    else:
        print("无效的选择，请重新输入")
```

**给家长的小贴士**：这个综合项目使用了字典的嵌套、增删改查等所有核心概念，是很好的实战练习。

---

## 字典和列表的选择

### 什么时候使用列表？

- 需要按顺序存储数据
- 使用数字索引访问元素
- 数据之间没有明确的"键"关系
- 例如：购物清单、待办事项列表

### 什么时候使用字典？

- 需要用有意义的名称访问数据
- 数据有明确的"键-值"关系
- 需要快速查找和更新
- 例如：电话簿、成绩表、配置信息

### 对比示例

```python
# 使用列表存储学生信息（不推荐）
student_list = ["小明", 12, 6, 95]  # 难以记住每个位置的含义

# 使用字典存储学生信息（推荐）
student_dict = {
    "name": "小明",
    "age": 12,
    "grade": 6,
    "score": 95
}  # 每个字段都有明确的含义
```

**给家长的小贴士**：选择合适的数据结构是编程的重要能力，鼓励孩子在编写程序前先思考："用列表还是字典更合适？"

---

## 常见错误和调试

### 错误1：使用不存在的键

```python
scores = {"语文": 95, "数学": 98}

# 错误：直接访问不存在的键
print(scores["英语"])  # KeyError: '英语'

# 正确：使用get()方法
print(scores.get("英语", "没有这门课"))
```

### 错误2：使用可变类型作为键

```python
# 错误：列表不能作为键
# my_dict = {[1, 2]: "value"}  # TypeError

# 正确：元组可以作为键
my_dict = {(1, 2): "value"}
```

### 错误3：遍历字典时修改字典

```python
scores = {"语文": 95, "数学": 98, "英语": 88}

# 错误：遍历时修改字典
for subject in scores:
    if scores[subject] < 90:
        del scores[subject]  # RuntimeError

# 正确：先收集要删除的键，再删除
to_remove = [subject for subject in scores if scores[subject] < 90]
for subject in to_remove:
    del scores[subject]
```

### 错误4：混淆赋值和copy()

```python
original = {"语文": 95, "数学": 98}

# 错误：这只是创建了一个引用
copied = original
copied["英语"] = 88
print(original)  # original也被修改了！

# 正确：使用copy()创建独立副本
copied = original.copy()
copied["英语"] = 88
print(original)  # original不受影响
```

### 调试技巧

1. **打印字典内容**：
```python
scores = {"语文": 95, "数学": 98}
print(scores)  # 查看完整字典
```

2. **检查键是否存在**：
```python
if "数学" in scores:
    print("数学成绩存在")
```

3. **使用type()检查类型**：
```python
print(type(scores))  # 确认是字典类型
```

**给家长的小贴士**：字典的错误通常比较隐蔽，建议在调试时多使用`print()`语句，逐步检查每一步的执行结果。

---

## 性能考虑

### 字典的查找速度

字典的查找速度非常快（O(1)），而列表的查找速度较慢（O(n)）。

```python
# 使用列表查找（慢）
students_list = ["小明", "小红", "小华", "小刚", "小李"]
if "小华" in students_list:  # 需要逐个比较
    print("找到了")

# 使用字典查找（快）
students_dict = {"小明": 1, "小红": 2, "小华": 3}
if "小华" in students_dict:  # 直接找到
    print("找到了")
```

### 什么时候考虑性能？

- 数据量很大时（比如超过1000个元素）
- 需要频繁查找时
- 对性能要求高的程序

**给家长的小贴士**：对于小学阶段的学习，性能不是重点，但了解这个知识点有助于培养良好的编程习惯。

---

## 字典的高级应用

### 使用字典作为缓存

```python
# 斐波那契数列（带缓存）
cache = {}

def fib(n):
    if n in cache:
        return cache[n]

    if n <= 1:
        result = n
    else:
        result = fib(n-1) + fib(n-2)

    cache[n] = result
    return result

print(fib(100))  # 计算很快，因为有缓存
```

### 使用字典统计

```python
# 统计单词词频
text = "hello world hello python world"

words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
# 输出: {'hello': 2, 'world': 2, 'python': 1}
```

### 使用字典分组

```python
# 按成绩分组
students = [
    {"name": "小明", "score": 95},
    {"name": "小红", "score": 87},
    {"name": "小华", "score": 92}
]

# 按分数段分组
groups = {"优秀": [], "良好": [], "及格": []}

for student in students:
    score = student["score"]
    if score >= 90:
        groups["优秀"].append(student["name"])
    elif score >= 80:
        groups["良好"].append(student["name"])
    else:
        groups["及格"].append(student["name"])

print(groups)
```

**给家长的小贴士**：这些高级应用可能比较复杂，可以让孩子先掌握基础，等有更多编程经验后再学习。

---

## 字典 vs 其他数据结构

| 数据结构 | 特点 | 适用场景 |
|---------|------|---------|
| 列表 | 有序、可重复 | 存储序列数据 |
| 元组 | 有序、不可变 | 固定不变的数据 |
| 集合 | 无序、唯一 | 去重、集合运算 |
| 字典 | 键值对 | 快速查找、关联数据 |

```python
# 列表：购物清单
shopping_list = ["苹果", "香蕉", "橙子"]

# 元组：固定坐标
point = (10, 20)

# 集合：去重
numbers = {1, 2, 3, 2, 1}  # {1, 2, 3}

# 字典：成绩表
scores = {"小明": 95, "小红": 98}
```

**给家长的小贴士**：让孩子理解不同数据结构的特点和适用场景，有助于选择合适的工具。

---

## 章节小结

### 核心知识点

1. **字典的基本概念**：
   - 字典是键值对的集合
   - 键必须是不可变类型且唯一
   - 值可以是任意类型

2. **字典的基本操作**：
   - 创建：`{}` 或 `dict()`
   - 访问：`dict[key]` 或 `dict.get(key)`
   - 添加：`dict[key] = value`
   - 修改：`dict[key] = new_value`
   - 删除：`del dict[key]` 或 `dict.pop(key)`

3. **字典的常用方法**：
   - `keys()`: 获取所有键
   - `values()`: 获取所有值
   - `items()`: 获取所有键值对
   - `get()`: 安全访问
   - `update()`: 更新字典
   - `clear()`: 清空字典

4. **遍历字典**：
   - 遍历键：`for key in dict`
   - 遍历值：`for value in dict.values()`
   - 遍历键值对：`for key, value in dict.items()`

5. **嵌套字典**：
   - 字典的值可以是另一个字典
   - 访问嵌套数据：`dict[key1][key2]`

### 重要概念

- 字典的键必须是不可变类型（字符串、数字、元组）
- 字典的键必须唯一
- 字典的查找速度很快（O(1)）
- 字典适合存储有关联关系的数据

---

## 挑战练习

### 挑战1：制作一个简单的游戏配置系统

创建一个游戏配置系统，可以设置和读取游戏参数（如难度、音量、玩家名称等）。

<details>
<summary>提示</summary>

使用字典存储配置信息，每个配置项是一个键值对。

</details>

### 挑战2：制作一个图书管理系统

创建一个图书管理系统，每本书包含：书名、作者、出版社、出版年份、价格等信息。支持添加、查找、删除、列出所有书籍等功能。

<details>
<summary>提示</summary>

使用嵌套字典，书名作为键，书的详细信息作为值。

</details>

### 挑战3：制作一个简单的投票统计系统

创建一个投票统计系统，可以统计多个候选人的得票数，并按票数排序显示结果。

<details>
<summary>提示</summary>

使用字典存储候选人姓名和票数，使用`sorted()`函数排序。

</details>

---

## 下一步

恭喜你完成了字典的学习！现在你已经掌握了：

✅ 列表（List）
✅ 字典（Dictionary）

这两种数据结构是Python中最常用的数据存储方式。下一章，我们将学习**函数**，这是一种让代码更简洁、更可重用的重要工具。

函数就像是给一段代码起个名字，以后就可以通过这个名字重复使用这段代码，而不需要重复编写。这将大大提高我们的编程效率！

继续加油，你正在成为一名优秀的程序员！🎉
