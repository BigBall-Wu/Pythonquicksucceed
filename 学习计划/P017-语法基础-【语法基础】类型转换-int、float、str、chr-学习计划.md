---
title: "学习计划 P017 【语法基础】类型转换"
p_no: 17
category: 语法基础
created: 2026-06-24
updated: 2026-06-24
type: study-plan
---

# 学习计划 P017　【语法基础】类型转换

## 一、本节在课程中的位置

| 项目 | 内容 |
|------|------|
| 课程章节 | 第 17 集 / 共 100 集 |
| 分类 | 语法基础 |
| 视频时长 | 1773 秒（约 30 分钟） |
| 难度 | 基础 |

## 二、为什么先学这一节

这节是数据类型部分的核心补充。理解类型转换才能：
- 在不同数据类型间自由切换
- 处理用户输入（字符串 → 数字）
- 避免 `TypeError` 经典报错
- 为后续文件操作、API 调用打基础

## 三、本节要回答的核心问题

1. **类型转换函数有哪些？**
2. **int/float/str 互转的细节？**
3. **bool() 的陷阱？**
4. **list/tuple/set/dict 互转？**
5. **eval() 什么时候能用、什么时候危险？**

## 四、课本对照

本节课本对应《Python编程：从入门到实践》第2版 **2.4 数**。

课本讲了整数、浮点数的基础运算，但**类型转换函数**在课本中没有专门章节，需要本节补全。

## 五、具体学习步骤

### 第 1 步：类型转换函数全表（10 分钟）

```python
# 类型转换函数一览
# int(x)      → 整数（截断，不是四舍五入）
# float(x)    → 浮点数
# str(x)      → 字符串
# bool(x)     → 布尔值
# list(x)     → 列表
# tuple(x)    → 元组
# set(x)      → 集合
# chr(x)      → 整数 → 字符（如 65 → 'A'）
# ord(x)      → 字符 → 整数（如 'A' → 65）
# hex(x)      → 整数 → 十六进制字符串
# oct(x)      → 整数 → 八进制字符串
# bin(x)      → 整数 → 二进制字符串

# 示例
int(3.9)        # 3（截断）
float("3.14")   # 3.14
str(42)         # "42"
chr(65)         # 'A'
ord('A')        # 65
hex(255)        # '0xff'
oct(8)          # '0o10'
bin(10)         # '0b1010'
```

### 第 2 步：int() 的细节（15 分钟）

```python
# int() 截断小数（不是四舍五入）
int(3.9)           # 3
int(-3.9)          # -3

# int() 自动去空白
int("  42  ")      # 42

# ⚠️ 小数字符串不能直接 int()
int("42.0")        # ValueError!
int("42.0", 16)    # 不接受 base + 浮点

# int() 支持进制转换
int("ff", 16)      # 255（十六进制）
int("1010", 2)     # 10（二进制）
int("0xff", 0)     # 255（自动识别前缀）

# round() 是四舍五入（但 Python 3 用银行家舍入）
round(3.5)         # 4
round(2.5)         # 2（最近的偶数）
round(3.14159, 2)  # 3.14
```

### 第 3 步：bool() 的陷阱（15 分钟）

```python
# 任何非零、非空都是 True
bool(0)            # False
bool(0.0)          # False
bool("")           # False
bool([])           # False
bool({})           # False
bool(None)         # False

# ⚠️ 这些都是 True！
bool("False")      # True（字符串 "False" 非空）
bool(-1)           # True（非零）
bool([0])          # True（非空列表）
bool(" ")          # True（空格字符串）

# 实际应用：判断非空
if user_input:     # 等价于 if user_input != ""
    print("有输入")
```

### 第 4 步：str() vs repr()（10 分钟）

```python
# str：面向用户，可读性好
# repr：面向开发者，可以 eval 重建

s = "hello\nworld"
print(str(s))       # hello(换行)world
print(repr(s))      # 'hello\nworld'

# 自定义类示例
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(1, 2)
print(str(p))       # (1, 2)
print(repr(p))      # Point(1, 2)
```

### 第 5 步：list/tuple/set 互转（15 分钟）

```python
# tuple → list
list((1, 2, 3))             # [1, 2, 3]

# list → tuple
tuple([1, 2, 3])            # (1, 2, 3)

# 字符串 → 字符列表
list("hello")               # ['h', 'e', 'l', 'l', 'o']

# dict → 列表（默认取 key）
list({"a": 1, "b": 2})      # ['a', 'b']
list({"a": 1, "b": 2}.items())  # [('a', 1), ('b', 2)]
list({"a": 1, "b": 2}.keys())   # ['a', 'b']
list({"a": 1, "b": 2}.values()) # [1, 2]

# 去重用 set
list(set([1, 2, 2, 3]))     # [1, 2, 3]（顺序可能变化）
```

### 第 6 步：eval() 和 exec()（危险但有用）（15 分钟）

```python
# ⚠️ 警告：eval/exec 是安全漏洞！绝不要用在用户输入上

# eval：执行表达式返回结果
result = eval("3 + 4")      # 7
x = 10
eval("x * 2")               # 20

# exec：执行语句（不返回）
exec("x = 100")

# ❌ 危险示例：用户输入 os.system('rm -rf /') 会执行！
user_input = input()
result = eval(user_input)    # 绝对不要这样写！
```

### 第 7 步：自定义类型转换（10 分钟）

```python
# 实现 __int__、__float__、__str__ 等魔法方法
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __int__(self):
        return int(self.celsius)

    def __float__(self):
        return float(self.celsius)

    def __str__(self):
        return f"{self.celsius}°C"

t = Temperature(36.5)
int(t)      # 36
float(t)    # 36.5
str(t)      # "36.5°C"
```

## 六、这一节要掌握的知识点

- [ ] 类型转换函数全表（int/float/str/bool/list/tuple/set/chr/ord/hex/oct/bin）
- [ ] int() 截断而非四舍五入
- [ ] int() 支持进制转换
- [ ] bool() 的假值列表（0/0.0/""/[]/{}/None）
- [ ] str() vs repr() 的区别
- [ ] 容器类型互转（list/tuple/set/dict）
- [ ] eval() 的危险性和安全用法
- [ ] 自定义类的类型转换（__int__/__str__ 等）

## 七、动手练习

### 练习 1：类型转换速算

```python
# 写出下列表达式的结果（先猜，再运行验证）
print(int(3.7))           # ?
print(int("42"))          # ?
print(int("3.14"))        # ?
print(float("3.14"))      # ?
print(str(42))            # ?
print(bool(""))           # ?
print(bool(" "))          # ?
print(list("abc"))        # ?
print(list((1, 2, 3)))   # ?
print(set([1, 2, 2, 3])) # ?
```

### 练习 2：用户输入计算器

```python
# 用户输入两个数，输出它们的和
# 要求：处理类型转换和输入错误
num1 = input("第一个数: ")
num2 = input("第二个数: ")
# ... 实现代码
```

### 练习 3：完成课本 2.4 练习

完成课本第 2 章的动手试一试：
- 练习 2-8：数字 8
- 练习 2-9：最喜欢的数

## 八、自测题

- [ ] **Q1**：`int(3.7)` 和 `round(3.7)` 的结果分别是？
- [ ] **Q2**：哪些值在 `bool()` 中返回 `False`？
- [ ] **Q3**：`str()` 和 `repr()` 的区别是什么？
- [ ] **Q4**：为什么不能对用户输入使用 `eval()`？
- [ ] **Q5**：如何把字符串 `"hello"` 转换成列表 `['h', 'e', 'l', 'l', 'o']`？

## 九、参考资料

- 视频 BV1rpWjevEip P17
- 课本：《Python编程：从入门到实践》第2版 2.4 节

### 选读

- Python 官方文档 - 内置类型：https://docs.python.org/zh-cn/3/library/stdtypes.html
- Python 官方文档 - 内置函数：https://docs.python.org/zh-cn/3/library/functions.html

## 十、关联 Vault 笔记

- [[学习指南/P017-语法基础-【语法基础】类型转换]]
- [[学习计划/P016-语法基础-【语法基础】字典的常见操作二、集合的格式及使用-学习计划]]（上一节）
- [[学习计划/P018-语法基础-【语法基础】赋值、深浅拷贝、可变与不可变对象-学习计划]]（下一节）
- [[index]]

---

> **预计总时长**：90 分钟（视频 30 + 实操 60）
>
> **完成标志**：能熟练进行 int/float/str/bool 互转，理解 bool() 陷阱，能安全处理用户输入
