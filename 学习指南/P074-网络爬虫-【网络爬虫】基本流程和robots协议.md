---
title: "P74 【网络爬虫】基本流程和robots协议"
p_no: 74
category: 网络爬虫
duration: 550
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P74 【网络爬虫】基本流程和robots协议

> **课程分类**：网络爬虫
> **时长**：550 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

网络爬虫阶段，从 HTTP 基础到 requests 模块，再到综合案例。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
## robots.txt 详解

```
# 注释
User-agent: *                  # 适用所有爬虫
Disallow: /admin/              # 禁止爬 /admin/ 下的所有页面
Disallow: /private/*.html      # 禁止爬 /private/ 下 .html 文件
Allow: /public/                # 允许爬 /public/

User-agent: Googlebot          # 仅适用 Google
Allow: /                       # 没有禁止就是允许

Crawl-delay: 10                # 每次请求间隔 10 秒
Sitemap: https://example.com/sitemap.xml
```

## Python 处理 robots.txt

```python
from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url("https://www.example.com/robots.txt")
rp.read()

# 检查某个 URL 是否允许爬
can_fetch = rp.can_fetch("*", "https://www.example.com/page")
print(can_fetch)    # True / False

# 检查爬取延迟
delay = rp.crawl_delay("*")
print(f"Delay: {delay}")
```

## 实际爬虫的 robots 检查

```python
import requests
from urllib.robotparser import RobotFileParser

def can_fetch(url, user_agent="*"):
    from urllib.parse import urlparse
    parsed = urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"

    rp = RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
        return rp.can_fetch(user_agent, url)
    except Exception:
        return True    # 加载失败时默认允许

url = "https://www.example.com/page.html"
if can_fetch(url):
    resp = requests.get(url)
    print(resp.text)
else:
    print("robots.txt 禁止爬取")
```

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）