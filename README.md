# 🐍 Python 少儿编程教程

<div align="center">

**一本专门为小学高年级孩子（10-12岁）编写的Python入门教程**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![mdBook](https://img.shields.io/badge/docs-mdBook-orange)](https://rust-lang.github.io/mdBook/)

</div>

---

## 📖 项目简介

这是一本为家长和孩子共同学习Python编程而设计的教程。作为一个有编程经验的家长，我在2020年疫情期间开始教当时10岁的孩子学习Python。这份教程记录了我们的学习历程，从简单的备课大纲逐渐扩展成系统的教学内容。

### 为什么选择Python而不是Scratch？

对于**小学高年级（10-12岁）**的孩子来说，Python是比Scratch更好的选择：

✅ **真实的编程体验** - 直接接触真实的代码和编程工具，了解计算机程序、命令行、开发工具以及基本的计算机体系结构

✅ **更深入的概念理解** - 每一步都是透明的，孩子能真正理解程序是如何运行的

✅ **更好的知识迁移** - 学到的编程思维可以轻松迁移到其他编程语言

✅ **更大的成长空间** - 可以陪伴孩子从小学到高中，甚至大学和工作

> 💡 **实践证明**：小学高年级的孩子完全有能力接受这些概念，并且会借此了解一些计算机体系结构的基本知识！

---

## 🎯 这本书适合谁？

### 👦👧 对于孩子
- **年龄**：10-12岁（小学高年级）
- **数学基础**：会基本的数学运算，了解未知数和方程的概念
- **编程基础**：零起点，没有学过编程
- **学习方式**：可以在家长指导下学习，也可以独立阅读参考

### 👨‍👩‍👧‍👦 对于家长
- 有一定编程经验，想亲自教孩子学编程
- 希望有一份系统的备课材料作为参考
- 愿意花时间陪伴孩子，把编程教学变成亲子互动的过程

---

## 📚 内容结构

整个教程分为 **5个阶段**，共 **18章**，循序渐进地引导孩子进入Python编程的世界：

### 第一阶段：入门基础（第1-5章）
- 安装Python和编程工具
- 学习输入输出、变量（字符串、数字、布尔值）

### 第二阶段：程序控制（第6-9章）
- 顺序执行、条件判断、循环语句
- 用流程图理解程序逻辑

### 第三阶段：数据组织（第10-12章）
- 列表、字典、函数

### 第四阶段：综合应用（第13-16章）
- 库的使用、命令行程序、图表、图形界面

### 第五阶段：知识扩展（第17-18章）
- 程序设计方法、计算机体系结构

---

## 📖 在线阅读

### 🌐 HTML版本（推荐）

点击访问：**[Python少儿编程教程 - 在线版](https://magicbowen.github.io/python-for-kids/)**

使用 [mdBook](https://rust-lang.github.io/mdBook/) 生成的精美网页版，支持：
- ✅ 响应式设计，支持手机、平板、电脑阅读
- ✅ 内置搜索功能
- ✅ 代码高亮和复制功能
- ✅ 侧边栏导航

### 📄 章节目录

| 章节 | 标题 | 内容简介 |
|------|------|----------|
| [第1章](src/01-introduce.md) | 安装环境 | 搭建Python开发环境 |
| [第2章](src/02-input-and-output.md) | 输入与输出 | 学会与计算机对话 |
| [第3章](src/03-str-variable.md) | 字符串变量 | 处理文字信息 |
| [第4章](src/04-number-variable.md) | 数值变量 | 数学计算 |
| [第5章](src/05-bool-variable.md) | 布尔变量 | 真与假的判断 |
| [第6章](src/06-Sequential-statement.md) | 顺序语句 | 程序的执行流程 |
| [第7章](src/07-condition-statement.md) | 条件语句 | 让程序做决定 |
| [第8章](src/08-loop-statement.md) | 循环语句 | 重复执行的技巧 |
| [第9章](src/09-flow-chart.md) | 流程图 | 用图形理解程序 |
| [第10章](src/10-list.md) | 列表 | 管理多个数据 |
| [第11章](src/11-dict.md) | 字典 | 键值对组织信息 |
| [第12章](src/12-function.md) | 函数 | 代码复用 |
| [第13章](src/13-library.md) | 库 | 使用现成的工具 |
| [第14章](src/14-command-line.md) | 命令行程序 | 制作实用工具 |
| [第15章](src/15-chart.md) | 报表程序 | 数据可视化 |
| [第16章](src/16-UI.md) | 图形程序 | 创建可视化界面 |
| [第17章](src/17-extension.md) | 程序设计 | 设计大型程序 |
| [第18章](src/18-computer-architecture.md) | 计算机体系结构 | 理解硬件基础 |

---

## 🛠️ 本地构建

如果你想在自己的电脑上阅读或修改教程，可以使用 mdBook 构建本地版本。

### 前置要求

1. **安装 Rust**（如果尚未安装）
   ```bash
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   ```

2. **安装 mdBook**
   ```bash
   cargo install mdbook
   ```

3. **安装推荐插件**（可选）
   ```bash
   # Mermaid 图表支持
   cargo install mdbook-mermaid

   # 提示框支持
   cargo install mdbook-admonish
   ```

### 构建和预览

```bash
# 克隆仓库
git clone https://github.com/magicbowen/python-for-kids.git
cd python-for-kids

# 启动本地服务器
mdbook serve --open
```

浏览器会自动打开 `http://localhost:3000`，你就可以看到本地版本的教程了。

### 生成 PDF

如果你想导出PDF版本，最简单的方式是：

1. 在网页版本中点击右上角的打印机图标
2. 使用浏览器的"打印 → 另存为PDF"功能

---

## 🎨 特色设计

### 📝 编写原则

考虑到小学阶段孩子的知识结构特点：
- ✅ **已掌握**：基本的数学运算、未知数和方程、简单的逻辑推理
- ⚠️ **未学习**：数学中的函数概念、逻辑运算符号、抽象的数据结构

因此，在内容编排上：
- 每个概念都用生活化的例子来引入
- 从简单到复杂，做好足够的逻辑台阶搭建
- 大量使用类比和比喻
- 提供详细的步骤说明和注释

### 👨‍👩‍👧‍👦 双重视角

这本书既可以作为家长的教学手册，也可以作为孩子的参考书：
- **对孩子**：用生动有趣的语言讲解，配上大量练习
- **对家长**：提供教学建议（Tips标注的板块），指出易错点和教学技巧

### 🎮 趣味性与实用性结合

- 练习题目贴近孩子的生活（计算图形、课表管理、小游戏）
- 从基础的命令行程序，到图形界面，再到数据报表
- 让孩子看到编程的实际用途，保持学习动力

---

## 🤝 贡献指南

欢迎任何形式的贡献！

### 🐛 报告问题

如果你发现了：
- 错别字或表述不清的地方
- 代码错误
- 内容缺失或需要改进

请提交 [Issue](https://github.com/magicbowen/python-for-kids/issues)

### 💡 提出建议

如果你有：
- 更好的讲解方式
- 新的练习题目
- 有趣的项目想法

欢迎提交 Issue 或 Pull Request！

### ✍️ 贡献流程

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的修改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

---

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源协议。

---

## 💬 关于AI时代的学习

有人可能会问：AI这么强大，还需要学编程吗？

**答案是需要的。**

AI虽然很早就在下棋上战胜了人类，但是我们依旧会陪孩子下棋，通过下棋锻炼孩子的策略性思维，并享受下棋时候的亲子乐趣！

因此，我建议如果父母本身会一些编程，可以亲自给孩子教编程，除了培养孩子逻辑思考、问题分解、抽象建模的能力，更是一个和孩子一起体验创造的乐趣的亲子时光！

**在这个AI大行其道的时代，人类的学习重在过程，不在目的！**

学习编程的目的是**了解数字世界运行的原理，培养思维能力和创造能力**，而不是一定要成为程序员。

---

## 📮 联系方式

如果你有任何问题或建议，欢迎通过以下方式联系：

- 提交 [Issue](https://github.com/magicbowen/python-for-kids/issues)
- 发起 [Discussion](https://github.com/magicbowen/python-for-kids/discussions)

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给个 Star！⭐**

Made with ❤️ by [magicbowen](https://github.com/magicbowen)

</div>
