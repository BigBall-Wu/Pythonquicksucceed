---
title: P067-项目实战-【项目实战】API开发与RESTful接口-学习计划
created: 2026-06-24
updated: 2026-06-24
type: permanent
tags: [python, 项目实战, API, RESTful]
summary: 使用Flask/FastAPI开发爬虫数据API服务
---

# P067 - 项目实战：API 开发与 RESTful 接口

## 本节知识点总览

| 知识点 | 难度 | 重要度 | 课本定位 |
|--------|------|--------|----------|
| RESTful 规范 | ⭐⭐ | ⭐⭐⭐ | L5685-L5720 |
| Flask 基础 | ⭐⭐ | ⭐⭐ | L5725-L5760 |
| FastAPI 入门 | ⭐⭐ | ⭐⭐ | L5765-L5800 |
| CRUD 实现 | ⭐⭐ | ⭐⭐ | L5805-L5840 |

---

## 一、RESTful 规范

### 1.1 REST 原则

| 原则 | 说明 |
|------|------|
| 资源 | 用 URL 表示资源 |
| 动词 | 用 HTTP 方法表示操作 |
| 无状态 | 每个请求包含所有信息 |
| 统一接口 | 标准化的接口设计 |

### 1.2 HTTP 方法

| 方法 | 操作 | 示例 |
|------|------|------|
| GET | 查询资源 | GET /articles |
| POST | 创建资源 | POST /articles |
| PUT | 更新资源 | PUT /articles/1 |
| DELETE | 删除资源 | DELETE /articles/1 |

### 1.3 URL 设计

```bash
# 好设计
GET    /articles              # 获取文章列表
GET    /articles/1            # 获取文章详情
POST   /articles              # 创建文章
PUT    /articles/1            # 更新文章
DELETE /articles/1            # 删除文章
GET    /articles?category=tech # 条件查询
GET    /articles?page=1&size=20  # 分页

# 不好设计
GET    /getArticles
POST   /createArticle
POST   /updateArticle
```

---

## 二、Flask 基础

### 2.1 第一个 API

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# 模拟数据
articles = [
    {"id": 1, "title": "文章1", "content": "内容1"},
    {"id": 2, "title": "文章2", "content": "内容2"},
]

@app.route("/")
def index():
    return jsonify({"message": "Welcome to API"})

@app.route("/api/articles", methods=["GET"])
def get_articles():
    return jsonify({"data": articles, "total": len(articles)})

@app.route("/api/articles/<int:article_id>", methods=["GET"])
def get_article(article_id):
    article = next((a for a in articles if a["id"] == article_id), None)
    if article:
        return jsonify({"data": article})
    return jsonify({"error": "Article not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
```

### 2.2 请求与响应

```python
from flask import request, jsonify

@app.route("/api/articles", methods=["POST"])
def create_article():
    # 获取 JSON 数据
    data = request.get_json()
    
    # 验证数据
    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400
    
    # 创建新文章
    new_article = {
        "id": max(a["id"] for a in articles) + 1,
        "title": data["title"],
        "content": data.get("content", "")
    }
    articles.append(new_article)
    
    return jsonify({"data": new_article, "message": "Created"}), 201

@app.route("/api/articles/<int:article_id>", methods=["PUT"])
def update_article(article_id):
    data = request.get_json()
    
    for article in articles:
        if article["id"] == article_id:
            article.update(data)
            return jsonify({"data": article})
    
    return jsonify({"error": "Article not found"}), 404

@app.route("/api/articles/<int:article_id>", methods=["DELETE"])
def delete_article(article_id):
    global articles
    articles = [a for a in articles if a["id"] != article_id]
    return jsonify({"message": "Deleted"})
```

---

## 三、FastAPI 基础

### 3.1 第一个 API

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

app = FastAPI(title="新闻 API", version="1.0.0")

# 数据模型
class Article(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    author: Optional[str] = ""
    category: Optional[str] = ""
    created_at: Optional[datetime] = None

# 模拟数据
articles_db = []

@app.get("/")
def read_root():
    return {"message": "Welcome to News API"}

@app.get("/articles", response_model=List[Article])
def get_articles(skip: int = 0, limit: int = 10):
    """获取文章列表"""
    return articles_db[skip:skip + limit]

@app.get("/articles/{article_id}", response_model=Article)
def get_article(article_id: int):
    """获取单个文章"""
    for article in articles_db:
        if article.id == article_id:
            return article
    return {"error": "Not found"}, 404

@app.post("/articles", response_model=Article)
def create_article(article: Article):
    """创建文章"""
    article.id = len(articles_db) + 1
    article.created_at = datetime.now()
    articles_db.append(article)
    return article

@app.put("/articles/{article_id}", response_model=Article)
def update_article(article_id: int, article: Article):
    """更新文章"""
    for i, a in enumerate(articles_db):
        if a.id == article_id:
            articles_db[i] = article
            article.id = article_id
            return article
    return {"error": "Not found"}, 404

@app.delete("/articles/{article_id}")
def delete_article(article_id: int):
    """删除文章"""
    global articles_db
    articles_db = [a for a in articles_db if a.id != article_id]
    return {"message": "Deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### 3.2 查询参数

```python
from fastapi import Query

@app.get("/articles")
def search_articles(
    keyword: Optional[str] = None,
    category: Optional[str] = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    sort_by: str = "created_at",
    order: str = "desc"
):
    """搜索文章"""
    results = articles_db
    
    # 过滤
    if keyword:
        results = [a for a in results if keyword in a.title or keyword in a.content]
    
    if category:
        results = [a for a in results if a.category == category]
    
    # 排序
    if order == "desc":
        results = sorted(results, key=lambda x: getattr(x, sort_by, ""), reverse=True)
    else:
        results = sorted(results, key=lambda x: getattr(x, sort_by, ""))
    
    # 分页
    total = len(results)
    start = (page - 1) * page_size
    end = start + page_size
    
    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "data": results[start:end]
    }
```

---

## 四、数据库集成

### 4.1 MongoDB 集成

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

# MongoDB 连接
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["news_api"]

class ArticleIn(BaseModel):
    title: str
    content: str
    author: Optional[str] = ""
    category: Optional[str] = ""

@app.on_event("startup")
async def startup():
    pass

@app.on_event("shutdown")
async def shutdown():
    client.close()

@app.post("/articles")
async def create_article(article: ArticleIn):
    article_dict = article.dict()
    article_dict["created_at"] = datetime.now()
    result = await db.articles.insert_one(article_dict)
    
    return {"id": str(result.inserted_id), "message": "Created"}

@app.get("/articles")
async def get_articles(skip: int = 0, limit: int = 10):
    cursor = db.articles.find().skip(skip).limit(limit)
    articles = await cursor.to_list(length=limit)
    
    for a in articles:
        a["id"] = str(a.pop("_id"))
    
    return {"data": articles}

@app.get("/articles/{article_id}")
async def get_article(article_id: str):
    from bson import ObjectId
    
    article = await db.articles.find_one({"_id": ObjectId(article_id)})
    
    if not article:
        raise HTTPException(status_code=404, detail="Not found")
    
    article["id"] = str(article.pop("_id"))
    return {"data": article}
```

---

## 五、认证与授权

### 5.1 JWT 认证

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime, timedelta
import jwt

app = FastAPI()

# 配置
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

security = HTTPBearer()

class Token(BaseModel):
    access_token: str
    token_type: str

class UserLogin(BaseModel):
    username: str
    password: str

# 模拟用户
users_db = {
    "admin": {"username": "admin", "password": "admin123", "role": "admin"},
    "user": {"username": "user", "password": "user123", "role": "user"}
}

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=24)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

@app.post("/login", response_model=Token)
def login(user: UserLogin):
    if user.username not in users_db:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    if users_db[user.username]["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_token({"sub": user.username, "role": users_db[user.username]["role"]})
    
    return {"access_token": token, "token_type": "bearer"}

@app.get("/protected")
def protected_route(user: dict = Depends(verify_token)):
    return {"message": "Protected data", "user": user}

@app.get("/admin-only")
def admin_only(user: dict = Depends(verify_token)):
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")
    return {"message": "Admin access granted"}
```

---

## 六、接口文档

### 6.1 Swagger UI

FastAPI 自动生成 Swagger 文档：
- 开发环境访问：http://localhost:8000/docs
- ReDoc 访问：http://localhost:8000/redoc

### 6.2 自定义文档

```python
from fastapi import FastAPI
from fastapi.openapi.docs import get_redoc_html

app = FastAPI(
    title="新闻 API",
    description="新闻聚合系统的 API 接口",
    version="1.0.0",
    docs_url="/docs",       # Swagger 文档
    redoc_url="/redoc",    # ReDoc 文档
    openapi_url="/openapi.json"
)

@app.get("/")
def read_root():
    return {"message": "See docs at /docs"}
```

---

## 七、课本重点标注

**《Python编程：从入门到实践》第3版 核心段落：**

| 章节 | 页码 | 重点内容 |
|------|------|----------|
| 26.1 | ~560 | RESTful 规范 |
| 26.2 | ~565 | Flask API |
| 26.3 | ~570 | FastAPI |

---

## 八、易错点与避坑指南

1. **状态码**：正确使用 HTTP 状态码
2. **分页**：大结果集必须分页
3. **验证**：严格验证输入数据
4. **错误处理**：统一的错误响应格式
5. **认证**：敏感接口必须认证

---

## 九、学习成果检验

- [ ] 理解 RESTful 设计规范
- [ ] 能用 Flask 创建 API
- [ ] 能用 FastAPI 创建 API
- [ ] 掌握 CRUD 操作实现
- [ ] 能进行数据库集成
- [ ] 能实现 JWT 认证
- [ ] 能设计良好的 API 接口
