---
title: "P50 【语法进阶】genent的使用与总结"
p_no: 50
category: 语法进阶
duration: 1988
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P50 【语法进阶】genent的使用与总结

> **课程分类**：语法进阶
> **时长**：1988 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

语法进阶阶段，OOP、文件、迭代、多线程、正则、标准库模块。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
## 一、gevent 是什么

**gevent** = greenlet + 自动 I/O 调度（基于 libev/libuv）

特点：
- 当 greenlet 做 I/O 时，自动切换到其他 greenlet
- 用 monkey patch 把标准库阻塞调用改成非阻塞

## 二、gevent 基础

```python
import gevent

def task(name, n):
    print(f"{name} start")
    gevent.sleep(n)              # 协作式 sleep
    print(f"{name} end")

g1 = gevent.spawn(task, "A", 2)  # 启动一个协程
g2 = gevent.spawn(task, "B", 1)
g3 = gevent.spawn(task, "C", 3)

gevent.joinall([g1, g2, g3])     # 等待所有
# B start → A start → C start → B end → A end → C end
```

## 三、Monkey Patch（关键！）

gevent 通过打补丁让标准库的阻塞 I/O 变成非阻塞：

```python
from gevent import monkey
monkey.patch_all()               # 必须在文件开头、其他 import 之前

import time
import requests

def fetch(url):
    print(f"GET {url}")
    resp = requests.get(url)
    print(f"{url}: {len(resp.text)} bytes")

gevent.joinall([
    gevent.spawn(fetch, "https://www.baidu.com"),
    gevent.spawn(fetch, "https://www.python.org"),
    gevent.spawn(fetch, "https://www.github.com"),
])
# 三个请求并发执行（不是串行！）
```

**注意**：`monkey.patch_all()` 必须在所有其他 import 之前调用，否则可能不生效。

## 四、gevent 池

```python
from gevent.pool import Pool

def task(n):
    gevent.sleep(1)
    return n ** 2

pool = Pool(5)
results = pool.map(task, range(10))
print(results)    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## 五、信号量限制并发

```python
import gevent
from gevent.lock import Semaphore

sem = Semaphore(2)               # 同时最多 2 个

def task(i):
    with sem:
        print(f"task {i} start")
        gevent.sleep(1)
        print(f"task {i} end")

gevent.joinall([gevent.spawn(task, i) for i in range(5)])
```

## 六、gevent 的 Event

```python
import gevent

event = gevent.event.Event()

def setter():
    gevent.sleep(2)
    event.set()
    print("已 set")

def waiter():
    print("等待...")
    event.wait()
    print("继续")

gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
])
```

## 七、gevent 超时

```python
import gevent

def slow_task():
    gevent.sleep(10)

with gevent.Timeout(2):
    gevent.spawn(slow_task).join()
# 2 秒后抛 Timeout
```

## 八、gevent 实战：并发爬虫

```python
from gevent import monkey
monkey.patch_all()

import gevent
import requests

def fetch(url):
    resp = requests.get(url, timeout=5)
    print(f"{url}: {resp.status_code}, {len(resp.text)} bytes")

urls = [
    "https://www.baidu.com",
    "https://www.python.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
]

gevent.joinall([gevent.spawn(fetch, url) for url in urls])
# 4 个请求并发（每个平均 500ms，总耗时约 500ms）
```

## 九、asyncio vs gevent

| 特性 | gevent | asyncio |
|------|--------|---------|
| 风格 | 隐式（monkey patch） | 显式（async/await） |
| 性能 | 高 | 高 |
| 兼容性 | 改动标准库 | 不改动 |
| 学习曲线 | 较陡 | 较缓 |
| Python 3.4+ | 需要装第三方 | 内置 |

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）