---
title: "P87 【网络爬虫】url传参的两种方式"
p_no: 87
category: 网络爬虫
duration: 635
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P87 【网络爬虫】url传参的两种方式

> **课程分类**：网络爬虫
> **时长**：635 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

网络爬虫阶段，从 HTTP 基础到 requests 模块，再到综合案例。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
## URL 参数的两种传递方式

### 1. GET 参数（URL 后面）

```python
import requests

# 方式 A：params 参数（推荐，requests 自动编码）
r = requests.get("https://api.example.com/search", params={"q": "python", "page": 1})

# 方式 B：直接拼到 URL
url = "https://api.example.com/search?q=python&page=1"
r = requests.get(url)

# 方式 C：手动 urlencode
from urllib.parse import urlencode
params = urlencode({"q": "python", "page": 1})
url = f"https://api.example.com/search?{params}"
r = requests.get(url)
```

### 2. POST 参数（请求体里）

```python
import requests

# form 表单
data = {"username": "alice", "password": "secret"}
r = requests.post("https://example.com/login", data=data)

# JSON
payload = {"name": "alice", "age": 25}
r = requests.post("https://api.example.com/users", json=payload)

# 原始字符串（自定义 Content-Type）
import json
r = requests.post(
    "https://api.example.com/data",
    data=json.dumps(payload),
    headers={"Content-Type": "application/json"}
)

# 文件上传
files = {"file": open("data.csv", "rb")}
r = requests.post("https://api.example.com/upload", files=files)

# multipart
files = {
    "file": ("data.csv", open("data.csv", "rb"), "text/csv")
}
r = requests.post("https://api.example.com/upload", files=files)
```

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）