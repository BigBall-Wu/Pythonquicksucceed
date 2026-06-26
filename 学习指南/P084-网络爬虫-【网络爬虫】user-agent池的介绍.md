---
title: "P84 【网络爬虫】user-agent池的介绍"
p_no: 84
category: 网络爬虫
duration: 455
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P84 【网络爬虫】user-agent池的介绍

> **课程分类**：网络爬虫
> **时长**：455 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

网络爬虫阶段，从 HTTP 基础到 requests 模块，再到综合案例。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
## User-Agent 池

```python
import random
import requests

UA_POOL = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15",
    "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 Chrome/120.0.0.0",
]

class UAPoolSession(requests.Session):
    """自动随机 UA 的 Session"""
    def __init__(self, ua_pool=None):
        super().__init__()
        self.ua_pool = ua_pool or UA_POOL

    def request(self, *args, **kwargs):
        headers = kwargs.pop("headers", {})
        headers.setdefault("User-Agent", random.choice(self.ua_pool))
        return super().request(*args, headers=headers, **kwargs)

# 使用
session = UAPoolSession()
r = session.get("https://example.com")
```

## fake-useragent 库（推荐）

```bash
pip install fake-useragent
```

```python
from fake_useragent import UserAgent

ua = UserAgent()
print(ua.random)     # 随机 UA
print(ua.chrome)    # Chrome UA
print(ua.firefox)    # Firefox UA
print(ua.safari)    # Safari UA

# 在 requests 中使用
headers = {"User-Agent": ua.random}
r = requests.get("https://example.com", headers=headers)
```

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）