---
title: "P94 【网络爬虫】post请求"
p_no: 94
category: 网络爬虫
duration: 304
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P94 【网络爬虫】post请求

> **课程分类**：网络爬虫
> **时长**：304 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

网络爬虫阶段，从 HTTP 基础到 requests 模块，再到综合案例。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
## POST 请求详解

```python
import requests

# 1. form 表单（最常用）
data = {
    "username": "alice",
    "password": "secret",
}
r = requests.post("https://example.com/login", data=data)
print(r.cookies)          # 登录后 Set-Cookie
print(r.history)          # 重定向历史

# 2. JSON 请求
payload = {
    "title": "Hello",
    "content": "World",
    "tags": ["python", "tutorial"],
}
r = requests.post(
    "https://api.example.com/posts",
    json=payload,
    headers={"Authorization": "Bearer xxx"}
)
print(r.json())

# 3. 原始 body
import json
r = requests.post(
    "https://api.example.com/data",
    data=json.dumps(payload),
    headers={"Content-Type": "application/json"}
)
```

## 金山翻译案例

```python
import requests

# 金山翻译 API（简化版）
url = "https://ifanyi.iciba.com/index.php?c=trans&m=getTrans"
data = {
    "from": "en",
    "to": "zh",
    "query": "hello world",
}
headers = {
    "User-Agent": "Mozilla/5.0 ...",
    "Origin": "https://www.iciba.com",
    "Referer": "https://www.iciba.com/",
}

r = requests.post(url, data=data, headers=headers)
result = r.json()
print(result.get("content", {}).get("out", ""))
```

## POST vs GET 区别

| 维度 | GET | POST |
|------|-----|------|
| 参数位置 | URL | 请求体 |
| 长度限制 | 约 2KB | 无（理论上） |
| 可见性 | URL 中可见 | 不在 URL |
| 缓存 | 可缓存 | 通常不缓存 |
| 用途 | 读取数据 | 提交/创建数据 |

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）