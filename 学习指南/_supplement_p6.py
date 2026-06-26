# -*- coding: utf-8 -*-
"""补全知识库 - 第六批：HTTP/爬虫/案例（紧凑版）"""
SUPPLEMENT_6 = {

# HTTP 基础
"http_basics": """\
## 一、HTTP 协议基础

**HTTP**（HyperText Transfer Protocol）是浏览器与服务器通信的协议。

### 请求-响应模型

```
浏览器 → GET /index.html HTTP/1.1     ← 请求
浏览器 → Host: www.example.com
浏览器 → User-Agent: Chrome/120
浏览器 → [空行]

服务器 → HTTP/1.1 200 OK               ← 响应
服务器 → Content-Type: text/html
服务器 → Content-Length: 1234
服务器 → [空行]
服务器 → <html>...</html>
```

### 请求方法（Method）

| 方法 | 用途 | 幂等？ |
|------|------|--------|
| `GET` | 获取资源 | ✅ |
| `POST` | 创建/提交 | ❌ |
| `PUT` | 替换资源 | ✅ |
| `PATCH` | 部分修改 | ❌ |
| `DELETE` | 删除 | ✅ |
| `HEAD` | 只获取响应头 | ✅ |
| `OPTIONS` | 询问支持的方法 | ✅ |

### 常见状态码

| 类别 | 范围 | 含义 |
|------|------|------|
| 1xx | 100-199 | 信息 |
| 2xx | 200-299 | 成功 |
| 3xx | 300-399 | 重定向 |
| 4xx | 400-499 | 客户端错误 |
| 5xx | 500-599 | 服务器错误 |

常见：
- `200 OK`：成功
- `301 Moved Permanently`：永久重定向
- `302 Found`：临时重定向
- `304 Not Modified`：使用缓存
- `400 Bad Request`：请求语法错
- `401 Unauthorized`：未认证
- `403 Forbidden`：禁止访问
- `404 Not Found`：资源不存在
- `500 Internal Server Error`：服务器内部错误
- `503 Service Unavailable`：服务不可用

## 二、HTTP 头（Headers）

### 常见请求头

```http
User-Agent: Mozilla/5.0 ...
Accept: text/html, application/json
Accept-Language: zh-CN,zh;q=0.9
Accept-Encoding: gzip, deflate
Cookie: session=abc123
Referer: https://www.example.com/page
Authorization: Bearer xxx
Content-Type: application/json
```

### 常见响应头

```http
Content-Type: text/html; charset=utf-8
Content-Length: 12345
Set-Cookie: session=xyz
Location: /new-path
Cache-Control: max-age=3600
ETag: "abc123"
Server: nginx
```

## 三、HTTPS

**HTTPS** = HTTP + TLS/SSL，加密传输。

```python
# Python 默认验证证书
import requests
r = requests.get("https://example.com")   # 自动 HTTPS

# 跳过验证（仅测试用！）
r = requests.get("https://example.com", verify=False)

# 指定客户端证书
r = requests.get("https://example.com", cert="/path/to/cert.pem")
```
""",

"crawler_intro": """\
## 一、爬虫概述

**爬虫**（Crawler/Spider）：自动从网页提取数据的程序。

### 爬虫三步骤

1. **获取网页**（下载 HTML）
2. **解析内容**（提取数据）
3. **保存数据**（写入文件/数据库）

### 法律与道德

- ✅ 遵守 `robots.txt`
- ✅ 控制请求频率（不要 1 秒 100 次）
- ✅ 尊重网站版权
- ❌ 不要爬取个人隐私
- ❌ 不要绕过付费墙
- ❌ 不要爬取被禁止的内容（robots.txt 禁止的）

### robots.txt

每个网站根目录通常有 `robots.txt`：

```
# https://www.example.com/robots.txt
User-agent: *
Allow: /public/
Disallow: /private/
Crawl-delay: 1
```

含义：所有爬虫可以爬 `/public/`，禁止爬 `/private/`，每两次请求间隔至少 1 秒。
""",

"robots_txt": """\
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
""",

"crawler_classification": """\
## 爬虫分类

| 类型 | 特点 | 例子 |
|------|------|------|
| 通用爬虫 | 抓全网，搜索引擎用 | Googlebot |
| 聚焦爬虫 | 抓特定主题/网站 | 抓取某网站所有商品 |
| 增量爬虫 | 只抓新内容/更新 | 新闻订阅 |
| 深度爬虫 | 跟踪链接，深入抓取 | 学术论文 |

## 按实现技术

| 方式 | 优缺点 |
|------|--------|
| `requests + BeautifulSoup` | 简单静态页面 |
| `requests + lxml/XPath` | 高效解析 |
| `Scrapy` | 大型项目 |
| `Selenium` | JS 渲染页面 |
| `Playwright` | 现代浏览器自动化 |
| `pyppeteer` | 无头 Chrome |
""",

"http_request_steps": """\
## 网络请求步骤（一次完整 HTTP）

1. **DNS 解析**：域名 → IP
   - `example.com` → `93.184.216.34`
2. **TCP 握手**：三次握手建立连接
   - 客户端 → SYN → 服务器
   - 服务器 → SYN+ACK → 客户端
   - 客户端 → ACK → 服务器
3. **TLS 握手**（HTTPS 才有）
   - 协商加密算法
   - 验证证书
   - 生成会话密钥
4. **发送 HTTP 请求**
5. **服务器处理**
6. **返回 HTTP 响应**
7. **浏览器渲染**
   - 解析 HTML
   - 加载 CSS/JS
   - 渲染 DOM
   - 执行 JS

## 抓包看请求

```python
import requests

# 启用详细日志
import logging
logging.basicConfig(level=logging.DEBUG)

response = requests.get("https://httpbin.org/get")
```

或者用浏览器的 F12 → Network 面板。
""",

"http_https": """\
## HTTP vs HTTPS

| 维度 | HTTP | HTTPS |
|------|------|-------|
| 端口 | 80 | 443 |
| 加密 | ❌ 明文 | ✅ TLS/SSL |
| 证书 | 不需要 | 需要 CA 签发 |
| 速度 | 略快 | 略慢（+ TLS 握手） |
| SEO | ❌ 不利 | ✅ 谷歌优先 |

## SSL/TLS 握手流程

```
客户端 → ClientHello（支持的 TLS 版本、加密算法、随机数）
服务器 → ServerHello（选定算法、服务器证书、随机数）
客户端 → 验证证书、生成预主密钥、用公钥加密发送
双方 → 用预主密钥派生出会话密钥
之后 → 用会话密钥加密通信
```

## Python 中处理 HTTPS

```python
import requests

# 默认
r = requests.get("https://api.github.com")

# 跳过证书验证（仅测试）
r = requests.get("https://self-signed.example.com", verify=False)

# 自定义 CA
r = requests.get("https://internal.example.com", verify="/path/to/ca-bundle.crt")

# 客户端证书
r = requests.get("https://example.com", cert=("/path/to/client.crt", "/path/to/client.key"))
```

## 常见 HTTPS 问题

```python
# SSLError: CERTIFICATE_VERIFY_FAILED
# → 证书过期/不受信任

# requests.exceptions.SSLError
# → 检查 verify 参数

# SSL: CERTIFICATE_VERIFY_FAILED
# Mac 上：/Applications/Python\\ 3.x/Install\\ Certificates.command
```
""",

"browser_devtools": """\
## 浏览器 F12 抓包

### Chrome DevTools Network 面板

打开方式：`F12` → `Network` 面板

### 关键列

| 列 | 含义 |
|------|------|
| Name | 请求名 |
| Status | 状态码 |
| Type | 类型（xhr/fetch/img） |
| Initiator | 发起者 |
| Size | 大小 |
| Time | 耗时 |

### 过滤请求

- `XHR`：只看 AJAX 请求（API）
- `JS`：JavaScript
- `Img`：图片
- `Doc`：HTML
- `WS`：WebSocket

### 查看请求详情

点击请求 → 看 Headers / Preview / Response / Cookies / Timing

**Headers 面板**：
- General：URL、方法、状态码
- Response Headers：响应头
- Request Headers：请求头（**最重要的**）
- Query String Parameters：URL 参数

**Response 面板**：原始响应内容

### 复制为 cURL

右键请求 → Copy → Copy as cURL (bash)

```bash
curl 'https://api.example.com/data' \\
  -H 'User-Agent: Mozilla/5.0 ...' \\
  -H 'Authorization: Bearer xxx' \\
  -H 'Cookie: session=abc' \\
  --data-raw '{"key":"value"}'
```

转 Python requests：

```python
import requests

headers = {
    "User-Agent": "Mozilla/5.0 ...",
    "Authorization": "Bearer xxx",
    "Cookie": "session=abc",
}

response = requests.post(
    "https://api.example.com/data",
    headers=headers,
    json={"key": "value"}
)
```
""",

"http_headers": """\
## HTTP 请求头详解

```python
import requests

headers = {
    # 身份
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer": "https://www.example.com/previous-page",
    "Origin": "https://www.example.com",

    # 接受格式
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",

    # 缓存
    "Cache-Control": "no-cache",
    "If-None-Match": '"abc123"',
    "If-Modified-Since": "Wed, 21 Oct 2023 07:28:00 GMT",

    # 认证
    "Authorization": "Bearer xxx",
    "Cookie": "session=abc; token=xyz",

    # 内容类型
    "Content-Type": "application/json",
}

response = requests.get("https://api.example.com", headers=headers)
```

## 常见反爬 header

| Header | 含义 |
|--------|------|
| User-Agent | 浏览器标识 |
| Referer | 来源页面（防盗链） |
| Cookie | 会话/认证 |
| Authorization | API 认证 |
| Accept-Language | 语言偏好 |
| X-Requested-With | 标记 AJAX 请求 |
""",

"requests_module": """\
## 一、requests 模块

```python
import requests

# 1. GET 请求
r = requests.get("https://api.github.com")
print(r.status_code)    # 200
print(r.text)           # 响应文本
print(r.content)        # bytes
print(r.json())         # JSON → dict

# 2. 带参数
params = {"key1": "value1", "key2": "value2"}
r = requests.get("https://httpbin.org/get", params=params)

# 3. POST 请求
data = {"username": "alice", "password": "secret"}
r = requests.post("https://httpbin.org/post", data=data)

# JSON 提交
r = requests.post("https://httpbin.org/post", json=data)

# 4. Headers
headers = {"User-Agent": "MyApp/1.0"}
r = requests.get("https://api.github.com", headers=headers)

# 5. Cookies
cookies = {"session": "abc123"}
r = requests.get("https://example.com", cookies=cookies)

# 6. 超时
r = requests.get("https://example.com", timeout=5)
```

## 二、Session（保持 Cookie）

```python
import requests

session = requests.Session()
session.get("https://example.com/login")      # 获取初始 Cookie
session.post("https://example.com/login", data={...})  # 登录（设置 Cookie）
response = session.get("https://example.com/dashboard")  # 自动带 Cookie
```

## 三、代理

```python
proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}
r = requests.get("https://example.com", proxies=proxies)
```

## 四、错误处理

```python
import requests
from requests.exceptions import RequestException

try:
    r = requests.get("https://example.com", timeout=5)
    r.raise_for_status()    # 4xx/5xx 抛 HTTPError
except requests.exceptions.Timeout:
    print("超时")
except requests.exceptions.HTTPError as e:
    print(f"HTTP 错误：{e}")
except RequestException as e:
    print(f"请求失败：{e}")
```
""",

"response_save": """\
## 响应保存方式

```python
import requests

r = requests.get("https://example.com/image.png", stream=True)

# 1. 保存为文件
with open("image.png", "wb") as f:
    for chunk in r.iter_content(chunk_size=8192):
        f.write(chunk)

# 2. 一次性保存（小文件）
with open("image.png", "wb") as f:
    f.write(r.content)

# 3. 保存文本
with open("page.html", "w", encoding="utf-8") as f:
    f.write(r.text)
```

## 流式下载（大文件）

```python
import requests
from pathlib import Path

def download(url, filename, chunk_size=1024 * 1024):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total = int(r.headers.get("Content-Length", 0))
        downloaded = 0
        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                downloaded += len(chunk)
                if total:
                    pct = downloaded / total * 100
                    print(f"\\r{pct:.1f}%", end="")

download("https://example.com/big.zip", "big.zip")
```
""",

"response_attrs": """\
## Response 对象属性

```python
import requests

r = requests.get("https://api.github.com")

# 状态
r.status_code            # 200
r.reason                # "OK"
r.ok                    # True（状态码 < 400）
r.is_redirect           # False
r.is_permanent_redirect # False
r.url                   # 最终 URL（可能重定向）

# 头部
r.headers               # 响应头（dict）
r.headers["Content-Type"]
r.headers.get("Set-Cookie")

# 内容
r.text                  # 文本（自动解码）
r.content               # bytes
r.json()                # JSON → dict（dict/list）
r.encoding              # 编码

# Cookie
r.cookies               # RequestsCookieJar
r.cookies.get_dict()

# 请求信息
r.request               # 原始请求对象
r.request.headers        # 请求头
r.request.method        # 'GET'
r.request.url           # 请求 URL
r.request.body          # 请求体

# 时间
r.elapsed               # timedelta，请求耗时
r.history               # 重定向历史
```

## 高级用法

```python
# 获取原始 socket-level 响应
r = requests.get("https://api.github.com", stream=True)
r.raw                     # urllib3.HTTPResponse
r.raw.read(100)           # 读 100 字节

# 链接解析
r.links                   # 解析 Link 头（rel -> url）
r.links["next"]["url"]    # 下一页 URL
```
""",

"user_agent": """\
## User-Agent 详解

**User-Agent** 标识客户端软件，网站用它判断：
- 浏览器类型/版本
- 操作系统
- 设备类型（桌面/移动）

## 常见 UA

```
# Chrome (Windows)
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36

# Safari (Mac)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15

# Firefox (Linux)
Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0

# 爬虫（容易被反爬）
python-requests/2.31.0
```

## Python 中设置 UA

```python
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

r = requests.get("https://example.com", headers=headers)
```

## 随机 UA

```python
import random

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
]

def get_random_ua():
    return random.choice(user_agents)

headers = {"User-Agent": get_random_ua()}
```
""",

"ua_pool": """\
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
""",

"browser_principle": """\
## 浏览器工作原理

### 浏览器渲染流程

1. 解析 HTML → DOM 树
2. 解析 CSS → CSSOM 树
3. 合并 → 渲染树（Render Tree）
4. 布局（Layout）：计算每个节点位置
5. 绘制（Paint）：绘制像素
6. 合成（Composite）：合成图层

### JS 在页面中的作用

```html
<script>
// 同步执行
document.getElementById("price").innerText = "$99";

// 异步（AJAX）
fetch("/api/data").then(r => r.json()).then(data => {
    document.getElementById("result").innerHTML = data.html;
});

// 定时器
setTimeout(() => {
    console.log("5 秒后");
}, 5000);
</script>
```

### 为什么 requests 抓不到 JS 渲染的内容？

```python
import requests

r = requests.get("https://spa-example.com")
print(r.text)
# 只有 <div id="root"></div> 这样的空壳
# 内容由 JS 后来填充
```

**解决方案**：
1. **Selenium / Playwright**：模拟浏览器
2. **找到 API**：直接请求数据接口
3. **逆向 JS**：分析 JS 代码找到数据来源

### Selenium 例子

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://example.com")

# 等待 JS 渲染
time.sleep(2)

# 提取渲染后的内容
content = driver.find_element(By.ID, "content").text
print(content)

driver.quit()
```
""",

"url_params": """\
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
""",

"url_param_methods": """\
## URL 参数的两种传递方式

### 1. GET 参数（URL 后面）

```python
import requests

# 方式 A：params 参数（推荐，requests 自动编码）
r = requests.get("https://api.example.com/search", params={"q": "python", "page": 1})

# 方式 B：直接拼到 URL
url = "https://api.example.com/search?q=python&page=1"
r = requests.get(url)

# 方式 C：手动 urlencode
from urllib.parse import urlencode
params = urlencode({"q": "python", "page": 1})
url = f"https://api.example.com/search?{params}"
r = requests.get(url)
```

### 2. POST 参数（请求体里）

```python
import requests

# form 表单
data = {"username": "alice", "password": "secret"}
r = requests.post("https://example.com/login", data=data)

# JSON
payload = {"name": "alice", "age": 25}
r = requests.post("https://api.example.com/users", json=payload)

# 原始字符串（自定义 Content-Type）
import json
r = requests.post(
    "https://api.example.com/data",
    data=json.dumps(payload),
    headers={"Content-Type": "application/json"}
)

# 文件上传
files = {"file": open("data.csv", "rb")}
r = requests.post("https://api.example.com/upload", files=files)

# multipart
files = {
    "file": ("data.csv", open("data.csv", "rb"), "text/csv")
}
r = requests.post("https://api.example.com/upload", files=files)
```
""",

"post_request": """\
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
""",

"cookie_login": """\
## Cookie 登录

```python
import requests

# 1. 手动构造 Cookie
headers = {"Cookie": "session=abc123; token=xyz"}
r = requests.get("https://example.com/dashboard", headers=headers)

# 2. requests 自动管理 Cookie
session = requests.Session()
# 第一次访问获取 cookie
session.get("https://example.com/")
# 登录（带 cookie）
session.post("https://example.com/login", data={"user": "alice", "pwd": "secret"})
# 后续请求自动带 cookie
r = session.get("https://example.com/dashboard")
```

## 从浏览器导入 Cookie

```python
# 从 Chrome 复制的 Cookie（字符串格式）
cookie_str = "BIDUPSID=xxx; BAIDUID=yyy; ..."
cookies = {}
for item in cookie_str.split("; "):
    key, value = item.split("=", 1)
    cookies[key] = value

session = requests.Session()
session.cookies.update(cookies)
r = session.get("https://example.com/dashboard")
```

## Cookie 持久化

```python
import requests
import json
import pickle

# 保存
session = requests.Session()
session.get("https://example.com/login")

with open("cookies.pkl", "wb") as f:
    pickle.dump(session.cookies, f)

# 加载
with open("cookies.pkl", "rb") as f:
    cookies = pickle.load(f)

session = requests.Session()
session.cookies.update(cookies)
r = session.get("https://example.com/dashboard")
```
""",

"session": """\
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
""",

"cookie_pool": """\
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
""",

"proxy_intro": """\
## 代理 IP 概念

### 为什么需要代理？

1. **访问限制**：某些网站限制地区访问
2. **IP 封禁**：爬虫太频繁被封 IP
3. **隐藏身份**：不想暴露真实 IP
4. **负载均衡**：分散请求到不同 IP

### 代理类型

| 类型 | 说明 | 速度 |
|------|------|------|
| HTTP 代理 | 仅代理 HTTP | 中 |
| HTTPS 代理 | 代理 HTTPS | 中 |
| SOCKS4/5 代理 | 通用代理 | 慢 |
| 透明代理 | 服务器知道你在用代理 | - |
| 匿名代理 | 服务器不知道 | - |
| 高匿代理 | 服务器认为你是普通用户 | - |

### 代理来源

- **免费代理**：质量差、不稳定
- **付费代理**：
  - 隧道代理：每次请求换 IP（如 阿布云、快代理）
  - 包时代理：固定 IP（如 蘑菇代理）
- **自建代理**：VPS 上搭建（推荐）
""",

"proxy_use": """\
## 在 Python 中使用代理

### requests 设置代理

```python
import requests

proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}

r = requests.get("https://example.com", proxies=proxies)
```

### 带认证的代理

```python
proxies = {
    "http": "http://user:password@10.10.1.10:3128",
    "https": "http://user:password@10.10.1.10:1080",
}
r = requests.get("https://example.com", proxies=proxies)
```

### SOCKS 代理

```bash
pip install requests[socks]
```

```python
proxies = {
    "http": "socks5://user:pass@127.0.0.1:1080",
    "https": "socks5://user:pass@127.0.0.1:1080",
}
```

### 代理池

```python
import random
import requests

class ProxyPool:
    def __init__(self, proxies):
        self.proxies = proxies    # list of proxy dicts

    def get_random(self):
        return random.choice(self.proxies)

PROXIES = [
    {"http": "http://1.1.1.1:8080", "https": "http://1.1.1.1:8080"},
    {"http": "http://2.2.2.2:8080", "https": "http://2.2.2.2:8080"},
]

pool = ProxyPool(PROXIES)

for url in urls:
    try:
        r = requests.get(url, proxies=pool.get_random(), timeout=5)
        process(r)
    except requests.exceptions.ProxyError:
        continue    # 换下一个
```

### 自建代理池思路

```python
# 1. 爬取免费代理
# 2. 验证可用性
def validate_proxy(proxy):
    try:
        r = requests.get("https://httpbin.org/ip", proxies=proxy, timeout=5)
        return r.status_code == 200
    except:
        return False

# 3. 定期更新（每 5-10 分钟）
# 4. 按速度/匿名度评分
# 5. 优先用高质量代理
```
""",

# 案例
"netease_image": """\
## 案例：网易云单张图片爬取

```python
import requests
from bs4 import BeautifulSoup
import re

def download_netease_image(song_id):
    """根据歌曲 ID 下载封面"""
    url = f"https://music.163.com/song?id={song_id}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Referer": "https://music.163.com/",
    }

    r = requests.get(url, headers=headers)
    r.encoding = "utf-8"

    # 用正则提取图片 URL
    match = re.search(r'<img src="([^"]+)" class="j-img"', r.text)
    if match:
        img_url = match.group(1)
        # 下载图片
        img_data = requests.get(img_url, headers=headers).content
        with open(f"cover_{song_id}.jpg", "wb") as f:
            f.write(img_data)
        print(f"Downloaded: cover_{song_id}.jpg")
    else:
        print("未找到封面")

download_netease_image(1234567)
```

## 难点：网易云反爬

```python
# 网易云用 iframe，需要切换 iframe 才能拿到完整内容
import requests
from selenium import webdriver

# 方案 A：直接用 API（推荐）
api_url = f"https://music.163.com/api/song/detail?id={song_id}&ids=%5B{song_id}%5D"
r = requests.get(api_url, headers={"User-Agent": "Mozilla/5.0"})
data = r.json()
cover_url = data["songs"][0]["album"]["picUrl"]

# 下载
r = requests.get(cover_url)
with open("cover.jpg", "wb") as f:
    f.write(r.content)

# 方案 B：用 Selenium
driver = webdriver.Chrome()
driver.get(f"https://music.163.com/song?id={song_id}")
time.sleep(2)
img = driver.find_element(By.CSS_SELECTOR, ".j-img")
img.screenshot("cover.png")
driver.quit()
```
""",

"netease_song": """\
## 案例：网易云单首歌曲下载

```python
import requests
from Crypto.Cipher import AES
import base64
import json

def encrypted_request(params):
    """网易云加密请求（需要 AES）"""
    # 加密参数
    # 详见：https://github.com/geneasy/netease-cloud-music-api
    pass

def get_song_url(song_id):
    """获取歌曲播放 URL"""
    # 网易云外链 API
    url = f"https://music.163.com/song/media/outer/url?id={song_id}.mp3"
    headers = {
        "User-Agent": "Mozilla/5.0 ...",
        "Referer": "https://music.163.com/",
    }

    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 302:
        real_url = r.headers["Location"]
        return real_url
    return None

def download_song(song_id):
    song_url = get_song_url(song_id)
    if song_url:
        r = requests.get(song_url, stream=True)
        with open(f"song_{song_id}.mp3", "wb") as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)
        print(f"Downloaded: song_{song_id}.mp3")
    else:
        print("歌曲不可用（VIP/无版权）")

download_song(1234567)
```

## 难点：VIP 歌曲

```python
# VIP 歌曲需要登录 + VIP 账号的 Cookie
# 或用第三方工具：YouTube Music、Spotify
```
""",

"netease_mv": """\
## 案例：网易云 MV 下载

```python
import requests
import re

def get_mv_url(mv_id):
    """获取 MV 播放 URL"""
    # 网易云 MV API
    api = f"https://music.163.com/mv?id={mv_id}"

    headers = {
        "User-Agent": "Mozilla/5.0 ...",
        "Referer": "https://music.163.com/",
    }

    r = requests.get(api, headers=headers)

    # 从页面源码提取
    match = re.search(r'"url":\s*"([^"]+)"', r.text)
    if match:
        return match.group(1).replace("\\\\/", "/")
    return None

def download_mv(mv_id):
    url = get_mv_url(mv_id)
    if url:
        r = requests.get(url, stream=True)
        filename = f"mv_{mv_id}.mp4"
        with open(filename, "wb") as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)
        print(f"Downloaded: {filename}")

download_mv(12345)
```

## 用 ffmpeg 下载高清版本

```bash
# 安装 ffmpeg
# Mac: brew install ffmpeg
# Linux: apt install ffmpeg
# Windows: https://ffmpeg.org/download.html

# 提取音频
ffmpeg -i mv_12345.mp4 -vn -c:a mp3 song.mp3
```
""",

"tieba_single": """\
## 案例：贴吧单页爬取

```python
import requests

def scrape_tieba_page(tieba_name, page=1):
    """抓取单个贴吧单页帖子"""
    url = f"https://tieba.baidu.com/f?kw={tieba_name}&pn={page}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Cookie": "BAIDUID=xxx; TIEBA_USERTYPE=xxx",
    }

    r = requests.get(url, headers=headers)
    r.encoding = "utf-8"
    return r.text

# 解析
from bs4 import BeautifulSoup
html = scrape_tieba_page("python")
soup = BeautifulSoup(html, "lxml")

threads = []
for item in soup.select(".threadlist_title"):
    title = item.get_text().strip()
    link = item["href"]
    threads.append({"title": title, "link": f"https://tieba.baidu.com{link}"})

for t in threads[:10]:
    print(t["title"], "->", t["link"])
```

## 贴吧 API

```python
# 贴吧开放 API（需登录）
import requests

def get_tieba_threads(tieba_name, page=1, page_size=30):
    """通过 API 获取帖子列表"""
    url = "https://tieba.baidu.com/f/fdir"
    params = {
        "fd": tieba_name,
        "word": tieba_name,
        "page": page,
        "rn": page_size,
    }

    r = requests.get(url, params=params)
    return r.json()
```
""",

"tieba_paging": """\
## 案例：贴吧翻页爬取

```python
import requests
from bs4 import BeautifulSoup
import time

def scrape_tieba_all_pages(tieba_name, start=1, end=10, delay=2):
    """翻页爬取"""
    all_threads = []

    for page in range(start, end + 1):
        url = f"https://tieba.baidu.com/f?kw={tieba_name}&pn={(page-1)*50}"
        headers = {
            "User-Agent": "Mozilla/5.0 ...",
            "Cookie": "BAIDUID=xxx",
        }

        try:
            r = requests.get(url, headers=headers, timeout=10)
            r.encoding = "utf-8"
            soup = BeautifulSoup(r.text, "lxml")

            for item in soup.select(".threadlist_title"):
                title = item.get_text().strip()
                link = item["href"]
                all_threads.append({
                    "page": page,
                    "title": title,
                    "link": f"https://tieba.baidu.com{link}",
                })

            print(f"Page {page}: got {len(soup.select('.threadlist_title'))} threads")
        except Exception as e:
            print(f"Page {page} failed: {e}")
            continue

        # 控制频率
        time.sleep(delay)

    return all_threads

threads = scrape_tieba_all_pages("python", 1, 5, delay=2)
print(f"Total: {len(threads)}")
```
""",

# 进阶 OOP 爬虫
"oop_crawler": """\
## 案例：OOP 改写爬虫（继承 + 封装）

```python
import requests
from bs4 import BeautifulSoup
import time

class BaseCrawler:
    """爬虫基类"""
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(headers or {
            "User-Agent": "Mozilla/5.0 ..."
        })
        self.results = []

    def fetch(self, url, **kwargs):
        """获取页面"""
        response = self.session.get(url, timeout=10, **kwargs)
        response.encoding = "utf-8"
        return response

    def parse(self, html):
        """解析页面（子类实现）"""
        raise NotImplementedError

    def save(self, data, filename):
        """保存数据"""
        import json
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def run(self, **kwargs):
        """主流程（模板方法）"""
        for url in self.urls(**kwargs):
            html = self.fetch(url).text
            items = self.parse(html)
            self.results.extend(items)
            time.sleep(1)
        self.save(self.results, "result.json")
        return self.results


class TiebaCrawler(BaseCrawler):
    """贴吧爬虫"""
    def __init__(self, tieba_name):
        super().__init__(f"https://tieba.baidu.com/f?kw={tieba_name}")
        self.tieba_name = tieba_name

    def urls(self, start=1, end=5):
        """生成 URL"""
        for page in range(start, end + 1):
            yield f"https://tieba.baidu.com/f?kw={self.tieba_name}&pn={(page-1)*50}"

    def parse(self, html):
        """解析帖子列表"""
        soup = BeautifulSoup(html, "lxml")
        items = []
        for tag in soup.select(".threadlist_title"):
            items.append({
                "title": tag.get_text().strip(),
                "link": f"https://tieba.baidu.com{tag['href']}",
            })
        return items


class GitHubRepoCrawler(BaseCrawler):
    """GitHub 仓库爬虫"""
    def urls(self, language="python", sort="stars"):
        """GitHub 搜索 API"""
        return [f"https://api.github.com/search/repositories?q=language:{language}&sort={sort}"]

    def parse(self, html):
        """解析 JSON"""
        import json
        data = json.loads(html)
        items = []
        for repo in data["items"]:
            items.append({
                "name": repo["full_name"],
                "stars": repo["stargazers_count"],
                "url": repo["html_url"],
            })
        return items


# 使用
crawler = TiebaCrawler("python")
results = crawler.run(start=1, end=3)
print(f"抓取了 {len(results)} 条")
```

## 优势

1. **复用**：基类提供 fetch/save/run，子类只实现 parse
2. **可扩展**：加新的爬虫只需继承
3. **易维护**：修改一处生效所有子类
""",

"kingsoft_translate": """\
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
""",

"oop_crawler": """\
## 案例：OOP 改写翻页爬虫（继承 + 封装）

```python
import requests
from bs4 import BeautifulSoup
import time

class BaseCrawler:
    """爬虫基类"""
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(headers or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        self.results = []

    def fetch(self, url, **kwargs):
        response = self.session.get(url, timeout=10, **kwargs)
        response.encoding = "utf-8"
        return response

    def parse(self, html):
        raise NotImplementedError

    def save(self, data, filename):
        import json
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def run(self, **kwargs):
        for url in self.urls(**kwargs):
            html = self.fetch(url).text
            items = self.parse(html)
            self.results.extend(items)
            time.sleep(1)
        self.save(self.results, "result.json")
        return self.results


class TiebaCrawler(BaseCrawler):
    def __init__(self, tieba_name):
        super().__init__(f"https://tieba.baidu.com/f?kw={tieba_name}")
        self.tieba_name = tieba_name

    def urls(self, start=1, end=5):
        for page in range(start, end + 1):
            yield f"https://tieba.baidu.com/f?kw={self.tieba_name}&pn={(page-1)*50}"

    def parse(self, html):
        soup = BeautifulSoup(html, "lxml")
        items = []
        for tag in soup.select(".threadlist_title"):
            items.append({
                "title": tag.get_text().strip(),
                "link": f"https://tieba.baidu.com{tag['href']}",
            })
        return items


# 用
crawler = TiebaCrawler("python")
results = crawler.run(start=1, end=3)
print(f"抓取了 {len(results)} 条")
```

## 模板方法模式

`BaseCrawler.run` 是 **模板方法**：定义算法骨架，子类实现具体步骤。
""",

}


}