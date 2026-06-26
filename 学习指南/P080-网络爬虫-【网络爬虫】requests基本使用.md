---
title: "P80 【网络爬虫】requests基本使用"
p_no: 80
category: 网络爬虫
duration: 504
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P80 【网络爬虫】requests基本使用

> **课程分类**：网络爬虫
> **时长**：504 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

网络爬虫阶段，从 HTTP 基础到 requests 模块，再到综合案例。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
## 一、requests 模块

```python
import requests

# 1. GET 请求
r = requests.get("https://api.github.com")
print(r.status_code)    # 200
print(r.text)           # 响应文本
print(r.content)        # bytes
print(r.json())         # JSON → dict

# 2. 带参数
params = {"key1": "value1", "key2": "value2"}
r = requests.get("https://httpbin.org/get", params=params)

# 3. POST 请求
data = {"username": "alice", "password": "secret"}
r = requests.post("https://httpbin.org/post", data=data)

# JSON 提交
r = requests.post("https://httpbin.org/post", json=data)

# 4. Headers
headers = {"User-Agent": "MyApp/1.0"}
r = requests.get("https://api.github.com", headers=headers)

# 5. Cookies
cookies = {"session": "abc123"}
r = requests.get("https://example.com", cookies=cookies)

# 6. 超时
r = requests.get("https://example.com", timeout=5)
```

## 二、Session（保持 Cookie）

```python
import requests

session = requests.Session()
session.get("https://example.com/login")      # 获取初始 Cookie
session.post("https://example.com/login", data={...})  # 登录（设置 Cookie）
response = session.get("https://example.com/dashboard")  # 自动带 Cookie
```

## 三、代理

```python
proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}
r = requests.get("https://example.com", proxies=proxies)
```

## 四、错误处理

```python
import requests
from requests.exceptions import RequestException

try:
    r = requests.get("https://example.com", timeout=5)
    r.raise_for_status()    # 4xx/5xx 抛 HTTPError
except requests.exceptions.Timeout:
    print("超时")
except requests.exceptions.HTTPError as e:
    print(f"HTTP 错误：{e}")
except RequestException as e:
    print(f"请求失败：{e}")
```

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）