---
title: "学习计划 P074 【网络爬虫】基本流程和robots协议"
p_no: 74
category: 网络爬虫
created: 2026-06-24
updated: 2026-06-24
type: study-plan
---

# 学习计划 P074　【网络爬虫】基本流程和robots协议

## 一、本节在课程中的位置

| 项目 | 内容 |
|------|------|
| 课程章节 | 第 74 集 / 共 100 集 |
| 分类 | 网络爬虫 |
| 视频时长 | 550 秒（约 9 分钟） |
| 难度 | 基础 |

## 二、为什么先学这一节

学完 HTTP 基础后，需要了解爬虫的完整工作流程，以及最重要的**法律合规**要求——robots.txt 协议。理解爬虫基本流程才能正确设计爬虫，理解 robots.txt 才能避免法律风险。

## 三、本节要回答的核心问题

1. **爬虫的基本工作流程是什么？**
2. **robots.txt 是什么？**
3. **如何用 Python 解析 robots.txt？**
4. **如何判断某个 URL 是否可以爬取？**
5. **爬虫的法律和伦理边界？**

## 四、课本对照

本节内容**书本未涵盖**。爬虫相关内容需要靠课程视频 + 知识补全学习。

## 五、具体学习步骤

### 第 1 步：爬虫基本流程（10 分钟）

```python
# 爬虫的 5 步流程
# 1. 确定目标：选网站、选数据
# 2. 发送请求：HTTP GET/POST
# 3. 获取响应：HTML/JSON/二进制
# 4. 解析数据：正则/BeautifulSoup/XPath
# 5. 保存数据：文件/数据库

# 最小爬虫示例
import requests

# 第 2 步：发送请求
response = requests.get("https://example.com")

# 第 3 步：获取响应
print(response.status_code)  # 200
print(response.text[:200])   # HTML 内容

# 第 4 步：解析数据（后续课程会详细讲）
# 第 5 步：保存数据（后续课程会详细讲）
```

### 第 2 步：robots.txt 协议详解（15 分钟）

```python
# robots.txt 示例
# 语法规则：
# - # 开头是注释
# - User-agent: 指定爬虫名称
# - Disallow: 禁止访问的路径
# - Allow: 允许访问的路径
# - Crawl-delay: 请求间隔（秒）

# robots.txt 文件内容示例：
"""
# 注释
User-agent: *                  # 适用所有爬虫
Disallow: /admin/              # 禁止爬 /admin/ 下的所有页面
Disallow: /private/*.html      # 禁止爬 /private/ 下 .html 文件
Allow: /public/                # 允许爬 /public/

User-agent: Googlebot          # 仅适用 Google
Allow: /                       # 没有禁止就是允许

Crawl-delay: 10                # 每次请求间隔 10 秒
Sitemap: https://example.com/sitemap.xml
"""
```

### 第 3 步：Python 解析 robots.txt（15 分钟）

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
print(f"Delay: {delay}")  # 10 或 None

# 检查是否有特定的 robots 规则
request_rate = rp.request_rate("*")
print(f"Request rate: {request_rate}")
```

### 第 4 步：实际爬虫的 robots 检查（15 分钟）

```python
import requests
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse

def can_fetch(url, user_agent="*"):
    """检查 URL 是否可以被爬取"""
    parsed = urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"

    rp = RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
        return rp.can_fetch(user_agent, url)
    except Exception:
        return True    # 加载失败时默认允许（保守策略）

# 使用示例
url = "https://www.example.com/page.html"
if can_fetch(url):
    print("可以爬取，开始请求...")
    resp = requests.get(url)
    # 处理响应...
else:
    print("robots.txt 禁止爬取，跳过")
```

### 第 5 步：爬虫的法律与伦理（10 分钟）

```python
# 爬虫法律风险点：
# 1. 版权内容：不要爬取受版权保护的文章、图片、音乐
# 2. 个人隐私：不要爬取个人隐私数据（身份证、电话、地址）
# 3. 付费墙：不要绕过付费墙或验证码
# 4. robots.txt：遵守网站的爬虫协议
# 5. 请求频率：不要频繁请求导致服务器宕机

# 合规爬虫最佳实践：
# 1. 先读 robots.txt
# 2. 设置合理的请求间隔（Crawl-delay）
# 3. 设置 User-Agent 标识
# 4. 不要爬取个人隐私数据
# 5. 数据仅供个人学习使用
```

## 六、这一节要掌握的知识点

- [ ] 爬虫的 5 步基本流程（确定目标→请求→响应→解析→保存）
- [ ] robots.txt 协议语法（User-agent/Disallow/Allow/Crawl-delay）
- [ ] 用 `urllib.robotparser` 解析 robots.txt
- [ ] `can_fetch()` 判断 URL 是否可爬
- [ ] 爬虫法律风险（版权、隐私、付费墙）
- [ ] 合规爬虫最佳实践

## 七、动手练习

### 练习 1：检查目标网站 robots.txt

```python
# 检查以下网站的 robots.txt
sites = [
    "https://www.baidu.com/robots.txt",
    "https://www.taobao.com/robots.txt",
    "https://github.com/robots.txt",
]

# 用代码检查这些网站是否允许爬取某个 URL
```

### 练习 2：封装 robots 检查函数

```python
# 封装一个通用的 robots 检查函数
def check_robots(url, user_agent="MyBot/1.0"):
    """
    返回：
    - can_fetch: bool，是否可以爬取
    - delay: 请求间隔（秒），None 表示未指定
    """
    # 实现代码...
    pass
```

## 八、自测题

- [ ] **Q1**：爬虫的 5 步基本流程是什么？
- [ ] **Q2**：robots.txt 中 `Disallow: /private/` 是什么意思？
- [ ] **Q3**：如何用 Python 检查某个 URL 是否允许爬取？
- [ ] **Q4**：爬虫可能涉及哪些法律风险？
- [ ] **Q5**：为什么爬虫要设置请求间隔？

## 九、参考资料

- 视频 BV1rpWjevEip P74
- 官方 robots.txt 规范：https://www.robotstxt.org/
- 百度 robots.txt：https://www.baidu.com/robots.txt
- Google robots.txt：https://www.google.com/robots.txt

### 选读

- Scrapy 文档：https://docs.scrapy.org/
- 爬虫伦理指南：https://www.nature.com/articles/d41586-021-02961-9

## 十、关联 Vault 笔记

- [[学习指南/P074-网络爬虫-【网络爬虫】基本流程和robots协议]]
- [[学习计划/P073-网络爬虫-【网络爬虫】爬虫的概念与分类-学习计划]]（上一节）
- [[学习计划/P075-网络爬虫-【网络爬虫】爬虫的分类-学习计划]]（下一节）
- [[index]]

---

> **预计总时长**：65 分钟（视频 9 + 实操 56）
>
> **完成标志**：能解释爬虫基本流程，能用 Python 检查 robots.txt，理解爬虫法律边界
