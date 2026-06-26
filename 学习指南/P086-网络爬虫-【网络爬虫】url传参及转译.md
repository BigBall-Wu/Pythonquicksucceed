---
title: "P86 【网络爬虫】url传参及转译"
p_no: 86
category: 网络爬虫
duration: 515
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P86 【网络爬虫】url传参及转译

> **课程分类**：网络爬虫
> **时长**：515 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

网络爬虫阶段，从 HTTP 基础到 requests 模块，再到综合案例。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
## URL 参数详解

### URL 结构

```
https://www.example.com:8080/path/to/page?key1=value1&key2=value2#section
│              │          │                  │                       │
scheme        host        path              query                   fragment
```

### URL 编码

URL 中只能包含 ASCII 字符 + 少数特殊字符。

```python
from urllib.parse import quote, unquote

# 编码
quote("你好世界")           # '%E4%BD%A0%E5%A5%BD%E4%B8%96%E7%95%8C'
quote("a&b=c")             # 'a%26b%3Dc'

# 解码
unquote("%E4%BD%A0%E5%A5%BD")    # '你好'

# 完整 URL 编码
from urllib.parse import quote_plus, unquote_plus
quote_plus("a b")          # 'a+b'
unquote_plus("a+b")        # 'a b'
```

### urlencode 构造查询字符串

```python
from urllib.parse import urlencode

params = {"q": "python 教程", "page": 1, "type": "video"}
query = urlencode(params)
# "q=python+%E6%95%99%E7%A8%8B&page=1&type=video"

url = f"https://www.example.com/search?{query}"
# "https://www.example.com/search?q=python+%E6%95%99%E7%A8%8B&page=1&type=video"
```

### requests 自动编码

```python
import requests

# requests 自动处理编码
params = {"q": "你好", "page": 1}
r = requests.get("https://example.com/search", params=params)
print(r.url)    # https://example.com/search?q=%E4%BD%A0%E5%A5%BD&page=1
```

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）