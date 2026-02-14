# 第15章 报表程序 - 让数据说话

## 引言:从数字到图表

想象一下,如果你是一名老师,手里有一份学生的考试成绩单,上面只有密密麻麻的数字:

```
小明: 语文85 数学92 英语78
小红: 语文90 数学88 英语95
小刚: 语文78 数学85 英语82
...
```

你能快速看出:
- 哪个科目最难?
- 每个学生的强项是什么?
- 全班的平均成绩如何?

如果把这些数字画成图表,比如柱状图或折线图,答案就会一目了然!这就是**数据可视化**的作用——把枯燥的数字变成直观的图形,让数据"说话"。

### 什么是报表程序?

**报表程序**就是用来收集、处理和展示数据的程序。在我们的日常生活中:

- **天气预报**:用折线图显示未来一周的气温变化
- **股票软件**:用K线图显示股票价格波动
- **运动APP**:用饼图显示你今天的运动时间分配
- **游戏排行榜**:用柱状图显示玩家积分排名

这些程序都有一个共同点:把数据变成图表,让人更容易理解数据背后的信息。

### 为什么学习报表程序?

学习制作报表程序,你将掌握:
1. **数据处理能力**:学会整理和分析数据
2. **可视化思维**:学会用图形表达信息
3. **实用工具**:能制作出真正有用的程序

比如,你可以:
- 制作班级成绩分析报告
- 记录自己的零花钱使用情况
- 统计家里的电费水费变化
- 分析自己喜欢的游戏数据

### 本章学习路线

本章将教你如何使用**pyecharts**库制作各种图表:

```
第1步: 安装和配置pyecharts库
   ↓
第2步: 柱状图 - 比较不同类别的数据
   ↓
第3步: 折线图 - 显示数据的变化趋势
   ↓
第4步: 饼图 - 显示各部分占整体的比例
   ↓
第5步: 综合项目 - 制作完整的数据报表
```

> #### 给家长的小贴士
> - **数据可视化**是现代信息时代的重要技能
> - 图表能培养孩子的**抽象思维能力**
> - 建议选择孩子感兴趣的数据(如游戏数据、运动数据)作为练习素材
> - 鼓励孩子用图表解决实际问题(如班级统计、家庭记账)

---

## 15.1 认识pyecharts库

### 15.1.1 什么是pyecharts?

**pyecharts**是一个专门用于生成图表的Python库。它的名字可以拆解为:
- **py**: Python的缩写
- **echarts**: 百度开源的一个强大图表工具
- **s**: 表示这是echarts的Python版本

**为什么要使用pyecharts?**
1. **功能强大**: 支持几十种图表类型
2. **美观漂亮**: 生成的图表配色和样式都很专业
3. **易于使用**: 只需要几行代码就能生成图表
4. **交互式**: 生成的图表支持鼠标悬停、点击缩放等操作

### 15.1.2 安装pyecharts

在开始使用pyecharts之前,需要先安装它。还记得我们在第13章学过的**pip**工具吗?

#### 步骤1: 打开命令行窗口

**Windows系统**:
1. 按Win+R键
2. 输入`cmd`
3. 按回车键

**Mac系统**:
1. 按Command+空格键
2. 输入"终端"
3. 按回车键

#### 步骤2: 安装pyecharts

在命令行窗口中输入以下命令:

```bash
pip install pyecharts
```

你会看到类似这样的输出:

```
Collecting pyecharts
  Downloading pyecharts-2.0.4-py3-none-any.whl (...)
Installing collected packages: pyecharts
Successfully installed pyecharts-2.0.4
```

#### 步骤3: 验证安装

安装完成后,在Python中输入以下代码测试:

```python
from pyecharts.charts import Bar
print("pyecharts安装成功!")
```

如果输出"pyecharts安装成功!"说明安装成功了!

#### 步骤4: (可选)安装图片快照功能

如果你想直接把图表保存为图片格式,需要安装额外的插件:

```bash
pip install pyecharts_snapshot
```

这个功能可以把HTML格式的图表转换为PNG或JPG图片。

> #### 给家长的小贴士
> - **pip安装失败**: 可能是因为网络问题,可以尝试使用国内镜像源:`pip install pyecharts -i https://pypi.tuna.tsinghua.edu.cn/simple`
> - **权限问题**: 如果提示权限不足,在Windows上以管理员身份运行命令行,Mac上使用sudo
> - **版本问题**: pyecharts有v1和v2两个版本,本书使用v2版本
> - **离线安装**: 如果网络不好,可以下载whl文件后本地安装

> #### 常见问题解答
> **Q: 为什么要安装这么大的库?**
> A: pyecharts包含了大量的图表模板和样式文件,所以比较大。但这些文件让我们能做出更专业的图表。
>
> **Q: 安装失败怎么办?**
> A: 1) 检查网络连接 2) 尝试升级pip:`python -m pip install --upgrade pip` 3) 使用国内镜像源
>
> **Q: 每次使用都要重新安装吗?**
> A: 不需要!安装一次后,以后在任何Python程序中都可以使用。

### 15.1.3 pyecharts的基本使用流程

使用pyecharts生成图表一般分为5个步骤:

```python
# 步骤1: 导入需要的图表类
from pyecharts.charts import Bar

# 步骤2: 创建图表对象
bar = Bar()

# 步骤3: 添加数据
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 10, 100])

# 步骤4: 设置全局选项(可选)
bar.set_global_opts(title_opts={"text": "我的第一个图表"})

# 步骤5: 渲染生成HTML文件
bar.render("my_first_chart.html")
```

**代码解析**:
1. **导入**: 从pyecharts.charts导入你需要的图表类(如Bar、Line、Pie)
2. **创建**: 创建一个图表对象
3. **数据**: 用add_xaxis()添加x轴数据,用add_yaxis()添加y轴数据
4. **选项**: 设置标题、图例、工具箱等配置
5. **渲染**: 生成一个HTML文件,用浏览器打开就能看到图表

**运行结果**:
程序运行后,会在当前目录下生成`my_first_chart.html`文件。双击这个文件,浏览器会打开它,你就能看到一个漂亮的柱状图了!

> #### 给家长的小贴士
> - **HTML文件**: 生成的图表是网页格式(HTML),不需要额外安装软件就能打开
> - **代码结构**: 强调"导入-创建-添加数据-设置选项-渲染"这5步固定流程
> - **逐步演示**: 建议先让孩子看完整的运行效果,激发学习兴趣
> - **文件位置**: 提醒孩子注意HTML文件的保存位置,方便查找

> #### 实践练习1:修改数据
>
> **任务**: 将上面的代码复制下来,修改数据:
> - x轴改成你喜欢的6种水果
> - y轴改成每种水果的价格(元)
> - 标题改成"水果价格表"
>
> **提示**:
> ```python
> bar.add_xaxis(["苹果", "香蕉", "橙子", "草莓", "葡萄", "西瓜"])
> bar.add_yaxis("价格", [8, 3, 6, 15, 12, 5])
> ```
>
> **答案**:
> <details>
> <summary>点击查看完整代码</summary>
>
> ```python
> from pyecharts.charts import Bar
>
> # 创建图表对象
> bar = Bar()
>
> # 添加数据
> bar.add_xaxis(["苹果", "香蕉", "橙子", "草莓", "葡萄", "西瓜"])
> bar.add_yaxis("价格(元)", [8, 3, 6, 15, 12, 5])
>
> # 设置标题
> bar.set_global_opts(title_opts={"text": "水果价格表"})
>
> # 生成图表
> bar.render("fruit_price.html")
> ```
> 运行后打开`fruit_price.html`,你就能看到水果价格的柱状图了!
> </details>

---

## 15.2 柱状图 - 比较大小的高手

### 15.2.1 柱状图的应用场景

**柱状图(Bar Chart)**是最常见的图表类型之一,它用柱子的高度来表示数据的大小。

**柱状图适合用来**:
- **比较不同类别**: 比较不同产品的销量
- **排名**: 显示班级成绩排名
- **统计**: 统计每个月的零花钱支出

**生活中的柱状图例子**:
- 奥运会奖牌榜
- 游戏英雄战斗力对比
- 各城市人口数量对比

### 15.2.2 创建一个简单的柱状图

让我们从最简单的例子开始——制作一个班级成绩的柱状图:

```python
from pyecharts.charts import Bar

# 创建柱状图
bar = Bar()

# 添加x轴数据(学生姓名)
bar.add_xaxis(["小明", "小红", "小刚", "小丽", "小华"])

# 添加y轴数据(语文成绩)
bar.add_yaxis("语文成绩", [85, 90, 78, 92, 88])

# 设置标题
bar.set_global_opts(title_opts={"text": "班级语文成绩"})

# 生成HTML文件
bar.render("class_scores.html")
```

**运行结果**:
程序会生成`class_scores.html`文件,用浏览器打开后,你会看到5个不同高度的柱子,每个柱子代表一个学生的语文成绩。

### 15.2.3 添加多个系列的数据

有时候我们需要对比多组数据。比如,想同时显示每个学生的语文、数学、英语成绩:

```python
from pyecharts.charts import Bar

bar = Bar()

# 添加x轴(学生姓名)
bar.add_xaxis(["小明", "小红", "小刚", "小丽", "小华"])

# 添加多组数据
bar.add_yaxis("语文", [85, 90, 78, 92, 88])
bar.add_yaxis("数学", [92, 88, 85, 95, 90])
bar.add_yaxis("英语", [78, 95, 82, 88, 91])

# 设置标题
bar.set_global_opts(title_opts={"text": "班级成绩表"})

# 生成图表
bar.render("class_scores_all.html")
```

**图表解读**:
- 每个学生会有3根柱子,分别代表语文、数学、英语成绩
- 不同颜色的柱子代表不同的科目
- 图表右上角会显示图例(语文、数学、英语),点击可以隐藏/显示对应的数据

> #### 给家长的小贴士
> - **颜色区分**: 帮助孩子理解不同颜色代表不同数据系列
> - **图例功能**: 演示点击图例可以隐藏/显示数据,这是pyecharts的交互功能
> - **数据对应**: 确保x轴和y轴的数据数量一致,否则会报错
> - **中文字符**: pyecharts完全支持中文,不会出现乱码问题

> #### 实践练习2:最喜欢的运动统计
>
> **任务**: 调查班级同学最喜欢的运动,制作柱状图:
> - x轴: 篮球、足球、羽毛球、乒乓球、跑步、游泳
> - y轴: 喜欢该项运动的人数(假设为: 15, 12, 8, 10, 6, 9)
> - 标题: "班级运动喜好调查"
>
> **要求**:
> 1. 添加y轴名称:"人数"
> 2. 添加数据标签显示每个柱子上的具体数值
>
> **答案**:
> <details>
> <summary>点击查看完整代码</summary>
>
> ```python
> from pyecharts.charts import Bar
> from pyecharts import options as opts
>
> bar = Bar()
>
> # 添加数据
> bar.add_xaxis(["篮球", "足球", "羽毛球", "乒乓球", "跑步", "游泳"])
> bar.add_yaxis(
>     series_name="人数",
>     yaxis_data=[15, 12, 8, 10, 6, 9],
>     label_opts=opts.LabelOpts(is_show=True)  # 显示数据标签
> )
>
> # 设置全局选项
> bar.set_global_opts(
>     title_opts={"text": "班级运动喜好调查"},
>     yaxis_opts=opts.AxisOpts(name="人数"),
>     xaxis_opts=opts.AxisOpts(name="运动项目")
> )
>
> # 生成图表
> bar.render("sports_survey.html")
> ```
> 运行后,每个柱子上会显示具体人数,方便读取数据!
> </details>

### 15.2.4 柱状图的高级设置

#### 1. 水平柱状图

默认的柱状图是垂直的,柱子从下往上。有时我们需要水平的柱状图,柱子从左往右:

```python
from pyecharts.charts import Bar
from pyecharts import options as opts

bar = Bar()

# 添加数据(反转x和y轴的添加顺序)
bar.add_xaxis(["篮球", "足球", "羽毛球", "乒乓球", "跑步", "游泳"])
bar.add_yaxis("人数", [15, 12, 8, 10, 6, 9])

# 设置全局选项
bar.set_global_opts(
    title_opts={"text": "班级运动喜好调查"},
    yaxis_opts=opts.AxisOpts(name="人数"),
    xaxis_opts=opts.AxisOpts(name="运动项目")
)

# 反转x轴和y轴
bar.reversal_axis()

# 生成图表
bar.render("horizontal_bar.html")
```

**使用场景**: 水平柱状图适合类别名称很长的情况(如"数学竞赛成绩"、"英语演讲比赛"等),避免文字重叠。

#### 2. 堆叠柱状图

堆叠柱状图可以让多组数据叠加显示:

```python
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# 使用主题
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(["第一季度", "第二季度", "第三季度", "第四季度"])
bar.add_yaxis("电子产品", [10, 20, 30, 40], stack="stack1")
bar.add_yaxis("服装", [15, 25, 20, 35], stack="stack1")
bar.add_yaxis("食品", [20, 15, 25, 30], stack="stack1")

bar.set_global_opts(
    title_opts={"text": "季度销售额"},
    yaxis_opts=opts.AxisOpts(name="销售额(万元)"),
    xaxis_opts=opts.AxisOpts(name="季度"),
    toolbox_opts=opts.ToolboxOpts(is_show=True)  # 显示工具栏
)

bar.render("stacked_bar.html")
```

**使用场景**: 堆叠柱状图适合显示部分与整体的关系,比如每天不同类别商品的销售总额。

> #### 给家长的小贴士
> - **主题样式**: pyecharts提供了多个主题(LIGHT, DARK, ROMA等),可以尝试不同风格
> - **工具栏**: toolbox_opts会显示下载图片、数据视图等功能,很实用
> - **堆叠概念**: 用积木叠高高来类比堆叠柱状图,孩子更容易理解
> - **代码复用**: 鼓励孩子把常用配置保存起来,下次直接使用

### 15.2.5 柱状图的常见问题

**问题1: 中文显示乱码**

虽然pyecharts默认支持中文,但如果你的Python文件编码不是UTF-8,可能会出现乱码。

**解决方法**:
在Python文件的第一行添加:
```python
# -*- coding: utf-8 -*-
```

**问题2: 柱子太多显示不下**

当x轴的类别太多时,柱子会挤在一起。

**解决方法**:
```python
bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(rotate=45)  # 旋转标签45度
    )
)
```

**问题3: 数值差异太大**

如果一组数据是[5, 8, 10],另一组是[1000, 2000, 3000],数值小的柱子几乎看不见。

**解决方法**:
使用**双y轴**(在高级应用中会学习)或调整数据比例。

> #### 实践练习3:比较自己和偶像的数据
>
> **任务**: 制作一个柱状图,对比你和偶像的数据(可以是游戏、运动、学习等):
> - 要求:至少3个对比项目(如:身高、体重、年龄,或游戏等级、胜率、场次)
> - 使用水平柱状图
> - 添加标题和数据标签
>
> **示例数据**:
> ```python
> me = [165, 50, 12]  # 身高cm, 体重kg, 年龄
> idol = [178, 65, 25]
> items = ["身高(cm)", "体重(kg)", "年龄"]
> ```
>
> **答案**:
> <details>
> <summary>点击查看完整代码</summary>
>
> ```python
> from pyecharts.charts import Bar
> from pyecharts import options as opts
>
> # 你的数据
> me = [165, 50, 12]
> idol = [178, 65, 25]
> items = ["身高(cm)", "体重(kg)", "年龄"]
>
> bar = Bar()
>
> bar.add_xaxis(items)
> bar.add_yaxis("我", me, label_opts=opts.LabelOpts(is_show=True))
> bar.add_yaxis("偶像", idol, label_opts=opts.LabelOpts(is_show=True))
>
> bar.set_global_opts(
>     title_opts={"text": "我和偶像的对比"}
> )
>
> bar.reversal_axis()
> bar.render("me_vs_idol.html")
> ```
> </details>

---

## 15.3 折线图 - 追踪变化趋势

### 15.3.1 折线图的应用场景

**折线图(Line Chart)**用线段连接各个数据点,显示数据随时间或其他因素的变化趋势。

**折线图适合用来**:
- **显示趋势**: 比如一年的气温变化
- **对比变化**: 比较两个学生的成绩进步情况
- **预测未来**: 根据历史数据预测趋势

**生活中的折线图例子**:
- 天气预报的气温曲线
- 新冠疫情的数据曲线
- 股票价格的K线图

### 15.3.2 创建一个简单的折线图

让我们制作一个显示一周气温变化的折线图:

```python
from pyecharts.charts import Line

# 创建折线图
line = Line()

# 添加x轴数据(星期)
line.add_xaxis(["周一", "周二", "周三", "周四", "周五", "周六", "周日"])

# 添加y轴数据(最高气温)
line.add_yaxis("最高气温(°C)", [22, 24, 26, 25, 23, 28, 30])

# 设置标题
line.set_global_opts(title_opts={"text": "一周气温变化"})

# 生成图表
line.render("temperature_line.html")
```

**图表解读**:
- x轴表示星期
- y轴表示温度
- 折线显示温度的变化趋势
- 可以看出哪天最热,哪天最凉快

### 15.3.3 添加多个数据系列

折线图特别适合对比多个数据系列的变化趋势:

```python
from pyecharts.charts import Line

line = Line()

# 添加x轴
line.add_xaxis(["周一", "周二", "周三", "周四", "周五", "周六", "周日"])

# 添加多组数据
line.add_yaxis("最高气温(°C)", [22, 24, 26, 25, 23, 28, 30])
line.add_yaxis("最低气温(°C)", [15, 16, 18, 17, 14, 19, 20])

# 设置标题
line.set_global_opts(title_opts={"text": "一周气温变化"})

# 生成图表
line.render("temperature_double_line.html")
```

**图表解读**:
- 两条折线分别代表最高气温和最低气温
- 可以看出每天的温差(两条线之间的距离)
- 可以看出气温的总体变化趋势

> #### 给家长的小贴士
> - **趋势解读**: 教孩子如何从折线图中读取信息(上升、下降、波动)
> - **数据对比**: 多条折线对比时,引导孩子找出规律(如:A一直比B高,A和B呈相反变化)
> - **实际应用**: 鼓励孩子记录自己的数据(如每天的学习时间),用折线图分析
> - **数据收集**: 这个过程还能培养孩子的数据收集习惯

> #### 实践练习4:我的成绩进步曲线
>
> **任务**: 制作一个折线图,显示你最近5次考试的成绩变化:
> - x轴: 第1次、第2次、第3次、第4次、第5次
> - y轴: 语文和数学的成绩
> - 添加数据标记点
>
> **示例数据**:
> ```python
> chinese = [75, 78, 82, 85, 88]
> math = [80, 79, 83, 87, 90]
> exams = ["第1次", "第2次", "第3次", "第4次", "第5次"]
> ```
>
> **答案**:
> <details>
> <summary>点击查看完整代码</summary>
>
> ```python
> from pyecharts.charts import Line
> from pyecharts import options as opts
>
> # 成绩数据
> chinese = [75, 78, 82, 85, 88]
> math = [80, 79, 83, 87, 90]
> exams = ["第1次", "第2次", "第3次", "第4次", "第5次"]
>
> line = Line()
>
> line.add_xaxis(exams)
> line.add_yaxis(
>     "语文",
>     chinese,
>     markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
>     markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")])
> )
> line.add_yaxis("数学", math)
>
> line.set_global_opts(
>     title_opts={"text": "我的成绩进步曲线"},
>     yaxis_opts=opts.AxisOpts(name="分数"),
>     xaxis_opts=opts.AxisOpts(name="考试次数")
> )
>
> line.render("my_scores.html")
> ```
> 运行后,你会看到两条折线,语文的最高分会自动标记,平均分也会显示!
> </details>

### 15.3.4 平滑曲线和面积图

#### 1. 平滑曲线

默认的折线图是直线连接各个点。设置`is_smooth=True`可以让线条变得平滑:

```python
from pyecharts.charts import Line

line = Line()

line.add_xaxis(["1月", "2月", "3月", "4月", "5月", "6月"])
line.add_yaxis("销售额(万元)", [10, 15, 13, 18, 20, 25], is_smooth=True)

line.set_global_opts(title_opts={"text": "上半年销售额"})

line.render("smooth_line.html")
```

**效果**: 折线变成了平滑的曲线,看起来更美观,适合表示连续变化的数据(如气温、速度等)。

#### 2. 面积图

面积图是在折线图下方填充颜色,强调数据的"量":

```python
from pyecharts.charts import Line
from pyecharts import options as opts

line = Line()

line.add_xaxis(["周一", "周二", "周三", "周四", "周五", "周六", "周日"])
line.add_yaxis(
    "学习时间(小时)",
    [2, 2.5, 3, 2, 3.5, 4, 3],
    areastyle_opts=opts.AreaStyleOpts(opacity=0.5)  # 填充区域,透明度0.5
)

line.set_global_opts(title_opts={"text": "一周学习时间统计"})

line.render("area_line.html")
```

**使用场景**: 面积图适合强调累积量或总量,如每天的学习时间、每月的零花钱支出。

> #### 给家长的小贴士
> - **平滑 vs 直线**: 平滑曲线看起来更美观,但不适合强调精确的数据点
> - **面积图**: 适合用"积木堆叠"或"装水"的类比解释
> - **透明度**: opacity范围是0到1,0表示完全透明,1表示不透明
> - **交互功能**: 鼠标悬停在图表上时,会显示详细的数据提示框

### 15.3.5 折线图的标记功能

pyecharts可以在折线图上自动标记特殊点:

```python
from pyecharts.charts import Line
from pyecharts import options as opts

line = Line()

line.add_xaxis(["1月", "2月", "3月", "4月", "5月", "6月"])
line.add_yaxis(
    "销售额(万元)",
    [10, 15, 13, 18, 20, 25],
    # 标记点:最大值、最小值
    markpoint_opts=opts.MarkPointOpts(
        data=[
            opts.MarkPointItem(type_="max", name="最大值"),
            opts.MarkPointItem(type_="min", name="最小值")
        ]
    ),
    # 标记线:平均值
    markline_opts=opts.MarkLineOpts(
        data=[
            opts.MarkLineItem(type_="average", name="平均值")
        ]
    )
)

line.set_global_opts(title_opts={"text": "上半年销售额"})

line.render("marked_line.html")
```

**标记说明**:
- **标记点**: 用圆点标记特殊位置(最大值、最小值、自定义点)
- **标记线**: 用直线标记特殊位置(平均值、自定义线)

> #### 实践练习5:游戏等级提升记录
>
> **任务**: 假设你在一周内玩游戏,每天记录等级提升:
> - x轴: 周一到周日
> - y轴: 等级(假设起始等级1,每天提升不同)
> - 要求:标记最大提升的那一天,显示平均等级
>
> **示例数据**:
> ```python
> levels = [1, 3, 5, 8, 10, 15, 18]
> gains = [0, 2, 2, 3, 2, 5, 3]  # 每天提升的等级
> ```
>
> **答案**:
> <details>
> <summary>点击查看完整代码</summary>
>
> ```python
> from pyecharts.charts import Line
> from pyecharts import options as opts
>
> levels = [1, 3, 5, 8, 10, 15, 18]
> days = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
>
> line = Line()
>
> line.add_xaxis(days)
> line.add_yaxis(
>     "等级",
>     levels,
>     markpoint_opts=opts.MarkPointOpts(
>         data=[
>             opts.MarkPointItem(type_="max", name="最高等级"),
>             opts.MarkPointItem(type_="min", name="最低等级")
> ]
>     ),
>     markline_opts=opts.MarkLineOpts(
>         data=[
>             opts.MarkLineItem(type_="average", name="平均等级")
>         ]
>     )
> )
>
> line.set_global_opts(
>     title_opts={"text": "游戏等级提升记录"},
>     yaxis_opts=opts.AxisOpts(name="等级"),
>     xaxis_opts=opts.AxisOpts(name="日期")
> )
>
> line.render("game_levels.html")
> ```
> </details>

---

## 15.4 饼图 - 显示比例关系

### 15.4.1 饼图的应用场景

**饼图(Pie Chart)**用圆形的扇形大小表示各部分占整体的比例。

**饼图适合用来**:
- **显示占比**: 班级男女生比例
- **分配关系**: 零花钱的用途分配
- **组成结构**: 家庭支出中各项费用的占比

**生活中的饼图例子**:
- 预算分配图
- 选举结果占比
- 手机存储空间使用情况

**重要**: 饼图的数据加起来应该是100%(或1),表示一个整体。

### 15.4.2 创建一个简单的饼图

让我们制作一个显示班级运动爱好的饼图:

```python
from pyecharts.charts import Pie

# 数据
sports = ["篮球", "足球", "羽毛球", "乒乓球", "跑步", "游泳"]
counts = [15, 12, 8, 10, 6, 9]

# 创建饼图
pie = Pie()

# 添加数据
pie.add("", list(zip(sports, counts)))

# 设置标题
pie.set_global_opts(title_opts={"text": "班级运动喜好分布"})

# 生成图表
pie.render("sports_pie.html")
```

**代码解析**:
- `list(zip(sports, counts))`将两个列表合并成:`[("篮球", 15), ("足球", 12), ...]`
- 饼图的`add()`方法的第一个参数是系列名称(可以为空字符串)

### 15.4.3 饼图的样式设置

#### 1. 显示百分比和标签

默认情况下,饼图会显示类别名称。我们可以同时显示百分比:

```python
from pyecharts.charts import Pie
from pyecharts import options as opts

sports = ["篮球", "足球", "羽毛球", "乒乓球", "跑步", "游泳"]
counts = [15, 12, 8, 10, 6, 9]

pie = Pie()

pie.add(
    "",
    list(zip(sports, counts)),
    label_opts=opts.LabelOpts(formatter="{b}: {d}%")  # {b}=名称, {d}=百分比
)

pie.set_global_opts(title_opts={"text": "班级运动喜好分布"})

pie.render("sports_pie_percent.html")
```

**formatter参数说明**:
- `{a}`: 系列名称
- `{b}`: 数据项名称(如"篮球")
- `{c}`: 数值(如15)
- `{d}`: 百分比(如18.07%)

#### 2. 环形饼图

环形饼图比普通饼图更美观,中间是空心的:

```python
from pyecharts.charts import Pie
from pyecharts import options as opts

sports = ["篮球", "足球", "羽毛球", "乒乓球", "跑步", "游泳"]
counts = [15, 12, 8, 10, 6, 9]

pie = Pie()

pie.add(
    "",
    list(zip(sports, counts)),
    radius=["30%", "70%"]  # 内圆半径30%,外圆半径70%
)

pie.set_global_opts(title_opts={"text": "班级运动喜好分布"})

pie.render("donut_pie.html")
```

**radius参数**:
- 第一个值: 内圆半径
- 第二个值: 外圆半径
- 两个值越接近,环形越细

> #### 给家长的小贴士
> - **百分比概念**: 饼图是帮助孩子理解百分比的绝佳工具
> - **数据归一化**: 如果数据加起来不是100%,pyecharts会自动计算百分比
> - **颜色识别**: 教孩子如何从饼图的颜色和面积大小直观地理解比例
> - **环形 vs 实心**: 环形饼图可以在中间显示总数或标题,更美观

> #### 实践练习6:我的零花钱花哪里了
>
> **任务**: 制作一个饼图,显示你一个月零花钱的使用情况:
> - 类别: 零食、文具、玩具、游戏、其他
> - 数据: 自己设定一个合理的分配(如: 30%, 20%, 15%, 25%, 10%)
> - 要求:使用环形饼图,显示百分比
>
> **示例数据**:
> ```python
> items = ["零食", "文具", "玩具", "游戏", "其他"]
> money = [60, 40, 30, 50, 20]  # 单位:元
> ```
>
> **答案**:
> <details>
> <summary>点击查看完整代码</summary>
>
> ```python
> from pyecharts.charts import Pie
> from pyecharts import options as opts
>
> items = ["零食", "文具", "玩具", "游戏", "其他"]
> money = [60, 40, 30, 50, 20]
>
> pie = Pie()
>
> pie.add(
>     "",
>     list(zip(items, money)),
>     radius=["35%", "65%"],  # 环形
>     label_opts=opts.LabelOpts(formatter="{b}: {c}元 ({d}%)")
> )
>
> pie.set_global_opts(
>     title_opts={"text": "我的零花钱使用情况"},
>     legend_opts=opts.LegendOpts(orient="vertical", pos_left="left")
> )
>
> pie.render("allowance_spending.html")
> ```
> 运行后,你会看到一个漂亮的环形饼图,每个部分显示金额和百分比!
> </details>

### 15.4.4 饼图的Rose图

Rose图(玫瑰图)是饼图的变体,扇形的半径不同:

```python
from pyecharts.charts import Pie
from pyecharts import options as opts

sports = ["篮球", "足球", "羽毛球", "乒乓球", "跑步", "游泳"]
counts = [15, 12, 8, 10, 6, 9]

pie = Pie()

pie.add(
    "",
    list(zip(sports, counts)),
    radius="60%",  # 半径
    rosetype="radius"  # 设置为玫瑰图
)

pie.set_global_opts(title_opts={"text": "班级运动喜好分布(Rose图)"})

pie.render("rose_pie.html")
```

**Rose图特点**:
- 每个扇形的半径不同,数据越大,扇形越大
- 适合数据差异较大的情况
- 视觉效果更丰富

> #### 给家长的小贴士
> - **Rose图 vs 饼图**: Rose图强调数值差异,饼图强调比例关系
> - **选择建议**: 数据差异大时用Rose图,数据相近时用普通饼图
> - **交互功能**: 点击某个扇形,该扇形会突出显示

### 15.4.5 饼图的嵌套

饼图可以嵌套,显示多层数据:

```python
from pyecharts.charts import Pie
from pyecharts import options as opts

# 内圈数据
inner_data = [("电子产品", 60), ("服装", 30), ("食品", 50)]
# 外圈数据(细分)
outer_data = [
    ("手机", 30), ("电脑", 20), ("耳机", 10),
    ("男装", 15), ("女装", 15),
    ("零食", 25), ("饮料", 15), ("水果", 10)
]

pie = Pie()

# 添加内圈
pie.add(
    "",
    inner_data,
    radius=["0%", "35%"],  # 从中心到35%的区域
    label_opts=opts.LabelOpts(formatter="{b}: {d}%")
)

# 添加外圈
pie.add(
    "",
    outer_data,
    radius=["45%", "70%"],  # 从45%到70%的区域
    label_opts=opts.LabelOpts(formatter="{b}: {d}%")
)

pie.set_global_opts(title_opts={"text": "销售额分布(嵌套饼图)"})

pie.render("nested_pie.html")
```

**使用场景**: 嵌套饼图适合显示"大类-小类"的层级关系,如"运动-球类、跑步、游泳"。

> #### 实践练习7:我的时间分配
>
> **任务**: 制作一个嵌套饼图,显示你一天的时间分配:
>
> **内圈(大类)**:
> - 睡眠: 9小时
> - 上学: 8小时
> - 作业: 3小时
> - 娱乐: 4小时
>
> **外圈(娱乐细分)**:
> - 看电视: 1.5小时
> - 玩游戏: 1小时
> - 运动: 1小时
> - 其他: 0.5小时
>
> **答案**:
> <details>
> <summary>点击查看完整代码</summary>
>
> ```python
> from pyecharts.charts import Pie
> from pyecharts import options as opts
>
> # 内圈: 大类
> inner_data = [
>     ("睡眠", 9), ("上学", 8), ("作业", 3), ("娱乐", 4)
> ]
>
> # 外圈: 娱乐细分
> outer_data = [
>     ("看电视", 1.5), ("玩游戏", 1), ("运动", 1), ("其他", 0.5),
>     # 补充其他类别的数据(为了图形完整)
>     ("睡眠细分", 9), ("上学细分", 8), ("作业细分", 3)
> ]
>
> pie = Pie()
>
> pie.add(
>     "",
>     inner_data,
>     radius=["0%", "35%"],
>     label_opts=opts.LabelOpts(formatter="{b}: {c}小时")
> )
>
> pie.add(
>     "",
>     outer_data,
>     radius=["45%", "70%"],
>     label_opts=opts.LabelOpts(formatter="{b}: {c}小时")
> )
>
> pie.set_global_opts(title_opts={"text": "我的一天时间分配"})
>
> pie.render("my_day_pie.html")
> ```
> **提示**: 这个例子展示了嵌套饼图的应用,但外圈数据不完全对称,实际情况中可能需要更完整的数据分类。
> </details>

---

## 15.5 综合项目:制作班级成绩分析报告

现在我们已经学会了柱状图、折线图、饼图,让我们做一个**综合项目**:班级成绩分析报告系统。

这个项目会综合运用我们学到的所有知识!

### 15.5.1 项目需求

假设你是班长,老师给你一份班级成绩数据,你需要:
1. 用**柱状图**显示每个学生的总分排名
2. 用**折线图**显示班级平均分的变化趋势
3. 用**饼图**显示各分数段的人数分布
4. 生成一个完整的HTML报告

**原始数据**:

| 姓名 | 语文 | 数学 | 英语 | 物理 | 化学 |
|-----|------|------|------|------|------|
| 小明 | 85 | 92 | 78 | 88 | 90 |
| 小红 | 90 | 88 | 95 | 92 | 94 |
| 小刚 | 78 | 85 | 82 | 80 | 83 |
| 小丽 | 92 | 95 | 88 | 90 | 91 |
| 小华 | 88 | 90 | 91 | 85 | 89 |
| 小强 | 80 | 82 | 85 | 78 | 80 |
| 小芳 | 95 | 90 | 92 | 95 | 93 |

### 15.5.2 项目实现

让我们一步步完成这个项目:

#### 步骤1: 准备数据

```python
# 学生姓名
students = ["小明", "小红", "小刚", "小丽", "小华", "小强", "小芳"]

# 各科成绩
chinese = [85, 90, 78, 92, 88, 80, 95]
math = [92, 88, 85, 95, 90, 82, 90]
english = [78, 95, 82, 88, 91, 85, 92]
physics = [88, 92, 80, 90, 85, 78, 95]
chemistry = [90, 94, 83, 91, 89, 80, 93]

# 计算总分
total_scores = []
for i in range(len(students)):
    total = chinese[i] + math[i] + english[i] + physics[i] + chemistry[i]
    total_scores.append(total)

print("总分:", total_scores)
```

**运行结果**:
```
总分: [433, 459, 408, 456, 443, 405, 465]
```

#### 步骤2: 柱状图 - 总分排名

```python
from pyecharts.charts import Bar
from pyecharts import options as opts

# 创建柱状图
bar = Bar()

# 添加数据
bar.add_xaxis(students)
bar.add_yaxis(
    "总分",
    total_scores,
    label_opts=opts.LabelOpts(is_show=True)  # 显示数值
)

# 设置全局选项
bar.set_global_opts(
    title_opts={"text": "班级总分排名"},
    yaxis_opts=opts.AxisOpts(name="分数"),
    xaxis_opts=opts.AxisOpts(name="学生"),
    toolbox_opts=opts.ToolboxOpts(is_show=True)  # 显示工具栏
)

# 生成图表
bar.render("class_ranking.html")
```

#### 步骤3: 折线图 - 科目平均分

```python
from pyecharts.charts import Line

# 计算各科平均分
chinese_avg = sum(chinese) // len(chinese)
math_avg = sum(math) // len(math)
english_avg = sum(english) // len(english)
physics_avg = sum(physics) // len(physics)
chemistry_avg = sum(chemistry) // len(chemistry)

subjects = ["语文", "数学", "英语", "物理", "化学"]
avg_scores = [chinese_avg, math_avg, english_avg, physics_avg, chemistry_avg]

# 创建折线图
line = Line()

line.add_xaxis(subjects)
line.add_yaxis(
    "平均分",
    avg_scores,
    markpoint_opts=opts.MarkPointOpts(
        data=[
            opts.MarkPointItem(type_="max", name="最高分"),
            opts.MarkPointItem(type_="min", name="最低分")
        ]
    )
)

line.set_global_opts(
    title_opts={"text": "各科目平均分"},
    yaxis_opts=opts.AxisOpts(name="分数"),
    xaxis_opts=opts.AxisOpts(name="科目")
)

line.render("subject_averages.html")
```

#### 步骤4: 饼图 - 分数段分布

```python
from pyecharts.charts import Pie

# 统计分数段
ranges = ["优秀(90分以上)", "良好(80-89)", "及格(60-79)", "不及格(60分以下)"]
counts = [0, 0, 0, 0]

# 统计总分段
for score in total_scores:
    avg = score / 5  # 计算平均分
    if avg >= 90:
        counts[0] += 1
    elif avg >= 80:
        counts[1] += 1
    elif avg >= 60:
        counts[2] += 1
    else:
        counts[3] += 1

print("分数段分布:", counts)

# 创建饼图
pie = Pie()

pie.add(
    "",
    list(zip(ranges, counts)),
    radius=["30%", "60%"],
    label_opts=opts.LabelOpts(formatter="{b}: {c}人 ({d}%)")
)

pie.set_global_opts(title_opts={"text": "班级成绩分布"})

pie.render("score_distribution.html")
```

**运行结果**:
```
分数段分布: [3, 3, 1, 0]  # 优秀3人,良好3人,及格1人,不及格0人
```

#### 步骤5: 组合所有图表

pyecharts提供了一个**Page**类,可以把多个图表组合在一个HTML页面:

```python
from pyecharts.charts import Bar, Line, Pie
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

# 数据准备(省略,参考上面的代码)

# 创建三个图表(代码省略)
bar = Bar()
# ... 添加数据和选项

line = Line()
# ... 添加数据和选项

pie = Pie()
# ... 添加数据和选项

# 组合图表
from pyecharts.charts import Page

page = Page(layout=Page.SimplePageLayout)

page.add(
    bar,
    line,
    pie
)

page.render("class_report.html")
```

**运行结果**: 打开`class_report.html`,你会看到三个图表从上到下排列在一个页面中,形成一个完整的成绩分析报告!

> #### 给家长的小贴士
> - **项目式学习**: 这个综合项目能培养孩子的整体思维和问题解决能力
> - **数据收集**: 鼓励孩子用真实数据(如自己班级的成绩)替换示例数据
> - **分析能力**: 让孩子根据图表分析班级情况(如:哪科最难,谁进步最大)
> - **逐步完成**: 强调分步骤完成,不要试图一次写完所有代码
> - **调试技巧**: 如果某个图表有问题,单独运行它的代码,找出错误

> #### 综合练习8:完整的数据分析报告
>
> **任务**: 选择一个你感兴趣的主题,制作一个完整的数据分析报告:
>
> **主题建议**:
> 1. **运动数据分析**: 班级同学最喜欢的运动类型
> 2. **游戏数据分析**: 你和朋友的游戏等级、胜率、场次对比
> 3. **零花钱分析**: 一个月的零花钱来源和用途
> 4. **阅读分析**: 这学期读了多少本书,各类书的比例
> 5. **自定义主题**: 其他你感兴趣的数据
>
> **要求**:
> 1. 至少包含3种图表(柱状图、折线图、饼图)
> 2. 每个图表都要有标题和坐标轴说明
> 3. 用Page组合所有图表
> 4. 根据图表写出3条分析结论
>
> **示例代码框架**:
> <details>
> <summary>点击查看代码框架</summary>
>
> ```python
> from pyecharts.charts import Bar, Line, Pie
> from pyecharts.charts import Page
> from pyecharts import options as opts
>
> # 步骤1: 准备数据
> # TODO: 填写你的数据
>
> # 步骤2: 创建柱状图
> bar = Bar()
> # TODO: 添加数据和选项
>
> # 步骤3: 创建折线图
> line = Line()
> # TODO: 添加数据和选项
>
> # 步骤4: 创建饼图
> pie = Pie()
> # TODO: 添加数据和选项
>
> # 步骤5: 组合所有图表
> page = Page()
> page.add(bar, line, pie)
> page.render("my_report.html")
>
> print("报告已生成!")
> ```
> </details>

---

## 15.6 进阶技巧:让图表更美观

### 15.6.1 使用主题

pyecharts提供了多种预设主题,可以快速改变图表的配色:

```python
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# 使用DARK主题
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))

bar.add_xaxis(["苹果", "香蕉", "橙子", "草莓", "葡萄"])
bar.add_yaxis("价格", [8, 3, 6, 15, 12])

bar.set_global_opts(title_opts={"text": "水果价格表"})

bar.render("themed_chart.html")
```

**可用主题**:
- `ThemeType.LIGHT`: 浅色主题(默认)
- `ThemeType.DARK`: 深色主题
- `ThemeType.ROMA`: 罗马主题
- `ThemeType.SHINE`: 闪亮主题
- `ThemeType.VINTAGE`: 复古主题

### 15.6.2 自定义颜色

如果你想自定义图表的颜色,可以使用颜色列表:

```python
from pyecharts.charts import Pie
from pyecharts import options as opts

items = ["篮球", "足球", "羽毛球", "乒乓球", "跑步", "游泳"]
counts = [15, 12, 8, 10, 6, 9]

pie = Pie()

pie.add(
    "",
    list(zip(items, counts)),
    # 自定义颜色
    color=["#FF6B6B", "#4ECDC4", "#45B7D1", "#FFA07A", "#98D8C8", "#F7DC6F"]
)

pie.set_global_opts(title_opts={"text": "班级运动喜好"})

pie.render("custom_colors.html")
```

**颜色代码说明**:
- 使用十六进制颜色码(如`#FF6B6B`)
- 可以在线搜索"hex color picker"选择颜色
- 颜色列表长度应该与数据项数量一致

### 15.6.3 添加提示框和工具栏

```python
from pyecharts.charts import Bar
from pyecharts import options as opts

bar = Bar()

bar.add_xaxis(["第一季度", "第二季度", "第三季度", "第四季度"])
bar.add_yaxis("销售额", [120, 200, 150, 180])

bar.set_global_opts(
    # 提示框配置
    tooltip_opts=opts.TooltipOpts(
        trigger="axis",  # 坐标轴触发
        axis_pointer_type="shadow"  # 阴影指示器
    ),
    # 工具栏配置
    toolbox_opts=opts.ToolboxOpts(
        is_show=True,
        feature={
            "saveAsImage": {},  # 保存为图片
            "dataView": {},     # 数据视图
            "restore": {}        # 还原
        }
    ),
    # 区域缩放
    datazoom_opts=opts.DataZoomOpts(is_show=True)
)

bar.render("advanced_features.html")
```

**功能说明**:
- **提示框**: 鼠标悬停时显示详细信息
- **工具栏**: 右上角显示保存、数据视图等工具
- **区域缩放**: 可以缩放查看部分数据

> #### 给家长的小贴士
> - **颜色搭配**: 教孩子基本的配色原则(对比色、同类色)
> - **主题选择**: 不同主题适合不同场合(如DARK适合夜间查看)
> - **功能叠加**: 不要一次添加太多功能,会影响图表的可读性
> - **审美培养**: 鼓励孩子尝试不同的配色,培养审美能力

---

## 15.7 常见错误和调试

### 15.7.1 数据类型错误

**错误代码**:
```python
from pyecharts.charts import Bar

bar = Bar()
bar.add_xaxis("苹果")  # 错误:应该是列表
bar.add_yaxis("价格", 8)  # 错误:应该是列表
```

**错误信息**:
```
TypeError: Input x_axis data must be list
```

**正确代码**:
```python
bar.add_xaxis(["苹果"])  # 使用列表
bar.add_yaxis("价格", [8])  # 使用列表
```

> #### 给家长的小贴士
> - **列表 vs 单个值**: pyecharts需要列表,即使只有一个数据也要用`[8]`
> - **仔细阅读错误信息**: 错误信息会明确告诉你是哪个参数有问题

### 15.7.2 数据长度不一致

**错误代码**:
```python
bar.add_xaxis(["苹果", "香蕉", "橙子"])
bar.add_yaxis("价格", [8, 3])  # 只有2个数据,少了1个
```

**错误信息**:
```
AssertionError: x_axis data and y_axis data must be same length
```

**解决方法**: 确保x轴和y轴的数据数量一致:

```python
bar.add_xaxis(["苹果", "香蕉", "橙子"])
bar.add_yaxis("价格", [8, 3, 6])  # 3个数据
```

### 15.7.3 文件路径错误

**错误代码**:
```python
bar.render("C:\Users\用户名\桌面\chart.html")
```

**错误信息**:
```
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes
```

**原因**: Python中`\`是转义字符,`\U`会被认为是Unicode转义。

**解决方法1**: 使用原始字符串
```python
bar.render(r"C:\Users\用户名\桌面\chart.html")  # 注意r前缀
```

**解决方法2**: 使用正斜杠
```python
bar.render("C:/Users/用户名/桌面/chart.html")  # 使用/
```

**解决方法3**: 只写文件名(推荐)
```python
bar.render("chart.html")  # 保存到当前目录
```

> #### 给家长的小贴士
> - **路径问题**: 小学生可能不理解文件路径,建议让他们只写文件名
> - **文件查找**: 生成的HTML文件在当前工作目录,可以让孩子用文件管理器搜索
> - **桌面快捷方式**: 在桌面上创建一个"我的图表"文件夹,方便查找

### 15.7.4 HTML文件打不开或空白

**问题1: HTML文件打开后是空白页**

**原因**: 代码运行时出现错误,但没有生成完整的HTML文件。

**解决方法**: 在Python中运行代码时,查看是否有错误提示。常见的错误:
- 拼写错误:`add_xasis`应该是`add_xaxis`
- 缺少括号或引号
- 变量名未定义

**问题2: 浏览器打不开HTML文件**

**原因**: 浏览器太老,不支持某些特性。

**解决方法**: 更新浏览器或使用Chrome、Edge、Firefox等现代浏览器。

### 15.7.5 调试技巧

#### 技巧1: 逐步验证

不要一次写完所有代码,而是分步测试:

```python
# 步骤1: 测试数据
print("x轴:", ["苹果", "香蕉"])
print("y轴:", [8, 3])

# 步骤2: 测试图表创建
bar = Bar()
print("图表创建成功")

# 步骤3: 测试添加数据
bar.add_xaxis(["苹果", "香蕉"])
bar.add_yaxis("价格", [8, 3])
print("数据添加成功")

# 步骤4: 测试渲染
bar.render("test.html")
print("渲染完成")
```

#### 技巧2: 简化数据

如果数据很复杂,先用简单数据测试:

```python
# 复杂数据可能有1000条
# x_data = [...]  # 1000条
# y_data = [...]  # 1000条

# 先用3条数据测试
x_data = ["A", "B", "C"]
y_data = [1, 2, 3]

bar = Bar()
bar.add_xaxis(x_data)
bar.add_yaxis("测试", y_data)
bar.render("simple_test.html")
```

#### 技巧3: 查看HTML源代码

如果图表显示不正常,用文本编辑器打开HTML文件,搜索`"code"`:

```html
<script>
  var chart = echarts.init(...);
  var option = {
    "title": {...},
    "tooltip": {...},
    ...
  };
  chart.setOption(option);
</script>
```

查看是否有`"error"`或`"undefined"`等异常信息。

> #### 给家长的小贴士
> - **调试思维**: 教孩子"分而治之"的调试方法,把大问题拆成小问题
> - **错误是朋友**: 强调错误信息是帮助我们解决问题的线索
> - **保存中间版本**: 鼓励孩子定期保存代码的备份,出错时可以回退

---

## 15.8 本章小结

### 15.8.1 核心知识点回顾

#### 1. 数据可视化的重要性
- 把抽象的数字变成直观的图形
- 让数据更容易理解和分析
- 帮助发现数据背后的规律

#### 2. pyecharts库的使用流程
```
安装: pip install pyecharts
  ↓
导入: from pyecharts.charts import Bar
  ↓
创建: bar = Bar()
  ↓
数据: bar.add_xaxis() / bar.add_yaxis()
  ↓
选项: bar.set_global_opts()
  ↓
渲染: bar.render("file.html")
```

#### 3. 三种常见图表

| 图表类型 | 用途 | 适合场景 |
|---------|------|----------|
| **柱状图** | 比较不同类别 | 排名、对比、统计 |
| **折线图** | 显示变化趋势 | 成绩进步、气温变化、股票走势 |
| **饼图** | 显示比例关系 | 费用分配、偏好分布、成分构成 |

#### 4. 图表的配置选项
- **标题**: title_opts
- **坐标轴**: xaxis_opts / yaxis_opts
- **标签**: label_opts
- **图例**: legend_opts
- **工具栏**: toolbox_opts
- **提示框**: tooltip_opts

#### 5. 高级功能
- **多系列**: 在一个图表上显示多组数据
- **堆叠**: 堆叠柱状图显示部分与整体
- **嵌套**: 嵌套饼图显示层级关系
- **组合**: 用Page组合多个图表

### 15.8.2 能力检查表

请孩子自我检查以下技能是否掌握:

- [ ] 能独立安装pyecharts库
- [ ] 能创建并保存一个简单的柱状图
- [ ] 能创建并保存一个简单的折线图
- [ ] 能创建并保存一个简单的饼图
- [ ] 能为图表添加标题和坐标轴说明
- [ ] 能在一个图表上显示多组数据
- [ ] 能使用Page组合多个图表
- [ ] 能读懂简单的错误信息并调试
- [ ] 能独立完成一个数据分析小项目

### 15.8.3 常见问题快速参考

| 问题 | 解决方法 |
|------|----------|
| 安装失败 | 使用国内镜像源:`pip install pyecharts -i https://pypi.tuna.tsinghua.edu.cn/simple` |
| 中文乱码 | 在文件第一行添加`# -*- coding: utf-8 -*-` |
| 数据长度不一致 | 检查x轴和y轴的数据数量是否相同 |
| HTML文件找不到 | 只写文件名(如`chart.html`),保存到当前目录 |
| 图表空白 | 检查浏览器,使用Chrome或Edge等现代浏览器 |

---

## 15.9 挑战练习

### 挑战1: 天气数据分析

**任务**: 从网上查找你所在城市最近一周的天气数据(最高气温、最低气温、天气状况),制作:
1. 折线图:显示气温变化
2. 饼图:显示不同天气状况的比例(如:晴天3天,阴天2天,雨天2天)

**要求**:
- 使用真实数据
- 图表有标题和说明
- 添加数据标记点(最高温、最低温)

### 挑战2: 我的学习时间统计

**任务**: 记录自己一周每天的学习时间,制作:
1. 柱状图:显示每天的学习时长
2. 饼图:显示学习时间的分配(如:周一2小时,周二3小时...)

**要求**:
- 数据真实可靠
- 分析哪天学习时间最长/最短
- 找出学习规律并给出建议

### 挑战3: 游戏数据分析

**任务**: 如果你有喜欢的游戏,记录游戏数据,制作:
1. 柱状图:你和朋友的等级对比
2. 折线图:最近10次的胜率变化
3. 饼图:使用英雄/武器的频率

**要求**:
- 至少包含3种图表
- 用Page组合所有图表
- 写出分析结论(如:我最擅长哪个英雄)

### 挑战4: 班级调查报告

**任务**: 设计一个班级调查(如:最喜欢的科目、最喜欢的运动、每天的学习时间...),收集数据后制作完整的分析报告。

**要求**:
- 调查至少10名同学
- 使用柱状图、折线图、饼图
- 报告包含:
  - 调查主题
  - 数据来源
  - 图表分析
  - 你的建议

### 挑战5: 创意数据可视化

**任务**: 选择一个你感兴趣的主题(如:我的阅读记录、零花钱追踪、运动数据分析...),制作一个创意数据可视化项目。

**要求**:
- 数据真实且有连续性(至少记录一周)
- 至少3个图表
- 尝试使用主题、自定义颜色等高级功能
- 向同学展示你的报告,并收集反馈

---

## 15.10 下一步预告

恭喜你完成了第15章的学习!你已经掌握了:
- ✅ 数据可视化的基本概念
- ✅ 柱状图、折线图、饼图的制作
- ✅ pyecharts库的使用方法
- ✅ 完整的数据分析报告制作

在**第16章:图形程序**中,你将学习:
- 使用**tkinter**库创建图形界面
- 按钮、文本框、标签等控件
- 制作带界面的交互程序

想象一下,不再是在黑色的命令行窗口输入命令,而是有漂亮的窗口、按钮、输入框...这就是图形界面的魅力!我们下一章见!

---

## 附录:pyecharts速查表

### 常用图表类

```python
from pyecharts.charts import Bar, Line, Pie

# 柱状图
bar = Bar()
bar.add_xaxis(x_data)
bar.add_yaxis(series_name, y_data)
bar.render("bar.html")

# 折线图
line = Line()
line.add_xaxis(x_data)
line.add_yaxis(series_name, y_data)
line.render("line.html")

# 饼图
pie = Pie()
pie.add(series_name, data)
pie.render("pie.html")
```

### 常用配置选项

```python
from pyecharts import options as opts

# 标题
title_opts={"text": "图表标题"}

# 坐标轴
xaxis_opts=opts.AxisOpts(name="x轴名称")
yaxis_opts=opts.AxisOpts(name="y轴名称")

# 标签
label_opts=opts.LabelOpts(is_show=True)  # 显示数据标签

# 提示框
tooltip_opts=opts.TooltipOpts(trigger="axis")

# 工具栏
toolbox_opts=opts.ToolboxOpts(is_show=True)

# 数据缩放
datazoom_opts=opts.DataZoomOpts(is_show=True)
```

### 常用主题

```python
from pyecharts.globals import ThemeType

bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMA))
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.SHINE))
```

### Page组合图表

```python
from pyecharts.charts import Page

page = Page()
page.add(chart1, chart2, chart3)
page.render("combined.html")
```

---

**祝贺你完成第15章的学习!** 🎉

现在,你已经能用Python制作专业的数据报表了!试试用你学到的技能,记录和分析生活中的数据吧!
