---
title: "P59 【语法进阶】time模块之时间元组与时间字符串相互转换"
p_no: 59
category: 语法进阶
duration: 327
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P59 【语法进阶】time模块之时间元组与时间字符串相互转换

> **课程分类**：语法进阶
> **时长**：327 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

语法进阶阶段，OOP、文件、迭代、多线程、正则、标准库模块。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
## 一、struct_time 字段

```python
import time

t = time.localtime()
# t.tm_year    年（4 位）
# t.tm_mon     月（1-12）
# t.tm_mday    日（1-31）
# t.tm_hour    时（0-23）
# t.tm_min     分（0-59）
# t.tm_sec     秒（0-61，处理闰秒）
# t.tm_wday    周几（0=周一，6=周日）
# t.tm_yday    一年中第几天（1-366）
# t.tm_isdst   是否夏令时（-1=未知）
```

## 二、strftime 详细格式

```python
import time

t = time.localtime()

# 日期
time.strftime("%Y-%m-%d")           # 2024-06-24
time.strftime("%y%m%d")             # 240624
time.strftime("%d/%m/%Y")           # 24/06/2024（欧洲格式）

# 时间
time.strftime("%H:%M:%S")           # 14:30:45
time.strftime("%I:%M:%S %p")        # 02:30:45 PM（12 小时制）
time.strftime("%H:%M")              # 14:30

# 完整
time.strftime("%Y-%m-%d %H:%M:%S")  # 2024-06-24 14:30:45
time.strftime("%c")                  # Mon Jun 24 14:30:45 2024

# 自定义
time.strftime("Today is %A, %B %d, %Y")
# Today is Monday, June 24, 2024

# 中文
time.strftime("%Y年%m月%d日 %H时%M分%S秒")
# 2024年06月24日 14时30分45秒

# ISO 8601
time.strftime("%Y-%m-%dT%H:%M:%S")  # 2024-06-24T14:30:45
```

## 三、strptime 解析

```python
import time

# 解析 ISO 格式
t = time.strptime("2024-06-24", "%Y-%m-%d")

# 解析中文
t = time.strptime("2024年06月24日", "%Y年%m月%d日")

# 解析自定义
t = time.strptime("24/06/2024", "%d/%m/%Y")

# 解析 12 小时制
t = time.strptime("02:30:45 PM", "%I:%M:%S %p")
```

## 四、datetime 高级用法

```python
from datetime import datetime, timedelta, timezone

# 当前时间
now = datetime.now()
print(now.isoformat())          # '2024-06-24T14:30:45.123456'

# 时区
utc = timezone.utc
beijing = timezone(timedelta(hours=8))

dt = datetime.now(beijing)
print(dt.tzinfo)                # UTC+08:00

# 格式化
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%Y年%m月%d日"))

# 解析
dt = datetime.strptime("2024-06-24", "%Y-%m-%d")
dt = datetime.fromisoformat("2024-06-24T14:30:00")

# 时间运算
yesterday = now - timedelta(days=1)
next_year = now + timedelta(days=365)
two_hours_later = now + timedelta(hours=2)

# 差值
diff = next_year - now
print(diff.days, diff.seconds)

# 时间戳
ts = now.timestamp()              # float
dt = datetime.fromtimestamp(ts)   # 本地时区
dt = datetime.utcfromtimestamp(ts) # UTC

# 比较
if now > yesterday:
    print("now is after yesterday")

# 提取分量
print(now.year, now.month, now.day)
print(now.weekday())              # 周几（0=周一）
print(now.isoweekday())           # 周几（1=周一，7=周日）
print(now.date())                 # date 部分
print(now.time())                 # time 部分
```

## 五、时区处理（Python 3.9+ zoneinfo）

```python
from datetime import datetime
from zoneinfo import ZoneInfo

# 列出所有时区
from zoneinfo import available_timezones
print("Asia/Shanghai" in available_timezones())    # True

# 切换时区
shanghai = ZoneInfo("Asia/Shanghai")
tokyo = ZoneInfo("Asia/Tokyo")
nyc = ZoneInfo("America/New_York")

dt = datetime.now(shanghai)
print(dt.astimezone(tokyo))      # 转东京时间
print(dt.astimezone(nyc))        # 转纽约时间
```

## 六、时间运算示例

```python
from datetime import datetime, timedelta

# 计算年龄
birth = datetime(2000, 1, 1)
today = datetime.now()
age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

# 计算下个工作日
def next_weekday(d):
    while d.weekday() >= 5:  # 周末
        d += timedelta(days=1)
    return d

# 计算两个时间间隔
start = datetime(2024, 1, 1)
end = datetime(2024, 12, 31)
diff = end - start
print(f"全年 {diff.days} 天")

# 倒计时到周末
now = datetime.now()
days_to_weekend = 5 - now.weekday()
if days_to_weekend < 0:
    days_to_weekend += 7
print(f"距周末还有 {days_to_weekend} 天")
```

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）