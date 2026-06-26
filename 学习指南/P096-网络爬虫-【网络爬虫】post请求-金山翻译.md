---
title: "P96 【网络爬虫】post请求-金山翻译"
p_no: 96
category: 网络爬虫
duration: 526
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P96 【网络爬虫】post请求-金山翻译

> **课程分类**：网络爬虫
> **时长**：526 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

网络爬虫阶段，从 HTTP 基础到 requests 模块，再到综合案例。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
## 案例：金山翻译 POST 请求

```python
import requests
import time
import hashlib

def kingsoft_translate(text, from_lang="en", to_lang="zh"):
    """金山翻译 API（简化版）"""
    url = "https://ifanyi.iciba.com/index.php?c=trans&m=getTrans"

    # 时间戳 + 签名（部分 API 需要）
    timestamp = str(int(time.time()))
    salt = timestamp

    # 请求参数
    data = {
        "from": from_lang,
        "to": to_lang,
        "query": text,
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Origin": "https://www.iciba.com",
        "Referer": "https://www.iciba.com/",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
    }

    r = requests.post(url, data=data, headers=headers, timeout=10)
    result = r.json()

    if result.get("status") == 1:
        return result["content"]["out"]
    return None

# 测试
text = "Hello, world! Python is great."
translation = kingsoft_translate(text, "en", "zh")
print(f"{text}\\n→ {translation}")
```

## 实际的金山 API 加密

真实 API 会有更多参数（sign、ts、salt）：

```python
import hashlib
import time

def generate_sign(query, salt):
    """生成签名（实际规则需要查文档/逆向）"""
    s = f"{query}{salt}secret_key"
    return hashlib.md5(s.encode()).hexdigest()

def kingsoft_translate_real(text, from_lang="en", to_lang="zh"):
    url = "https://ifanyi.iciba.com/index.php?c=trans&m=getTrans"

    timestamp = str(int(time.time()))
    salt = timestamp[:10]    # 部分 API 用
    sign = generate_sign(text, salt)

    data = {
        "from": from_lang,
        "to": to_lang,
        "query": text,
        "ts": timestamp,
        "salt": salt,
        "sign": sign,
    }

    r = requests.post(url, data=data, headers={
        "User-Agent": "Mozilla/5.0 ...",
        "Origin": "https://www.iciba.com",
        "Referer": "https://www.iciba.com/",
    })
    return r.json()
```

## 调试技巧

```python
# 1. 先用浏览器抓包看真实请求
# F12 → Network → 找 XHR 请求 → Copy as cURL

# 2. 转 Python
# https://curlconverter.com/

# 3. 测试
import requests

r = requests.post(
    "https://...",
    data={"key": "value"},
    headers={"User-Agent": "Mozilla/5.0 ..."}
)
print(r.status_code, r.text[:500])
```

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）