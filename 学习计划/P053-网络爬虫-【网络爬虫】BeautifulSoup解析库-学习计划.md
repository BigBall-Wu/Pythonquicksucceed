---
title: P053-网络爬虫-【网络爬虫】BeautifulSoup解析库-学习计划
created: 2026-06-24
updated: 2026-06-24
type: permanent
tags: [python, 网络爬虫, BeautifulSoup]
summary: 掌握BeautifulSoup解析HTML/XML文档的方法与CSS选择器
---

# P053 - 网络爬虫：BeautifulSoup 解析库

## 本节知识点总览

| 知识点 | 难度 | 重要度 | 课本定位 |
|--------|------|--------|----------|
| BeautifulSoup 初始化 | ⭐⭐ | ⭐⭐⭐ | L3500-L3530 |
| 元素选择器 | ⭐⭐ | ⭐⭐⭐ | L3535-L3570 |
| CSS 选择器 | ⭐⭐ | ⭐⭐ | L3575-L3610 |
| 遍历文档树 | ⭐⭐ | ⭐⭐ | L3615-L3650 |

---

## 一、BeautifulSoup 基础

### 1.1 安装与导入

```bash
pip install beautifulsoup4 lxml
```

```python
from bs4 import BeautifulSoup

html = """
<html>
    <head><title>测试页面</title></head>
    <body>
        <h1 class="title">欢迎来到 Python 世界</h1>
        <div id="content">
            <p class="intro">这是一个测试页面。</p>
            <a href="https://example.com">访问链接</a>
        </div>
    </body>
</html>
"""

# 初始化 BeautifulSoup
soup = BeautifulSoup(html, "lxml")  # 使用 lxml 解析器

# prettify() 格式化输出
print(soup.prettify())
```

### 1.2 解析器对比

| 解析器 | 速度 | 容错性 | 说明 |
|--------|------|--------|------|
| html.parser | 中等 | 中等 | Python 内置，无需安装 |
| lxml | 快 | 高 | 需要 pip install lxml |
| html5lib | 慢 | 最高 | 需要 pip install html5lib |

```python
from bs4 import BeautifulSoup

html = "<html>...</html>"

# 选择解析器
soup1 = BeautifulSoup(html, "html.parser")
soup2 = BeautifulSoup(html, "lxml")
soup3 = BeautifulSoup(html, "html5lib")
```

---

## 二、元素选择器

### 2.1 基本选择方法

```python
html = """
<div>
    <h1 class="title">标题1</h1>
    <h1 class="subtitle">副标题</h1>
    <p id="intro">介绍段落</p>
</div>
"""

soup = BeautifulSoup(html, "lxml")

# 按标签名查找
h1_tags = soup.find_all("h1")
print(f"找到 {len(h1_tags)} 个 h1 标签")

# find() 返回第一个
first_h1 = soup.find("h1")
print(first_h1.text)

# 按 class 查找
subtitle = soup.find("h1", class_="subtitle")
print(subtitle.text)

# 按 id 查找
intro = soup.find("p", id="intro")
print(intro.text)
```

### 2.2 find() vs find_all()

```python
# find() - 返回第一个匹配
result = soup.find("div")
print(result)

# find_all() - 返回所有匹配
results = soup.find_all("a")
for a in results:
    print(a.get("href"))

# 限制数量
results = soup.find_all("a", limit=3)

# 递归选项
results = soup.find_all("a", recursive=False)  # 不在子标签中查找
```

### 2.3 CSS 类选择器

```python
html = """
<div class="container">
    <div class="item active">项目1</div>
    <div class="item">项目2</div>
    <div class="item">项目3</div>
</div>
"""

soup = BeautifulSoup(html, "lxml")

# 选择所有 class="item" 的元素
items = soup.select(".item")
for item in items:
    print(item.text)

# 选择 class="item active" 的元素
active_items = soup.select(".item.active")

# 选择 id="container" 下的所有 div
container_divs = soup.select("#container div")

# 选择直接子元素
direct_children = soup.select(".container > .item")
```

### 2.4 属性选择器

```python
html = """
<a href="https://example1.com">链接1</a>
<a href="https://example2.com" target="_blank">链接2</a>
<a>无链接</a>
"""

soup = BeautifulSoup(html, "lxml")

# 有 href 属性的 a 标签
with_href = soup.select("a[href]")

# href 以 https 开头的
https_links = soup.select('a[href^="https"]')

# href 以 .com 结尾的
com_links = soup.select('a[href$=".com"]')

# href 包含 example 的
example_links = soup.select('a[href*="example"]')
```

---

## 三、获取元素内容

### 3.1 获取文本

```python
html = """
<div>
    <h1>标题 <span class="highlight">高亮</span> 文字</h1>
    <p>普通文本</p>
</div>
"""

soup = BeautifulSoup(html, "lxml")
h1 = soup.find("h1")

# get_text() - 获取所有文本（包括子元素）
print(h1.get_text())           # "标题 高亮 文字"

# get_text(separator) - 指定分隔符
print(h1.get_text(separator="|"))  # "标题|高亮|文字"

# get_text(strip=True) - 去除空白
print(h1.get_text(strip=True))  # "标题高亮文字"

# .text 属性
print(h1.text)                 # "标题 高亮 文字"

# .string 属性（只返回当前标签的文本，不含子元素）
print(h1.string)               # None（因为有子元素）
```

### 3.2 获取属性

```python
html = """
<a href="https://example.com" title="示例链接" class="link external">
    访问网站
</a>
<img src="image.jpg" alt="图片描述" width="100" height="200">
"""

soup = BeautifulSoup(html, "lxml")
a = soup.find("a")
img = soup.find("img")

# get() 方法获取单个属性
href = a.get("href")
print(href)  # "https://example.com"

# 获取不存在的属性返回 None
print(a.get("target"))  # None

# 获取所有属性
attrs = a.attrs
print(attrs)  # {'href': '...', 'title': '...', 'class': ['link', 'external']}

# img 标签
print(img.get("src"))   # "image.jpg"
print(img.get("alt"))   # "图片描述"
```

---

## 四、遍历文档树

### 4.1 上下遍历

```python
html = """
<html>
    <body>
        <div id="parent">
            <p id="child1">子元素1</p>
            <p id="child2">子元素2</p>
            <p id="child3">子元素3</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html, "lxml")
parent = soup.find("div", id="parent")

# 父元素
print(parent.parent.name)  # body

# 所有父元素（直到根节点）
for ancestor in parent.parents:
    print(ancestor.name)

# 子元素
for child in parent.children:
    print(child.name, child.get("id"))

# 所有子孙元素
for descendant in parent.descendants:
    if hasattr(descendant, 'name'):
        print(descendant.name)
```

### 4.2 兄弟遍历

```python
html = """
<div>
    <p id="first">第一个</p>
    <p id="second">第二个</p>
    <p id="third">第三个</p>
</div>
"""

soup = BeautifulSoup(html, "lxml")
second = soup.find("p", id="second")

# 前一个兄弟
print(second.previous_sibling)  # <p id="first">

# 后一个兄弟
print(second.next_sibling)   # <p id="third">

# 所有前兄弟
for sibling in second.previous_siblings:
    if hasattr(sibling, 'name') and sibling.name:
        print(sibling.get("id"))

# 所有后兄弟
for sibling in second.next_siblings:
    if hasattr(sibling, 'name') and sibling.name:
        print(sibling.get("id"))
```

---

## 五、实战案例

### 5.1 提取新闻列表

```python
import requests
from bs4 import BeautifulSoup

def extract_news(url):
    """提取新闻列表"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    
    news_list = []
    
    # 假设新闻在 .news-item 类的 div 中
    for item in soup.select(".news-item"):
        news = {
            "title": item.select_one("h3.title").text.strip(),
            "link": item.select_one("a.title").get("href"),
            "time": item.select_one(".time").text.strip() if item.select_one(".time") else None,
            "summary": item.select_one(".summary").text.strip() if item.select_one(".summary") else None
        }
        news_list.append(news)
    
    return news_list

# 示例使用
# news = extract_news("https://news.example.com")
# for item in news:
#     print(f"{item['time']} - {item['title']}")
```

### 5.2 提取表格数据

```python
import requests
from bs4 import BeautifulSoup

def parse_table(url):
    """解析 HTML 表格"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    
    table = soup.find("table", class_="data-table")
    if not table:
        return []
    
    # 提取表头
    headers = [th.text.strip() for th in table.select("thead th")]
    
    # 提取数据行
    rows = []
    for tr in table.select("tbody tr"):
        cells = [td.text.strip() for td in tr.select("td")]
        row_data = dict(zip(headers, cells))
        rows.append(row_data)
    
    return rows

# 示例
# data = parse_table("https://example.com/table")
# for row in data:
#     print(row)
```

### 5.3 提取分页链接

```python
from bs4 import BeautifulSoup

def extract_pagination(html):
    """提取分页链接"""
    soup = BeautifulSoup(html, "lxml")
    
    pagination = soup.select(".pagination a.page-link")
    
    pages = []
    for link in pagination:
        pages.append({
            "text": link.text.strip(),
            "url": link.get("href"),
            "page_num": link.get("data-page")
        })
    
    return pages

html = """
<nav class="pagination">
    <a href="/page/1" class="page-link" data-page="1">1</a>
    <a href="/page/2" class="page-link" data-page="2">2</a>
    <a href="/page/3" class="page-link" data-page="3">3</a>
</nav>
"""

pages = extract_pagination(html)
for p in pages:
    print(f"第 {p['text']} 页: {p['url']}")
```

---

## 六、注意事项

### 6.1 编码问题

```python
from bs4 import BeautifulSoup

# 自动检测编码
soup = BeautifulSoup(html, "lxml", from_encoding="utf-8")

# 获取文档编码
print(soup.original_encoding)
```

### 6.2 性能优化

```python
# ❌ 不好：多次解析同一文档
soup = BeautifulSoup(html, "lxml")
titles = soup.find_all("h1")
links = soup.find_all("a")

# ✅ 好：一次解析，多次使用
soup = BeautifulSoup(html, "lxml")
# 或者使用 lxml 直接解析
from lxml import html
root = html.fromstring(html)
```

### 6.3 容错处理

```python
# 安全获取元素
def safe_get_text(element, selector, default=""):
    """安全获取文本内容"""
    target = element.select_one(selector) if element else None
    return target.get_text(strip=True) if target else default

def safe_get_attr(element, selector, attr, default=None):
    """安全获取属性值"""
    target = element.select_one(selector) if element else None
    return target.get(attr, default) if target else default

# 使用
soup = BeautifulSoup(html, "lxml")
title = safe_get_text(soup, "h1.title")
link = safe_get_attr(soup, "a.main-link", "href")
```

---

## 七、课本重点标注

**《Python编程：从入门到实践》第3版 核心段落：**

| 章节 | 页码 | 重点内容 |
|------|------|----------|
| 12.1 | ~280 | BeautifulSoup 基础 |
| 12.2 | ~285 | 选择元素 |
| 12.3 | ~290 | 提取数据 |

---

## 八、易错点与避坑指南

1. **解析器选择**：生产环境推荐使用 lxml
2. **空元素处理**：使用 try-except 或条件判断
3. **编码问题**：确保正确处理中文编码
4. **选择器效率**：CSS 选择器比 find_all 更直观
5. **动态内容**：BeautifulSoup 无法处理 JavaScript 渲染的内容

---

## 九、学习成果检验

- [ ] 掌握 BeautifulSoup 的初始化方法
- [ ] 能使用 find/select 方法选择元素
- [ ] 掌握 CSS 选择器的用法
- [ ] 能遍历文档树获取元素
- [ ] 能提取文本和属性值
- [ ] 能处理常见的网页解析场景
- [ ] 能处理编码和异常情况
