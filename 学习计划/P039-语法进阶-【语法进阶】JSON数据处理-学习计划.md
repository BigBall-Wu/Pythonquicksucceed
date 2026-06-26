---
title: P039-语法进阶-【语法进阶】JSON数据处理-学习计划
created: 2026-06-24
updated: 2026-06-24
type: permanent
tags: [python, 语法进阶, JSON]
summary: 掌握JSON数据格式与Python的json模块进行序列化与反序列化
---

# P039 - 语法进阶：JSON 数据处理

## 本节知识点总览

| 知识点 | 难度 | 重要度 | 课本定位 |
|--------|------|--------|----------|
| JSON 格式规范 | ⭐⭐ | ⭐⭐⭐ | L2800-L2820 |
| json.dumps/loads | ⭐⭐ | ⭐⭐⭐ | L2825-L2845 |
| json.dump/load | ⭐⭐ | ⭐⭐ | L2850-L2870 |
| 自定义编码器 | ⭐⭐⭐ | ⭐⭐ | L2875-L2900 |

---

## 一、JSON 基础概念

### 1.1 什么是 JSON

JSON（JavaScript Object Notation）是一种轻量级的数据交换格式，易于人阅读和编写，同时也易于机器解析和生成。

```json
{
    "name": "张三",
    "age": 25,
    "is_student": false,
    "skills": ["Python", "JavaScript", "SQL"],
    "address": {
        "city": "北京",
        "district": "朝阳区"
    }
}
```

### 1.2 JSON vs Python 数据类型对照

| JSON 类型 | Python 类型 | 示例 |
|-----------|------------|------|
| object | dict | `{"name": "张三"}` |
| array | list | `["a", "b", "c"]` |
| string | str | `"Hello"` |
| number | int/float | `42`, `3.14` |
| true/false | True/False | `true` → `True` |
| null | None | `null` → `None` |

### 1.3 JSON 的应用场景

```python
# API 响应
response = requests.get("https://api.example.com/user")
user_data = response.json()  # 直接解析为 Python 对象

# 配置文件
config = json.load(open("config.json", encoding="utf-8"))

# 数据存储
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(database_records, f, ensure_ascii=False)
```

---

## 二、Python json 模块核心函数

### 2.1 序列化：Python → JSON 字符串

#### dumps（dump to string）

```python
import json

data = {
    "name": "李四",
    "age": 30,
    "scores": [95, 88, 92]
}

# 序列化为字符串
json_str = json.dumps(data)
print(json_str)
# 输出：{"name": "李四", "age": 30, "scores": [95, 88, 92]}

# 中文处理
data_cn = {"城市": "上海", "著名建筑": "东方明珠"}
json_str_cn = json.dumps(data_cn, ensure_ascii=False)
print(json_str_cn)
# 输出：{"城市": "上海", "著名建筑": "东方明珠"}
```

#### 格式化输出

```python
data = {"name": "测试", "value": 12345}

# 紧凑格式（默认）
print(json.dumps(data))
# {"name": "测试", "value": 12345}

# 格式化（带缩进）
print(json.dumps(data, indent=4, ensure_ascii=False))
# {
#     "name": "测试",
#     "value": 12345
# }

# 按键排序
print(json.dumps(data, indent=4, sort_keys=True))
# {
#     "name": "测试",
#     "value": 12345
# }
```

### 2.2 反序列化：JSON 字符串 → Python

#### loads（load from string）

```python
import json

json_str = '{"name": "王五", "age": 28, "is_active": true}'

# 从字符串反序列化
data = json.loads(json_str)
print(data)
# {'name': '王五', 'age': 28, 'is_active': True}
print(type(data["is_active"]))  # <class 'bool'>
```

### 2.3 文件操作

#### dump（写入文件）

```python
import json

data = {
    "username": "alice",
    "email": "alice@example.com",
    "preferences": {
        "theme": "dark",
        "language": "zh-CN"
    }
}

# 写入文件
with open("user_config.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("配置文件已保存")
```

#### load（读取文件）

```python
import json

# 读取文件
with open("user_config.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print(loaded_data)
# {'username': 'alice', 'email': 'alice@example.com', ...}
```

---

## 三、进阶技巧

### 3.1 自定义序列化（JSONEncoder）

#### 处理日期时间

```python
import json
from datetime import datetime, date

class DateTimeEncoder(json.JSONEncoder):
    """自定义编码器：处理日期时间类型"""
    
    def default(self, obj):
        if isinstance(obj, datetime):
            return {
                "__type": "datetime",
                "value": obj.isoformat()
            }
        if isinstance(obj, date):
            return {
                "__type": "date",
                "value": obj.isoformat()
            }
        return super().default(obj)

def datetime_decoder(dct):
    """解码器：还原日期时间类型"""
    if "__type" in dct:
        if dct["__type"] == "datetime":
            return datetime.fromisoformat(dct["value"])
        if dct["__type"] == "date":
            return date.fromisoformat(dct["value"])
    return dct

# 使用
data = {
    "event": "产品发布会",
    "date": date(2026, 6, 30),
    "time": datetime(2026, 6, 30, 14, 30)
}

encoded = json.dumps(data, cls=DateTimeEncoder, ensure_ascii=False)
print(encoded)

decoded = json.loads(encoded, object_hook=datetime_decoder)
print(decoded)
print(type(decoded["date"]))  # <class 'datetime.date'>
```

#### 处理自定义对象

```python
import json

class User:
    """用户类"""
    
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
    
    def to_dict(self):
        """转换为字典"""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email
        }
    
    @classmethod
    def from_dict(cls, d):
        """从字典创建"""
        return cls(d["user_id"], d["name"], d["email"])

class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {"__user__": True, **obj.to_dict()}
        return super().default(obj)

def user_decoder(dct):
    if dct.get("__user__"):
        return User.from_dict(dct)
    return dct

# 使用
user = User(1001, "Alice", "alice@example.com")
encoded = json.dumps(user, cls=UserEncoder)
decoded = json.loads(encoded, object_hook=user_decoder)
print(decoded.name)  # Alice
```

### 3.2 部分序列化

```python
import json

# 只序列化部分字段
class PartialEncoder(json.JSONEncoder):
    """只序列化特定字段"""
    
    def __init__(self, fields, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = fields
    
    def default(self, obj):
        if hasattr(obj, "__dict__"):
            return {k: v for k, v in obj.__dict__.items() if k in self.fields}
        return super().default(obj)

class Product:
    def __init__(self, pid, name, price, internal_code):
        self.pid = pid
        self.name = name
        self.price = price
        self.internal_code = internal_code  # 内部代码，不对外公开

product = Product(101, "笔记本电脑", 5999.00, "LAPTOP-2026")

# 只序列化公开字段
encoder = PartialEncoder(fields=["pid", "name", "price"])
print(json.dumps(product, cls=encoder, indent=4, ensure_ascii=False))
```

### 3.3 流式读写大文件

```python
import json

# 流式写入（适用于大数据集）
def stream_write_jsonl(filepath, items):
    """
    写入 JSONL 格式（每行一个 JSON 对象）
    适用于超大数据集，避免一次性加载
    """
    with open(filepath, "w", encoding="utf-8") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

# 流式读取
def stream_read_jsonl(filepath):
    """
    读取 JSONL 格式
    """
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)

# 使用示例
stream_write_jsonl("large_data.jsonl", [
    {"id": 1, "data": "item1"},
    {"id": 2, "data": "item2"},
    {"id": 3, "data": "item3"}
])

for item in stream_read_jsonl("large_data.jsonl"):
    print(item)
```

---

## 四、实际应用场景

### 4.1 API 数据处理

```python
import json
import requests

def fetch_and_parse_api(url, headers=None):
    """
    获取 API 数据并解析为 Python 对象
    
    Args:
        url: API 地址
        headers: 请求头
    
    Returns:
        解析后的数据字典
    """
    response = requests.get(url, headers=headers or {})
    response.raise_for_status()
    
    return response.json()

# GitHub API 示例
def get_github_user(username):
    """获取 GitHub 用户信息"""
    url = f"https://api.github.com/users/{username}"
    return fetch_and_parse_api(url)

user = get_github_user("torvalds")
print(f"用户：{user['name']}")
print(f"仓库数：{user['public_repos']}")
print(f"粉丝数：{user['followers']}")
```

### 4.2 配置管理

```python
import json
from pathlib import Path

class ConfigManager:
    """配置文件管理器"""
    
    def __init__(self, config_path):
        self.config_path = Path(config_path)
        self._config = None
    
    @property
    def config(self):
        if self._config is None:
            self.load()
        return self._config
    
    def load(self):
        """从文件加载配置"""
        if self.config_path.exists():
            with open(self.config_path, "r", encoding="utf-8") as f:
                self._config = json.load(f)
        else:
            self._config = self.get_default_config()
            self.save()
        return self._config
    
    def save(self):
        """保存配置到文件"""
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self._config, f, indent=4, ensure_ascii=False)
    
    @staticmethod
    def get_default_config():
        """默认配置"""
        return {
            "app_name": "MyApp",
            "version": "1.0.0",
            "debug": False,
            "database": {
                "host": "localhost",
                "port": 5432,
                "name": "myapp_db"
            },
            "features": {
                "dark_mode": True,
                "auto_save": True,
                "notifications": True
            }
        }

# 使用
config = ConfigManager("app_config.json")
config.config["debug"] = True
config.save()
```

### 4.3 数据缓存

```python
import json
import hashlib
from pathlib import Path

class JsonCache:
    """基于 JSON 文件的简单缓存"""
    
    def __init__(self, cache_dir=".cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
    
    def _get_cache_key(self, key):
        """生成缓存文件名"""
        hash_key = hashlib.md5(str(key).encode()).hexdigest()
        return self.cache_dir / f"{hash_key}.json"
    
    def get(self, key):
        """获取缓存"""
        cache_file = self._get_cache_key(key)
        if cache_file.exists():
            with open(cache_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return None
    
    def set(self, key, value, ttl=None):
        """设置缓存"""
        cache_file = self._get_cache_key(key)
        data = {
            "key": key,
            "value": value,
            "ttl": ttl
        }
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
    
    def delete(self, key):
        """删除缓存"""
        cache_file = self._get_cache_key(key)
        if cache_file.exists():
            cache_file.unlink()
    
    def clear(self):
        """清空所有缓存"""
        for cache_file in self.cache_dir.glob("*.json"):
            cache_file.unlink()

# 使用示例
cache = JsonCache()

# 缓存数据
cache.set("user_profile_1001", {"name": "Alice", "level": 5})

# 获取缓存
profile = cache.get("user_profile_1001")
print(profile)  # {'name': 'Alice', 'level': 5}
```

---

## 五、错误处理

### 5.1 常见错误

```python
import json

# 错误1：无效的 JSON 格式
try:
    json.loads('{"name": "test",}')  # 尾随逗号
except json.JSONDecodeError as e:
    print(f"JSON 解析错误：{e}")

# 错误2：Python 特有类型
try:
    json.dumps(set([1, 2, 3]))  # set 不是 JSON 类型
except TypeError as e:
    print(f"类型错误：{e}")

# 错误3：文件不存在
try:
    with open("nonexistent.json", "r") as f:
        json.load(f)
except FileNotFoundError as e:
    print(f"文件不存在：{e}")

# 错误4：编码问题
try:
    with open("chinese.json", "r", encoding="utf-8") as f:
        json.load(f)
except json.JSONDecodeError as e:
    print(f"编码或格式错误：{e}")
```

### 5.2 安全加载

```python
import json

def safe_json_load(filepath, default=None):
    """
    安全加载 JSON 文件
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"加载失败：{e}")
        return default if default is not None else {}

def safe_json_loads(json_str, default=None):
    """
    安全解析 JSON 字符串
    """
    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"解析失败：{e}")
        return default if default is not None else {}
```

---

## 六、课本重点标注

**《Python编程：从入门到实践》第3版 核心段落：**

| 章节 | 页码 | 重点内容 |
|------|------|----------|
| 14.1 | ~310 | 读取 JSON 数据 |
| 14.2 | ~315 | API 请求 |
| 14.3 | ~320 | 使用 API |
| 14.4 | ~325 | GitHub API |

---

## 七、实战练习

### 练习一：TODO 列表持久化

```python
import json
from pathlib import Path
from datetime import datetime

class TodoList:
    """带持久化的待办事项列表"""
    
    def __init__(self, filepath="todos.json"):
        self.filepath = Path(filepath)
        self.todos = []
        self.load()
    
    def load(self):
        """加载待办事项"""
        if self.filepath.exists():
            with open(self.filepath, "r", encoding="utf-8") as f:
                self.todos = json.load(f)
    
    def save(self):
        """保存待办事项"""
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.todos, f, indent=4, ensure_ascii=False)
    
    def add(self, title, description=""):
        """添加待办事项"""
        todo = {
            "id": len(self.todos) + 1,
            "title": title,
            "description": description,
            "completed": False,
            "created_at": datetime.now().isoformat(),
            "completed_at": None
        }
        self.todos.append(todo)
        self.save()
        return todo["id"]
    
    def complete(self, todo_id):
        """标记完成"""
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["completed"] = True
                todo["completed_at"] = datetime.now().isoformat()
                self.save()
                return True
        return False
    
    def list_all(self):
        """列出所有待办"""
        return self.todos

# 使用
todos = TodoList()
todos.add("学习 Python", "掌握基础语法和面向对象")
todos.add("完成项目", "开发一个 Web 应用")
todos.complete(1)

for todo in todos.list_all():
    status = "✓" if todo["completed"] else "○"
    print(f"{status} [{todo['id']}] {todo['title']}")
```

---

## 八、学习成果检验

- [ ] 掌握 JSON 与 Python 数据类型的对应关系
- [ ] 熟练使用 dumps/loads 进行字符串序列化
- [ ] 熟练使用 dump/load 进行文件操作
- [ ] 能处理中文和非 ASCII 字符
- [ ] 理解自定义 JSONEncoder 的用法
- [ ] 能处理日期时间等特殊类型
- [ ] 掌握 JSONL 流式读写大文件
- [ ] 能处理 JSON 解析错误
