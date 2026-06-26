---
title: P063-项目实战-【项目实战】Scrapy-redis分布式爬虫-学习计划
created: 2026-06-24
updated: 2026-06-24
type: permanent
tags: [python, 项目实战, Scrapy-Redis]
summary: 使用Scrapy-Redis构建企业级分布式爬虫系统
---

# P063 - 项目实战：Scrapy-Redis 分布式爬虫

## 本节知识点总览

| 知识点 | 难度 | 重要度 | 课本定位 |
|--------|------|--------|----------|
| Scrapy-Redis 架构 | ⭐⭐⭐ | ⭐⭐⭐ | L5045-L5080 |
| RedisPipeline | ⭐⭐ | ⭐⭐⭐ | L5085-L5120 |
| 分布式调度 | ⭐⭐ | ⭐⭐ | L5125-L5160 |
| 实战项目 | ⭐⭐⭐ | ⭐⭐ | L5165-L5200 |

---

## 一、Scrapy-Redis 简介

### 1.1 与 Scrapy 的区别

| 特性 | Scrapy | Scrapy-Redis |
|------|--------|--------------|
| 调度器 | 本机内存 | Redis |
| 去重 | 内存 | Redis Set |
| 请求队列 | 单机 | 分布式 |
| 断点续爬 | 不支持 | 支持 |
| 水平扩展 | 困难 | 简单 |

### 1.2 安装

```bash
pip install scrapy-redis
```

---

## 二、项目配置

### 2.1 settings.py 配置

```python
# settings.py

# ========== 调度器 ==========
# 使用 Redis 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 持久化调度器（断点续爬）
SCHEDULER_PERSIST = True

# 调度器队列类型
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"

# ========== 去重 ==========
# 使用 Redis 去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 去重键（指纹过期时间）
# DUPEFILTER_KEY = "%(spider)s:dupefilter"

# ========== Redis 连接 ==========
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = None

# 连接参数
REDIS_PARAMS = {
    "socket_timeout": 30,
    "socket_connect_timeout": 30,
}

# ========== 性能 ==========
# Redis 连接池
REDIS_START_URLS_AS_SET = False
REDIS_START_URLS_KEY = "%(spider)s:start_urls"

# 请求队列序列化
SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"

# ========== 爬虫配置 ==========
ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 16
DOWNLOAD_DELAY = 0.5
```

---

## 三、编写分布式爬虫

### 3.1 Spider 实现

```python
# myproject/spiders/distributed.py
import scrapy
from scrapy_redis.spiders import RedisSpider

class DistributedSpider(RedisSpider):
    """基于 Redis 的分布式爬虫"""
    
    name = "distributed_spider"
    redis_key = "distributed_spider:start_urls"
    
    # 可选：限制并发
    # CONCURRENT_REQUESTS_PER_DOMAIN = 8
    
    def parse(self, response):
        """解析页面"""
        # 提取数据
        items = []
        
        for article in response.css("div.article"):
            item = {
                "title": article.css("h2.title::text").get(),
                "url": article.css("a::attr(href)").get(),
                "author": article.css("span.author::text").get(),
                "publish_date": article.css("time::attr(datetime)").get(),
            }
            items.append(item)
            
            # 返回 Item（会自动提交给 Pipeline）
            yield item
        
        # 提取新 URL
        for href in response.css("a.next::attr(href)").getall():
            yield response.follow(href, self.parse)
    
    def parse_item(self, response):
        """解析详情页"""
        item = {
            "url": response.url,
            "title": response.css("h1.title::text").get(),
            "content": "".join(response.css("div.content p::text").getall()),
        }
        yield item
```

### 3.2 使用 start_urls

```python
# 也可以使用传统的 start_urls
class TraditionalSpider(scrapy.Spider):
    """传统方式 + Redis 调度"""
    
    name = "traditional_spider"
    start_urls = [
        "https://example.com/page1",
        "https://example.com/page2",
    ]
    
    def parse(self, response):
        # 解析逻辑
        pass
```

---

## 四、Redis 数据结构

### 4.1 键说明

| 键名 | 类型 | 说明 |
|------|------|------|
| `{spider}:items` | List | 已爬取的数据 |
| `{spider}:start_urls` | List/Set | 起始 URL |
| `{spider}:dupefilter` | Set | 已访问 URL 指纹 |
| `{spider}:requests` | List | 待爬请求队列 |

### 4.2 查看状态

```python
import redis

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

def get_spider_status(spider_name):
    """获取爬虫状态"""
    return {
        "待爬请求数": r.llen(f"{spider_name}:requests"),
        "已爬取数": r.llen(f"{spider_name}:items"),
        "去重指纹数": r.scard(f"{spider_name}:dupefilter"),
        "起始URL数": r.llen(f"{spider_name}:start_urls"),
    }

# 查看
print(get_spider_status("distributed_spider"))
```

---

## 五、添加起始 URL

### 5.1 命令行添加

```bash
# 方式一：使用 Redis CLI
redis-cli
LPUSH distributed_spider:start_urls "https://example.com/page1"
LPUSH distributed_spider:start_urls "https://example.com/page2"

# 方式二：使用 lpush
redis-cli LPUSH distributed_spider:start_urls '{"url": "https://example.com", "meta": {"key": "value"}}'
```

### 5.2 Python 添加

```python
import redis
import json

r = redis.Redis(host="localhost", port=6379, db=0)

def push_start_urls(spider_name, urls):
    """添加起始 URL"""
    for url in urls:
        r.lpush(f"{spider_name}:start_urls", url)

def push_start_urls_with_meta(spider_name, url_list):
    """添加带元数据的起始 URL"""
    for url, meta in url_list:
        data = json.dumps({"url": url, "meta": meta})
        r.lpush(f"{spider_name}:start_urls", data)

# 使用
push_start_urls("distributed_spider", [
    "https://example.com/category/1",
    "https://example.com/category/2",
])
```

### 5.3 动态添加

```python
# spider 中动态添加
class DynamicSpider(RedisSpider):
    name = "dynamic_spider"
    redis_key = "dynamic_spider:start_urls"
    
    def parse(self, response):
        # 解析当前页面
        items = self.parse_items(response)
        
        # 如果没有更多页，添加新的起始 URL
        if not items:
            new_urls = self.get_new_urls()
            for url in new_urls:
                self.server.lpush(self.redis_key, url)
        
        yield from items
    
    def get_new_urls(self):
        """获取新 URL（可以从数据库等来源）"""
        return []
```

---

## 六、Pipeline 配置

### 6.1 Redis Item Pipeline

```python
# pipelines.py
from scrapy_redis.pipelines import RedisPipeline

class MyRedisPipeline(RedisPipeline):
    """自定义 Redis Pipeline"""
    
    def item_key(self, item, spider):
        """定义 Item 存储的键"""
        return f"{spider.name}:items"
    
    def _process_item(self, item, spider):
        """处理 Item"""
        key = self.item_key(item, spider)
        data = self.serialize(item)
        self.server.rpush(key, data)
        return item
```

### 6.2 MongoDB Pipeline

```python
# pipelines.py
from pymongo import MongoClient

class MongoPipeline:
    """MongoDB Pipeline"""
    
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
        self.collection = self.db[spider.name]
    
    def process_item(self, item, spider):
        self.collection.update_one(
            {"url": item["url"]},
            {"$set": dict(item)},
            upsert=True
        )
        return item
    
    def close_spider(self, spider):
        self.client.close()
```

### 6.3 settings.py 配置

```python
ITEM_PIPELINES = {
    "myproject.pipelines.MongoPipeline": 300,
    "scrapy_redis.pipelines.RedisPipeline": 400,
}
```

---

## 七、部署与运行

### 7.1 Master 节点

```bash
# Master 节点运行（调度器 + 爬虫）
scrapy runspider myproject/spiders/distributed.py

# 或使用 scrapy crawl
scrapy crawl distributed_spider
```

### 7.2 Worker 节点

```bash
# Worker 节点只运行爬虫
scrapy runspider myproject/spiders/distributed.py

# 多个 Worker 进程
for i in {1..3}; do
    scrapy runspider myproject/spiders/distributed.py &
done
```

### 7.3 Docker Compose 部署

```yaml
version: '3.8'

services:
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
  
  master:
    build: .
    command: scrapy crawl distributed_spider
    depends_on:
      - redis
    environment:
      - REDIS_HOST=redis
      - REDIS_PORT=6379
  
  worker:
    build: .
    command: scrapy runspider myproject/spiders/distributed.py
    depends_on:
      - redis
    deploy:
      replicas: 3
    environment:
      - REDIS_HOST=redis
      - REDIS_PORT=6379
```

---

## 八、监控管理

### 8.1 管理脚本

```python
# manage.py
import redis
import json
from scrapy.utils.reqser import request_to_dict, request_from_dict

class RedisManager:
    """Redis 爬虫管理"""
    
    def __init__(self, spider_name, redis_host="localhost", redis_port=6379):
        self.spider_name = spider_name
        self.r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
    
    def get_stats(self):
        """获取统计信息"""
        return {
            "待爬请求": self.r.llen(f"{self.spider_name}:requests"),
            "已爬取": self.r.llen(f"{self.spider_name}:items"),
            "去重数": self.r.scard(f"{self.spider_name}:dupefilter"),
            "起始URL": self.r.llen(f"{self.spider_name}:start_urls"),
        }
    
    def clear_dupefilter(self):
        """清除去重指纹"""
        self.r.delete(f"{self.spider_name}:dupefilter")
    
    def clear_queue(self):
        """清除待爬队列"""
        self.r.delete(f"{self.spider_name}:requests")
    
    def view_requests(self, count=10):
        """查看待爬请求"""
        requests = self.r.lrange(f"{self.spider_name}:requests", 0, count - 1)
        return [json.loads(r) for r in requests]
    
    def view_items(self, count=10):
        """查看已爬取数据"""
        items = self.r.lrange(f"{self.spider_name}:items", -count, -1)
        return [json.loads(i) for i in items]

if __name__ == "__main__":
    manager = RedisManager("distributed_spider")
    
    while True:
        print("\n=== 分布式爬虫管理 ===")
        print("1. 查看状态")
        print("2. 清除去重")
        print("3. 清除队列")
        print("4. 查看请求")
        print("5. 查看数据")
        print("0. 退出")
        
        choice = input("选择: ")
        
        if choice == "1":
            print(manager.get_stats())
        elif choice == "2":
            manager.clear_dupefilter()
            print("去重已清除")
        elif choice == "3":
            manager.clear_queue()
            print("队列已清除")
        elif choice == "4":
            for req in manager.view_requests():
                print(req)
        elif choice == "5":
            for item in manager.view_items():
                print(item)
        elif choice == "0":
            break
```

---

## 九、课本重点标注

**《Python编程：从入门到实践》第3版 核心段落：**

| 章节 | 页码 | 重点内容 |
|------|------|----------|
| 22.1 | ~480 | Scrapy-Redis 架构 |
| 22.2 | ~485 | 分布式配置 |
| 22.3 | ~490 | 部署运行 |

---

## 十、易错点与避坑指南

1. **Redis 连接**：确保多节点能连接同一 Redis
2. **序列化问题**：Request 序列化需要 pickle
3. **去重冲突**：分布式环境下去重键要唯一
4. **队列阻塞**：使用 BRPOP 而不是 SPOP
5. **内存溢出**：定期清理 Redis 数据

---

## 十一、学习成果检验

- [ ] 理解 Scrapy-Redis 架构
- [ ] 能配置分布式爬虫
- [ ] 能编写 RedisSpider
- [ ] 掌握 Redis 数据结构
- [ ] 能添加和管理起始 URL
- [ ] 能部署多节点爬虫
- [ ] 能监控爬虫状态
