---
title: P049-语法进阶-【语法进阶】Python内存管理与垃圾回收-学习计划
created: 2026-06-24
updated: 2026-06-24
type: permanent
tags: [python, 语法进阶, 内存管理, 垃圾回收]
summary: 深入理解Python的内存分配机制、垃圾回收算法与性能优化
---

# P049 - 语法进阶：Python 内存管理与垃圾回收

## 本节知识点总览

| 知识点 | 难度 | 重要度 | 课本定位 |
|--------|------|--------|----------|
| 内存管理机制 | ⭐⭐⭐ | ⭐⭐ | L2515-L2545 |
| 引用计数 | ⭐⭐ | ⭐⭐⭐ | L2550-L2580 |
| 垃圾回收算法 | ⭐⭐⭐ | ⭐⭐ | L2585-L2620 |
| 循环引用处理 | ⭐⭐⭐ | ⭐⭐ | L2625-L2660 |

---

## 一、Python 内存管理架构

### 1.1 三层架构

```
应用程序
    ↓
Python 内存分配器
    ↓
操作系统（虚拟内存）
```

### 1.2 内存池机制

```python
import sys

# 小整数池（-5 到 256）
a = 257
b = 257
print(f"小整数池外：a is b = {a is b}")  # False

a = 256
b = 256
print(f"小整数池内：a is b = {a is b}")  # True

# 字符串驻留
a = "hello"
b = "hello"
print(f"字符串驻留：a is b = {a is b}")  # True

# 字符串不驻留
a = "hello world"
b = "hello world"
print(f"长字符串：a is b = {a is b}")  # 可能 False

# 查看对象大小
print(f"整数对象大小：{sys.getsizeof(42)} bytes")
print(f"列表对象大小：{sys.getsizeof([1, 2, 3])} bytes")
```

### 1.3 内存分配策略

```python
import tracemalloc

# 开启内存追踪
tracemalloc.start()

# 记录初始状态
snapshot1 = tracemalloc.take_snapshot()

# 执行代码
data = [i ** 2 for i in range(10000)]
more_data = {"key": "value" * 1000}

# 记录新状态
snapshot2 = tracemalloc.take_snapshot()

# 对比差异
top_stats = snapshot2.compare_to(snapshot1, 'lineno')
print("内存增长 Top 10：")
for stat in top_stats[:10]:
    print(stat)

# 停止追踪
tracemalloc.stop()
```

---

## 二、引用计数机制

### 2.1 引用计数基础

```python
import sys

# 获取引用计数
ref_count = sys.getrefcount
x = object()  # 引用计数 +1
print(f"初始引用计数：{sys.getrefcount(x) - 1}")

# 引用和副本
y = x  # 引用计数 +1
print(f"引用后：{sys.getrefcount(x) - 1}")

del y  # 引用计数 -1
print(f"删除引用后：{sys.getrefcount(x) - 1}")

# 函数参数也会增加引用计数
def check_ref(obj):
    print(f"函数内引用计数：{sys.getrefcount(obj) - 1}")

check_ref(x)
```

### 2.2 引用计数的变化

```python
import sys

# 引用计数测试
def test_refcount():
    obj = [1, 2, 3]  # 引用计数 = 1
    print(f"创建后：{sys.getrefcount(obj) - 1}")
    
    obj2 = obj       # 引用计数 = 2
    print(f"赋值引用后：{sys.getrefcount(obj) - 1}")
    
    obj_list = [obj, obj]  # 引用计数 = 4
    print(f"放入列表后：{sys.getrefcount(obj) - 1}")
    
    del obj          # 引用计数 = 3
    print(f"删除obj后：{sys.getrefcount(obj2) - 1}")
    
    del obj2         # 引用计数 = 2
    print(f"删除obj2后：{sys.getrefcount(obj_list[0]) - 1}")
    
    del obj_list     # 引用计数 = 0，对象被销毁
    # 此时对象已被垃圾回收

test_refcount()
```

### 2.3 引用计数的局限性

```python
# 引用计数无法处理循环引用
class Node:
    def __init__(self):
        self.next = None

# 创建循环引用
node1 = Node()
node2 = Node()
node1.next = node2  # node1 引用 node2
node2.next = node1  # node2 引用 node1

# 即使删除所有外部引用，对象仍相互引用
del node1
del node2
# 此时两个对象的引用计数都不为 0，但已经无法访问
# 这就是循环引用问题
```

---

## 三、垃圾回收算法

### 3.1 分代回收

```python
import gc

# Python 垃圾回收使用分代算法
# 对象被分为三代：0、1、2
# 新创建的对象在 0 代
# 经历一次 GC 仍然存活的对象进入 1 代
# 经历两次 GC 仍然存活的对象进入 2 代

print(f"代数阈值：{gc.get_threshold()}")  # (700, 10, 10)
print(f"当前代数统计：{gc.get_counts()}")

# 手动触发垃圾回收
gc.collect()

# 查看回收统计
print(f"回收统计：{gc.get_stats()}")
```

### 3.2 GC 触发条件

```python
import gc

# 0 代对象数量超过阈值时触发 0 代 GC
# 0 代 GC 次数超过阈值时触发 1 代 GC
# 1 代 GC 次数超过阈值时触发 2 代 GC

# 修改阈值（不推荐生产环境）
gc.set_threshold(100, 10, 10)

# 禁用自动 GC
gc.disable()
gc.collect()  # 仍可手动触发
gc.enable()
```

### 3.3 GC 与内存

```python
import gc

# 禁用 GC，观察内存变化
gc.disable()

data = []
for i in range(100000):
    data.append({"id": i, "data": "x" * 100})

# 重新启用并回收
gc.enable()
gc.collect()  # 手动回收

# 或者让 GC 自动处理
gc.collect()
```

---

## 四、循环引用处理

### 4.1 循环引用示例

```python
import gc

class Parent:
    def __init__(self, name):
        self.name = name
        self.child = None
    def __repr__(self):
        return f"Parent({self.name})"

class Child:
    def __init__(self, name):
        self.name = name
        self.parent = None
    def __repr__(self):
        return f"Child({self.name})"

# 创建循环引用
parent = Parent("Dad")
child = Child("Son")
parent.child = child  # 父 -> 子
child.parent = parent  # 子 -> 父

print(f"父引用子：{parent.child}")
print(f"子引用父：{child.parent}")

# 删除外部引用
del parent
del child

# 此时 GC 应该能检测到循环引用并回收
gc.collect()
```

### 4.2 weakref 弱引用

```python
import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = self  # 普通引用造成循环引用

# 使用 weakref 避免循环引用
class NodeWeak:
    def __init__(self, value):
        self.value = value
        self.parent = None  # 弱引用
        self.children = []  # 弱引用列表

# 或者使用 weakref.proxy
class NodeProxy:
    def __init__(self, value):
        self.value = value
        self.parent = None
    
    def add_child(self, child):
        self.children.append(child)
        child.parent = weakref.proxy(self)

# 使用 weakref.ref
parent = Node("Parent")
child = Node("Child")
child.parent_ref = weakref.ref(parent)  # 不增加引用计数

print(f"获取弱引用：{child.parent_ref()}")
del parent
print(f"删除后：{child.parent_ref()}")  # None
```

### 4.3 weakref 模块详解

```python
import weakref

# 创建弱引用
obj = [1, 2, 3]
ref = weakref.ref(obj)

print(f"引用对象：{ref()}")
print(f"对象是否存活：{ref() is not None}")

del obj
print(f"删除后：{ref()}")  # None

# WeakValueDictionary：值是弱引用的字典
import weakref

class Cache:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    
    def set(self, key, value):
        self._cache[key] = value
    
    def get(self, key):
        return self._cache.get(key)

# 使用
cache = Cache()
cache.set("user1", {"name": "Alice", "data": "x" * 1000})
print(cache.get("user1"))  # 获取
# 当对象被其他地方删除时，WeakValueDictionary 中的引用也会自动清除
```

---

## 五、性能优化技巧

### 5.1 避免频繁创建对象

```python
# ❌ 不好：在循环中频繁创建对象
def bad_example():
    result = []
    for i in range(10000):
        result.append({"index": i, "value": i * 2})
    return result

# ✅ 更好：使用生成器
def good_example():
    for i in range(10000):
        yield {"index": i, "value": i * 2}

# ✅ 更好：使用 __slots__
class Point:
    __slots__ = ['x', 'y']  # 减少内存占用
    def __init__(self, x, y):
        self.x = x
        self.y = y

import sys
print(f"使用 __slots__：{sys.getsizeof(Point(1, 2))} bytes")

class PointNormal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

print(f"不使用 __slots__：{sys.getsizeof(PointNormal(1, 2))} bytes")
```

### 5.2 对象复用

```python
# 复用对象而不是创建新对象
class ObjectPool:
    """对象池"""
    
    def __init__(self, factory):
        self._factory = factory
        self._pool = []
    
    def acquire(self):
        if self._pool:
            return self._pool.pop()
        return self._factory()
    
    def release(self, obj):
        self._pool.append(obj)

# 使用对象池
import uuid

pool = ObjectPool(lambda: {"data": None})

obj1 = pool.acquire()
obj1["id"] = str(uuid.uuid4())
print(f"使用对象1：{obj1}")

pool.release(obj1)

obj2 = pool.acquire()
print(f"复用对象2：{obj2}")
print(f"对象相同：{obj1 is obj2}")
```

### 5.3 内存分析

```python
import tracemalloc

# 基本用法
tracemalloc.start()

# 执行代码
import json
data = {"users": [{"id": i, "name": f"user_{i}"} for i in range(1000)]}
json_str = json.dumps(data)

# 获取当前内存使用
current, peak = tracemalloc.get_traced_memory()
print(f"当前内存：{current / 1024 / 1024:.2f} MB")
print(f"峰值内存：{peak / 1024 / 1024:.2f} MB")

# 获取最占用内存的代码行
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
for stat in top_stats[:5]:
    print(stat)

tracemalloc.stop()
```

---

## 六、__del__ 析构函数

### 6.1 基本用法

```python
class Resource:
    def __init__(self, name):
        self.name = name
        print(f"创建 Resource: {name}")
    
    def __del__(self):
        print(f"销毁 Resource: {self.name}")

# 使用
r = Resource("test")
del r  # 调用 __del__

# 注意：__del__ 不保证在对象销毁时一定被调用
```

### 6.2 __del__ 的陷阱

```python
# 陷阱1：循环引用中的 __del__
class A:
    def __init__(self):
        self.b = None
    def __del__(self):
        print("A 被销毁")

class B:
    def __init__(self):
        self.a = None
    def __del__(self):
        print("B 被销毁")

# 创建循环引用
a = A()
b = B()
a.b = b
b.a = a

del a
del b
# 此时 A 和 B 都不会被销毁（循环引用）

# 陷阱2：__del__ 中抛异常
class Bad:
    def __del__(self):
        raise ValueError("在 __del__ 中抛出异常")

# 可能导致警告
```

### 6.3 最佳实践

```python
# 推荐使用上下文管理器而不是 __del__
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self
    
    def __exit__(self, *args):
        if self.file:
            self.file.close()
    
    def read(self):
        return self.file.read()

# 使用 with 语句确保关闭
with FileHandler("test.txt") as handler:
    content = handler.read()
```

---

## 七、实战案例

### 7.1 大数据处理优化

```python
import tracemalloc

def process_large_data():
    """处理大数据集的优化示例"""
    import json
    
    tracemalloc.start()
    
    # 方法1：一次性加载（内存压力大）
    # with open("large_file.json") as f:
    #     data = json.load(f)
    
    # 方法2：流式处理（内存友好）
    result = []
    with open("large_file.json") as f:
        for line in f:
            data = json.loads(line)
            result.append(data)
    
    current, peak = tracemalloc.get_traced_memory()
    print(f"方法2 - 当前：{current / 1024 / 1024:.2f} MB, 峰值：{peak / 1024 / 1024:.2f} MB")
    
    tracemalloc.stop()
    return result

# 使用生成器处理超大文件
def stream_process_large_file(filepath):
    """流式处理超大文件"""
    with open(filepath, 'r') as f:
        for line in f:
            # 处理每一行
            yield line.strip().split(',')
```

### 7.2 内存泄漏检测

```python
import gc
import sys

class MemoryLeakDemo:
    """模拟内存泄漏"""
    
    _cache = {}  # 类变量，可能导致内存泄漏
    
    @classmethod
    def add_to_cache(cls, key, value):
        # 无限增长的缓存
        cls._cache[key] = value

def detect_leak():
    """检测内存泄漏"""
    gc.collect()
    
    before = sys.getsizeof(MemoryLeakDemo._cache)
    
    for i in range(1000):
        MemoryLeakDemo.add_to_cache(f"key_{i}", {"data": "x" * 100})
    
    gc.collect()
    
    after = sys.getsizeof(MemoryLeakDemo._cache)
    print(f"缓存前：{before} bytes")
    print(f"缓存后：{after} bytes")
    print(f"缓存大小：{len(MemoryLeakDemo._cache)} 项")

detect_leak()

# 修复方法：使用 LRU 缓存或限制大小
from functools import lru_cache

class FixedCache:
    _cache = lru_cache(maxsize=1000)(lambda x: {"data": "x" * 100})
```

---

## 八、课本重点标注

**《Python编程：从入门到实践》第3版 核心段落：**

| 章节 | 页码 | 重点内容 |
|------|------|----------|
| 8.1 | ~165 | 内存管理初步 |
| 8.2 | ~170 | 引用和副本 |
| 8.3 | ~175 | 垃圾回收 |

---

## 九、易错点与避坑指南

1. **循环引用**：注意对象间相互引用的情况
2. **全局变量**：类变量可能阻止对象被回收
3. **__del__ 不靠谱**：不要依赖析构函数进行资源清理
4. **大对象**：处理大文件时使用流式处理
5. **缓存溢出**：使用有界缓存如 LRU Cache

---

## 十、学习成果检验

- [ ] 理解 Python 内存管理的基本架构
- [ ] 掌握引用计数机制及其局限性
- [ ] 理解分代垃圾回收算法
- [ ] 能处理循环引用问题
- [ ] 掌握 weakref 模块的使用
- [ ] 能使用内存分析工具排查问题
- [ ] 理解 __slots__ 的内存优化作用
