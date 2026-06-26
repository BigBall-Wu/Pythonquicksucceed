---
title: "学习计划 P095 【网络爬虫】使用cookie获取登录后的页面数据"
p_no: 95
category: 网络爬虫
created: 2026-06-24
updated: 2026-06-24
type: study-plan
---

# 学习计划 P095　【网络爬虫】使用cookie获取登录后的页面数据

## 一、本节在课程中的位置

| 项目 | 内容 |
|------|------|
| 课程章节 | 第 95 集 / 共 100 集 |
| 分类 | 网络爬虫 |
| 视频时长 | 330 秒（约 6 分钟） |
| 难度 | 中级 |

## 二、为什么先学这一节

很多网站的数据需要登录后才能访问。学会使用 Cookie 可以：
- 爬取登录后的私有数据
- 保持会话状态
- 模拟用户行为
- 理解认证机制

## 三、本节要回答的核心问题

1. **Cookie 的作用是什么？**
2. **如何从浏览器获取 Cookie？**
3. **如何在 requests 中使用 Cookie？**
4. **如何保存和加载 Cookie？**
5. **Cookie 的安全问题？**

## 四、课本对照

本节内容**书本未涵盖**。Cookie 和认证属于网络进阶知识，需要靠课程视频 + 知识补全学习。

## 五、具体学习步骤

### 第 1 步：Cookie 机制（10 分钟）

```python
# Cookie 工作原理：
"""
1. 用户首次访问服务器
2. 服务器生成会话，保存用户信息
3. 服务器通过 Set-Cookie 头返回 Cookie
4. 浏览器保存 Cookie
5. 后续请求自动带上 Cookie
6. 服务器识别用户身份

┌──────────┐         ┌──────────┐
│  浏览器   │         │  服务器   │
└────┬─────┘         └────┬─────┘
     │                     │
     │  GET /page          │
     │────────────────────>│
     │                     │
     │  200 + Set-Cookie  │
     │<────────────────────│
     │                     │
     │  GET /page          │
     │  Cookie: session=xxx│
     │────────────────────>│
     │                     │
     │  200 (个性化页面)   │
     │<────────────────────│
"""
```

### 第 2 步：从浏览器获取 Cookie（10 分钟）

```python
# 从 Chrome 获取 Cookie：
# 1. 登录网站
# 2. 按 F12 打开开发者工具
# 3. 切换到 Application 标签
# 4. 左侧选择 Cookies -> 网站
# 5. 找到需要的 Cookie，复制值

# 示例：获取 GitHub 登录 Cookie
github_cookies = {
    "logged_in": "yes",
    "user_session": "xxx...",  # 主要的会话 Cookie
    "_gh_sess": "xxx...",
}
```

### 第 3 步：requests 使用 Cookie（15 分钟）

```python
import requests

# 方法 1：直接设置 Cookie（不推荐）
headers = {
    "Cookie": "session_id=abc123; token=xyz789"
}
r = requests.get("https://example.com/dashboard", headers=headers)

# 方法 2：使用 cookies 参数
cookies = {
    "session_id": "abc123",
    "token": "xyz789"
}
r = requests.get("https://example.com/dashboard", cookies=cookies)

# 方法 3：使用 Session 自动管理（推荐）
session = requests.Session()

# 方式 A：手动设置 cookies
session.cookies.set("session_id", "abc123")

# 方式 B：从 dict 更新
session.cookies.update({
    "user_id": "12345",
    "preferences": "dark_mode"
})

# 方式 C：加载 Cookie jar
session.cookies = requests.cookies.RequestsCookieJar()
session.cookies.update(cookies)

r = session.get("https://example.com/dashboard")
```

### 第 4 步：完整登录流程（15 分钟）

```python
import requests

def login_and_get_data(url, username, password):
    """登录并获取数据"""
    session = requests.Session()

    # 1. 获取登录页面（可能需要 CSRF token）
    login_page = session.get("https://example.com/login")
    # 解析 CSRF token（如果有）

    # 2. 提交登录表单
    login_data = {
        "username": username,
        "password": password,
        # "csrf_token": "xxx",  # 如果有 CSRF
    }

    response = session.post(
        "https://example.com/login",
        data=login_data,
        allow_redirects=True
    )

    # 3. 检查是否登录成功
    if response.status_code == 200:
        # 检查是否包含登录后的内容
        if "dashboard" in response.url or "logout" in response.text:
            print("登录成功")

            # 4. 访问需要登录的页面
            dashboard = session.get("https://example.com/dashboard")
            return dashboard.text
        else:
            print("登录失败")
            return None

# 使用
data = login_and_get_data(
    "https://example.com/dashboard",
    "username",
    "password"
)
```

### 第 5 步：Cookie 持久化（10 分钟）

```python
import requests
import pickle
import json
from pathlib import Path

# 保存 Cookie
def save_cookies(session, filepath="cookies.pkl"):
    """保存 Cookie 到文件"""
    with open(filepath, "wb") as f:
        pickle.dump(session.cookies, f)
    print(f"Cookie 保存到 {filepath}")

# 加载 Cookie
def load_cookies(filepath="cookies.pkl"):
    """从文件加载 Cookie"""
    if Path(filepath).exists():
        with open(filepath, "rb") as f:
            cookies = pickle.load(f)

        session = requests.Session()
        session.cookies.update(cookies)
        return session
    return None

# 使用
session = load_cookies()
if session is None:
    # 需要重新登录
    session = login_and_get_data(...)
    save_cookies(session)

# 使用 Cookie 访问
r = session.get("https://example.com/dashboard")

# JSON 格式保存（跨平台）
def save_cookies_json(session, filepath="cookies.json"):
    """保存为 JSON 格式"""
    cookies = {k: v for k, v in session.cookies.items()}
    with open(filepath, "w") as f:
        json.dump(cookies, f)

def load_cookies_json(filepath="cookies.json"):
    """从 JSON 加载"""
    if Path(filepath).exists():
        with open(filepath) as f:
            cookies = json.load(f)

        session = requests.Session()
        session.cookies.update(cookies)
        return session
    return None
```

### 第 6 步：Cookie 安全（10 分钟）

```python
# ⚠️ Cookie 安全警告：

安全提醒 = """
1. 绝对不要提交 Cookie 到 Git 或公开仓库
   - 放到 .gitignore
   - 使用环境变量

2. Cookie 包含敏感信息
   - user_session 可能等于账号密码
   - 泄露后他人可登录你的账号

3. Cookie 有时效
   - 大多数网站 Cookie 会在 24h-30d 内过期
   - 过期后需要重新登录

4. 避免明文存储
   - 不要存到文本文件
   - 加密存储更安全
"""

# 安全存储示例
import os
from pathlib import Path

# 使用环境变量
session_cookie = os.environ.get("SESSION_COOKIE")
if session_cookie:
    session = requests.Session()
    session.cookies.set("session", session_cookie)

# 使用 .env 文件（需要 python-dotenv）
# .env 内容：SESSION_COOKIE=xxx
# .gitignore 添加：.env
```

## 六、这一节要掌握的知识点

- [ ] Cookie 的工作原理
- [ ] 从浏览器获取 Cookie
- [ ] requests 中 Cookie 的使用
- [ ] Session 自动管理 Cookie
- [ ] Cookie 持久化（pickle/JSON）
- [ ] Cookie 安全注意事项

## 七、动手练习

### 练习 1：GitHub API 访问

```python
# 使用 Cookie 访问 GitHub API
# 获取你的个人信息、仓库列表等

def github_api_request(endpoint):
    """访问 GitHub API"""
    # 使用 GitHub Cookie
    # 实现代码...
    pass
```

### 练习 2：保存和加载 Cookie

```python
# 实现一个 Cookie 管理类
class CookieManager:
    """Cookie 管理器"""

    def __init__(self, storage_path):
        # 初始化...
        pass

    def save(self, session):
        # 保存 Cookie...
        pass

    def load(self):
        # 加载 Cookie...
        pass

    def is_valid(self):
        # 检查 Cookie 是否有效...
        pass
```

## 八、自测题

- [ ] **Q1**：Cookie 的作用是什么？
- [ ] **Q2**：如何在 requests 中设置 Cookie？
- [ ] **Q3**：为什么推荐使用 Session？
- [ ] **Q4**：Cookie 持久化有哪些方式？
- [ ] **Q5**：Cookie 安全需要注意什么？

## 九、参考资料

- 视频 BV1rpWjevEip P95
- HTTP Cookie：https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Cookies
- requests Session：https://docs.python-requests.org/zh_CN/latest/user/advanced.html

### 选读

- Cookie 安全：https://owasp.org/www-community/attacks/Cross-Site_Cookies
- SameSite Cookie：https://web.dev/samesite-cookies-explained/

## 十、关联 Vault 笔记

- [[学习指南/P095-网络爬虫-【网络爬虫】使用cookie获取登录后的页面数据]]
- [[学习计划/P094-网络爬虫-【网络爬虫】post请求-学习计划]]（上一节）
- [[学习计划/P096-网络爬虫-【网络爬虫】post请求-金山翻译-学习计划]]（下一节）
- [[index]]

---

> **预计总时长**：70 分钟（视频 6 + 实操 64）
>
> **完成标志**：能理解 Cookie 机制，能在 requests 中使用 Cookie，能实现 Cookie 持久化
