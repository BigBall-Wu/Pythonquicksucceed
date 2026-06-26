---
title: "P97 【网络爬虫】session自动携带cookie"
p_no: 97
category: 网络爬虫
duration: 357
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P97 【网络爬虫】session自动携带cookie

> **课程分类**：网络爬虫
> **时长**：357 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

网络爬虫阶段，从 HTTP 基础到 requests 模块，再到综合案例。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
## Session（保持会话）

```python
import requests

session = requests.Session()

# 自动管理 Cookie
session.get("https://example.com/")          # 获取初始 cookie
session.post("https://example.com/login", data={"user": "alice", "pwd": "secret"})

# 后续请求自动带登录 cookie
r = session.get("https://example.com/profile")
print(r.text)

# 多个请求之间共享 headers
session.headers.update({"Authorization": "Bearer xxx"})
```

## Session 高级用法

```python
import requests

# 1. 上下文管理器（自动关闭）
with requests.Session() as s:
    s.get("https://example.com")

# 2. 合并多个 session
s1 = requests.Session()
s2 = requests.Session()

# 3. 重试（urllib3 内置）
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
)

adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("http://", adapter)
session.mount("https://", adapter)
```

## Session vs 直接 requests

| 特性 | `requests` | `requests.Session` |
|------|-----------|-------------------|
| Cookie 管理 | 每次新建 | 跨请求保持 |
| 连接复用 | 否 | 是（HTTP Keep-Alive） |
| 性能 | 较低 | 高（TCP 握手省） |
| 适用 | 一次性请求 | 多次相关请求 |

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）