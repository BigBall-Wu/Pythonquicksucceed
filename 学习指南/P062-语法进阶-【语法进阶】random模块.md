---
title: "P62 【语法进阶】random模块"
p_no: 62
category: 语法进阶
duration: 471
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P62 【语法进阶】random模块

> **课程分类**：语法进阶
> **时长**：471 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

语法进阶阶段，OOP、文件、迭代、多线程、正则、标准库模块。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
## 一、random 模块基础

```python
import random

# 1. 随机浮点数
random.random()             # [0, 1) 之间的浮点数
random.uniform(1, 10)        # [1, 10] 之间的浮点数

# 2. 随机整数
random.randint(1, 10)        # [1, 10] 之间的整数（包含两端）
random.randrange(0, 100, 2)  # [0, 100) 之间的偶数（range 风格）

# 3. 随机序列
random.choice([1, 2, 3, 4, 5])     # 随机选一个
random.choices([1, 2, 3], k=2)    # 随机选 k 个（可重复）
random.sample([1, 2, 3, 4], 2)    # 随机选 k 个（不重复）

# 4. 打乱序列
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)          # 原地打乱
print(lst)
```

## 二、种子（可重复随机）

```python
import random

# 设置种子
random.seed(42)
print(random.random())       # 0.6394267984578837

random.seed(42)
print(random.random())       # 0.6394267984578837（一样）

# 默认种子是系统时间
random.seed()
```

**用途**：
- 调试随机代码（固定种子让 bug 可重现）
- 单元测试
- 蒙特卡洛模拟

## 三、常用场景

### 1. 随机密码

```python
import random
import string

def gen_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%"
    return ''.join(random.choice(chars) for _ in range(length))

print(gen_password())        # "aB3$kL9pQ!m2"
```

### 2. 洗牌（Fisher-Yates）

```python
import random

def fisher_yates(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]
    return lst

print(fisher_yates([1,2,3,4,5]))
# 注意：random.shuffle 内部就是这个算法
```

### 3. 加权随机

```python
import random

items = ["apple", "banana", "cherry"]
weights = [0.5, 0.3, 0.2]      # 概率

# 单选
choice = random.choices(items, weights=weights, k=1)[0]

# 多选
choices = random.choices(items, weights=weights, k=10)
# 按概率分布抽取
```

### 4. 随机抽样

```python
import random

# 不重复抽样
population = list(range(100))
sample = random.sample(population, 10)    # 抽 10 个

# 分层抽样（按比例）
groups = {
    "A": ["a1", "a2", "a3"],
    "B": ["b1", "b2"],
    "C": ["c1", "c2", "c3", "c4"],
}
for g, items in groups.items():
    k = max(1, len(items) // 2)
    sample = random.sample(items, k)
```

## 四、secrets 模块（密码学安全）

```python
import secrets

# 1. 安全随机整数
secrets.randbelow(100)           # [0, 100)
secrets.randbits(32)             # 32 位随机整数

# 2. 安全随机字节
token = secrets.token_bytes(16)  # 16 字节（128 位）
hex_token = secrets.token_hex(16)  # 32 字符的十六进制

# 3. 安全 URL 安全 token
url_token = secrets.token_urlsafe(16)

# 4. 对比（防止时序攻击）
secrets.compare_digest(a, b)     # 恒定时间比较

# 应用：API token、密码重置链接、session ID
```

## 五、UUID（通用唯一标识符）

```python
import uuid

# UUID v1：基于时间 + MAC 地址
u1 = uuid.uuid1()

# UUID v4：完全随机（最常用）
u4 = uuid.uuid4()

# UUID v5：基于名字 + 命名空间
u5 = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")

# 转字符串
str(u4)              # '12345678-1234-4abc-9def-123456789012'

# 从字符串解析
u = uuid.UUID("12345678-1234-4abc-9def-123456789012")
```

## 六、random 性能与陷阱

```python
import random

# 1. random 不是密码学安全的！用 secrets 替代
# ❌ random.random()   # 可预测
# ✅ secrets.token_hex()  # 不可预测

# 2. 性能
import time

n = 1_000_000
start = time.time()
for _ in range(n):
    random.random()
print(f"random.random: {time.time() - start:.3f}s")

start = time.time()
for _ in range(n):
    secrets.token_hex(16)
print(f"secrets.token_hex: {time.time() - start:.3f}s")
# secrets 慢约 10 倍（但安全）
```

## 七、应用案例

```python
import random

# 1. 抽奖
participants = ["Alice", "Bob", "Charlie", "David", "Eve"]
winners = random.sample(participants, 3)
print(f"中奖者：{winners}")

# 2. 模拟掷骰子
def roll_dice(n=2):
    return [random.randint(1, 6) for _ in range(n)]

# 3. 随机点名
students = ["张三", "李四", "王五", "赵六"]
print(f"今天回答问题的是：{random.choice(students)}")

# 4. 蒙特卡洛求 π
def monte_carlo_pi(n=1_000_000):
    inside = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x*x + y*y < 1:
            inside += 1
    return 4 * inside / n

print(f"π ≈ {monte_carlo_pi():.6f}")
```

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）