# Quick Start Guide

## 1. 安装 Rust 和 mdBook

mdBook 是基于 Rust 的，所以推荐先安装 Rust 环境（虽然也可以直接下载 mdBook 的二进制文件，但安装 Rust 更方便后续管理插件）。

*   **安装 Rust (Windows/Mac/Linux):**
    打开终端（Terminal 或 PowerShell），运行以下命令：
    ```bash
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```
    安装完成后，重启终端，输入 `cargo --version` 确认安装成功。

*   **安装 mdBook:**
    ```bash
    cargo install mdbook
    ```

*   **安装常用插件 (推荐):**
    为了增强功能（如目录生成、链接检查等），建议安装以下插件：
    ```bash
    # 增加 mermaid 图表支持 (如果你书里有流程图)
    cargo install mdbook-mermaid

    # 增加 admonish (警告/提示框) 支持，类似 GitBook 的 hints
    cargo install mdbook-admonish

    # 增加 PDF 生成支持
    cargo install mdbook-pdf

    # 增加 epub 生成支持
    cargo install mdbook-epub   
    ```

## 2. 初始化工程
在你的工作目录下，创建一个新项目：

```bash
mdbook init my-book
```

终端会询问几个问题：
1.  *Do you want a .gitignore to be created?* -> **y**
2.  *What title would you like to give the book?* -> 输入你的书名（例如：**我的技术笔记**）

现在你会得到一个如下的目录结构：
```text
my-book/
├── book/          # 生成的静态网页（构建后出现）
├── src/           # 你的 Markdown 源码放这里
│   ├── chapter_1.md
│   └── SUMMARY.md # 目录文件
└── book.toml      # 配置文件
```

## 3. 配置与美化 (`book.toml`)

`book.toml` 是 mdBook 的核心。我们需要配置元数据、插件和输出格式。

打开 `book.toml`，将其修改为以下内容（这是一个功能齐全的配置模板）：

```toml
[book]
authors = ["你的名字"]
language = "zh"
multilingual = false
src = "src"
title = "我的电子书标题"
description = "这是一本关于...的书"

# --- 输出配置 ---

[output.html]
default-theme = "light" # 默认主题
preferred-dark-theme = "navy" # 默认深色主题
mathjax-support = true # 支持数学公式
# 启用搜索功能
[output.html.search]
enable = true
limit-results = 30
teaser-word-count = 30
use-boolean-and = true
boost-title = 2
boost-hierarchy = 1
boost-paragraph = 1

# 侧边栏配置
[output.html.fold]
enable = true    # 允许折叠章节
level = 0        # 默认折叠级别

# 打印配置 (生成单页 HTML 用于打印)
[output.html.print]
enable = true

# --- 插件配置 (前提是你安装了这些插件) ---

# Mermaid 图表支持
[preprocessor.mermaid]
command = "mdbook-mermaid"
```

## 4. 生成 Web 版本预览

在 mdbook 项目根目录运行：
```bash
mdbook serve --open
```
*   `serve`: 启动本地服务器。
*   `--open`: 自动在浏览器打开。

此时，你可以修改 `src` 下的 Markdown 文件，浏览器会自动刷新，实现**所见即所得**的编辑体验。

## 5. 生成 PDF 文档

mdBook 本身不直接生成 PDF，但官方推荐使用 `mdbook-pdf` 插件，或者通过浏览器打印功能（最简单且效果不错）。

### 方法 A：使用浏览器打印 (最简单，推荐)
我们在 `book.toml` 中配置了 `[output.html.print] enable = true`。
1.  在生成的网页右上角，会有一个打印机图标。
2.  点击它，mdBook 会将整本书渲染成一个长 HTML 页面。
3.  使用浏览器的 "打印 -> 另存为 PDF"。
    *   **技巧：** 在打印设置中，勾选 "背景图形" 以保留代码块背景色。

### 方法 B：使用 Webkit 自动化工具 (更专业)
如果你需要自动化的 PDF 生成（比如 CI/CD 流程），可以使用 `mdbook-pdf`。

1.  **安装 Google Chrome** (用于无头渲染)。
2.  **安装 mdbook-pdf:**
    ```bash
    cargo install mdbook-pdf
    ```
3.  **修改 `book.toml`:**
    ```toml
    [output.pdf]
    ```
4.  **生成:**
    ```bash
    mdbook build
    ```
    生成的 PDF 会出现在 `book/pdf/` 目录下。

## 6. 生成 epub

```
ebook-convert book/index.html book.epub --title "你的书名" --authors "作者名"
```

## 7. 发布到 GitHub Pages

GitHub Pages 是一个免费的静态网站托管服务，非常适合托管 mdBook 生成的文档。以下是将你的 Python 教程发布到 https://magicbowen.github.io/python-for-kids/ 的完整操作指南。

### 7.1 准备工作

确保你已经：
- 拥有一个 GitHub 账号
- 仓库已经创建（本例中为 `python-for-kids`）
- 本地已完成 mdBook 的构建预览

### 7.2 创建 GitHub Actions 工作流（推荐方法）

这是最现代化的方法，使用 GitHub Actions 自动构建和部署。

**步骤 1：创建工作流配置文件**

在项目根目录创建 `.github/workflows/deploy.yml` 文件：

```bash
mkdir -p .github/workflows
```

**步骤 2：编写部署配置**

创建 `.github/workflows/deploy.yml` 文件，内容如下：

```yaml
name: Deploy mdBook to GitHub Pages

on:
  push:
    branches:
      - main  # 或者是 master，根据你的默认分支名
    # 可选：当 src/SUMMARY.md 或 src 目录下的文件变化时触发
    paths:
      - 'src/**'
      - 'book.toml'
      - '.github/workflows/deploy.yml'

# 设置权限
permissions:
  contents: read
  pages: write
  id-token: write

# 允许只有一个并发部署
concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup mdBook
        uses: peaceiris/actions-mdbook@v1
        with:
          mdbook-version: 'latest'
          # 如果使用了插件，可以在这里安装
          # mdbook-version: '0.4.40'

      - name: Install mdBook plugins (可选)
        run: |
          # 如果你使用了 mermaid 插件
          cargo install mdbook-mermaid
          # 如果你使用了其他插件，继续添加
          # cargo install mdbook-admonish

      - name: Build book
        run: mdbook build

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./book

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

**步骤 3：配置 GitHub Pages**

在 GitHub 仓库页面进行设置：

1. 进入仓库的 **Settings**（设置）
2. 点击左侧菜单的 **Pages**
3. 在 **Build and deployment** 部分：
   - **Source** 选择 **GitHub Actions**
4. 保存设置

**步骤 4：推送代码触发部署**

```bash
# 添加所有文件
git add .

# 提交更改
git commit -m "添加 GitHub Actions 部署配置"

# 推送到远程仓库
git push origin main
```

**步骤 5：查看部署状态**

1. 在 GitHub 仓库页面，点击 **Actions** 标签
2. 你会看到部署工作流正在运行
3. 等待几分钟，工作流完成后，你的网站就会自动部署到：https://magicbowen.github.io/python-for-kids/

### 7.3 手动部署方法（备选方案）

如果你不想使用 GitHub Actions，也可以手动部署：

**步骤 1：构建书籍**

```bash
mdbook build
```

这会在 `book/` 目录生成静态网站文件。

**步骤 2：使用 gh-pages 分支**

```bash
# 安装 gh-pages 包（如果还没有）
npm install -g gh-pages

# 部署到 gh-pages 分支
gh-pages -d book
```

**步骤 3：在 GitHub 设置 Pages**

1. 进入仓库 **Settings** -> **Pages**
2. **Source** 选择 **Deploy from a branch**
3. **Branch** 选择 **gh-pages** 和 **/ (root)**
4. 点击 **Save**

### 7.4 验证部署

部署完成后（通常需要几分钟），访问：
```
https://magicbowen.github.io/python-for-kids/
```

你应该能看到完整的 Python 教程网站。

### 7.5 更新网站

当你修改了 `src/` 目录下的内容后：

**如果使用 GitHub Actions（推荐）：**
- 只需要 `git add`、`git commit`、`git push`
- GitHub Actions 会自动重新构建和部署

**如果使用手动方法：**
```bash
# 重新构建
mdbook build

# 重新部署
gh-pages -d book
```

### 7.6 自定义域名（可选）

如果你想使用自己的域名：

1. 在 `book.toml` 中添加：
```toml
[output.html]
# 其他配置...
git-repository-url = "https://github.com/magicbowen/python-for-kids"
```

2. 在项目根目录创建 `CNAME` 文件：
```bash
echo "yourdomain.com" > CNAME
```

3. 在域名提供商处添加 DNS 记录指向 GitHub Pages

### 7.7 常见问题

**Q: 部署后页面显示 404**
A: 检查 GitHub Pages 设置是否正确启用，等待几分钟让 CDN 刷新

**Q: 插件不工作**
A: 确保在 GitHub Actions 中安装了相应的插件（参考工作流配置中的 "Install mdBook plugins" 步骤）

**Q: 中文显示乱码**
A: 在 `book.toml` 中设置 `language = "zh"`，确保 Markdown 文件保存为 UTF-8 编码

**Q: 更新后网站没有变化**
A: 清除浏览器缓存，或等待 5-10 分钟让 GitHub Pages 完成 CDN 更新

### 7.8 提示和最佳实践

- **使用 GitHub Actions**：这是最可靠的方法，每次推送代码都会自动部署
- **本地预览**：部署前先运行 `mdbook serve` 在本地检查效果
- **版本控制**：所有的 Markdown 源文件都在 Git 仓库中，方便回滚和历史追踪
- **定期备份**：虽然 GitHub 很可靠，但重要的教程内容建议定期备份到本地或其他位置