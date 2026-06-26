---
title: "P95 【网络爬虫】使用cookie获取登录后的页面数据"
p_no: 95
category: 网络爬虫
duration: 330
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P95 【网络爬虫】使用cookie获取登录后的页面数据

> **课程分类**：网络爬虫
> **时长**：330 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

网络爬虫阶段，从 HTTP 基础到 requests 模块，再到综合案例。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
## Cookie 登录

```python
import requests

# 1. 手动构造 Cookie
headers = {"Cookie": "session=abc123; token=xyz"}
r = requests.get("https://example.com/dashboard", headers=headers)

# 2. requests 自动管理 Cookie
session = requests.Session()
# 第一次访问获取 cookie
session.get("https://example.com/")
# 登录（带 cookie）
session.post("https://example.com/login", data={"user": "alice", "pwd": "secret"})
# 后续请求自动带 cookie
r = session.get("https://example.com/dashboard")
```

## 从浏览器导入 Cookie

```python
# 从 Chrome 复制的 Cookie（字符串格式）
cookie_str = "BIDUPSID=xxx; BAIDUID=yyy; ..."
cookies = {}
for item in cookie_str.split("; "):
    key, value = item.split("=", 1)
    cookies[key] = value

session = requests.Session()
session.cookies.update(cookies)
r = session.get("https://example.com/dashboard")
```

## Cookie 持久化

```python
import requests
import json
import pickle

# 保存
session = requests.Session()
session.get("https://example.com/login")

with open("cookies.pkl", "wb") as f:
    pickle.dump(session.cookies, f)

# 加载
with open("cookies.pkl", "rb") as f:
    cookies = pickle.load(f)

session = requests.Session()
session.cookies.update(cookies)
r = session.get("https://example.com/dashboard")
```

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）