---
title: P054-网络爬虫-【网络爬虫】Scrapy框架入门-学习计划
created: 2026-06-24
updated: 2026-06-24
type: permanent
tags: [python, 网络爬虫, Scrapy]
summary: 掌握Scrapy框架的核心组件与爬虫开发流程
---

# P054 - 网络爬虫：Scrapy 框架入门

## 本节知识点总览

| 知识点 | 难度 | 重要度 | 课本定位 |
|--------|------|--------|----------|
| Scrapy 架构 | ⭐⭐⭐ | ⭐⭐⭐ | L3655-L3690 |
| Spider 编写 | ⭐⭐ | ⭐⭐⭐ | L3695-L3730 |
| Item Pipeline | ⭐⭐ | ⭐⭐ | L3735-L3770 |
| 中间件 | ⭐⭐⭐ | ⭐⭐ | L3775-L3810 |

---

## 一、Scrapy 简介

### 1.1 为什么使用 Scrapy

```bash
# 安装 Scrapy
pip install scrapy

# 或使用 conda
conda install -c conda-forge scrapy
```

| 对比项 | requests + BeautifulSoup | Scrapy |
|--------|---------------------------|--------|
| 学习曲线 | 简单 | 较陡 |
| 功能完整性 | 需要自己实现很多功能 | 开箱即用 |
| 性能 | 一般 | 高 |
| 扩展性 | 一般 | 强 |
| 适用场景 | 小规模爬虫 | 大规模爬虫 |

### 1.2 Scrapy 架构

```
Scrapy 架构
├── Spiders（爬虫）
│   └── 定义如何抓取网站
├── Engine（引擎）
│   └── 核心，控制数据流
├── Scheduler（调度器）
│   └── 存储待抓取 URL
├── Downloader（下载器）
│   └── 下载网页
├── Item Pipeline（管道）
│   └── 处理抓取的数据
└── Downloader Middleware（下载中间件）
    └── 处理请求/响应
```

---

## 二、创建项目

### 2.1 命令行创建

```bash
# 创建新项目
scrapy startproject myproject

# 查看项目结构
cd myproject
ls -la

# 创建爬虫
scrapy genspider example example.com
```

### 2.2 项目结构

```
myproject/
├── myproject/
│   ├── __init__.py
│   ├── items.py          # 定义数据结构
│   ├── middlewares.py     # 中间件
│   ├── pipelines.py       # 数据处理管道
│   ├── settings.py        # 配置文件
│   └── spiders/
│       └── __init__.py
└── scrapy.cfg            # 项目配置
```

---

## 三、编写 Spider

### 3.1 基本 Spider

```python
import scrapy

class ExampleSpider(scrapy.Spider):
    name = "example"  # 爬虫名称，唯一
    allowed_domains = ["example.com"]  # 允许的域名
    start_urls = [
        "https://www.example.com/page/1",
        "https://www.example.com/page/2",
    ]
    
    def parse(self, response):
        """解析页面"""
        # response 是 Scrapy 的响应对象
        # 可以使用 CSS 或 XPath 选择器
        
        # 提取所有文章标题
        titles = response.css("h2.article-title::text").getall()
        
        for title in titles:
            yield {
                "title": title.strip(),
            }
        
        # 提取下一页链接
        next_page = response.css("a.next-page::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
```

### 3.2 Item 定义

```python
# items.py
import scrapy

class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    publish_date = scrapy.Field()
    content = scrapy.Field()
    tags = scrapy.Field()
```

```python
# 使用 Item
from myproject.items import ArticleItem

class ArticleSpider(scrapy.Spider):
    name = "article"
    
    def parse(self, response):
        item = ArticleItem()
        item["title"] = response.css("h1.title::text").get()
        item["url"] = response.url
        item["author"] = response.css("span.author::text").get()
        item["publish_date"] = response.css("time.date::attr(datetime)").get()
        yield item
```

---

## 四、CSS 与 XPath 选择器

### 4.1 CSS 选择器

```python
# 基本 CSS 选择器
response.css("title::text").get()           # 获取文本
response.css("a::attr(href)").get()         # 获取属性
response.css("div.content").get()           # 获取元素
response.css("div.content p").getall()     # 获取所有子元素

# 伪类
response.css("li:first-child::text").get()
response.css("li:nth-child(2)::text").get()

# 类选择器
response.css(".article-title").get()
response.css("div#content").get()
```

### 4.2 XPath 选择器

```python
# 基本 XPath
response.xpath("//title/text()").get()
response.xpath("//a/@href").get()
response.xpath("//div[@class='content']").get()

# 条件选择
response.xpath("//div[@id='main']//p[@class='intro']").get()

# 函数
response.xpath("string(//div[@class='content'])").get()  # 获取所有文本
response.xpath("//a[contains(@href, 'example')]/@href").get()  # 包含文本

# 位置选择
response.xpath("//li[position() <= 5]/text()").getall()
```

### 4.3 选择器链

```python
# 链接到下一页并继续爬取
next_page = response.css("a.next::attr(href)").get()
if next_page:
    yield response.follow(next_page, self.parse)

# 使用 Link 对象
for href in response.css("a.article-link::attr(href)").getall():
    yield response.follow(href, self.parse_article)

# 处理相对 URL
yield response.follow(url, callback, meta={"key": "value"})
```

---

## 五、Item Pipeline

### 5.1 自定义 Pipeline

```python
# pipelines.py
class ArticlePipeline:
    """文章处理管道"""
    
    def open_spider(self, spider):
        """爬虫启动时调用"""
        self.file = open("articles.json", "w", encoding="utf-8")
    
    def process_item(self, item, spider):
        """处理每个 Item"""
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    
    def close_spider(self, spider):
        """爬虫关闭时调用"""
        self.file.close()
```

```python
# pipelines.py - 验证数据
class ValidationPipeline:
    def process_item(self, item, spider):
        if not item.get("title"):
            raise DropItem("缺少标题")
        if not item.get("url"):
            raise DropItem("缺少 URL")
        return item
```

### 5.2 启用 Pipeline

```python
# settings.py
ITEM_PIPELINES = {
    "myproject.pipelines.ValidationPipeline": 100,
    "myproject.pipelines.ArticlePipeline": 200,
}
```

---

## 六、Settings 配置

### 6.1 常用配置

```python
# settings.py

# 爬虫名称
BOT_NAME = "myproject"

# 并发请求数
CONCURRENT_REQUESTS = 16

# 下载延迟（秒）
DOWNLOAD_DELAY = 0.5

# 单域名并发
CONCURRENT_REQUESTS_PER_DOMAIN = 8

# 用户代理
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

# 请求头
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

# 启用 Cookie
COOKIES_ENABLED = False

# 禁用 robots.txt
ROBOTSTXT_OBEY = False

# 启用缓存
HTTPCACHE_ENABLED = True
```

### 6.2 代理配置

```python
# settings.py
DOWNLOADER_MIDDLEWARES = {
    "myproject.middlewares.ProxyMiddleware": 100,
}

# middlewares.py
class ProxyMiddleware:
    def process_request(self, request, spider):
        request.meta["proxy"] = "http://username:password@proxy.example.com:8080"
```

---

## 七、命令行工具

### 7.1 常用命令

```bash
# 查看可用命令
scrapy

# 运行爬虫
scrapy crawl example
scrapy crawl example -o output.json     # 输出到 JSON
scrapy crawl example -o output.csv      # 输出到 CSV
scrapy crawl example -o output.jl      # 输出到 JSON Lines

# 查看爬虫
scrapy list

# 检查爬虫
scrapy check

# shell 交互式调试
scrapy shell "https://example.com"

# 抓取页面
scrapy fetch "https://example.com"

# 查看响应
scrapy view "https://example.com"
```

### 7.2 Shell 调试

```bash
scrapy shell "https://example.com"

# 在 shell 中
response.css("title::text").get()
response.xpath("//title/text()").get()
response.headers
response.status
```

---

## 八、实战案例

### 8.1 完整爬虫示例

```python
import scrapy
from myproject.items import ArticleItem

class ArticlesSpider(scrapy.Spider):
    name = "articles"
    allowed_domains = ["blog.example.com"]
    start_urls = ["https://blog.example.com"]
    
    def parse(self, response):
        # 提取文章链接
        article_links = response.css("h2.title > a::attr(href)").getall()
        for link in article_links:
            yield response.follow(link, self.parse_article)
        
        # 翻页
        next_page = response.css("a.next-page::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
    
    def parse_article(self, response):
        item = ArticleItem()
        item["title"] = response.css("h1.article-title::text").get()
        item["url"] = response.url
        item["author"] = response.css("span.author::text").get()
        item["publish_date"] = response.css("time::attr(datetime)").get()
        item["content"] = "".join(response.css("div.article-content p::text").getall())
        item["tags"] = response.css("ul.tags > li::text").getall()
        yield item
```

### 8.2 中间件示例

```python
# middlewares.py
class RandomUserAgentMiddleware:
    """随机用户代理"""
    
    def __init__(self):
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...",
            "Mozilla/5.0 (X11; Linux x86_64)...",
        ]
    
    def process_request(self, request, spider):
        request.headers["User-Agent"] = random.choice(self.user_agents)
```

---

## 九、课本重点标注

**《Python编程：从入门到实践》第3版 核心段落：**

| 章节 | 页码 | 重点内容 |
|------|------|----------|
| 13.1 | ~295 | Scrapy 简介 |
| 13.2 | ~300 | 创建项目 |
| 13.3 | ~305 | 编写爬虫 |

---

## 十、易错点与避坑指南

1. **startproject 必须在项目目录下运行**
2. **allowed_domains 限制爬虫范围**
3. **parse 方法必须 yield Item 或 Request**
4. **Middleware 顺序很重要**
5. **注意 robots.txt 协议**

---

## 十一、学习成果检验

- [ ] 理解 Scrapy 架构
- [ ] 能创建和管理 Scrapy 项目
- [ ] 掌握 Spider 的编写方法
- [ ] 能使用 CSS 和 XPath 选择器
- [ ] 理解 Item Pipeline 的作用
- [ ] 能配置中间件
- [ ] 能使用命令行工具调试爬虫
