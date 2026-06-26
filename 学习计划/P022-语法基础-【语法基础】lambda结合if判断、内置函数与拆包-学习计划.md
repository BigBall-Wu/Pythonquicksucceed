---
title: "学习计划 P022 【语法基础】lambda 结合 if 判断、内置函数与拆包"
p_no: 22
category: 语法基础
created: 2026-06-24
updated: 2026-06-24
type: study-plan
---

# 学习计划 P022　【语法基础】lambda 结合 if 判断、内置函数与拆包

## 一、本节在课程中的位置

- **课程章节**：第 22 集 / 共 100 集
- **分类**：语法基础
- **视频时长**：2776 秒（约 46 分钟）⭐ 重点章节
- **难度**：入门

## 二、本节核心目标

> **lambda 是 Python 中最"紧凑"的函数**。一行的 lambda 在 sorted/filter/map 中能省大段代码。

学完后你能：
1. 写一行的 lambda 函数（含三元）
2. 用 lambda + map/filter/sorted 做数据处理
3. 写复杂的解包（嵌套、忽略值、命名）
4. 区分 lambda 和 def 的使用场景

## 三、课本对照

| 章节 | 行号范围 | 重点 |
|------|---------|------|
| 8.5 传递任意数量的实参 | L7912-L8078 | **核心**：*args / **kwargs |
| 9.4 导入类 | L9172-L9513 | 模块化组织 |

## 四、具体学习步骤

### 第 1 步：lambda 基础（10 分钟）

```python
# 普通函数
def add(a, b):
    return a + b

# 等价 lambda
add = lambda a, b: a + b

# 用 lambda
print(add(3, 5))                   # 8

# 立即调用（IIFE）
result = (lambda x, y: x * y)(3, 4)  # 12
```

### 第 2 步：lambda + 三元（10 分钟）

```python
# 简单分支
sgn = lambda x: "正" if x > 0 else ("负" if x < 0 else "零")
print(sgn(5))                       # 正
print(sgn(-3))                      # 负
print(sgn(0))                       # 零

# 数据处理
scores = [85, 42, 90, 67, 55]
results = list(map(lambda s: "及格" if s >= 60 else "不及格", scores))
# ['及格', '不及格', '及格', '及格', '不及格']

# 排序
students = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
by_age = sorted(students, key=lambda s: s[1])
# [('Bob', 20), ('Alice', 25), ('Charlie', 30)]
```

### 第 3 步：lambda + map/filter/zip/enumerate（10 分钟）

```python
nums = [1, 2, 3, 4, 5]

# map：每个元素应用函数
squared = list(map(lambda x: x ** 2, nums))
# [1, 4, 9, 16, 25]

# filter：筛选
evens = list(filter(lambda x: x % 2 == 0, nums))
# [2, 4]

# zip：并行遍历
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name}: {age}")

# enumerate：索引 + 值
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")
```

### 第 4 步：解包的 5 种高级用法（10 分钟）

```python
# 1. 基础解包
a, b, c = (1, 2, 3)

# 2. * 收集剩余
first, *rest, last = [1, 2, 3, 4, 5]
# first=1, rest=[2,3,4], last=5

# 3. 忽略某些值
a, _, _, d = (1, 2, 3, 4)         # 忽略中间值

# 4. 函数调用解包
def func(a, b, c):
    return a + b + c

args = (1, 2, 3)
print(func(*args))                  # 6

kwargs = {"a": 1, "b": 2, "c": 3}
print(func(**kwargs))                # 6

# 5. 字典合并
defaults = {"host": "localhost", "port": 80}
overrides = {"port": 8080, "debug": True}
config = {**defaults, **overrides}
# {'host': 'localhost', 'port': 8080, 'debug': True}
```

### 第 5 步：实战 - 数据处理 pipeline（10 分钟）

```python
# 销售数据
sales = [
    {"product": "A", "price": 100, "qty": 5, "region": "north"},
    {"product": "B", "price": 200, "qty": 3, "region": "south"},
    {"product": "A", "price": 100, "qty": 8, "region": "north"},
    {"product": "C", "price": 50, "qty": 10, "region": "east"},
    {"product": "B", "price": 200, "qty": 2, "region": "south"},
]

# 1. 计算总金额
def total(s):
    return s["price"] * s["qty"]

totals = list(map(total, sales))
print(f"总金额：{sum(totals)}")

# 2. 提取产品 A 的销售
a_sales = list(filter(lambda s: s["product"] == "A", sales))
print(f"A 销售：{sum(map(total, a_sales))}")

# 3. 按区域分组
from collections import defaultdict
by_region = defaultdict(int)
for s in sales:
    by_region[s["region"]] += total(s)
print(dict(by_region))

# 4. 按总金额降序
sales_with_total = [{"s": s, "t": total(s)} for s in sales]
ranked = sorted(sales_with_total, key=lambda x: -x["t"])
for item in ranked:
    print(f"{item['s']['product']}: {item['t']}")
```

### 第 6 步：lambda vs def（10 分钟）

```python
# 用 def：复杂逻辑
def get_user_status(age, is_student):
    if age < 18:
        return "未成年"
    if is_student:
        return "学生"
    return "成年人"

# 用 lambda：简单一行
get_user_status = lambda age, is_student: (
    "未成年" if age < 18 else ("学生" if is_student else "成年人")
)

# 经验法则：
# - 一行能写完：lambda
# - 多行/有文档：def
# - 需要调试（pdb 断点）：def
# - lambda 用作参数：map/filter/sorted
# - 需要测试：def
```

## 五、这一节要掌握的知识点

- [ ] 8.5 传递任意数量的实参
- [ ] lambda 表达式
- [ ] lambda + 三元
- [ ] map / filter / sorted + lambda
- [ ] zip / enumerate
- [ ] 元组 / 列表 / 字典解包
- [ ] *args / **kwargs 收集和展开
- [ ] 字典合并
- [ ] lambda vs def 的选择
- [ ] lambda 的限制（单表达式）

## 六、动手练习

### 练习 1：成绩排序

```python
students = [
    {"name": "Alice", "math": 85, "english": 90},
    {"name": "Bob", "math": 92, "english": 78},
    {"name": "Charlie", "math": 78, "english": 95},
]
# 按总分排序
ranked = sorted(students, key=lambda s: -(s["math"] + s["english"]))
```

### 练习 2：解包应用

```python
data = [
    ("Alice", 25, "Beijing"),
    ("Bob", 30, "Shanghai"),
    ("Charlie", 35, "Guangzhou"),
]
# 用 for 解包
for name, age, city in data:
    print(f"{name} ({age}) 在 {city}")

# 提取第一个
first_name, *_ = data
```

### 练习 3：lambda + filter

```python
# 过滤出偶数
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, nums))
```

### 练习 4：完成课本「动手试一试」

课本 L8000 附近的练习 8-12（三明治）、8-14（汽车）。至少做 1 题。

## 七、自测题

- [ ] **Q1**：lambda 的限制是什么？
- [ ] **Q2**：lambda + 三元的语法？
- [ ] **Q3**：`map` 和列表推导式的选择？
- [ ] **Q4**：解包 `*` 和 `**` 的区别？
- [ ] **Q5**：什么时候用 lambda vs def？

## 八、参考资料

### 必读
- 课本 8.5 节（L7912-L8078）
- 视频 BV1rpWjevEip P22（46 分钟）

### 选读
- Python 官方 lambda：https://docs.python.org/zh-cn/3/tutorial/controlflow.html#lambda-expressions
- functools 工具：https://docs.python.org/zh-cn/3/library/functools.html

## 九、关联 Vault 笔记

- [[Python编程-从入门到实践-第2版]]
- [[学习指南/P022-语法基础-【语法基础】lambda结合if判断、内置函数与拆包]]
- [[学习计划/P021-语法基础-【语法基础】作用域、匿名函数与匿名函数的参数-学习计划]]（上一节）

---

> **预计总时长**：110 分钟（视频 46 + 实操 64）
>
> **完成标志**：能熟练写 lambda + 解包，写出简洁 Pythonic 的数据处理代码