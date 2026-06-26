---
title: "P49 【语法进阶】协程操作与greenlet使用"
p_no: 49
category: 语法进阶
duration: 1806
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P49 【语法进阶】协程操作与greenlet使用

> **课程分类**：语法进阶
> **时长**：1806 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

语法进阶阶段，OOP、文件、迭代、多线程、正则、标准库模块。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
## 一、协程（Coroutine）是什么

**协程**是用户态的轻量级线程，由程序自己调度（而不是 OS）。

| 特性 | 线程 | 协程 |
|------|------|------|
| 调度方 | OS | 程序 |
| 切换开销 | 大（系统调用） | 小（用户态） |
| 并行 | 真并行 | 协作式 |
| 数据共享 | 容易（共享变量） | 容易（同一线程） |
| 创建数量 | 几百 | 几十万 |

## 二、greenlet（最轻量的协程库）

```python
from greenlet import greenlet
import time

def task1():
    print("task1 start")
    gr2.switch()                  # 切到 task2
    print("task1 end")
    gr2.switch()

def task2():
    print("task2 start")
    time.sleep(0.1)               # 注意：阻塞 sleep 会阻塞整个线程
    gr1.switch()                  # 切回 task1
    print("task2 end")

gr1 = greenlet(task1)
gr2 = greenlet(task2)
gr1.switch()
# task1 start
# task2 start
# task1 end
# task2 end
```

## 三、greenlet 的局限

```python
# ❌ 阻塞调用会阻塞整个线程
def task():
    time.sleep(1)                # 整个线程被挂起
```

**greenlet 自己不解决 I/O 调度**，需要配合 `gevent` 一起用。

## 四、greenlet 切换底层

```python
# 手动切换示例
from greenlet import greenlet

def a():
    print("a1")
    b.switch()
    print("a2")

def b():
    print("b1")
    a.switch()
    print("b2")

a = greenlet(a)
b = greenlet(b)
a.switch()
# a1 → b1 → a2（b2 不会执行，因 a 已结束）
```

## 五、greenlet vs yield

```python
# yield 也能实现类似效果
def a():
    print("a1")
    yield
    print("a2")

def b():
    print("b1")
    yield
    print("b2")

g1 = a()
g2 = b()
next(g1)
next(g2)
next(g1)
# a1 → b1 → a2
```

但 greenlet 更灵活：可以从任何函数切换。

## 六、greenlet 父子关系

greenlet 有父子关系，父结束则子自动结束：

```python
from greenlet import greenlet

def child():
    import sys
    print(f"child parent: {greenlet.getcurrent().parent}")
    sys.exit(0)                  # 终止所有

def parent():
    g = greenlet(child)
    g.switch()

g = greenlet(parent)
g.switch()
print("parent done")
```

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）