---
title: "学习计划 P084 【网络爬虫】user-agent池的介绍"
p_no: 84
category: 网络爬虫
created: 2026-06-24
updated: 2026-06-24
type: study-plan
---

# 学习计划 P084　【网络爬虫】user-agent池的介绍

## 一、本节在课程中的位置

| 项目 | 内容 |
|------|------|
| 课程章节 | 第 84 集 / 共 100 集 |
| 分类 | 网络爬虫 |
| 视频时长 | 455 秒（约 8 分钟） |
| 难度 | 中级 |

## 二、为什么先学这一节

User-Agent 是最基础的反爬检查目标。很多网站会：
- 统计不同 User-Agent 的访问量
- 封禁非浏览器的 User-Agent
- 限制单一 User-Agent 的请求频率

学会使用 UA 池可以：
- 模拟多个浏览器，降低被封概率
- 避免单一来源的流量异常
- 提升爬虫的稳定性

## 三、本节要回答的核心问题

1. **什么是 User-Agent 池？**
2. **如何手动构建 UA 池？**
3. **如何使用 fake-useragent 库？**
4. **如何封装自动随机 UA 的 Session？**
5. **UA 池的最佳实践？**

## 四、课本对照

本节内容**书本未涵盖**。反爬策略属于进阶知识，需要靠课程视频 + 知识补全学习。

## 五、具体学习步骤

### 第 1 步：User-Agent 池概念（10 分钟）

```python
# 什么是 User-Agent 池？
# UA 池 = 多个 User-Agent 字符串的集合
# 爬虫从池中随机选择 UA，模拟不同浏览器

# 为什么需要 UA 池？
# 1. 避免被识别为爬虫
# 2. 分散请求来源
# 3. 模拟真实用户行为

# UA 池的工作原理：
"""
┌─────────────────────────────────────────┐
│           User-Agent 池                 │
│  ┌─────────────────────────────────┐   │
│  │ Chrome Windows                  │   │
│  │ Chrome Mac                      │   │
│  │ Firefox Windows                 │   │
│  │ Safari iPhone                   │   │
│  │ ...                             │   │
│  └─────────────────────────────────┘   │
│                   ↓                     │
│           random.choice()              │
│                   ↓                     │
│  ┌─────────────────────────────────┐   │
│  │ Headers: {                      │   │
│  │   "User-Agent": "随机选择一个"  │   │
│  │ }                               │   │
│  └─────────────────────────────────┘   │
"""
```

### 第 2 步：手动构建 UA 池（15 分钟）

```python
import random

# 常见的 User-Agent 池
UA_POOL = [
    # Chrome - Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",

    # Chrome - Mac
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",

    # Firefox - Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",

    # Firefox - Mac
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0",

    # Safari - Mac
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",

    # Safari - iPhone
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",

    # Edge
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",

    # Android Chrome
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
]

# 随机选择一个 UA
def get_random_ua():
    return random.choice(UA_POOL)

print(get_random_ua())
```

### 第 3 步：fake-useragent 库（15 分钟）

```python
# 推荐使用 fake-useragent 库，自动获取最新 UA

# 安装
# pip install fake-useragent

from fake_useragent import UserAgent

ua = UserAgent()

# 获取随机 UA
print(ua.random)    # 随机 UA
print(ua.chrome)    # Chrome UA
print(ua.firefox)   # Firefox UA
print(ua.safari)    # Safari UA
print(ua.edge)      # Edge UA
print(ua.ie)        # IE UA（不推荐）

# 在 requests 中使用
import requests

headers = {"User-Agent": ua.random}
response = requests.get("https://example.com", headers=headers)
```

### 第 4 步：封装自动随机 UA 的 Session（15 分钟）

```python
import random
import requests

# 方法 1：简单版
class RandomUASession(requests.Session):
    """自动随机 UA 的 Session"""

    def __init__(self, ua_pool=None):
        super().__init__()
        self.ua_pool = ua_pool or [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) Safari/604.1",
        ]

    def request(self, *args, **kwargs):
        headers = kwargs.pop("headers", {})
        headers.setdefault("User-Agent", random.choice(self.ua_pool))
        return super().request(*args, headers=headers, **kwargs)

# 使用
session = RandomUASession()
response1 = session.get("https://example.com/page1")  # 自动加随机 UA
response2 = session.get("https://example.com/page2")  # 每次不同 UA
```

### 第 5 步：UA 池最佳实践（10 分钟）

```python
# UA 池最佳实践：

# 1. 定期更新 UA 池
# UA 字符串会过期，需要定期从网上获取最新的
# 推荐：https://www.useragentstring.com/

# 2. 组合其他反爬策略
class AntiBanSession(requests.Session):
    """组合反爬策略的 Session"""

    def __init__(self):
        super().__init__()
        self.ua_pool = [...]
        self.request_count = 0

    def request(self, *args, **kwargs):
        # 策略 1：随机 UA
        headers = kwargs.pop("headers", {})
        headers.setdefault("User-Agent", random.choice(self.ua_pool))

        # 策略 2：随机延迟
        import time
        time.sleep(random.uniform(1, 3))

        # 策略 3：计数器
        self.request_count += 1

        return super().request(*args, headers=headers, **kwargs)

# 3. 记录和监控
# - 记录每个 UA 的成功率
# - 动态调整 UA 池
# - 失败时切换 UA
```

## 六、这一节要掌握的知识点

- [ ] User-Agent 池的概念和作用
- [ ] 常见浏览器的 User-Agent 字符串
- [ ] 手动构建 UA 池
- [ ] fake-useragent 库的使用
- [ ] 封装自动随机 UA 的 Session
- [ ] UA 池的最佳实践

## 七、动手练习

### 练习 1：构建自己的 UA 池

```python
# 从 https://www.useragentstring.com/ 获取最新的 UA 字符串
# 构建一个包含 10+ UA 的池
# 实现随机选择函数

UA_POOL = [
    # 添加你收集的 UA 字符串
]

def get_random_ua():
    """返回随机 User-Agent"""
    # 实现代码...
    pass
```

### 练习 2：封装 AntiBanSession

```python
# 封装一个综合反爬的 Session 类
class AntiBanSession(requests.Session):
    """带反爬功能的 Session"""

    def __init__(self, ua_pool=None, delay_range=(1, 3)):
        # 初始化代码...
        pass

    def request(self, *args, **kwargs):
        # 随机 UA + 随机延迟 + 记录统计
        pass
```

## 八、自测题

- [ ] **Q1**：什么是 User-Agent 池？为什么需要？
- [ ] **Q2**：如何手动构建 UA 池？
- [ ] **Q3**：fake-useragent 库有什么优势？
- [ ] **Q4**：如何封装自动随机 UA 的 Session？
- [ ] **Q5**：UA 池的最佳实践有哪些？

## 九、参考资料

- 视频 BV1rpWjevEip P84
- fake-useragent：https://github.com/fake-useragent/fake-useragent
- User-Agent String：https://www.useragentstring.com/

### 选读

- Chrome UA 列表：https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome
- 反爬策略汇总：https://github.com/chenjiandongx/anti-anti-spider

## 十、关联 Vault 笔记

- [[学习指南/P084-网络爬虫-【网络爬虫】user-agent池的介绍]]
- [[学习计划/P083-网络爬虫-【网络爬虫】用户代理的介绍-学习计划]]（上一节）
- [[学习计划/P085-网络爬虫-【网络爬虫】浏览器发送请求原理-学习计划]]（下一节）
- [[index]]

---

> **预计总时长**：65 分钟（视频 8 + 实操 57）
>
> **完成标志**：能构建 UA 池，能封装自动随机 UA 的 Session，能结合其他反爬策略使用
