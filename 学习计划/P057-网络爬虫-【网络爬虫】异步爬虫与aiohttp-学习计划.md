---
title: P057-网络爬虫-【网络爬虫】异步爬虫与aiohttp-学习计划
created: 2026-06-24
updated: 2026-06-24
type: permanent
tags: [python, 网络爬虫, aiohttp, 异步]
summary: 掌握Python异步编程与aiohttp实现高性能异步爬虫
---

# P057 - 网络爬虫：异步爬虫与 aiohttp

## 本节知识点总览

| 知识点 | 难度 | 重要度 | 课本定位 |
|--------|------|--------|----------|
| asyncio 基础 | ⭐⭐ | ⭐⭐⭐ | L4115-L4150 |
| aiohttp 客户端 | ⭐⭐ | ⭐⭐⭐ | L4155-L4190 |
| 异步爬虫架构 | ⭐⭐⭐ | ⭐⭐ | L4195-L4230 |
| 速率控制 | ⭐⭐ | ⭐⭐ | L4235-L4270 |

---

## 一、asyncio 基础

### 1.1 同步 vs 异步

```python
# 同步执行：串行，耗时
import time

def sync_task(url):
    response = requests.get(url)  # 阻塞
    return response.text

def main_sync(urls):
    start = time.time()
    results = []
    for url in urls:
        results.append(sync_task(url))
    print(f"同步耗时: {time.time() - start:.2f}s")
    return results
```

### 1.2 async/await 语法

```python
import asyncio

async def hello():
    """异步函数"""
    print("Hello")
    await asyncio.sleep(1)  # 异步等待，不阻塞
    print("World")

# 运行异步函数
asyncio.run(hello())

# 等价于
loop = asyncio.new_event_loop()
loop.run_until_complete(hello())
loop.close()
```

### 1.3 事件循环

```python
async def task1():
    print("Task 1 开始")
    await asyncio.sleep(1)
    print("Task 1 结束")

async def task2():
    print("Task 2 开始")
    await asyncio.sleep(1)
    print("Task 2 结束")

async def main():
    # 并发执行
    await asyncio.gather(task1(), task2())

asyncio.run(main())
# 两个任务几乎同时开始，耗时约 1 秒
# 如果串行执行需要 2 秒
```

---

## 二、aiohttp 客户端

### 2.1 基本使用

```bash
pip install aiohttp
```

```python
import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "https://example.com")
        print(f"获取到 {len(html)} 字节")

asyncio.run(main())
```

### 2.2 Session 管理

```python
import aiohttp

async def main():
    # 创建 Session
    async with aiohttp.ClientSession() as session:
        # 多个请求复用同一个 Session
        tasks = [
            fetch(session, f"https://example.com/page{i}")
            for i in range(10)
        ]
        
        # 并发执行所有请求
        results = await asyncio.gather(*tasks)
        
        for result in results:
            print(len(result))
```

### 2.3 请求参数

```python
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        # GET 请求
        async with session.get(
            "https://api.example.com/data",
            params={"key": "value", "page": 1},
            headers={"Authorization": "Bearer token"}
        ) as response:
            data = await response.json()
        
        # POST 请求
        async with session.post(
            "https://api.example.com/submit",
            json={"name": "test", "value": 123}
        ) as response:
            result = await response.json()
        
        # 带超时
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as response:
            return await response.text()
```

---

## 三、异步爬虫实战

### 3.1 并发爬取

```python
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import time

class AsyncCrawler:
    def __init__(self, concurrency=10):
        self.concurrency = concurrency
        self.session = None
        self.semaphore = None
    
    async def fetch(self, url):
        async with self.semaphore:  # 限流
            async with self.session.get(url) as response:
                return await response.text()
    
    async def parse(self, html):
        soup = BeautifulSoup(html, "lxml")
        titles = soup.find_all("h2", class_="title")
        return [t.text.strip() for t in titles]
    
    async def crawl(self, urls):
        self.semaphore = asyncio.Semaphore(self.concurrency)
        
        async with aiohttp.ClientSession() as session:
            self.session = session
            
            tasks = []
            for url in urls:
                task = self.fetch(url)
                tasks.append(task)
            
            # 并发执行
            htmls = await asyncio.gather(*tasks)
            
            # 解析结果
            all_titles = []
            for html in htmls:
                titles = await self.parse(html)
                all_titles.extend(titles)
            
            return all_titles

# 使用
async def main():
    crawler = AsyncCrawler(concurrency=10)
    urls = [f"https://example.com/page{i}" for i in range(100)]
    
    start = time.time()
    titles = await crawler.crawl(urls)
    print(f"耗时: {time.time() - start:.2f}s")
    print(f"获取 {len(titles)} 条标题")

asyncio.run(main())
```

### 3.2 速率控制

```python
import asyncio
import aiohttp
from dataclasses import dataclass
import time

@dataclass
class RateLimiter:
    """令牌桶限流器"""
    rate: float  # 每秒请求数
    burst: int   # 突发容量
    
    def __post_init__(self):
        self.tokens = self.burst
        self.last_update = time.time()
        self.lock = asyncio.Lock()
    
    async def acquire(self):
        async with self.lock:
            now = time.time()
            elapsed = now - self.last_update
            self.tokens = min(self.burst, self.tokens + elapsed * self.rate)
            self.last_update = now
            
            if self.tokens >= 1:
                self.tokens -= 1
                return True
            else:
                wait_time = (1 - self.tokens) / self.rate
                await asyncio.sleep(wait_time)
                self.tokens = 0
                return True

async def main():
    limiter = RateLimiter(rate=10, burst=20)  # 每秒 10 请求
    
    async def limited_request(url):
        await limiter.acquire()
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()
    
    # 测试
    urls = [f"https://example.com/{i}" for i in range(50)]
    start = time.time()
    
    tasks = [limited_request(url) for url in urls]
    await asyncio.gather(*tasks)
    
    elapsed = time.time() - start
    print(f"50 请求耗时: {elapsed:.2f}s (预期 ~5s)")
```

### 3.3 重试机制

```python
import aiohttp
import asyncio

async def fetch_with_retry(session, url, max_retries=3, timeout=10):
    """带重试的请求"""
    for attempt in range(max_retries):
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=timeout)) as response:
                if response.status == 200:
                    return await response.text()
                elif response.status == 429:  # 请求过多，等待后重试
                    await asyncio.sleep(2 ** attempt)
                    continue
                else:
                    raise aiohttp.ClientError(f"HTTP {response.status}")
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            if attempt == max_retries - 1:
                raise
            await asyncio.sleep(2 ** attempt)
    
    return None
```

---

## 四、错误处理

### 4.1 异常捕获

```python
import aiohttp

async def safe_fetch(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                print(f"HTTP {response.status}: {url}")
                return None
    except aiohttp.ClientError as e:
        print(f"请求错误 {url}: {e}")
        return None
    except asyncio.TimeoutError:
        print(f"超时: {url}")
        return None
```

### 4.2 结果收集

```python
import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        
        async def safe_fetch_with_index(url, index):
            try:
                async with session.get(url) as response:
                    return (index, await response.text())
            except Exception as e:
                return (index, None)
        
        urls = [f"https://example.com/{i}" for i in range(100)]
        tasks = [safe_fetch_with_index(url, i) for i, url in enumerate(urls)]
        
        # gather 返回所有结果
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        success_count = sum(1 for r in results if not isinstance(r, Exception) and r[1])
        print(f"成功: {success_count}/100")
```

---

## 五、aiohttp 与 BeautifulSoup

### 5.1 解析 HTML

```python
import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def parse_page(session, url):
    async with session.get(url) as response:
        html = await response.text()
    
    soup = BeautifulSoup(html, "lxml")
    
    # 提取数据
    data = {
        "title": soup.find("h1", class_="title").text if soup.find("h1", class_="title") else None,
        "links": [a.get("href") for a in soup.find_all("a", href=True)],
        "items": []
    }
    
    for item in soup.select(".item"):
        data["items"].append({
            "text": item.text.strip(),
            "url": item.get("data-url")
        })
    
    return data
```

### 5.2 链接跟踪

```python
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urljoin

async def crawl_site(base_url, max_depth=2):
    visited = set()
    
    async def fetch_and_parse(session, url, depth):
        if depth > max_depth or url in visited:
            return []
        
        visited.add(url)
        new_urls = []
        
        try:
            async with session.get(url) as response:
                html = await response.text()
            
            soup = BeautifulSoup(html, "lxml")
            
            # 提取同域名链接
            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link["href"])
                if full_url.startswith(base_url) and full_url not in visited:
                    new_urls.append(full_url)
            
            return new_urls
        
        except Exception as e:
            print(f"Error crawling {url}: {e}")
            return []
    
    async with aiohttp.ClientSession() as session:
        urls_to_crawl = [base_url]
        
        for depth in range(max_depth + 1):
            tasks = [fetch_and_parse(session, url, depth) for url in urls_to_crawl]
            results = await asyncio.gather(*tasks)
            
            new_urls = []
            for r in results:
                new_urls.extend(r)
            
            urls_to_crawl = new_urls
    
    return visited
```

---

## 六、实战案例

### 6.1 图片批量下载

```python
import asyncio
import aiohttp
import os
from pathlib import Path

async def download_image(session, url, folder):
    filename = Path(url).name or f"{hash(url)}.jpg"
    filepath = Path(folder) / filename
    
    try:
        async with session.get(url) as response:
            if response.status == 200:
                content = await response.read()
                with open(filepath, "wb") as f:
                    f.write(content)
                return filename
    except Exception as e:
        print(f"下载失败 {url}: {e}")
    return None

async def download_all(image_urls, folder, concurrency=10):
    Path(folder).mkdir(parents=True, exist_ok=True)
    
    semaphore = asyncio.Semaphore(concurrency)
    
    async def limited_download(url):
        async with semaphore:
            return await download_image(session, url, folder)
    
    async with aiohttp.ClientSession() as session:
        tasks = [limited_download(url) for url in image_urls]
        results = await asyncio.gather(*tasks)
    
    return [r for r in results if r]
```

### 6.2 API 批量请求

```python
import asyncio
import aiohttp
import json

async def api_request(session, endpoint, params):
    url = f"https://api.example.com/{endpoint}"
    async with session.get(url, params=params) as response:
        if response.status == 200:
            return await response.json()
        return None

async def batch_api_requests(endpoints_params, concurrency=20):
    """批量 API 请求"""
    semaphore = asyncio.Semaphore(concurrency)
    
    async def limited_request(endpoint, params):
        async with semaphore:
            async with aiohttp.ClientSession() as session:
                return await api_request(session, endpoint, params)
    
    tasks = [limited_request(ep, params) for ep, params in endpoints_params]
    results = await asyncio.gather(*tasks)
    
    return results
```

---

## 七、注意事项

### 7.1 性能优化

```python
# ❌ 不好：每个请求创建新 Session
for url in urls:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            ...

# ✅ 好：复用 Session
async with aiohttp.ClientSession() as session:
    for url in urls:
        async with session.get(url) as response:
            ...
```

### 7.2 内存管理

```python
# 使用 Semaphore 控制并发，避免内存溢出
semaphore = asyncio.Semaphore(100)

async def bounded_task(url):
    async with semaphore:
        # 处理请求
        pass
```

---

## 八、课本重点标注

**《Python编程：从入门到实践》第3版 核心段落：**

| 章节 | 页码 | 重点内容 |
|------|------|----------|
| 16.1 | ~350 | 异步编程基础 |
| 16.2 | ~355 | aiohttp 客户端 |
| 16.3 | ~360 | 异步爬虫实战 |

---

## 九、易错点与避坑指南

1. **忘记 await**：异步函数必须使用 await
2. **Session 泄漏**：确保使用 `async with` 管理 Session
3. **并发过高**：设置 Semaphore 限制并发
4. **阻塞操作**：避免在异步函数中使用同步操作
5. **异常处理**：使用 try-except 处理网络异常

---

## 十、学习成果检验

- [ ] 理解同步与异步的区别
- [ ] 掌握 async/await 语法
- [ ] 能使用 aiohttp 发送请求
- [ ] 能实现并发爬取
- [ ] 掌握速率控制方法
- [ ] 能处理错误和重试
- [ ] 理解异步爬虫的性能优势
