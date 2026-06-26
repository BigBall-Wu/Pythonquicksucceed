---
title: P055-网络爬虫-【网络爬虫】数据存储与MongoDB-学习计划
created: 2026-06-24
updated: 2026-06-24
type: permanent
tags: [python, 网络爬虫, MongoDB, 数据存储]
summary: 掌握将爬取数据存储到MongoDB数据库的方法与实践
---

# P055 - 网络爬虫：数据存储与 MongoDB

## 本节知识点总览

| 知识点 | 难度 | 重要度 | 课本定位 |
|--------|------|--------|----------|
| MongoDB 基础 | ⭐⭐ | ⭐⭐ | L3815-L3845 |
| PyMongo 使用 | ⭐⭐ | ⭐⭐⭐ | L3850-L3885 |
| Scrapy + MongoDB | ⭐⭐ | ⭐⭐ | L3890-L3925 |
| 数据去重 | ⭐⭐ | ⭐⭐ | L3930-L3965 |

---

## 一、MongoDB 基础

### 1.1 简介

MongoDB 是一个基于文档的 NoSQL 数据库，数据以 BSON（二进制 JSON）格式存储。

```bash
# 安装 MongoDB（Windows）
# 下载并安装 MongoDB Community Server

# 安装 PyMongo
pip install pymongo
```

### 1.2 基本概念

| SQL 概念 | MongoDB 概念 |
|----------|-------------|
| Database | Database |
| Table | Collection |
| Row | Document |
| Column | Field |
| Primary Key | _id (自动生成) |

### 1.3 启动 MongoDB

```bash
# Windows 服务启动
net start MongoDB

# 命令行启动
mongod --dbpath "C:\data\db"

# 连接 MongoDB
mongo
```

---

## 二、PyMongo 基础

### 2.1 连接数据库

```python
from pymongo import MongoClient

# 连接 MongoDB
client = MongoClient("mongodb://localhost:27017/")

# 选择数据库
db = client["crawler_db"]

# 或使用属性访问
db = client.crawler_db

# 测试连接
print(client.server_info())
```

### 2.2 插入数据

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.crawler_db
collection = db.articles

# 插入单条文档
article = {
    "title": "Python 教程",
    "url": "https://example.com/python",
    "author": "张三",
    "tags": ["Python", "编程"],
    "views": 1000,
    "published": True
}

result = collection.insert_one(article)
print(f"插入 ID：{result.inserted_id}")

# 插入多条文档
articles = [
    {"title": "JavaScript 教程", "url": "https://example.com/js"},
    {"title": "Java 教程", "url": "https://example.com/java"},
    {"title": "Go 教程", "url": "https://example.com/go"},
]

result = collection.insert_many(articles)
print(f"插入 IDs：{result.inserted_ids}")
```

### 2.3 查询数据

```python
# 查询单条
article = collection.find_one({"title": "Python 教程"})
print(article)

# 条件查询
articles = collection.find({"author": "张三"})
for article in articles:
    print(article)

# 比较运算符
articles = collection.find({"views": {"$gte": 1000}})
articles = collection.find({"tags": {"$in": ["Python", "Java"]}})

# 逻辑运算符
articles = collection.find({
    "$and": [
        {"views": {"$gte": 100}},
        {"published": True}
    ]
})
```

### 2.4 更新数据

```python
# 更新单条
result = collection.update_one(
    {"title": "Python 教程"},
    {"$set": {"views": 2000}}
)
print(f"更新数量：{result.modified_count}")

# 更新多条
result = collection.update_many(
    {"author": "张三"},
    {"$inc": {"views": 100}}  # 增加 100
)

# upsert：不存在则插入
collection.update_one(
    {"url": "https://example.com/new"},
    {"$set": {"title": "新文章", "url": "https://example.com/new"}},
    upsert=True
)
```

### 2.5 删除数据

```python
# 删除单条
result = collection.delete_one({"title": "删除的文章"})

# 删除多条
result = collection.delete_many({"author": "待删除作者"})

# 删除集合
collection.drop()
```

---

## 三、Scrapy + MongoDB

### 3.1 Pipeline 实现

```python
# pipelines.py
from pymongo import MongoClient

class MongoPipeline:
    """MongoDB 数据存储管道"""
    
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DB")
        )
    
    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    
    def process_item(self, item, spider):
        collection = self.db[spider.name]
        collection.insert_one(dict(item))
        return item
    
    def close_spider(self, spider):
        self.client.close()
```

### 3.2 Settings 配置

```python
# settings.py

MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB = "crawler_db"

ITEM_PIPELINES = {
    "myproject.pipelines.MongoPipeline": 300,
}
```

### 3.3 完整示例

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
    crawled_at = scrapy.Field()

# pipelines.py
from datetime import datetime

class MongoPipeline:
    def __init__(self, mongo_uri, mongo_db):
        self.client = None
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DB")
        )
    
    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
    
    def process_item(self, item, spider):
        item["crawled_at"] = datetime.now()
        self.db.articles.update_one(
            {"url": item["url"]},
            {"$set": dict(item)},
            upsert=True
        )
        return item
    
    def close_spider(self, spider):
        if self.client:
            self.client.close()
```

---

## 四、数据去重

### 4.1 URL 去重

```python
class DuplicateFilterPipeline:
    """基于 URL 的去重管道"""
    
    def __init__(self):
        self.seen_urls = set()
    
    def process_item(self, item, spider):
        if item.get("url") in self.seen_urls:
            raise DropItem("重复的 URL: %s" % item["url"])
        self.seen_urls.add(item["url"])
        return item
```

### 4.2 MongoDB 去重

```python
# 使用 upsert 去重
self.db.articles.update_one(
    {"url": item["url"]},           # 查询条件
    {"$setOnInsert": dict(item)},   # 只在插入时设置
    upsert=True                      # 不存在则插入
)

# 使用 $set 更新部分字段
self.db.articles.update_one(
    {"url": item["url"]},
    {
        "$set": {"crawled_at": datetime.now()},
        "$setOnInsert": dict(item)
    },
    upsert=True
)
```

### 4.3 增量更新

```python
class IncrementUpdatePipeline:
    """增量更新管道"""
    
    def process_item(self, item, spider):
        # 更新浏览量等增量字段
        self.db.articles.update_one(
            {"url": item["url"]},
            {
                "$set": {
                    "title": item.get("title"),
                    "views": item.get("views", 0)
                },
                "$inc": {"crawl_count": 1}  # 爬取次数 +1
            },
            upsert=True
        )
        return item
```

---

## 五、数据查询与分析

### 5.1 聚合查询

```python
from pymongo import MongoClient
from bson import Code

client = MongoClient("mongodb://localhost:27017/")
db = client.crawler_db

# 统计每个作者的文章数
result = db.articles.aggregate([
    {"$group": {"_id": "$author", "count": {"$sum": 1}}}
])

for r in result:
    print(f"{r['_id']}: {r['count']} 篇")

# 统计浏览量
result = db.articles.aggregate([
    {"$group": {"_id": None, "total_views": {"$sum": "$views"}}}
])

# 按日期分组
result = db.articles.aggregate([
    {"$group": {
        "_id": {"$dateToString": {"format": "%Y-%m", "date": "$crawled_at"}},
        "count": {"$sum": 1}
    }},
    {"$sort": {"_id": 1}}
])
```

### 5.2 索引

```python
# 创建索引
db.articles.create_index("url", unique=True)  # URL 唯一索引
db.articles.create_index("author")            # 作者索引
db.articles.create_index([("crawled_at", -1)])  # 按时间降序

# 查看索引
print(db.articles.index_information())

# 删除索引
db.articles.drop_index("url_1")
```

---

## 六、实战案例

### 6.1 新闻爬虫完整实现

```python
import scrapy
from datetime import datetime
from pymongo import MongoClient
from myproject.items import NewsItem

class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["news.example.com"]
    start_urls = ["https://news.example.com"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client.news_crawler
    
    def parse(self, response):
        # 提取新闻链接
        news_links = response.css("h2.news-title > a::attr(href)").getall()
        for link in news_links:
            yield response.follow(link, self.parse_news)
        
        # 翻页
        next_page = response.css("a.next-page::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)
    
    def parse_news(self, response):
        item = NewsItem()
        item["title"] = response.css("h1.title::text").get()
        item["url"] = response.url
        item["author"] = response.css("span.author::text").get()
        item["publish_date"] = response.css("time::attr(datetime)").get()
        item["content"] = "".join(response.css("div.content p::text").getall())
        item["source"] = "news.example.com"
        item["crawled_at"] = datetime.now()
        
        # 存储到 MongoDB
        self.db.news.update_one(
            {"url": item["url"]},
            {"$set": dict(item)},
            upsert=True
        )
        
        return item
```

### 6.2 数据导出

```python
import json
import csv
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.crawler_db

# 导出为 JSON
def export_to_json():
    articles = db.articles.find()
    with open("articles.json", "w", encoding="utf-8") as f:
        for article in articles:
            del article["_id"]  # 删除 ObjectId
            f.write(json.dumps(article, ensure_ascii=False) + "\n")

# 导出为 CSV
def export_to_csv():
    articles = db.articles.find()
    if not articles:
        return
    
    keys = ["title", "url", "author", "publish_date"]
    
    with open("articles.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
        writer.writeheader()
        for article in articles:
            writer.writerow(article)
```

---

## 七、注意事项

### 7.1 安全连接

```python
# 本地连接
client = MongoClient("mongodb://localhost:27017/")

# 认证连接
client = MongoClient(
    "mongodb://username:password@localhost:27017/",
    authSource="admin"
)

# TLS/SSL 连接
client = MongoClient(
    "mongodb://localhost:27017/",
    tls=True,
    tlsCertificateKeyFile="/path/to/cert.pem"
)
```

### 7.2 连接池

```python
# PyMongo 默认使用连接池
client = MongoClient(
    "mongodb://localhost:27017/",
    maxPoolSize=50,        # 最大连接数
    minPoolSize=10,         # 最小连接数
    maxIdleTimeMS=30000    # 空闲超时
)
```

---

## 八、课本重点标注

**《Python编程：从入门到实践》第3版 核心段落：**

| 章节 | 页码 | 重点内容 |
|------|------|----------|
| 14.1 | ~310 | 数据存储 |
| 14.2 | ~315 | MongoDB 基础 |
| 14.3 | ~320 | 与 Scrapy 集成 |

---

## 九、易错点与避坑指南

1. **ObjectId 无法序列化**：JSON 导出时需删除 `_id` 字段
2. **中文编码**：确保使用 UTF-8 编码
3. **连接关闭**：使用完记得关闭连接
4. **索引缺失**：大量数据查询需创建索引
5. **连接池配置**：高并发时注意连接池大小

---

## 十、学习成果检验

- [ ] 理解 MongoDB 基本概念
- [ ] 掌握 PyMongo 的增删改查操作
- [ ] 能将 Scrapy 与 MongoDB 集成
- [ ] 掌握数据去重方法
- [ ] 能进行数据聚合查询
- [ ] 能创建和管理索引
- [ ] 掌握数据导出方法
