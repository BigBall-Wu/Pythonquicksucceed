---
title: "P58 【语法进阶】time模块之三种时间表示"
p_no: 58
category: 语法进阶
duration: 808
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P58 【语法进阶】time模块之三种时间表示

> **课程分类**：语法进阶
> **时长**：808 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

语法进阶阶段，OOP、文件、迭代、多线程、正则、标准库模块。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
## 一、time 模块

```python
import time

# 1. 时间戳（自 1970-01-01 起的秒数）
t = time.time()              # 1719234567.123456
print(t)

# 2. 结构化时间（struct_time）
local_t = time.localtime()    # 本地时间
utc_t = time.gmtime()         # UTC 时间
print(local_t.tm_year)        # 2024
print(local_t.tm_hour)        # 14

# 3. 格式化字符串
time.strftime("%Y-%m-%d %H:%M:%S")           # '2024-06-24 14:30:00'
time.strftime("%Y年%m月%d日")                  # '2024年06月24日'

# 4. 解析字符串
time.strptime("2024-06-24", "%Y-%m-%d")
# time.struct_time(tm_year=2024, tm_mon=6, tm_mday=24, ...)

# 5. 休眠
time.sleep(1)                # 休眠 1 秒

# 6. 性能计时
start = time.time()
do_something()
elapsed = time.time() - start
print(f"耗时 {elapsed:.3f}s")
```

## 二、格式化符号

| 符号 | 含义 | 例子 |
|------|------|------|
| `%Y` | 4 位年 | 2024 |
| `%y` | 2 位年 | 24 |
| `%m` | 月（01-12） | 06 |
| `%d` | 日（01-31） | 24 |
| `%H` | 时（00-23） | 14 |
| `%I` | 时（01-12） | 02 |
| `%M` | 分（00-59） | 30 |
| `%S` | 秒（00-59） | 45 |
| `%p` | AM/PM | PM |
| `%a` | 星期缩写 | Mon |
| `%A` | 星期全称 | Monday |
| `%b` | 月份缩写 | Jun |
| `%B` | 月份全称 | June |
| `%j` | 一年中的第几天 | 176 |
| `%U` | 一年中的第几周（周日为第一天） | 25 |
| `%W` | 一年中的第几周（周一为第一天） | 25 |
| `%c` | 本地日期时间 | Mon Jun 24 14:30:00 2024 |
| `%x` | 本地日期 | 06/24/24 |
| `%X` | 本地时间 | 14:30:00 |
| `%z` | 时区偏移 | +0800 |

## 三、struct_time 字段

```python
import time

t = time.localtime()
print(t.tm_year)      # 年
print(t.tm_mon)       # 月 (1-12)
print(t.tm_mday)      # 日 (1-31)
print(t.tm_hour)      # 时 (0-23)
print(t.tm_min)       # 分 (0-59)
print(t.tm_sec)       # 秒 (0-61, 处理闰秒)
print(t.tm_wday)      # 周几 (0=周一)
print(t.tm_yday)      # 一年中第几天 (1-366)
print(t.tm_isdst)     # 是否夏令时
```

## 四、时间戳与结构化时间互转

```python
import time

# 时间戳 → 结构化
ts = 1719234567.123
t = time.localtime(ts)
print(t.tm_year)      # 2024

# 结构化 → 时间戳
t = time.localtime()
ts = time.mktime(t)

# UTC 时间戳
utc_ts = time.time()           # 当前 UTC 时间戳
```

## 五、高精度计时

```python
import time

# perf_counter：最高精度
start = time.perf_counter()
time.sleep(0.001)
elapsed = time.perf_counter() - start
print(f"耗时 {elapsed:.6f}s")

# monotonic：单调时间（不受系统时间修改影响）
start = time.monotonic()
time.sleep(0.5)
print(f"耗时 {time.monotonic() - start:.3f}s")

# process_time：进程 CPU 时间
start = time.process_time()
do_cpu_work()
print(f"CPU 耗时 {time.process_time() - start:.3f}s")
```

## 六、datetime 模块（推荐）

time 模块偏底层，实际项目更推荐用 datetime：

```python
from datetime import datetime, timedelta

# 当前时间
now = datetime.now()           # 2024-06-24 14:30:00.123456
utc_now = datetime.utcnow()    # UTC

# 创建特定时间
d = datetime(2024, 6, 24, 14, 30, 0)

# 格式化
now.strftime("%Y-%m-%d %H:%M:%S")

# 解析
d = datetime.strptime("2024-06-24", "%Y-%m-%d")

# 时间运算
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
diff = tomorrow - now          # timedelta

# 时间戳转换
ts = now.timestamp()           # → float
d = datetime.fromtimestamp(ts) # → datetime
```

## 七、性能对比

```python
import time

n = 1_000_000

# time.time() 的调用开销
start = time.time()
for _ in range(n):
    time.time()
print(f"time.time(): {time.time() - start:.3f}s")

# perf_counter
start = time.perf_counter()
for _ in range(n):
    time.perf_counter()
print(f"perf_counter: {time.perf_counter() - start:.3f}s")
# perf_counter 更精确
```

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）