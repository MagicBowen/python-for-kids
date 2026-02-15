# CommandLine程序

## 引言

同学们,你们有没有想过,我们每天在学校上课时,如果能有一个"电子小助手",随时告诉我们今天有什么课,那该多好啊?

在前面几章中,我们已经学习了很多Python知识:
- 第2章学会了输入和输出
- 第5章学会了布尔值判断
- 第7章学会了条件语句
- 第8章学会了循环语句
- 第10章学会了列表
- 第11章学会了字典
- 第12章学会了函数
- 第13章学会了各种库的使用

现在,是时候把这些知识都运用起来,开发一个**真正的实用程序**了!

我们将开发一个**智能课表查询系统**,它可以:
1. 📅 查询某天的课程
2. ➕ 添加新的课程
3. ✏️ 修改已有课程
4. ❌ 删除不要的课程
5. 📁 自动保存到文件,下次打开还能用
6. 🗣️ 理解各种说法(周一/星期一/礼拜一都可以)
7. 🕐 支持上午下午的区分
8. 📆 支持直接输入日期(如"10月15日")

这个程序将会像我们平时和机器人聊天一样自然,这就是**命令行程序(CommandLine Program)**的魅力!

---

## 什么是命令行程序?

命令行程序是一种通过**文字命令**和计算机交互的程序。没有漂亮的按钮和窗口,所有的操作都通过**输入命令**来完成。

### 🖥️ 计算机小知识:命令行的历史

你知道吗?在很久以前(1970-1980年代),计算机**没有图形界面**,没有鼠标,没有漂亮的窗口!

那时的程序员只能通过**命令行(Command Line)** 和计算机交流:
- 屏幕是黑底的,只有白色的文字
- 没有鼠标,只能用键盘输入命令
- 每个命令都要**准确记忆**和**准确拼写**

**为什么那时候没有图形界面呢?**
- 计算机的**CPU速度慢**,处理不动复杂的图形
- **内存很小**,存不下那么多图片和界面
- **硬盘很小**,存不了那么多数据

所以命令行程序是计算机发展早期的重要交互方式!即使现在有了图形界面,命令行仍然被程序员广泛使用,因为它:
- ✅ 运行速度快(不需要处理图形)
- ✅ 占用资源少(不需要加载图片)
- ✅ 灵活强大(可以组合各种命令)

### 命令行程序 vs 图形界面程序

| 特点 | 命令行程序 | 图形界面程序 |
|------|-----------|------------|
| **交互方式** | 输入文字命令 | 点击按钮、菜单 |
| **外观** | 黑色背景,白色文字 | 有图片、按钮、窗口 |
| **学习难度** | 需要记住命令 | 直观,容易上手 |
| **灵活性** | 非常灵活 | 功能固定 |
| **运行速度** | 快 | 相对慢 |
| **CPU占用** | 低 | 高 |
| **内存占用** | 少 | 多 |
| **例子** | 我们的课表系统 | 游戏、手机APP |

### 生活中的命令行程序

其实你早就用过命令行程序了!

**例子1: 和聊天机器人对话**
```
你: 今天天气怎么样?
机器人: 今天北京晴,温度15-25度
你: 明天呢?
机器人: 明天多云,温度18-28度
```

**例子2: 智能音箱**
```
你: 小爱同学,播放音乐
音箱: 好的,正在播放你喜欢的歌
你: 下一首
音箱: 正在切换到下一首
```

这些都和命令行程序类似:你用**文字**告诉它要做什么,它用**文字**回应你!

### Python中的命令行程序

在Python中,我们主要使用以下函数来实现命令行程序:

1. **`input()`** - 获取用户的输入
2. **`print()`** - 显示信息给用户
3. **`条件语句`** - 根据用户的输入判断要做什么
4. **`循环语句`** - 让程序持续运行,多次接收命令
5. **`字典/列表`** - 存储数据(如课表)
6. **`文件操作`** - 保存数据到文件
7. **`时间库`** - 处理日期和时间
8. **`正则表达式`** - 理解各种说法(周一/星期一/礼拜一)

---

## 第一步:最简单的课表查询系统

让我们从最简单的开始:只能查询,不能修改,程序退出后数据就丢失了。

### 程序1:固定课表查询

```python
# 最简单的课表查询程序
# 使用字典存储课表信息

# 定义课表字典
schedule = {
    "周一": "语文、数学、英语",
    "周二": "数学、语文、体育",
    "周三": "英语、科学、美术",
    "周四": "音乐、数学、语文",
    "周五": "体育、英语、班会"
}

# 欢迎信息
print("=" * 40)
print("       欢迎使用课表查询系统")
print("=" * 40)
print("支持查询: 周一 到 周日")
print("输入 '退出' 结束程序")
print("=" * 40)

# 主循环
while True:
    # 获取用户输入
    day = input("\n请输入要查询的星期: ")

    # 判断是否要退出
    if day == "退出":
        print("谢谢使用,再见!")
        break

    # 查询课表
    if day in schedule:
        print(f"\n{day}的课程是: {schedule[day]}")
    else:
        print(f"\n抱歉,{day}没有课,好好休息吧!")
```

**运行示例:**
```
========================================
       欢迎使用课表查询系统
========================================
支持查询: 周一 到 周日
输入 '退出' 结束程序
========================================

请输入要查询的星期: 周一

周一的课程是: 语文、数学、英语

请输入要查询的星期: 周六

抱歉,周六没有课,好好休息吧!

请输入要查询的星期: 退出
谢谢使用,再见!
```

### 给家长的小贴士

**教学重点**:
1. **字典的键值对**: `schedule[day]` 通过星期几(键)找到课程(值)
2. **`in` 操作符**: `if day in schedule` 判断这个键是否存在
3. **`while True` 循环**: 让程序持续运行,直到用户输入"退出"
4. **`break` 语句**: 跳出循环,结束程序

**常见问题**:
- **问**: 为什么用字典不用列表?
- **答**: 字典可以通过"周一"直接找到课程,列表需要遍历查找,字典更方便!

- **问**: `while True` 不是会永远循环吗?
- **答**: 是的,但我们在循环中用 `break` 跳出来,所以不会永远运行

**扩展思考**:
- 如果课程有很多节,用字符串存储不方便怎么办?(提示:用列表)
- 如何让程序同时识别"周一"、"星期一"、"礼拜一"?

---

### 练习1:完善基本课表查询

请完成以下任务:

**任务**: 修改上面的程序,让它:
1. 用列表存储每天的课程(因为可能有多节课)
2. 增加周末的课程(周六、周日)

<details>
<summary>🔍 查看答案</summary>

```python
# 用列表存储每天的课程
schedule = {
    "周一": ["语文", "数学", "英语"],
    "周二": ["数学", "语文", "体育"],
    "周三": ["英语", "科学", "美术"],
    "周四": ["音乐", "数学", "语文"],
    "周五": ["体育", "英语", "班会"],
    "周六": [],  # 空列表表示没有课
    "周日": []   # 空列表表示没有课
}

print("=" * 40)
print("       欢迎使用课表查询系统")
print("=" * 40)
print("支持查询: 周一 到 周日")
print("输入 '退出' 结束程序")
print("=" * 40)

while True:
    day = input("\n请输入要查询的星期: ")

    if day == "退出":
        print("谢谢使用,再见!")
        break

    if day in schedule:
        courses = schedule[day]
        if courses:  # 列表不为空
            print(f"\n{day}的课程有: {', '.join(courses)}")
        else:  # 列表为空
            print(f"\n{day}没有课,好好休息吧!")
    else:
        print(f"\n输入错误,请输入周一到周日之间!")
```

**改进说明**:
1. 每天的课程用列表存储: `["语文", "数学", "英语"]`
2. 用 `if courses:` 判断列表是否为空
3. 用 `', '.join(courses)` 把列表变成字符串,用逗号分隔

</details>

---

## 第二步:理解同义词(周一/星期一/礼拜一)

用户可能会说:
- "周一"
- "星期一"
- "礼拜一"
- "周1"

这些都表示同一天!我们需要让程序理解它们是同一个意思。

### 方法1:用多个键指向同一个值

```python
# 用多个键指向同一个列表
courses_monday = ["语文", "数学", "英语"]

schedule = {
    "周一": courses_monday,
    "星期一": courses_monday,
    "礼拜一": courses_monday,
    "周1": courses_monday,
    "1": courses_monday,
    # ... 其他天的课程
}

print("支持的输入: 周一/星期一/礼拜一/周1/1")
while True:
    day = input("\n请输入要查询的星期: ")

    if day == "退出":
        break

    if day in schedule:
        courses = schedule[day]
        if courses:
            print(f"课程有: {', '.join(courses)}")
        else:
            print("今天没有课!")
    else:
        print("输入错误,请重新输入!")
```

**优点**: 简单易懂
**缺点**: 要写很多重复的内容

---

### 方法2:用函数转换输入(推荐)

更好的方法是:把用户的各种说法,统一转换成标准格式(如"周一")。

```python
# 创建一个同义词映射表
synonyms = {
    # 星期一的同义词
    "周一": "周一", "星期一": "周一", "礼拜一": "周一",
    "周1": "周一", "星期1": "周一", "礼拜1": "周一", "1": "周一",
    # 星期二
    "周二": "周二", "星期二": "周二", "礼拜二": "周二",
    "周2": "周二", "星期2": "周二", "礼拜2": "周二", "2": "周二",
    # 星期三
    "周三": "周三", "星期三": "周三", "礼拜三": "周三",
    "周3": "周三", "星期3": "周三", "礼拜3": "周三", "3": "周三",
    # 星期四
    "周四": "周四", "星期四": "周四", "礼拜四": "周四",
    "周4": "周四", "星期4": "周四", "礼拜4": "周四", "4": "周四",
    # 星期五
    "周五": "周五", "星期五": "周五", "礼拜五": "周五",
    "周5": "周五", "星期5": "周五", "礼拜5": "周五", "5": "周五",
    # 星期六
    "周六": "周六", "星期六": "周六", "礼拜六": "周六",
    "周6": "周六", "星期6": "周六", "礼拜6": "周六", "6": "周六",
    # 星期日
    "周日": "周日", "星期日": "周日", "礼拜日": "周日", "礼拜天": "周日", "星期天": "周日",
    "周7": "周日", "星期7": "周日", "礼拜7": "周日", "7": "周日", "周0": "周日",
}

# 定义课表(只有标准格式)
schedule = {
    "周一": ["语文", "数学", "英语"],
    "周二": ["数学", "语文", "体育"],
    "周三": ["英语", "科学", "美术"],
    "周四": ["音乐", "数学", "语文"],
    "周五": ["体育", "英语", "班会"],
    "周六": [],
    "周日": []
}

print("=" * 40)
print("       欢迎使用课表查询系统")
print("=" * 40)
print("支持多种说法: 周一/星期一/礼拜一/周1/1")
print("输入 '退出' 结束程序")
print("=" * 40)

while True:
    day_input = input("\n请输入要查询的星期: ")

    if day_input == "退出":
        print("谢谢使用,再见!")
        break

    # 转换用户输入
    if day_input in synonyms:
        day = synonyms[day_input]  # 转换成标准格式
        courses = schedule[day]
        if courses:
            print(f"\n{day}的课程有: {', '.join(courses)}")
        else:
            print(f"\n{day}没有课,好好休息吧!")
    else:
        print("\n输入错误,请重新输入!")
```

**运行示例**:
```
请输入要查询的星期: 礼拜一

周一的课程有: 语文, 数学, 英语

请输入要查询的星期: 星期5

周五的课程有: 体育, 英语, 班会

请输入要查询的星期: 8
输入错误,请重新输入!
```

### 给家长的小贴士

**教学重点**:
1. **同义词映射**: 用 `synonyms` 字典把各种说法映射到标准格式
2. **分离数据和逻辑**: `schedule` 只存储标准格式,不存储所有同义词
3. **查表转换**: `day = synonyms[day_input]` 把用户输入转换成标准格式

**优点**:
- 代码更清晰,易于维护
- 增加新的同义词很容易
- 课表数据不冗余

**扩展思考**:
- 如果用户输入"星斯一"(错别字),怎么办?(提示:可以用模糊匹配或提示正确写法)
- 如何让程序记住用户最常用的说法,下次优先显示?

---

### 练习2:增加更多同义词

**任务**: 修改上面的程序,增加以下同义词的支持:
- "monday", "Mon", "mon" (英文)
- "星期天" (和"星期日"都指周日)

<details>
<summary>🔍 查看答案</summary>

```python
# 同义词映射表
synonyms = {
    # 星期一
    "周一": "周一", "星期一": "周一", "礼拜一": "周一",
    "周1": "周一", "星期1": "周一", "礼拜1": "周一", "1": "周一",
    "monday": "周一", "mon": "周一", "Mon": "周一",
    # 星期二
    "周二": "周二", "星期二": "周二", "礼拜二": "周二",
    "周2": "周二", "星期2": "周二", "礼拜2": "周二", "2": "周二",
    "tuesday": "周二", "tue": "周二", "Tue": "周二",
    # ... (星期三到星期五类似)
    # 星期日
    "周日": "周日", "星期日": "周日", "星期天": "周日",
    "礼拜日": "周日", "礼拜天": "周日",
    "周7": "周日", "星期7": "周日", "礼拜7": "周日", "7": "周日", "周0": "周日",
    "sunday": "周日", "sun": "周日", "Sun": "周日",
}

# 定义课表
schedule = {
    "周一": ["语文", "数学", "英语"],
    "周二": ["数学", "语文", "体育"],
    "周三": ["英语", "科学", "美术"],
    "周四": ["音乐", "数学", "语文"],
    "周五": ["体育", "英语", "班会"],
    "周六": [],
    "周日": []
}

print("=" * 40)
print("       欢迎使用课表查询系统")
print("=" * 40)
print("支持中文/英文: 周一/星期一/monday/mon")
print("输入 '退出' 结束程序")
print("=" * 40)

while True:
    day_input = input("\n请输入要查询的星期: ").lower()  # 转换成小写

    if day_input == "退出":
        print("谢谢使用,再见!")
        break

    if day_input in synonyms:
        day = synonyms[day_input]
        courses = schedule[day]
        if courses:
            print(f"\n{day}的课程有: {', '.join(courses)}")
        else:
            print(f"\n{day}没有课,好好休息吧!")
    else:
        print("\n输入错误,请重新输入!")
```

**改进说明**:
1. 在 `synonyms` 中增加英文同义词
2. 使用 `.lower()` 把用户输入转换成小写,这样"Monday"和"monday"都能识别
3. 增加了"星期天"的同义词

</details>

---

## 第三步:支持上午和下午

学校的课表通常会区分上午和下午,让我们来实现这个功能。

### ⏰ 数学小知识:时间计算

在编写课表程序时,我们会用到很多**时间计算**的知识!

**小学数学知识点:时间单位换算**

```
1小时 = 60分钟
1分钟 = 60秒
半天 = 4节课 (每节40-45分钟)
```

**实际应用**:
- 如果上午8:00开始上课,每节课40分钟,课间休息10分钟
- 第1节课: 8:00 - 8:40
- 第2节课: 8:50 - 9:30 (课间休息10分钟)
- 第3节课: 9:40 - 10:20
- 第4节课: 10:30 - 11:10

**你能算出:**
1. 上午4节课一共多少分钟?(40 × 4 = 160分钟)
2. 160分钟 = 多少小时多少分钟?(2小时40分钟)
3. 如果下午也是4节课,全天一共多少分钟?(320分钟 = 5小时20分钟)

这些时间计算在我们的课表程序中都会用到!

### 程序3:带时间信息的课表系统

```python
# 同义词映射表
synonyms = {
    "周一": "周一", "星期一": "周一", "礼拜一": "周一", "周1": "周一", "1": "周一",
    "周二": "周二", "星期二": "周二", "礼拜二": "周二", "周2": "周二", "2": "周二",
    "周三": "周三", "星期三": "周三", "礼拜三": "周三", "周3": "周三", "3": "周三",
    "周四": "周四", "星期四": "周四", "礼拜四": "周四", "周4": "周四", "4": "周四",
    "周五": "周五", "星期五": "周五", "礼拜五": "周五", "周5": "周五", "5": "周五",
    "周六": "周六", "星期六": "周六", "礼拜六": "周六", "周6": "周六", "6": "周六",
    "周日": "周日", "星期日": "周日", "星期天": "周日", "周7": "周日", "7": "周日", "0": "周日",
}

# 上午下午的同义词
time_synonyms = {
    "上午": "上午", "am": "上午", "早上": "上午", "早晨": "上午",
    "下午": "下午", "pm": "下午", "午后": "下午",
}

# 定义课表(嵌套字典: 星期 -> 时间段 -> 课程列表)
schedule = {
    "周一": {
        "上午": ["语文", "数学", "英语"],
        "下午": ["体育", "音乐"]
    },
    "周二": {
        "上午": ["数学", "语文", "英语"],
        "下午": ["科学", "美术"]
    },
    "周三": {
        "上午": ["英语", "数学", "语文"],
        "下午": ["体育", "班会"]
    },
    "周四": {
        "上午": ["音乐", "语文", "数学"],
        "下午": ["美术", "科学"]
    },
    "周五": {
        "上午": ["体育", "英语", "语文"],
        "下午": ["综合实践"]
    },
    "周六": {"上午": [], "下午": []},
    "周日": {"上午": [], "下午": []}
}

print("=" * 40)
print("       欢迎使用课表查询系统")
print("=" * 40)
print("查询方式:")
print("1. 输入 '周一' - 查询周一全天课程")
print("2. 输入 '周一上午' 或 '周一 am' - 查询周上午课程")
print("输入 '退出' 结束程序")
print("=" * 40)

while True:
    user_input = input("\n请输入要查询的: ")

    if user_input == "退出":
        print("谢谢使用,再见!")
        break

    # 尝试解析用户输入
    found = False  # 标记是否找到匹配

    # 先尝试匹配"星期+时间"的组合(如"周一上午")
    for day_syn, day_std in synonyms.items():
        for time_syn, time_std in time_synonyms.items():
            # 检查是否包含"星期+时间"或"时间+星期"
            if day_syn in user_input and time_syn in user_input:
                # 找到了匹配
                courses = schedule[day_std][time_std]
                if courses:
                    print(f"\n{day_std}{time_std}的课程有: {', '.join(courses)}")
                else:
                    print(f"\n{day_std}{time_std}没有课,好好休息!")
                found = True
                break
        if found:
            break

    # 如果没有找到"星期+时间",尝试只匹配"星期"
    if not found:
        for day_syn, day_std in synonyms.items():
            if day_syn in user_input or user_input == day_syn:
                day_schedule = schedule[day_std]
                morning_courses = day_schedule["上午"]
                afternoon_courses = day_schedule["下午"]

                print(f"\n{day_std}的课程安排:")
                print(f"  上午: {', '.join(morning_courses) if morning_courses else '无课'}")
                print(f"  下午: {', '.join(afternoon_courses) if afternoon_courses else '无课'}")
                found = True
                break

    if not found:
        print("\n输入错误,请重新输入!")
```

**运行示例**:
```
请输入要查询的: 周一上午

周一上午的课程有: 语文, 数学, 英语

请输入要查询的: 星期二下午

星期二下午的课程有: 科学, 美术

请输入要查询的: 周三

周三的课程安排:
  上午: 英语, 数学, 语文
  下午: 体育, 班会

请输入要查询的: 礼拜五am

周五上午的课程有: 体育, 英语, 语文
```

### 给家长的小贴士

**教学重点**:
1. **嵌套字典**: `schedule[day][time]` 先通过星期找到上午/下午的字典,再通过时间找到课程列表
2. **两层循环**: 外层循环遍历所有星期的同义词,内层循环遍历所有时间的同义词
3. **`in` 操作符**: `if day_syn in user_input` 检查用户输入是否包含某个关键词
4. **`break` 语句**: 找到匹配后跳出循环,避免重复查找
5. **`found` 标志**: 跟踪是否找到匹配,如果没有找到则提示输入错误

**数据结构图示**:
```
schedule (字典)
├── "周一" (字典)
│   ├── "上午" → ["语文", "数学", "英语"]
│   └── "下午" → ["体育", "音乐"]
├── "周二" (字典)
│   ├── "上午" → ["数学", "语文", "英语"]
│   └── "下午" → ["科学", "美术"]
└── ...
```

**常见问题**:
- **问**: 为什么不用 `if day_syn in user_input and time_syn in user_input:`?
- **答**: 因为用户可能输入"上午周一"或"周一上午",所以两种顺序都要判断

**优化建议**:
- 上面的代码效率不高,因为要遍历所有同义词
- 可以优化:先提取用户输入中的关键词,再匹配

---

### 练习3:支持"第几节课"的查询

**任务**: 修改上面的程序,支持以下查询:
- "周一第1节" → 查询周一第1节课
- "周二第2节" → 查询周二第2节课

<details>
<summary>🔍 查看答案</summary>

```python
# 同义词映射表
synonyms = {
    "周一": "周一", "星期一": "周一", "礼拜一": "周一", "周1": "周一", "1": "周一",
    "周二": "周二", "星期二": "周二", "礼拜二": "周二", "周2": "周二", "2": "周二",
    "周三": "周三", "星期三": "周三", "礼拜三": "周三", "周3": "周三", "3": "周三",
    "周四": "周四", "星期四": "周四", "礼拜四": "周四", "周4": "周四", "4": "周四",
    "周五": "周五", "星期五": "周五", "礼拜五": "周五", "周5": "周五", "5": "周五",
    "周六": "周六", "星期六": "周六", "礼拜六": "周六", "周6": "周六", "6": "周六",
    "周日": "周日", "星期日": "周日", "星期天": "周日", "周7": "周日", "7": "周日", "0": "周日",
}

# 定义课表(按节次存储)
schedule = {
    "周一": ["语文", "数学", "英语", "体育", "音乐"],
    "周二": ["数学", "语文", "英语", "科学", "美术"],
    "周三": ["英语", "数学", "语文", "体育", "班会"],
    "周四": ["音乐", "语文", "数学", "美术", "科学"],
    "周五": ["体育", "英语", "语文", "综合实践", "阅读"],
    "周六": [],
    "周日": []
}

print("=" * 40)
print("       欢迎使用课表查询系统")
print("=" * 40)
print("查询方式:")
print("1. 输入 '周一' - 查询周一全天课程")
print("2. 输入 '周一第1节' 或 '周一1' - 查询周一第1节")
print("输入 '退出' 结束程序")
print("=" * 40)

while True:
    user_input = input("\n请输入要查询的: ")

    if user_input == "退出":
        print("谢谢使用,再见!")
        break

    found = False

    # 先尝试匹配"星期+第几节"
    for day_syn, day_std in synonyms.items():
        # 检查是否包含这个星期
        if day_syn in user_input or user_input == day_syn:
            # 尝试提取"第几节"
            if "第" in user_input and "节" in user_input:
                # 提取数字
                for i in range(1, 10):  # 假设最多9节课
                    if f"第{i}节" in user_input or f"{i}" == user_input.strip()[-1]:
                        courses = schedule[day_std]
                        if i <= len(courses):
                            print(f"\n{day_std}第{i}节课是: {courses[i-1]}")
                        else:
                            print(f"\n{day_std}第{i}节没有课!")
                        found = True
                        break
            else:
                # 只查询星期,显示全天课程
                courses = schedule[day_std]
                if courses:
                    print(f"\n{day_std}的课程有:")
                    for i, course in enumerate(courses, 1):
                        print(f"  第{i}节: {course}")
                else:
                    print(f"\n{day_std}没有课,好好休息!")
                found = True
            break

    if not found:
        print("\n输入错误,请重新输入!")
```

**运行示例**:
```
请输入要查询的: 周一第1节

周一第1节课是: 语文

请输入要查询的: 周二第3节

周二第3节课是: 英语

请输入要查询的: 周三
周三的课程有:
  第1节: 英语
  第2节: 数学
  第3节: 语文
  第4节: 体育
  第5节: 班会
```

**改进说明**:
1. 把课表改成列表,每个元素代表一节课
2. 用 `enumerate(courses, 1)` 遍历列表,同时获取节次和课程
3. 用 `courses[i-1]` 获取第i节课(索引从0开始,所以是i-1)

</details>

---

### 练习3.5:时间计算挑战 🧮

现在让我们用编程来练习**数学中的时间计算**!

**任务**: 编写一个程序,计算上课的总时长

```python
# 每节课的时间信息(分钟)
class_duration = 40  # 每节课40分钟
break_duration = 10  # 课间休息10分钟

# 每天的课程安排
daily_schedule = {
    "周一": {"上午": 4, "下午": 3},  # 周一上午4节,下午3节
    "周二": {"上午": 4, "下午": 3},
    "周三": {"上午": 4, "下午": 3},
    "周四": {"上午": 4, "下午": 3},
    "周五": {"上午": 4, "下午": 2},
}

print("=" * 40)
print("       课程时间计算器")
print("=" * 40)

# 计算某天的上课总时长
day = input("请输入要计算的星期(如'周一'): ")

if day in daily_schedule:
    morning_classes = daily_schedule[day]["上午"]
    afternoon_classes = daily_schedule[day]["下午"]
    total_classes = morning_classes + afternoon_classes

    # 计算上课总时长(分钟)
    total_minutes = total_classes * class_duration

    # 计算在校总时长(包括课间休息)
    total_breaks = (morning_classes - 1) + (afternoon_classes - 1) + 1  # 上午课间+下午课间+午休
    total_with_breaks = total_minutes + total_breaks * break_duration + 60  # +60分钟午休

    # 转换成小时和分钟
    hours = total_minutes // 60
    minutes = total_minutes % 60

    print(f"\n{day}的课程安排:")
    print(f"  上午: {morning_classes}节课")
    print(f"  下午: {afternoon_classes}节课")
    print(f"  总共: {total_classes}节课")
    print(f"\n上课总时长: {total_minutes}分钟 = {hours}小时{minutes}分钟")
    print(f"在校时长(含课间): {total_with_breaks}分钟")

else:
    print("输入错误,请重新输入!")
```

**运行示例**:
```
请输入要计算的星期(如'周一'): 周一

周一的课程安排:
  上午: 4节课
  下午: 3节课
  总共: 7节课

上课总时长: 280分钟 = 4小时40分钟
在校时长(含课间): 420分钟
```

**🧮 数学练习**:

1. **基础题**: 如果每节课45分钟,课间休息10分钟,计算周一在校总时长?
   - 提示: 7节课 × 45分钟 = ?

2. **进阶题**: 一周5天,每天平均6节课,一周总共上多少分钟课?
   - 提示: 5天 × 6节课 × 40分钟 = ?
   - 答案: 1200分钟 = 20小时!

3. **挑战题**: 如果你每天早上7:30到校,下午4:30放学,你在学校多少小时?
   - 提示: 下午4:30 = 16:30
   - 计算: 16:30 - 7:30 = ?

<details>
<summary>🔍 查看答案</summary>

```python
# 答案1: 每节课45分钟
class_duration = 45
total_minutes = 7 * 45  # 315分钟
hours = 315 // 60  # 5小时
minutes = 315 % 60  # 15分钟
print(f"周一上课总时长: {hours}小时{minutes}分钟")  # 5小时15分钟

# 答案2: 一周总时长
weekly_minutes = 5 * 6 * 40  # 1200分钟
weekly_hours = 1200 // 60  # 20小时
print(f"一周上课总时长: {weekly_hours}小时")  # 20小时

# 答案3: 在校时长计算
# 16:30 - 7:30 = 9小时
print("在校时长: 9小时")
```

</details>

---

## 第四步:支持日期查询(10月15日是星期几?)

现在我们要实现一个更高级的功能:用户输入"10月15日",程序自动判断是星期几,然后查询课表!

这需要用到**时间库**(time库或datetime库)。

### 程序4:支持日期查询

```python
import datetime  # 导入时间库

# 同义词映射表
synonyms = {
    "周一": "周一", "星期一": "周一", "礼拜一": "周一", "周1": "周一", "1": "周一",
    "周二": "周二", "星期二": "周二", "礼拜二": "周二", "周2": "周二", "2": "周二",
    "周三": "周三", "星期三": "周三", "礼拜三": "周三", "周3": "周三", "3": "周三",
    "周四": "周四", "星期四": "周四", "礼拜四": "周四", "周4": "周四", "4": "周四",
    "周五": "周五", "星期五": "周五", "礼拜五": "周五", "周5": "周五", "5": "周五",
    "周六": "周六", "星期六": "周六", "礼拜六": "周六", "周6": "周六", "6": "周六",
    "周日": "周日", "星期日": "周日", "星期天": "周日", "周7": "周日", "7": "周日", "0": "周日",
}

# 定义课表
schedule = {
    "周一": ["语文", "数学", "英语"],
    "周二": ["数学", "语文", "体育"],
    "周三": ["英语", "科学", "美术"],
    "周四": ["音乐", "数学", "语文"],
    "周五": ["体育", "英语", "班会"],
    "周六": [],
    "周日": []
}

# 定义一个函数:根据日期判断星期几
def get_weekday(date_string):
    """
    根据日期字符串(如"10月15日"或"10-15")判断星期几
    返回"周一"、"周二"等
    """
    # 获取当前年份
    current_year = datetime.datetime.now().year

    # 尝试解析日期
    try:
        # 方式1: "10月15日" → "10-15"
        date_string = date_string.replace("月", "-").replace("日", "").replace(" ", "")

        # 方式2: "10/15"
        if "/" in date_string:
            month, day = date_string.split("/")
        # 方式3: "10-15"
        elif "-" in date_string:
            month, day = date_string.split("-")
        else:
            return None  # 无法解析

        # 转换成整数
        month = int(month)
        day = int(day)

        # 创建日期对象
        date_obj = datetime.date(current_year, month, day)

        # 获取星期几(0=周一, 6=周日)
        weekday = date_obj.weekday()

        # 转换成中文
        weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
        return weekdays[weekday]

    except:
        return None  # 解析失败

print("=" * 40)
print("       欢迎使用课表查询系统")
print("=" * 40)
print("查询方式:")
print("1. 输入 '周一' - 查询周一课程")
print("2. 输入 '10月15日' 或 '10-15' - 自动判断星期几并查询")
print("输入 '退出' 结束程序")
print("=" * 40)

while True:
    user_input = input("\n请输入要查询的: ")

    if user_input == "退出":
        print("谢谢使用,再见!")
        break

    found = False

    # 先尝试匹配星期
    for day_syn, day_std in synonyms.items():
        if day_syn in user_input or user_input == day_syn:
            courses = schedule[day_std]
            if courses:
                print(f"\n{day_std}的课程有: {', '.join(courses)}")
            else:
                print(f"\n{day_std}没有课,好好休息!")
            found = True
            break

    # 如果没有匹配到星期,尝试解析为日期
    if not found:
        weekday = get_weekday(user_input)
        if weekday:
            courses = schedule[weekday]
            print(f"\n{user_input} 是 {weekday}")
            if courses:
                print(f"课程有: {', '.join(courses)}")
            else:
                print(f"今天没有课,好好休息!")
            found = True

    if not found:
        print("\n输入错误,请重新输入!")
```

**运行示例**:
```
请输入要查询的: 10月15日

10月15日 是 周二
课程有: 数学, 语文, 体育

请输入要查询的: 10-20

10-20 是 周日
今天没有课,好好休息!

请输入要查询的: 周五

周五的课程有: 体育, 英语, 班会
```

### 给家长的小贴士

**教学重点**:
1. **`datetime` 库**: Python内置的时间处理库
2. **`datetime.date(year, month, day)`**: 创建一个日期对象
3. **`.weekday()` 方法**: 返回星期几(0=周一, 6=周日)
4. **字符串操作**: `.replace()` 替换字符,`.split()` 分割字符串
5. **异常处理**: `try-except` 捕获错误,避免程序崩溃

**🖥️ 计算机知识延伸:**

**1. 时间戳(Timestamp)**
- 计算机内部用**时间戳**表示时间:从1970年1月1日0时0分0秒到现在的秒数
- 例如: 2025年10月15日的时间戳可能是 `1728950400`
- 为什么要用时间戳? 方便计算时间差!

**2. UTC时间和本地时间**
- **UTC时间**: 世界标准时间(格林威治时间)
- **本地时间**: 你所在时区的时间(如北京时间 = UTC+8)
- 计算机通常存储UTC时间,显示时转换成本地时间

**3. 时区问题**
- 如果你的用户在不同国家,需要考虑时区差异
- 例如: 北京时间是晚上8点,伦敦时间是中午12点

**家长如何辅导**:
- 🔍 **观察生活**: 和孩子一起观察生活中的时间表示(钟表、日历、手机时间)
- 🧮 **数学联系**: 用时间计算复习小学数学的时间单位换算
- 🌍 **地理联系**: 通过时区学习地理知识(不同国家的时差)
- 💻 **技术联系**: 了解计算机如何存储和处理时间数据

**`datetime` 库详解**:
```python
import datetime

# 获取当前日期
today = datetime.date.today()
print(today)  # 2025-10-15

# 创建指定日期
date_obj = datetime.date(2025, 10, 15)
print(date_obj)  # 2025-10-15

# 获取星期几
weekday = date_obj.weekday()
print(weekday)  # 1 (表示周二)

# 获取年、月、日
print(date_obj.year)   # 2025
print(date_obj.month)  # 10
print(date_obj.day)    # 15
```

**常见问题**:
- **问**: 为什么 `weekday()` 返回0-6,不是1-7?
- **答**: 这是计算机的惯例,0表示周一,6表示周日
- **问**: `try-except` 是什么?
- **答**: try尝试执行代码,如果出错就执行except中的代码,避免程序崩溃

**扩展思考**:
- 如何支持"明天"、"后天"、"下周三"?(提示:计算日期偏移)
- 如何跨年查询?(提示:解析年份)

---

### 练习4:支持"明天"和"后天"

**任务**: 修改上面的程序,支持以下查询:
- "明天" → 查询明天的课程
- "后天" → 查询后天的课程
- "昨天" → 查询昨天的课程

<details>
<summary>🔍 查看答案</summary>

```python
import datetime

# 同义词映射表
synonyms = {
    "周一": "周一", "星期一": "周一", "礼拜一": "周一", "周1": "周一", "1": "周一",
    "周二": "周二", "星期二": "周二", "礼拜二": "周二", "周2": "周二", "2": "周二",
    "周三": "周三", "星期三": "周三", "礼拜三": "周三", "周3": "周三", "3": "周三",
    "周四": "周四", "星期四": "周四", "礼拜四": "周四", "周4": "周四", "4": "周四",
    "周五": "周五", "星期五": "周五", "礼拜五": "周五", "周5": "周五", "5": "周五",
    "周六": "周六", "星期六": "周六", "礼拜六": "周六", "周6": "周六", "6": "周六",
    "周日": "周日", "星期日": "周日", "星期天": "周日", "周7": "周日", "7": "周日", "0": "周日",
}

# 定义课表
schedule = {
    "周一": ["语文", "数学", "英语"],
    "周二": ["数学", "语文", "体育"],
    "周三": ["英语", "科学", "美术"],
    "周四": ["音乐", "数学", "语文"],
    "周五": ["体育", "英语", "班会"],
    "周六": [],
    "周日": []
}

# 定义一个函数:根据日期判断星期几
def get_weekday(date_obj):
    """根据日期对象返回星期几"""
    weekday = date_obj.weekday()
    weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    return weekdays[weekday]

print("=" * 40)
print("       欢迎使用课表查询系统")
print("=" * 40)
print("查询方式:")
print("1. 输入 '周一' - 查询周一课程")
print("2. 输入 '10月15日' - 查询指定日期的课程")
print("3. 输入 '明天'、'后天'、'昨天' - 查询相对日期的课程")
print("输入 '退出' 结束程序")
print("=" * 40)

while True:
    user_input = input("\n请输入要查询的: ")

    if user_input == "退出":
        print("谢谢使用,再见!")
        break

    found = False

    # 先尝试匹配星期
    for day_syn, day_std in synonyms.items():
        if day_syn in user_input or user_input == day_syn:
            courses = schedule[day_std]
            if courses:
                print(f"\n{day_std}的课程有: {', '.join(courses)}")
            else:
                print(f"\n{day_std}没有课,好好休息!")
            found = True
            break

    # 如果没有匹配到星期,尝试特殊关键词
    if not found:
        # 获取今天的日期
        today = datetime.date.today()

        # 判断"明天"、"后天"、"昨天"
        if user_input == "明天":
            tomorrow = today + datetime.timedelta(days=1)
            weekday = get_weekday(tomorrow)
            courses = schedule[weekday]
            print(f"\n明天是 {weekday}")
            print(f"课程有: {', '.join(courses) if courses else '无课'}")
            found = True

        elif user_input == "后天":
            day_after_tomorrow = today + datetime.timedelta(days=2)
            weekday = get_weekday(day_after_tomorrow)
            courses = schedule[weekday]
            print(f"\n后天是 {weekday}")
            print(f"课程有: {', '.join(courses) if courses else '无课'}")
            found = True

        elif user_input == "昨天":
            yesterday = today - datetime.timedelta(days=1)
            weekday = get_weekday(yesterday)
            courses = schedule[weekday]
            print(f"\n昨天是 {weekday}")
            print(f"课程有: {', '.join(courses) if courses else '无课'}")
            found = True

        else:
            # 尝试解析为日期
            try:
                current_year = today.year
                date_string = user_input.replace("月", "-").replace("日", "").replace(" ", "")

                if "/" in date_string:
                    month, day = date_string.split("/")
                elif "-" in date_string:
                    month, day = date_string.split("-")
                else:
                    raise ValueError("无法解析日期")

                month = int(month)
                day = int(day)

                date_obj = datetime.date(current_year, month, day)
                weekday = get_weekday(date_obj)
                courses = schedule[weekday]

                print(f"\n{user_input} 是 {weekday}")
                print(f"课程有: {', '.join(courses) if courses else '无课'}")
                found = True

            except:
                pass  # 解析失败,继续检查其他情况

    if not found:
        print("\n输入错误,请重新输入!")
```

**运行示例**:
```
请输入要查询的: 明天

明天是 周三
课程有: 英语, 科学, 美术

请输入要查询的: 后天

后天是 周四
课程有: 音乐, 数学, 语文

请输入要查询的: 昨天

昨天是 周一
课程有: 语文, 数学, 英语
```

**改进说明**:
1. 使用 `datetime.timedelta(days=1)` 表示时间差(1天)
2. `today + timedelta(days=1)` → 明天
3. `today - timedelta(days=1)` → 昨天
4. `today + timedelta(days=2)` → 后天

</details>

---

## 第五步:添加课程、修改课程、删除课程

现在我们的课表系统只能查询,接下来要增加增删改功能!

### 程序5:完整的课表管理系统

```python
import datetime

# 同义词映射表
synonyms = {
    "周一": "周一", "星期一": "周一", "礼拜一": "周一", "周1": "周一", "1": "周一",
    "周二": "周二", "星期二": "周二", "礼拜二": "周二", "周2": "周二", "2": "周二",
    "周三": "周三", "星期三": "周三", "礼拜三": "周三", "周3": "周三", "3": "周三",
    "周四": "周四", "星期四": "周四", "礼拜四": "周四", "周4": "周四", "4": "周四",
    "周五": "周五", "星期五": "周五", "礼拜五": "周五", "周5": "周五", "5": "周五",
    "周六": "周六", "星期六": "周六", "礼拜六": "周六", "周6": "周六", "6": "周六",
    "周日": "周日", "星期日": "周日", "星期天": "周日", "周7": "周日", "7": "周日", "0": "周日",
}

# 定义课表
schedule = {
    "周一": ["语文", "数学", "英语"],
    "周二": ["数学", "语文", "体育"],
    "周三": ["英语", "科学", "美术"],
    "周四": ["音乐", "数学", "语文"],
    "周五": ["体育", "英语", "班会"],
    "周六": [],
    "周日": []
}

# 定义一个函数:根据用户输入找到星期几
def find_weekday(user_input):
    """根据用户输入返回星期几(标准格式)"""
    for day_syn, day_std in synonyms.items():
        if day_syn in user_input or user_input == day_syn:
            return day_std
    return None  # 没找到

print("=" * 40)
print("       欢迎使用课表查询系统")
print("=" * 40)
print("命令列表:")
print("1. 查询: '周一' 或 '10月15日'")
print("2. 添加: '添加 周一 体育' - 在周一添加体育课")
print("3. 修改: '修改 周一第1节 英语' - 把周一第1节改成英语")
print("4. 删除: '删除 周一第3节' - 删除周一第3节课")
print("5. 显示全部: '显示' 或 '全部'")
print("输入 '退出' 结束程序")
print("=" * 40)

while True:
    user_input = input("\n请输入命令: ").strip()

    if user_input == "退出":
        print("谢谢使用,再见!")
        break

    # ========== 查询功能 ==========
    # 先尝试匹配星期
    weekday = find_weekday(user_input)
    if weekday and not user_input.startswith(("添加", "修改", "删除")):
        courses = schedule[weekday]
        if courses:
            print(f"\n{weekday}的课程有:")
            for i, course in enumerate(courses, 1):
                print(f"  第{i}节: {course}")
        else:
            print(f"\n{weekday}没有课,好好休息!")
        continue

    # ========== 显示全部课表 ==========
    if user_input in ["显示", "全部", "课表"]:
        print("\n" + "=" * 40)
        print("           完整课表")
        print("=" * 40)
        for day in ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]:
            courses = schedule[day]
            if courses:
                print(f"{day}: {', '.join(courses)}")
            else:
                print(f"{day}: 无课")
        print("=" * 40)
        continue

    # ========== 添加课程 ==========
    if user_input.startswith("添加"):
        # 提取信息: "添加 周一 体育"
        parts = user_input[3:].strip().split()  # 去掉"添加",然后按空格分割
        if len(parts) >= 2:
            # 第一部分是星期,第二部分是课程
            weekday_input = parts[0]
            course = parts[1]

            weekday = find_weekday(weekday_input)
            if weekday:
                schedule[weekday].append(course)  # 添加到列表末尾
                print(f"\n✓ 已在{weekday}添加课程: {course}")
            else:
                print("\n✗ 星期输入错误!")
        else:
            print("\n✗ 格式错误! 正确格式: 添加 周一 体育")
        continue

    # ========== 修改课程 ==========
    if user_input.startswith("修改"):
        # 提取信息: "修改 周一第1节 英语"
        content = user_input[3:].strip()  # 去掉"修改"
        found = False

        # 尝试找到星期和节次
        for day_syn, day_std in synonyms.items():
            if day_syn in content:
                # 尝试提取"第X节"
                for i in range(1, 10):
                    if f"第{i}节" in content:
                        # 提取新课程名称
                        # 例如: "周一第1节 英语"
                        course_start = content.find(f"第{i}节") + len(f"第{i}节")
                        new_course = content[course_start:].strip()

                        # 修改课程
                        if i <= len(schedule[day_std]):
                            old_course = schedule[day_std][i-1]
                            schedule[day_std][i-1] = new_course
                            print(f"\n✓ 已把{day_std}第{i}节从'{old_course}'修改为'{new_course}'")
                        else:
                            print(f"\n✗ {day_std}第{i}节不存在!")
                        found = True
                        break
                if found:
                    break
        if not found:
            print("\n✗ 格式错误! 正确格式: 修改 周一第1节 英语")
        continue

    # ========== 删除课程 ==========
    if user_input.startswith("删除"):
        # 提取信息: "删除 周一第3节"
        content = user_input[3:].strip()  # 去掉"删除"
        found = False

        # 尝试找到星期和节次
        for day_syn, day_std in synonyms.items():
            if day_syn in content:
                # 尝试提取"第X节"
                for i in range(1, 10):
                    if f"第{i}节" in content:
                        # 删除课程
                        if i <= len(schedule[day_std]):
                            deleted_course = schedule[day_std].pop(i-1)
                            print(f"\n✓ 已删除{day_std}第{i}节: {deleted_course}")
                        else:
                            print(f"\n✗ {day_std}第{i}节不存在!")
                        found = True
                        break
                if found:
                    break
        if not found:
            print("\n✗ 格式错误! 正确格式: 删除 周一第3节")
        continue

    # 如果都不匹配,提示错误
    print("\n✗ 无法识别的命令,请重新输入!")
```

**运行示例**:
```
请输入命令: 添加 周一 体育

✓ 已在周一添加课程: 体育

请输入命令: 添加 周二 音乐

✓ 已在周二添加课程: 音乐

请输入命令: 修改 周一第1节 英语

✓ 已把周一第1节从'语文'修改为'英语'

请输入命令: 删除 周三第2节

✓ 已删除周三第2节: 科学

请输入命令: 显示

========================================
           完整课表
========================================
周一: 英语, 数学, 英语, 体育
周二: 数学, 语文, 体育, 音乐
周三: 英语, 美术
周四: 音乐, 数学, 语文
周五: 体育, 英语, 班会
周六: 无课
周日: 无课
========================================
```

### 给家长的小贴士

**教学重点**:
1. **`.startswith()` 方法**: 判断字符串是否以某个词开头
2. **`.split()` 方法**: 按空格分割字符串
3. **`.append()` 方法**: 在列表末尾添加元素
4. **`.pop(index)` 方法**: 删除指定索引的元素
5. **`continue` 语句**: 跳过本次循环,进入下一次循环
6. **字符串切片**: `user_input[3:]` 去掉前3个字符

**命令解析技巧**:
```python
# "添加 周一 体育"
command = user_input[:2]  # "添加"
content = user_input[2:]    # " 周一 体育"
weekday = content.split()[0]  # "周一"
course = content.split()[1]     # "体育"
```

**常见错误**:
- **错误**: 忘记用 `.strip()` 去掉首尾空格
- **后果**: `"添加"` 和 `"添加 "` 会被判断为不同的命令
- **解决**: `user_input.strip()`

---

### 练习5:完善增删改功能

**任务**: 修改上面的程序,增加以下功能:
1. **清空课程**: "清空 周一" → 清空周一的所有课程
2. **插入课程**: "插入 周一第2节 美术" → 在周一第2节位置插入美术课
3. **课程统计**: "统计" → 显示每周共多少节课

<details>
<summary>🔍 查看答案</summary>

```python
# 在上面的程序基础上,增加以下功能:

# ========== 清空课程 ==========
if user_input.startswith("清空"):
    content = user_input[2:].strip()
    weekday = find_weekday(content)
    if weekday:
        count = len(schedule[weekday])
        schedule[weekday] = []  # 清空列表
        print(f"\n✓ 已清空{weekday}的所有课程 (共{count}节)")
    else:
        print("\n✗ 星期输入错误!")
    continue

# ========== 插入课程 ==========
if user_input.startswith("插入"):
    content = user_input[2:].strip()
    found = False

    for day_syn, day_std in synonyms.items():
        if day_syn in content:
            for i in range(1, 10):
                if f"第{i}节" in content:
                    # 提取课程名称
                    course_start = content.find(f"第{i}节") + len(f"第{i}节")
                    new_course = content[course_start:].strip()

                    # 插入课程
                    if i <= len(schedule[day_std]) + 1:
                        schedule[day_std].insert(i-1, new_course)
                        print(f"\n✓ 已在{day_std}第{i}节插入: {new_course}")
                    else:
                        print(f"\n✗ 节次超出范围!")
                    found = True
                    break
            if found:
                break
    if not found:
        print("\n✗ 格式错误! 正确格式: 插入 周一第2节 美术")
    continue

# ========== 课程统计 ==========
if user_input in ["统计", "总数"]:
    total = 0
    print("\n" + "=" * 40)
    print("           课程统计")
    print("=" * 40)
    for day in ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]:
        count = len(schedule[day])
        total += count
        print(f"{day}: {count}节课")
    print("=" * 40)
    print(f"每周共 {total} 节课")
    print("=" * 40)
    continue
```

**运行示例**:
```
请输入命令: 清空 周六

✓ 已清空周六的所有课程 (共0节)

请输入命令: 插入 周二第2节 计算机

✓ 已在周二第2节插入: 计算机

请输入命令: 统计

========================================
           课程统计
========================================
周一: 4节课
周二: 4节课
周三: 2节课
周四: 3节课
周五: 3节课
周六: 0节课
周日: 0节课
========================================
每周共 16 节课
========================================
```

</details>

---

## 第六步:保存到文件(数据持久化)

现在程序有个大问题:关闭程序后,所有修改都会丢失!我们需要把课表**保存到文件**,下次打开时还能用。

### 💾 计算机小知识:文件系统和硬盘

**什么是文件系统?**

文件系统是计算机**组织和管理文件**的方式。你可以把它想象成一个**超级大的文件柜**:
- 📁 **文件夹(目录)**:像文件柜的抽屉,用来分类存放文件
- 📄 **文件**:像文件柜里的文件,存放具体的内容(文字、图片、程序等)
- 🔍 **路径**:文件的地址,告诉计算机去哪里找这个文件

**文件存在哪里?**

文件保存在计算机的**硬盘(Hard Disk)** 或 **固态硬盘(SSD)** 中:

```
┌─────────────────────────────────┐
│         你的电脑                 │
│  ┌──────────┐  ┌──────────┐    │
│  │  内存    │  │   硬盘   │    │
│  │ (RAM)    │  │ (HDD/SSD)│    │
│  │          │  │          │    │
│  │ 程序运行  │  │ 文件存储  │    │
│  │ 时的数据  │  │  永久数据 │    │
│  └──────────┘  └──────────┘    │
│       ↑             ↑           │
│    断电丢失      断电保留        │
└─────────────────────────────────┘
```

**内存 vs 硬盘的区别:**

| 特点 | 内存(RAM) | 硬盘(HDD/SSD) |
|------|----------|--------------|
| **速度** | 非常快 | 慢一些 |
| **容量** | 相对小 | 很大 |
| **数据保留** | 断电后丢失 | 断电后保留 |
| **用途** | 运行程序 | 存储文件 |
| **价格** | 较贵 | 较便宜 |

**为什么需要保存到文件?**

当我们运行Python程序时:
- 程序和数据(如课表)都存储在**内存**中
- 如果不保存到文件,关闭程序后数据就会**丢失**
- 保存到文件后,数据存储在**硬盘**中,下次打开还能用

**JSON是什么?**

JSON是一种**数据格式**,就像一个"快递箱",可以把Python的字典、列表打包,存到文件里:

```python
# Python字典
schedule = {"周一": ["语文", "数学"]}

↓ 转换成JSON字符串

'{"周一": ["语文", "数学"]}'

↓ 保存到硬盘文件

schedule.json (硬盘上的文件)
```

### 程序6:支持文件保存和加载

```python
import datetime
import json  # 导入JSON库,用于保存数据

# 同义词映射表
synonyms = {
    "周一": "周一", "星期一": "周一", "礼拜一": "周一", "周1": "周一", "1": "周一",
    "周二": "周二", "星期二": "周二", "礼拜二": "周二", "周2": "周二", "2": "周二",
    "周三": "周三", "星期三": "周三", "礼拜三": "周三", "周3": "周三", "3": "周三",
    "周四": "周四", "星期四": "周四", "礼拜四": "周四", "周4": "周四", "4": "周四",
    "周五": "周五", "星期五": "周五", "礼拜五": "周五", "周5": "周五", "5": "周五",
    "周六": "周六", "星期六": "周六", "礼拜六": "周六", "周6": "周六", "6": "周六",
    "周日": "周日", "星期日": "周日", "星期天": "周日", "周7": "周日", "7": "周日", "0": "周日",
}

# 定义文件名
FILENAME = "schedule.json"

# 定义课表(默认数据)
default_schedule = {
    "周一": ["语文", "数学", "英语"],
    "周二": ["数学", "语文", "体育"],
    "周三": ["英语", "科学", "美术"],
    "周四": ["音乐", "数学", "语文"],
    "周五": ["体育", "英语", "班会"],
    "周六": [],
    "周日": []
}

# 定义一个函数:加载课表
def load_schedule():
    """从文件加载课表,如果文件不存在则使用默认课表"""
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            data = f.read()
            schedule = json.loads(data)
            print(f"\n✓ 已从 {FILENAME} 加载课表")
            return schedule
    except FileNotFoundError:
        print(f"\n✗ 文件 {FILENAME} 不存在,使用默认课表")
        return default_schedule.copy()  # 复制一份,避免修改原数据
    except Exception as e:
        print(f"\n✗ 加载失败: {e}")
        return default_schedule.copy()

# 定义一个函数:保存课表
def save_schedule(schedule):
    """把课表保存到文件"""
    try:
        data = json.dumps(schedule, ensure_ascii=False, indent=2)
        with open(FILENAME, "w", encoding="utf-8") as f:
            f.write(data)
        print(f"\n✓ 课表已保存到 {FILENAME}")
    except Exception as e:
        print(f"\n✗ 保存失败: {e}")

# 定义一个函数:根据用户输入找到星期几
def find_weekday(user_input):
    """根据用户输入返回星期几(标准格式)"""
    for day_syn, day_std in synonyms.items():
        if day_syn in user_input or user_input == day_syn:
            return day_std
    return None  # 没找到

# 加载课表
schedule = load_schedule()

print("=" * 40)
print("       欢迎使用课表查询系统")
print("=" * 40)
print("命令列表:")
print("1. 查询: '周一' 或 '10月15日'")
print("2. 添加: '添加 周一 体育' - 在周一添加体育课")
print("3. 修改: '修改 周一第1节 英语' - 把周一第1节改成英语")
print("4. 删除: '删除 周一第3节' - 删除周一第3节课")
print("5. 显示: '显示' 或 '全部'")
print("6. 保存: '保存' - 保存课表到文件")
print("输入 '退出' 结束程序")
print("=" * 40)

while True:
    user_input = input("\n请输入命令: ").strip()

    if user_input == "退出":
        # 退出前自动保存
        save_schedule(schedule)
        print("谢谢使用,再见!")
        break

    # ========== 查询功能 ==========
    weekday = find_weekday(user_input)
    if weekday and not user_input.startswith(("添加", "修改", "删除", "清空", "插入")):
        courses = schedule[weekday]
        if courses:
            print(f"\n{weekday}的课程有:")
            for i, course in enumerate(courses, 1):
                print(f"  第{i}节: {course}")
        else:
            print(f"\n{weekday}没有课,好好休息!")
        continue

    # ========== 显示全部课表 ==========
    if user_input in ["显示", "全部", "课表"]:
        print("\n" + "=" * 40)
        print("           完整课表")
        print("=" * 40)
        for day in ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]:
            courses = schedule[day]
            if courses:
                print(f"{day}: {', '.join(courses)}")
            else:
                print(f"{day}: 无课")
        print("=" * 40)
        continue

    # ========== 保存课表 ==========
    if user_input in ["保存", "save"]:
        save_schedule(schedule)
        continue

    # ========== 添加课程 ==========
    if user_input.startswith("添加"):
        parts = user_input[3:].strip().split()
        if len(parts) >= 2:
            weekday_input = parts[0]
            course = parts[1]

            weekday = find_weekday(weekday_input)
            if weekday:
                schedule[weekday].append(course)
                print(f"\n✓ 已在{weekday}添加课程: {course}")
            else:
                print("\n✗ 星期输入错误!")
        else:
            print("\n✗ 格式错误! 正确格式: 添加 周一 体育")
        continue

    # ========== 修改课程 ==========
    if user_input.startswith("修改"):
        content = user_input[3:].strip()
        found = False

        for day_syn, day_std in synonyms.items():
            if day_syn in content:
                for i in range(1, 10):
                    if f"第{i}节" in content:
                        course_start = content.find(f"第{i}节") + len(f"第{i}节")
                        new_course = content[course_start:].strip()

                        if i <= len(schedule[day_std]):
                            old_course = schedule[day_std][i-1]
                            schedule[day_std][i-1] = new_course
                            print(f"\n✓ 已把{day_std}第{i}节从'{old_course}'修改为'{new_course}'")
                        else:
                            print(f"\n✗ {day_std}第{i}节不存在!")
                        found = True
                        break
                if found:
                    break
        if not found:
            print("\n✗ 格式错误! 正确格式: 修改 周一第1节 英语")
        continue

    # ========== 删除课程 ==========
    if user_input.startswith("删除"):
        content = user_input[3:].strip()
        found = False

        for day_syn, day_std in synonyms.items():
            if day_syn in content:
                for i in range(1, 10):
                    if f"第{i}节" in content:
                        if i <= len(schedule[day_std]):
                            deleted_course = schedule[day_std].pop(i-1)
                            print(f"\n✓ 已删除{day_std}第{i}节: {deleted_course}")
                        else:
                            print(f"\n✗ {day_std}第{i}节不存在!")
                        found = True
                        break
                if found:
                    break
        if not found:
            print("\n✗ 格式错误! 正确格式: 删除 周一第3节")
        continue

    # 如果都不匹配,提示错误
    print("\n✗ 无法识别的命令,请重新输入!")
```

**运行示例**:
```
✓ 已从 schedule.json 加载课表

请输入命令: 添加 周二 计算机

✓ 已在周二添加课程: 计算机

请输入命令: 保存

✓ 课表已保存到 schedule.json

请输入命令: 退出

✓ 课表已保存到 schedule.json
谢谢使用,再见!
```

**保存的文件内容 (`schedule.json`)**:
```json
{
  "周一": [
    "语文",
    "数学",
    "英语"
  ],
  "周二": [
    "数学",
    "语文",
    "体育",
    "计算机"
  ],
  "周三": [
    "英语",
    "科学",
    "美术"
  ],
  "周四": [
    "音乐",
    "数学",
    "语文"
  ],
  "周五": [
    "体育",
    "英语",
    "班会"
  ],
  "周六": [],
  "周日": []
}
```

### 给家长的小贴士

**教学重点**:
1. **`json` 库**: 用于在文件中存储字典和列表
2. **`json.dumps()`**: 把Python对象转换成JSON字符串
3. **`json.loads()`**: 把JSON字符串转换成Python对象
4. **文件操作**: `open()` 打开文件,`f.read()` 读取,`f.write()` 写入
5. **异常处理**: `try-except` 捕获文件操作错误

**💾 计算机知识延伸:**

**1. 文件的编码(UTF-8)**
- 计算机存储文件时需要把字符转换成**二进制(0和1)**
- **UTF-8**是一种通用的字符编码标准,支持中文、英文、日文等
- 如果不用UTF-8,中文可能会乱码!

**2. 文本文件 vs 二进制文件**
- **文本文件**: 用字符编码存储,可以直接阅读(如.txt、.json、.md)
- **二进制文件**: 用二进制存储,需要专门软件打开(如.jpg、.mp3、.exe)

**3. 文件路径**
- **相对路径**: 相对于当前程序的位置(如`schedule.json`)
- **绝对路径**: 从根目录开始的完整路径(如`C:\Users\张三\schedule.json`)

**4. 文件读写模式**
- `"r"`: 只读模式(文件必须存在)
- `"w"`: 写入模式(会覆盖原文件!)
- `"a"`: 追加模式(在文件末尾添加)
- `"r+"`: 读写模式

**家长如何辅导**:
- 📂 **观察文件**: 打开`schedule.json`文件,让孩子看到JSON格式的结构
- 🔍 **对比数据**: 修改程序中的课表,保存后观察文件变化
- 💡 **讨论存储**: 为什么需要把数据保存到文件?关机后数据还在吗?
- 🛡️ **安全意识**: 讲解为什么"写入模式"会覆盖原文件,培养数据安全意识

**扩展活动**:
1. 用记事本打开`schedule.json`,手动修改课程名称,再运行程序看效果
2. 删除`schedule.json`文件,看程序如何处理(会使用默认课表)
3. 把`schedule.json`复制一份,体验"备份"的概念

**`json` 库详解**:
```python
import json

# Python字典
data = {
    "name": "小明",
    "age": 10,
    "courses": ["语文", "数学", "英语"]
}

# 转换成JSON字符串
json_string = json.dumps(data, ensure_ascii=False, indent=2)
print(json_string)
# 输出:
# {
#   "name": "小明",
#   "age": 10,
#   "courses": ["语文", "数学", "英语"]
# }

# 从JSON字符串转换回Python字典
data2 = json.loads(json_string)
print(data2["name"])  # 小明
```

**文件操作详解**:
```python
# 写入文件
with open("schedule.json", "w", encoding="utf-8") as f:
    f.write(json_string)

# 读取文件
with open("schedule.json", "r", encoding="utf-8") as f:
    content = f.read()
    data = json.loads(content)
```

**常见问题**:
- **问**: 为什么要用 `encoding="utf-8"`?
- **答**: 支持中文,避免乱码
- **问**: `with open(...)` 和 `f = open(); ...; f.close()` 有什么区别?
- **答**: `with` 会自动关闭文件,更安全

---

## 第七步:使用正则表达式(高级功能)

现在我们的程序有个问题:用户必须严格按照格式输入命令,比如:
- ✅ "添加 周一 体育"
- ❌ "添加周一体育" (缺少空格)
- ❌ "在周一添加体育课" (格式不对)

**正则表达式(Regular Expression)**可以帮我们灵活地解析用户输入!

### 什么是正则表达式?

正则表达式是一种**匹配字符串的模式**。它可以:
- ✅ 灵活匹配各种格式的输入
- ✅ 提取字符串中的关键信息
- ✅ 验证输入格式是否正确

**举个例子**:
```python
import re

# 匹配"周一"、"星期一"、"礼拜一"
pattern = r"(周一|星期一|礼拜一)"
text = "今天是星期一"
result = re.search(pattern, text)
if result:
    print("找到匹配:", result.group())  # 星期一
```

### 程序7:使用正则表达式解析命令

```python
import datetime
import json
import re  # 导入正则表达式库

# 同义词映射表(保持不变)
synonyms = {
    "周一": "周一", "星期一": "周一", "礼拜一": "周一", "周1": "周一", "1": "周一",
    "周二": "周二", "星期二": "周二", "礼拜二": "周二", "周2": "周二", "2": "周二",
    "周三": "周三", "星期三": "周三", "礼拜三": "周三", "周3": "周三", "3": "周三",
    "周四": "周四", "星期四": "周四", "礼拜四": "周四", "周4": "周四", "4": "周四",
    "周五": "周五", "星期五": "周五", "礼拜五": "周五", "周5": "周五", "5": "周五",
    "周六": "周六", "星期六": "周六", "礼拜六": "周六", "周6": "周六", "6": "周六",
    "周日": "周日", "星期日": "周日", "星期天": "周日", "周7": "周日", "7": "周日", "0": "周日",
}

# 文件名
FILENAME = "schedule.json"

# 默认课表
default_schedule = {
    "周一": ["语文", "数学", "英语"],
    "周二": ["数学", "语文", "体育"],
    "周三": ["英语", "科学", "美术"],
    "周四": ["音乐", "数学", "语文"],
    "周五": ["体育", "英语", "班会"],
    "周六": [],
    "周日": []
}

# 加载和保存函数(保持不变)
def load_schedule():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            data = f.read()
            schedule = json.loads(data)
            print(f"\n✓ 已从 {FILENAME} 加载课表")
            return schedule
    except:
        print(f"\n✓ 使用默认课表")
        return default_schedule.copy()

def save_schedule(schedule):
    try:
        data = json.dumps(schedule, ensure_ascii=False, indent=2)
        with open(FILENAME, "w", encoding="utf-8") as f:
            f.write(data)
        print(f"\n✓ 课表已保存")
    except Exception as e:
        print(f"\n✗ 保存失败: {e}")

# 新函数:使用正则表达式解析命令
def parse_command(user_input):
    """
    使用正则表达式解析用户命令
    返回: (命令类型, 星期, 节次, 课程名称)
    """
    # 定义正则表达式模式
    patterns = {
        "查询": r"(周一|周二|周三|周四|周五|周六|周日|星期一|星期二|星期三|星期四|星期五|星期六|星期日|礼拜一|礼拜二|礼拜三|礼拜四|礼拜五|礼拜六|礼拜日)",
        "添加": r"添加.*?(周一|周二|周三|周四|周五|周六|周日|星期一|星期二|星期三|星期四|星期五|星期六|星期日|礼拜一|礼拜二|礼拜三|礼拜四|礼拜五|礼拜六|礼拜日)\s*(.*)",
        "修改": r"修改.*?(周一|周二|周三|周四|周五|周六|周日|星期一|星期二|星期三|星期四|星期五|星期六|星期日|礼拜一|礼拜二|礼拜三|礼拜四|礼拜五|礼拜六|礼拜日).?第(\d+)节\s*(.*)",
        "删除": r"删除.*?(周一|周二|周三|周四|周五|周六|周日|星期一|星期二|星期三|星期四|星期五|星期六|星期日|礼拜一|礼拜二|礼拜三|礼拜四|礼拜五|礼拜六|礼拜日).?第(\d+)节",
    }

    # 尝试匹配每个模式
    for cmd_type, pattern in patterns.items():
        match = re.search(pattern, user_input)
        if match:
            groups = match.groups()
            if cmd_type == "查询":
                return ("查询", groups[0], None, None)
            elif cmd_type == "添加":
                return ("添加", groups[0], None, groups[1].strip())
            elif cmd_type == "修改":
                return ("修改", groups[0], int(groups[1]), groups[2].strip())
            elif cmd_type == "删除":
                return ("删除", groups[0], int(groups[1]), None)

    return (None, None, None, None)  # 没匹配到

# 加载课表
schedule = load_schedule()

print("=" * 40)
print("       欢迎使用课表查询系统")
print("=" * 40)
print("命令列表(更灵活的输入方式):")
print("1. 查询: '周一' / '今天是周几' / '查询周一'")
print("2. 添加: '添加周一体育' / '在周一添加体育课'")
print("3. 修改: '修改周一第1节英语' / '把周一第1节改成英语'")
print("4. 删除: '删除周一第3节' / '把周一第3节删了'")
print("5. 显示: '显示' / '全部课表'")
print("6. 保存: '保存'")
print("输入 '退出' 结束程序")
print("=" * 40)

while True:
    user_input = input("\n请输入命令: ").strip()

    if user_input == "退出":
        save_schedule(schedule)
        print("谢谢使用,再见!")
        break

    # 显示全部课表
    if user_input in ["显示", "全部", "课表", "全部课表"]:
        print("\n" + "=" * 40)
        print("           完整课表")
        print("=" * 40)
        for day in ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]:
            courses = schedule[day]
            if courses:
                print(f"{day}: {', '.join(courses)}")
            else:
                print(f"{day}: 无课")
        print("=" * 40)
        continue

    # 保存课表
    if user_input in ["保存", "save"]:
        save_schedule(schedule)
        continue

    # 使用正则表达式解析命令
    cmd_type, day_input, period, course = parse_command(user_input)

    # 转换星期成标准格式
    if day_input and day_input in synonyms:
        day_std = synonyms[day_input]
    else:
        day_std = None

    # 执行命令
    if cmd_type == "查询" and day_std:
        courses = schedule[day_std]
        if courses:
            print(f"\n{day_std}的课程有:")
            for i, c in enumerate(courses, 1):
                print(f"  第{i}节: {c}")
        else:
            print(f"\n{day_std}没有课,好好休息!")

    elif cmd_type == "添加" and day_std and course:
        schedule[day_std].append(course)
        print(f"\n✓ 已在{day_std}添加课程: {course}")

    elif cmd_type == "修改" and day_std and period and course:
        if period <= len(schedule[day_std]):
            old_course = schedule[day_std][period-1]
            schedule[day_std][period-1] = course
            print(f"\n✓ 已把{day_std}第{period}节从'{old_course}'修改为'{course}'")
else:
            print(f"\n✗ {day_std}第{period}节不存在!")

    elif cmd_type == "删除" and day_std and period:
        if period <= len(schedule[day_std]):
            deleted_course = schedule[day_std].pop(period-1)
            print(f"\n✓ 已删除{day_std}第{period}节: {deleted_course}")
        else:
            print(f"\n✗ {day_std}第{period}节不存在!")

    else:
        print("\n✗ 无法识别的命令,请重新输入!")
```

**运行示例**:
```
请输入命令: 查询周一

周一的课程有:
  第1节: 语文
  第2节: 数学
  第3节: 英语

请输入命令: 在周二添加计算机课

✓ 已在周二添加课程: 计算机课

请输入命令: 把周三第2节改成体育

✓ 已把周三第2节从'科学'修改为'体育'

请输入命令: 删除周四第3节课

✓ 已删除周四第3节: 语文

请输入命令: 今天是周几
无法识别的命令,请重新输入!
```

### 给家长的小贴士

**教学重点**:
1. **`re` 库**: Python的正则表达式库
2. **`re.search()`**: 在字符串中搜索模式
3. **`.groups()`**: 获取匹配的分组
4. **正则表达式语法**:
   - `.*?` 匹配任意字符(非贪婪)
   - `(a|b)` 匹配a或b
   - `\d+` 匹配一个或多个数字
   - `\s*` 匹配零个或多个空格

**正则表达式详解**:
```python
import re

# 示例1: 提取星期和课程
pattern = r"添加.*?(周一|周二).*?(.*)"
text = "在周一添加体育课"
match = re.search(pattern, text)
if match:
    day = match.group(1)  # 周一
    course = match.group(2)  # 体育课
    print(day, course)

# 示例2: 提取节次
pattern = r"第(\d+)节"
text = "修改周一第3节英语"
match = re.search(pattern, text)
if match:
    period = int(match.group(1))  # 3
    print(period)
```

**优点**:
- ✅ 用户可以用各种说法表达同一意思
- ✅ 代码更简洁,不需要很多 `if` 判断
- ✅ 易于扩展新的命令格式

**缺点**:
- ❌ 正则表达式语法复杂,难以学习
- ❌ 调试困难

---

## 综合项目:完整的智能课表系统

现在让我们把所有功能整合起来,做一个完整的课表系统!

### 完整功能列表

1. ✅ 查询课程(支持多种说法)
2. ✅ 添加/修改/删除课程
3. ✅ 支持上午/下午区分
4. ✅ 支持日期查询(10月15日)
5. ✅ 支持相对日期(明天、后天)
6. ✅ 自动保存到文件
7. ✅ 正则表达式解析命令
8. 🆕 课程提醒功能
9. 🆕 课程搜索功能
10. 🆕 数据备份功能

### 挑战练习

请尝试在现有程序基础上,增加以下功能:

#### 挑战1:课程搜索
**目标**: 用户输入"搜索体育",显示所有包含"体育"的课程

<details>
<summary>💡 提示</summary>

```python
if user_input.startswith("搜索"):
    keyword = user_input[3:].strip()
    print(f"\n搜索 '{keyword}':")

    found = False
    for day in ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]:
        courses = schedule[day]
        for i, course in enumerate(courses, 1):
            if keyword in course:
                print(f"  {day}第{i}节: {course}")
                found = True

    if not found:
        print(f"  没找到包含'{keyword}'的课程")
```

</details>

---

#### 挑战2:课程提醒
**目标**: 每次查询时,如果今天的课程很多(>5节),提醒用户"今天课程较重,注意休息!"

<details>
<summary>💡 提示</summary>

```python
# 在查询功能中增加:
if len(courses) > 5:
    print(f"\n⚠️ 提醒: 今天课程较多({len(courses)}节),注意休息!")
```

</details>

---

#### 挑战3:数据备份
**目标**: 增加"备份"命令,把当前课表复制到 `schedule_backup.json`

<details>
<summary>💡 提示</summary>

```python
if user_input in ["备份", "backup"]:
    backup_filename = "schedule_backup.json"
    data = json.dumps(schedule, ensure_ascii=False, indent=2)
    with open(backup_filename, "w", encoding="utf-8") as f:
        f.write(data)
    print(f"\n✓ 已备份到 {backup_filename}")
```

</details>

---

## 本章小结

### 核心知识点回顾

1. **命令行程序**: 通过文字命令和计算机交互的程序
2. **字典应用**: 用嵌套字典存储复杂数据(课表)
3. **同义词映射**: 用字典把各种说法统一成标准格式
4. **时间处理**: 使用 `datetime` 库处理日期和时间
5. **文件操作**: 使用 `json` 库保存和加载数据
6. **正则表达式**: 灵活解析用户输入
7. **函数封装**: 把重复的代码封装成函数

### 🖥️ 计算机知识回顾

本章我们学到了重要的计算机体系结构知识:

1. **命令行历史**
   - 早期计算机使用命令行交互(1970-1980年代)
   - 命令行占用CPU和内存资源少,运行速度快
   - 图形界面占用资源多,但更直观易用

2. **文件系统**
   - 文件系统是计算机组织文件的方式
   - 文件夹(目录)用于分类管理文件
   - 路径告诉计算机去哪里找文件

3. **内存 vs 硬盘**
   - **内存(RAM)**: 速度快,断电后数据丢失,用于运行程序
   - **硬盘(HDD/SSD)**: 速度较慢,断电后数据保留,用于存储文件
   - 数据需要保存到文件才能持久化

4. **数据编码**
   - **UTF-8**: 通用字符编码,支持中文等多种语言
   - **JSON**: 轻量级数据交换格式,易于人阅读和编写
   - 文本文件 vs 二进制文件

5. **时间表示**
   - **时间戳**: 计算机用从1970年1月1日到现在的秒数表示时间
   - **UTC vs 本地时间**: 世界标准时间 vs 你所在时区的时间
   - 时区差异: 不同国家的时间差异

### 🧮 数学知识回顾

本章用到了重要的数学知识:

1. **时间单位换算**
   - 1小时 = 60分钟
   - 1分钟 = 60秒
   - 时间加减法计算

2. **四则运算应用**
   - 计算上课总时长: 节数 × 分钟数
   - 时间单位转换: 分钟 → 小时和分钟
   - 整除和取余: `//` 和 `%`

3. **实际应用问题**
   - 计算在校时长(包括课间)
   - 计算一周总课时
   - 时间段计算(7:30 - 16:30)

### 能力检查表

**编程能力**:
- [ ] 能够使用字典存储课表数据
- [ ] 能够处理用户的多种说法(同义词)
- [ ] 能够使用 `datetime` 库判断星期几
- [ ] 能够使用 `json` 库保存和加载数据
- [ ] 能够使用正则表达式解析命令
- [ ] 能够设计一个完整的命令行程序

**计算机知识**:
- [ ] 理解命令行程序的历史和特点
- [ ] 理解文件系统的基本概念
- [ ] 理解内存和硬盘的区别
- [ ] 理解数据编码(UTF-8、JSON)
- [ ] 理解时间戳和时区

**数学能力**:
- [ ] 能够进行时间单位换算
- [ ] 能够计算上课时长
- [ ] 能够解决实际的时间问题

### 常见错误和调试

| 错误类型 | 原因 | 解决方法 |
|---------|------|---------|
| `KeyError: '周一'` | 字典中不存在这个键 | 用 `in` 检查键是否存在 |
| `IndexError: list index out of range` | 列表索引超出范围 | 检查 `i <= len(list)` |
| `FileNotFoundError` | 文件不存在 | 用 `try-except` 捕获异常 |
| `JSONDecodeError` | JSON格式错误 | 检查JSON格式是否正确 |
| 正则表达式不匹配 | 模式书写错误 | 使用在线工具测试正则表达式 |

### 调试技巧

1. **打印中间结果**:
   ```python
   print(f"解析结果: cmd={cmd_type}, day={day_std}, period={period}")
   ```

2. **简化问题**:
   - 先实现简单版本,再逐步增加功能
   - 每增加一个功能,测试一次

3. **使用在线工具**:
   - 正则表达式测试: https://regex101.com/
   - JSON格式化: https://www.json.cn/

---

## 挑战练习

### 练习1:课程时间表

**任务**: 在课表中增加每节课的时间,如:
```python
"周一": {
    "1": {"课程": "语文", "时间": "8:00-8:45"},
    "2": {"课程": "数学", "时间": "8:55-9:40"},
    ...
}
```

---

### 练习2:课程备注

**任务**: 为每节课增加备注字段,如:
```python
"周一": [
    {"课程": "语文", "备注": "带作文本"},
    {"课程": "数学", "备注": "带计算器"},
    ...
]
```

---

### 练习3:多课表管理

**任务**: 支持多个课表(如上半学期、下半学期),用户可以切换:
```
命令: 切换到上半学期
命令: 切换到下半学期
```

---

### 练习4:课表分享

**任务**: 增加"导出"功能,把课表导出为:
- 文本格式(`.txt`)
- Markdown格式(`.md`)
- HTML格式(`.html`)

---

### 练习5:图形化界面

**任务**: 使用 `tkinter` 库(第16章会学)为课表系统添加图形界面!

---

## 下一章预告

本章我们开发了一个功能完整的命令行程序,综合运用了:
- 字典和列表
- 条件和循环
- 文件操作
- 时间处理
- 正则表达式

下一章(第15章),我们将学习**报表程序**,使用 `pyecharts` 库生成各种图表(柱状图、折线图、饼图),让数据可视化!

准备好进入**数据可视化**的世界了吗? 🎨📊
