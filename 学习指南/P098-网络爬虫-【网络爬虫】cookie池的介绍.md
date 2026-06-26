---
title: "P98 【网络爬虫】cookie池的介绍"
p_no: 98
category: 网络爬虫
duration: 313
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P98 【网络爬虫】cookie池的介绍

> **课程分类**：网络爬虫
> **时长**：313 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

网络爬虫阶段，从 HTTP 基础到 requests 模块，再到综合案例。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
## Cookie 池

多个账号的 Cookie 轮换，避免单一账号被封。

```python
import random
import requests

class CookiePool:
    def __init__(self, cookies_list):
        """cookies_list: [{'sid': 'xxx'}, {'sid': 'yyy'}, ...]"""
        self.cookies_list = cookies_list

    def get_random(self):
        """随机获取一个 cookie"""
        return random.choice(self.cookies_list)

    def get_session(self):
        """获取一个带随机 cookie 的 Session"""
        session = requests.Session()
        session.cookies.update(self.get_random())
        return session

# 用法
pool = CookiePool([
    {"session_id": "alice_session"},
    {"session_id": "bob_session"},
    {"session_id": "charlie_session"},
])

for url in urls:
    session = pool.get_session()
    r = session.get(url)
    process(r)
    session.close()
```

## Cookie 池维护

```python
import json
import time

class CookiePoolManager:
    def __init__(self, storage_file="cookie_pool.json"):
        self.storage_file = storage_file
        self.cookies = self._load()

    def _load(self):
        try:
            with open(self.storage_file) as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def _save(self):
        with open(self.storage_file, "w") as f:
            json.dump(self.cookies, f, indent=2)

    def add(self, cookie, max_age=3600):
        """添加新 cookie（含过期时间）"""
        cookie["added_at"] = time.time()
        cookie["expires_at"] = time.time() + max_age
        self.cookies.append(cookie)
        self._save()

    def get_valid(self):
        """获取所有有效的 cookie"""
        now = time.time()
        valid = [c for c in self.cookies if c.get("expires_at", 0) > now]
        return valid

    def remove_expired(self):
        """清除过期 cookie"""
        now = time.time()
        self.cookies = [c for c in self.cookies if c.get("expires_at", 0) > now]
        self._save()
```

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）