---
title: "学习计划 P087 【网络爬虫】url传参的两种方式"
p_no: 87
category: 网络爬虫
created: 2026-06-24
updated: 2026-06-24
type: study-plan
---

# 学习计划 P087　【网络爬虫】url传参的两种方式

## 一、本节在课程中的位置

| 项目 | 内容 |
|------|------|
| 课程章节 | 第 87 集 / 共 100 集 |
| 分类 | 网络爬虫 |
| 视频时长 | 635 秒（约 11 分钟） |
| 难度 | 基础 |

## 二、为什么先学这一节

URL 参数传递是爬虫最常用的技能之一。理解两种传参方式可以：
- 正确构造搜索请求
- 实现翻页功能
- 处理需要登录的请求
- 避免 URL 编码问题

## 三、本节要回答的核心问题

1. **GET 参数和 POST 参数的区别？**
2. **如何在 URL 中传递参数？**
3. **requests 的 params 参数怎么用？**
4. **POST 请求如何传递数据？**
5. **如何处理文件上传？**

## 四、课本对照

本节内容**书本未涵盖**。HTTP 请求方法属于网络基础知识，需要靠课程视频 + 知识补全学习。

## 五、具体学习步骤

### 第 1 步：GET 参数传递（15 分钟）

```python
import requests
from urllib.parse import urlencode, quote

# GET 参数：参数在 URL 中，用 ? 分隔

# 方法 1：params 参数（推荐）
r = requests.get(
    "https://api.example.com/search",
    params={"q": "python", "page": 1}
)
print(r.url)  # https://api.example.com/search?q=python&page=1

# 方法 2：直接拼接 URL
url = "https://api.example.com/search?q=python&page=1"
r = requests.get(url)

# 方法 3：手动 urlencode
params = {"q": "python 教程", "page": 1}
encoded = urlencode(params)  # q=python+%E6%95%99%E7%A8%8B&page=1
url = f"https://api.example.com/search?{encoded}"
r = requests.get(url)

# 中文和特殊字符需要 URL 编码
print(quote("python 教程"))  # python%20%E6%95%99%E7%A8%8B
```

### 第 2 步：POST 表单提交（10 分钟）

```python
import requests

# POST 参数：参数在请求体中

# 方法 1：data 参数（表单提交）
r = requests.post(
    "https://example.com/login",
    data={
        "username": "alice",
        "password": "secret123",
        "remember": "on"
    }
)
# Content-Type: application/x-www-form-urlencoded

# 方法 2：JSON 提交
r = requests.post(
    "https://api.example.com/users",
    json={
        "name": "Alice",
        "email": "alice@example.com",
        "age": 25
    }
)
# Content-Type: application/json

# 方法 3：自定义 Content-Type
import json
payload = {"key": "value"}
r = requests.post(
    "https://api.example.com/data",
    data=json.dumps(payload),
    headers={"Content-Type": "application/json"}
)
```

### 第 3 步：文件上传（10 分钟）

```python
import requests

# 文件上传使用 files 参数
r = requests.post(
    "https://api.example.com/upload",
    files={"file": open("data.csv", "rb")}
)

# 指定文件名和 Content-Type
r = requests.post(
    "https://api.example.com/upload",
    files={
        "file": (
            "custom_name.csv",
            open("data.csv", "rb"),
            "text/csv"
        )
    }
)

# 上传多个文件
r = requests.post(
    "https://api.example.com/upload",
    files=[
        ("file1", open("file1.txt", "rb")),
        ("file2", open("file2.txt", "rb")),
    ]
)

# 同时传表单数据和文件
r = requests.post(
    "https://api.example.com/upload",
    data={"description": "数据文件"},
    files={"file": open("data.csv", "rb")}
)
```

### 第 4 步：混合使用（10 分钟）

```python
import requests

# GET + POST 可以同时使用

# 示例：搜索 + 翻页 + 筛选
r = requests.get(
    "https://api.example.com/search",
    params={"q": "python", "page": 1, "sort": "date"},
    headers={"User-Agent": "MyBot/1.0"}
)

# 示例：登录 + 获取数据
# 1. 登录获取 Cookie
login_resp = requests.post(
    "https://example.com/login",
    data={"username": "alice", "password": "xxx"}
)
cookies = login_resp.cookies

# 2. 用 Cookie 获取数据
data_resp = requests.get(
    "https://example.com/api/data",
    cookies=cookies
)
```

### 第 5 步：URL 编码详解（10 分钟）

```python
from urllib.parse import urlencode, quote, parse_qs, urlparse

# URL 编码规则
# - 字母数字：保持不变
# - 特殊字符：转为 %XX 格式
# - 空格：转为 + 或 %20

# 编码
print(urlencode({"name": "张三", "age": 25}))
# name=%E5%BC%A0%E4%B8%89&age=25

print(quote("hello world"))
# hello%20world

print(quote("hello world", safe=""))
# hello%20world

# 解码
from urllib.parse import unquote
print(unquote("%E5%BC%A0%E4%B8%89"))
# 张三

# 解析 URL 中的参数
url = "https://example.com/search?q=python&page=1"
parsed = urlparse(url)
print(parse_qs(parsed.query))
# {'q': ['python'], 'page': ['1']}
```

## 六、这一节要掌握的知识点

- [ ] GET 和 POST 的区别
- [ ] requests 的 params 参数用法
- [ ] POST 的 data 和 json 参数
- [ ] 文件上传的 files 参数
- [ ] URL 编码和解码（urlencode/quote）
- [ ] 解析 URL 参数（parse_qs）

## 七、动手练习

### 练习 1：构建搜索请求

```python
# 实现一个百度搜索函数
def baidu_search(keyword, page=1):
    """百度搜索请求"""
    # 参数：wd=关键词, pn=(page-1)*10（百度分页）
    # 返回搜索结果页面的 HTML

    # 实现代码...
    pass

# 测试
results = baidu_search("Python 爬虫教程")
print(results[:500])
```

### 练习 2：翻译 API

```python
# 调用百度翻译 API（需要申请 API Key）
# 或者使用免费的翻译 API
# 实现翻译函数

def translate(text, from_lang="zh", to_lang="en"):
    """翻译函数"""
    # POST 请求
    # 实现代码...
    pass

print(translate("你好世界"))
```

## 八、自测题

- [ ] **Q1**：GET 和 POST 的主要区别是什么？
- [ ] **Q2**：如何用 requests 传递 GET 参数？
- [ ] **Q3**：POST 提交 JSON 数据用什么参数？
- [ ] **Q4**：文件上传使用什么参数？
- [ ] **Q5**：URL 编码中空格如何表示？

## 九、参考资料

- 视频 BV1rpWjevEip P87
- URL 编码规范：https://www.w3.org/International/O-URL-code.html
- HTTP 方法：https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Methods

### 选读

- RESTful API 设计：https://restfulapi.net/
- multipart/form-data：https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Content-Type

## 十、关联 Vault 笔记

- [[学习指南/P087-网络爬虫-【网络爬虫】url传参的两种方式]]
- [[学习计划/P086-网络爬虫-【网络爬虫】url传参及转译-学习计划]]（上一节）
- [[学习计划/P088-网络爬虫-【网络爬虫】网易云单张图片案例-学习计划]]（下一节）
- [[index]]

---

> **预计总时长**：65 分钟（视频 11 + 实操 54）
>
> **完成标志**：能用 params 传递 GET 参数，能用 data/json 提交 POST 请求，能处理文件上传
