# -*- coding: utf-8 -*-
"""补全知识库 - 第二批：字符串/列表/类型/作用域/装饰器"""
SUPPLEMENT_2 = {

"str_encoding": """\
## 一、字符编码基础

### ASCII / Unicode / UTF-8 关系

- **ASCII**：1 字节（0-127），只覆盖英文和常用符号
- **Unicode**：字符集，给每个字符一个码点（如 '中' = U+4E2D）
- **UTF-8**：Unicode 的可变长编码（1-4 字节），英文 1 字节，中文 3 字节

### Python 3 的 str

Python 3 的 `str` 是 **Unicode 字符串**（内存中）：

```python
s = "你好世界"
print(type(s))                # <class 'str'>
print(len(s))                 # 4
print(s.encode("utf-8"))      # b'\\xe4\\xbd\\xa0\\xe5\\xa5\\xbd\\xe4\\xb8\\x96\\xe7\\x95\\x8c'
print(s.encode("gbk"))        # b'\\xc4\\xe3\\xba\\xc3\\xca\\xc0\\xbd\\xe7'

# 解码
b = b'\\xe4\\xbd\\xa0\\xe5\\xa5\\xbd'
print(b.decode("utf-8"))      # 你好
```

### 常见编码错误

```python
# UnicodeEncodeError：编码时不支持
"你好".encode("ascii")
# UnicodeEncodeError: 'ascii' codec can't encode characters

# 解决：明确指定目标编码
"你好".encode("ascii", errors="ignore")    # b''（丢弃）
"你好".encode("ascii", errors="replace")   # b'??'（替换为 ?）

# UnicodeDecodeError：解码时字节不匹配
b"\\xc4\\xe3\\xba\\xc3".decode("utf-8")
# UnicodeDecodeError

# 解决：用对的编码
b"\\xc4\\xe3\\xba\\xc3".decode("gbk")     # 你好
```

### 文件 I/O 中的编码

```python
# 默认编码可能是系统编码（Windows 是 GBK，Linux/Mac 是 UTF-8）
# 建议显式指定
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

with open("data.txt", "w", encoding="utf-8") as f:
    f.write("中文内容")
```

## 二、字符串常用操作（完整列表）

```python
s = "Hello, World!"

# 1. 大小写转换
s.upper()        # "HELLO, WORLD!"
s.lower()        # "hello, world!"
s.capitalize()   # "Hello, world!"（首字母大写）
s.title()        # "Hello, World!"（每个单词首字母大写）
s.swapcase()     # "hELLO, wORLD!"

# 2. 去除空白
"  hello  ".strip()       # "hello"
"  hello  ".lstrip()      # "hello  "
"  hello  ".rstrip()      # "  hello"

# 3. 对齐填充
"hi".center(10, "-")      # "----hi----"
"hi".ljust(10, ".")        # "hi........"
"hi".rjust(10, ".")        # "........hi"
"42".zfill(5)              # "00042"

# 4. 查找替换
s.find("World")            # 7（找到返回索引）
s.find("XXX")              # -1（未找到）
s.index("World")           # 7（未找到会抛 ValueError）
s.rfind("o")               # 8（从右往左找）
s.count("o")               # 2
s.replace("World", "Python")  # "Hello, Python!"
s.replace("o", "0", 1)     # 只替换第一个 "Hello, World!"

# 5. 分割拼接
"a,b,c,d".split(",")             # ['a', 'b', 'c', 'd']
"a,b,,c".split(",")              # ['a', 'b', '', 'c']
"line1\\nline2\\nline3".splitlines()  # ['line1', 'line2', 'line3']
"-".join(["2024", "06", "24"])   # "2024-06-24"

# 6. 判断（返回 bool）
"abc123".isalnum()         # True（字母数字）
"abc".isalpha()            # True
"123".isdigit()            # True
" ".isspace()              # True
"Hello".istitle()          # True
"hello".islower()          # True
"HELLO".isupper()          # True

# 7. 翻译表（高级替换）
trans = str.maketrans("aeiou", "12345")
"apple".translate(trans)   # "1ppl2"

# 8. 前缀/后缀
"hello.py".startswith("hello")   # True
"hello.py".endswith(".py")       # True
```

## 三、Python 字符串不可变

```python
s = "hello"
# s[0] = "H"    # ❌ TypeError: 'str' does not support item assignment
s = "H" + s[1:]  # ✅ 创建新字符串
print(s)          # "Hello"
```
""",

"str_methods": """\
## 一、字符串查找和判断方法

```python
s = "Hello, World!"

# 查找
s.find("World")        # 7（找到返回索引）
s.find("world")        # -1（区分大小写，找不到返回 -1）
s.rfind("o")           # 8（从右往左找）
s.index("World")       # 7（找不到抛 ValueError）

# 判断开头/结尾
s.startswith("Hello")  # True
s.endswith("!")        # True
s.startswith(("Hi", "Hello"))  # True（元组表示任一）

# 内容判断
"abc123".isalnum()    # True（字母或数字）
"abc".isalpha()       # True（纯字母）
"123".isdigit()       # True（纯数字）
" ".isspace()         # True（纯空白）
```

## 二、字符串修改方法

```python
s = "Hello, World!"

# 大小写
s.upper()              # "HELLO, WORLD!"
s.lower()              # "hello, world!"
s.capitalize()         # "Hello, world!"
s.title()              # "Hello, World!"
s.swapcase()           # "hELLO, wORLD!"

# 替换
s.replace("o", "0")           # "Hell0, W0rld!"（全部替换）
s.replace("o", "0", 1)        # "Hell0, World!"（只替换第一个）
s.replace("o", "0", -1)       # -1 表示全部（默认）

# 删除空白
"  hello  ".strip()     # "hello"（两端）
"  hello  ".lstrip()    # "hello  "（左端）
"  hello  ".rstrip()    # "  hello"（右端）
"**hello**".strip("*")  # "hello"（指定字符）

# 对齐填充
"hi".center(10, "-")    # "----hi----"
"hi".ljust(10)          # "hi        "
"hi".rjust(10)          # "        hi"
"42".zfill(5)           # "00042"

# 分割
"a,b,c".split(",")               # ['a', 'b', 'c']
"a,b,,c".split(",")              # ['a', 'b', '', 'c']
"a|b|c".split("|", 1)            # ['a', 'b|c']（最多分 1 次）
"  hello  ".split()              # ['hello']（默认按任意空白分）

# 拼接
",".join(["a", "b", "c"])        # "a,b,c"
"".join(["a", "b", "c"])         # "abc"
"-".join("abc")                  # "a-b-c"

# 翻译（批量替换）
table = str.maketrans("aeio", "4310")
"apple".translate(table)         # "1ppl3"
```

## 三、字符串 vs 字节 vs 字符

```python
# str：Unicode 字符串（Python 3 默认）
text = "你好"
print(type(text))        # <class 'str'>

# bytes：字节串（用于网络、文件）
data = b"hello"
print(type(data))        # <class 'bytes'>

# 转换
text.encode("utf-8")     # str → bytes
data.decode("utf-8")     # bytes → str

# 字符与码点
print(ord("A"))          # 65
print(chr(65))           # "A"
print(ord("中"))         # 20013
```
""",

"list_comprehension": """\
## 一、列表推导式基础

**列表推导式**（List Comprehension）：用一行代码创建列表

```python
# 传统方法
squares = []
for x in range(10):
    squares.append(x ** 2)

# 列表推导式（推荐）
squares = [x ** 2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## 二、语法格式

```python
[expression for item in iterable if condition]
```

### 三种用法

```python
# 1. 简单映射
nums = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in nums]
# [1, 4, 9, 16, 25]

# 2. 带过滤
evens = [x for x in nums if x % 2 == 0]
# [2, 4]

# 3. 完整形式
processed = [x ** 2 if x % 2 == 0 else x for x in nums]
# [1, 2, 9, 4, 25]
```

## 三、实战例子

```python
# 1. 字符串处理
words = ["hello", "world", "python"]
upper_words = [w.upper() for w in words]
# ['HELLO', 'WORLD', 'PYTHON']

# 2. 矩阵转置
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# 3. 文件处理
import os
files = [f for f in os.listdir(".") if f.endswith(".py")]

# 4. 展平嵌套列表
nested = [[1, 2], [3, 4], [5, 6]]
flat = [x for sublist in nested for x in sublist]
# [1, 2, 3, 4, 5, 6]

# 5. 双层循环（笛卡尔积）
colors = ["红", "蓝"]
sizes = ["S", "M", "L"]
combos = [(c, s) for c in colors for s in sizes]
# [('红', 'S'), ('红', 'M'), ('红', 'L'), ('蓝', 'S'), ('蓝', 'M'), ('蓝', 'L')]

# 6. 字典推导式
names = ["Alice", "Bob", "Charlie"]
lengths = {name: len(name) for name in names}
# {'Alice': 5, 'Bob': 3, 'Charlie': 7}

# 7. 集合推导式
nums = [1, 2, 2, 3, 3, 3]
unique_squares = {x ** 2 for x in nums}
# {1, 4, 9}
```

## 四、性能对比

```python
import time

# 列表推导式比循环 + append 快约 30-50%
# 测试
n = 1_000_000

start = time.time()
result = []
for i in range(n):
    result.append(i ** 2)
print(f"循环: {time.time() - start:.3f}s")

start = time.time()
result = [i ** 2 for i in range(n)]
print(f"推导式: {time.time() - start:.3f}s")
```

## 五、何时不用列表推导式

- 逻辑复杂（超过 2 层循环）
- 副作用（print、修改全局变量）
- 可读性差

```python
# ❌ 不要这样写
result = [func(x) for x in data if x > 0 if x < 100 if x % 2 == 0]

# ✅ 拆成循环
result = []
for x in data:
    if 0 < x < 100 and x % 2 == 0:
        result.append(func(x))
```
""",

"set_basics": """\
## 一、集合（set）的本质

**集合**是 **无序、不重复** 的元素集合：

```python
# 创建
s = {1, 2, 3}                    # 字面量
s = set([1, 2, 3])               # 构造器
s = set()                        # 空集合（不能用 {}，那是空字典）
print(type({}))                  # <class 'dict'>

# 自动去重
s = {1, 2, 2, 3, 3, 3}
print(s)                         # {1, 2, 3}
```

## 二、集合操作

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 1. 集合运算
a | b                  # 并集 {1, 2, 3, 4, 5, 6}
a & b                  # 交集 {3, 4}
a - b                  # 差集 {1, 2}（a 有 b 无）
a ^ b                  # 对称差 {1, 2, 5, 6}（不同时在两边）

# 方法形式
a.union(b)             # 并集
a.intersection(b)      # 交集
a.difference(b)        # 差集
a.symmetric_difference(b)  # 对称差

# 2. 比较
a.issubset(b)          # a 是否是 b 的子集
a.issuperset(b)        # a 是否是 b 的超集
a.isdisjoint(b)        # a 和 b 是否不相交
```

## 三、增删改查

```python
s = {1, 2, 3}

# 添加
s.add(4)               # {1, 2, 3, 4}
s.update([5, 6, 7])    # {1, 2, 3, 4, 5, 6, 7}（添加多个）

# 删除
s.remove(3)            # {1, 2, 4, 5, 6, 7}（不存在抛 KeyError）
s.discard(99)          # 不存在也不报错
s.pop()                # 随机删除一个（因为无序）
s.clear()              # 清空
```

## 四、应用场景

```python
# 1. 去重（最常用）
nums = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(nums))    # [1, 2, 3, 4]（顺序可能改变）

# 保持顺序的去重
unique = []
seen = set()
for x in nums:
    if x not in seen:
        unique.append(x)
        seen.add(x)

# 2. 成员测试（O(1) 比 list 的 O(n) 快）
allowed = {"admin", "user", "guest"}
if username in allowed:     # O(1)
    print("登录")

# 3. 找两个列表的共同元素
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
# {4, 5}
```

## 五、不可变集合 frozenset

```python
# frozenset：不可变集合，可以作为字典 key
fs = frozenset([1, 2, 3])
d = {fs: "value"}    # ✅ 可以作为 key
# fs.add(4)           # ❌ AttributeError
```

## 六、集合推导式

```python
nums = [1, 2, 3, 4, 5]
squares = {x ** 2 for x in nums}
# {1, 4, 9, 16, 25}
```
""",

"type_conversion": """\
## 一、类型转换函数全表

| 函数 | 作用 | 例子 | 结果 |
|------|------|------|------|
| `int(x)` | 转整数 | `int("42")` | 42 |
| `float(x)` | 转浮点数 | `float("3.14")` | 3.14 |
| `str(x)` | 转字符串 | `str(42)` | "42" |
| `bool(x)` | 转布尔 | `bool(0)` | False |
| `list(x)` | 转列表 | `list((1,2,3))` | [1,2,3] |
| `tuple(x)` | 转元组 | `tuple([1,2])` | (1,2) |
| `set(x)` | 转集合 | `set([1,2,2])` | {1,2} |
| `dict(x)` | 转字典 | `dict(a=1)` | {"a":1} |
| `chr(x)` | 整数 → 字符 | `chr(65)` | "A" |
| `ord(x)` | 字符 → 整数 | `ord("A")` | 65 |
| `hex(x)` | 整数 → 十六进制 | `hex(255)` | "0xff" |
| `oct(x)` | 整数 → 八进制 | `oct(8)` | "0o10" |
| `bin(x)` | 整数 → 二进制 | `bin(10)` | "0b1010" |

## 二、细节与陷阱

### int / float

```python
# int() 截断小数（不是四舍五入）
int(3.9)           # 3
int(-3.9)          # -3
int("  42  ")      # 42（自动去空白）
int("42.0")        # ❌ ValueError
int("42.0", 16)    # ❌ 不接受 base + 浮点

# int() 支持进制
int("ff", 16)      # 255
int("1010", 2)     # 10
int("0xff", 0)     # 255（自动识别前缀和进制）

# round() 是四舍五入（但银行家舍入）
round(3.5)         # 4
round(2.5)         # 2（最近的偶数）
round(3.14159, 2)  # 3.14
```

### bool 的陷阱

```python
# 任何非零、非空都是 True
bool(0)            # False
bool(0.0)          # False
bool("")           # False
bool([])           # False
bool({})           # False
bool(None)         # False
bool("False")      # True（字符串 "False" 是非空）
bool(-1)           # True
bool([0])          # True
```

### str() vs repr()

```python
# str：面向用户，可读性好
# repr：面向开发者，可以 eval 重建
s = "hello\\nworld"
print(str(s))       # hello（换行）world
print(repr(s))      # 'hello\\nworld'

# 自定义类
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

### list / tuple / set 互转

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
```

### eval() 和 exec()（小心使用！）

```python
# eval：执行表达式返回结果
result = eval("3 + 4")      # 7
x = 10
eval("x * 2")               # 20

# exec：执行语句（不返回）
exec("x = 100")

# ⚠️ 警告：eval/exec 是安全漏洞！绝不要用在用户输入上
user_input = input()
result = eval(user_input)    # ❌ 用户输入 os.system('rm -rf /') 会执行！
```

## 三、自定义类型转换

```python
# 实现 __int__、__float__、__str__ 等魔法方法
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    def __int__(self):
        return int(self.celsius)
    def __str__(self):
        return f"{self.celsius}°C"

t = Temperature(36.5)
int(t)      # 36
str(t)      # "36.5°C"
```
""",

"deep_copy": """\
## 一、Python 的赋值本质

**关键认知**：Python 变量是"标签"不是"盒子"。

```python
a = [1, 2, 3]
b = a                  # b 不是 a 的副本！是同一个列表的两个名字
print(a is b)          # True（同一个对象）
b.append(4)
print(a)               # [1, 2, 3, 4] ← a 也变了！
```

## 二、浅拷贝（shallow copy）

```python
import copy

original = [1, 2, [3, 4]]

# 三种浅拷贝方式
shallow1 = original.copy()
shallow2 = original[:]
shallow3 = list(original)
shallow4 = copy.copy(original)

# 浅拷贝只复制一层
shallow1.append(99)
print(original)        # [1, 2, [3, 4]] ← 顶层独立
print(shallow1)        # [1, 2, [3, 4], 99]

shallow1[2].append(5)
print(original)        # [1, 2, [3, 4, 5]] ← 嵌套对象还是共享！
```

## 三、深拷贝（deep copy）

```python
import copy

original = [1, 2, [3, 4]]
deep = copy.deepcopy(original)

deep[2].append(5)
print(original)        # [1, 2, [3, 4]] ← 完全独立
print(deep)            # [1, 2, [3, 4, 5]]
```

## 四、可变 vs 不可变对象

| 类型 | 可变？ | 例子 |
|------|--------|------|
| `int` `float` `bool` `str` | ❌ 不可变 | `x = 5; x = 6`（其实是创建新对象） |
| `tuple` `frozenset` | ❌ 不可变 | 不能 `t[0] = 1` |
| `list` `dict` `set` | ✅ 可变 | 可以原地修改 |
| 自定义类（默认） | ✅ 可变 | 需要 `__slots__` 才不可变 |

```python
# 不可变对象的"修改"其实是创建新对象
x = 5
print(id(x))            # 140234567890
x = x + 1               # 创建新 int 6
print(id(x))            # 140234567902（不同对象）

# 不可变对象天然不需要拷贝
a = "hello"
b = a                   # 安全！因为 str 不可变
b = b.upper()           # a 不会变
print(a)                # "hello"
```

## 五、传参语义：传引用（call by object reference）

```python
# Python 既不是传值也不是传引用，是"传对象引用"
def modify(lst):
    lst.append(99)     # 影响外部
    return lst

my_list = [1, 2, 3]
modify(my_list)
print(my_list)          # [1, 2, 3, 99]

def reassign(lst):
    lst = [9, 9, 9]     # 重新绑定，不影响外部
    return lst

my_list = [1, 2, 3]
reassign(my_list)
print(my_list)          # [1, 2, 3]
```

## 六、is 与 == 的区别

```python
# == 比较值
# is 比较身份（是否是同一个对象）

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)           # True（值相等）
print(a is b)           # False（不同对象）

# 不可变小整数和短字符串会被缓存
x = 256
y = 256
print(x is y)           # True（缓存）

x = 257
y = 257
print(x is y)           # False（不缓存）
```

## 七、性能影响

```python
# 浅拷贝耗时
import time, copy
big_list = list(range(100000))

start = time.time()
shallow = big_list.copy()
print(f"浅拷贝: {time.time() - start:.4f}s")

start = time.time()
deep = copy.deepcopy([[i] for i in range(100000)])
print(f"深拷贝: {time.time() - start:.4f}s")
# 深拷贝比浅拷贝慢 10-100 倍
```
""",

"scope_legb": """\
## 一、Python 作用域规则（LEGB）

Python 查找变量的顺序：**L → E → G → B**

| 字母 | 名称 | 含义 |
|------|------|------|
| L | Local | 当前函数内部的局部作用域 |
| E | Enclosing | 嵌套函数的外部函数作用域 |
| G | Global | 模块全局作用域 |
| B | Built-in | Python 内置作用域 |

```python
x = "global"           # G

def outer():
    x = "enclosing"    # E
    def inner():
        x = "local"    # L
        print(x)       # "local"
    inner()
    print(x)           # "enclosing"

outer()
print(x)               # "global"
```

## 二、global 关键字

```python
x = 10

def modify():
    global x            # 声明使用全局 x
    x = 20              # 修改全局变量

modify()
print(x)                # 20
```

**没有 global 会怎样**：

```python
x = 10

def modify():
    x = 20              # 创建新的局部变量，不影响全局

modify()
print(x)                # 10
```

## 三、nonlocal 关键字（Python 3+）

```python
def outer():
    count = 0
    def inner():
        nonlocal count      # 声明使用外层（而非全局）
        count += 1          # 修改外层变量
    inner()
    inner()
    print(count)            # 2

outer()
```

## 四、闭包（Closure）

```python
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = make_counter()
print(c())            # 1
print(c())            # 2
print(c())            # 3
```

**闭包三要素**：
1. 嵌套函数
2. 内层函数引用外层函数的变量
3. 外层函数返回内层函数

## 五、内置作用域

```python
# Python 内置的名字（不导入也能用）
print(len, max, min, sum, sorted, range, list, dict, set)
# <built-in function len> ...

# 查看所有内置
import builtins
print(dir(builtins))
# ['ArithmeticError', 'AssertionError', ..., 'len', 'list', ...]

# 不要覆盖内置名！
# ❌ list = [1, 2, 3]  # 之后 list() 函数就用不了了
# ✅ my_list = [1, 2, 3]
```

## 六、最佳实践

```python
# 1. 尽量少用全局变量（难调试）
# 2. 函数应该通过参数和返回值通信
# 3. 必须修改全局状态时，明确用 global
# 4. 闭包用于工厂函数、装饰器
```
""",

"lambda_unpack": """\
## 一、lambda 表达式

**lambda** 是匿名函数（一行的小函数）：

```python
# 普通函数
def add(a, b):
    return a + b

# 等价 lambda
add = lambda a, b: a + b

# 调用
print(add(3, 5))       # 8
```

## 二、lambda 的限制

- 只能包含 **单个表达式**（不能有语句）
- 不能有 `return`（表达式本身就是返回值）
- 不能包含多行逻辑

```python
# ❌ 不行
# f = lambda x:
#     y = x + 1       # 不允许赋值语句
#     return y

# ✅ 可以（单表达式）
f = lambda x: x + 1
```

## 三、lambda 实战场景

### 1. 与 sorted 配合

```python
# 按第二个元素排序
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda p: p[1])
# [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# 按字符串长度排序
words = ['apple', 'fig', 'banana']
words.sort(key=lambda w: len(w))
# ['fig', 'apple', 'banana']
```

### 2. 与 map 配合

```python
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, nums))
# [1, 4, 9, 16, 25]
```

### 3. 与 filter 配合

```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
# [2, 4, 6]
```

### 4. 与 reduce 配合（functools）

```python
from functools import reduce
nums = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, nums)
# 15
```

## 四、序列拆包（Unpacking）

```python
# 1. 基本拆包
a, b, c = [1, 2, 3]
a, b, c = (1, 2, 3)
a, b, c = "abc"

# 2. 扩展拆包（*）
first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2,3,4], last=5

first, *rest = [1, 2, 3]
# first=1, rest=[2, 3]

*head, last = [1, 2, 3]
# head=[1, 2], last=3

# 3. 字典拆包
d = {"name": "Alice", "age": 25}
print({**d, "city": "Beijing"})
# {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 函数调用拆包
def greet(name, age):
    print(f"{name} is {age}")

greet(**d)             # Alice is 25

# 列表/元组拆包
nums = [1, 2, 3]
print(*nums)           # 1 2 3

args = ["Alice", 25]
greet(*args)           # Alice is 25
```

## 五、lambda 与 def 的选择

```python
# ✅ 适合用 lambda：简单、一次性、内嵌使用
sorted(data, key=lambda x: x.score)

# ✅ 适合用 def：有名字、复杂逻辑、会被复用
def get_score(item):
    if item.active:
        return item.score * 2
    return item.score
```

## 六、lambda 与三元运算符

```python
# lambda 里可以用三元
sgn = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"
print(sgn(5))         # positive
print(sgn(-3))        # negative
print(sgn(0))         # zero
```
""",

"builtin_functions": """\
## 一、Python 内置函数分类速查

### 数值类

| 函数 | 作用 | 例子 |
|------|------|------|
| `abs(x)` | 绝对值 | `abs(-5)` → 5 |
| `round(x, n)` | 四舍五入 | `round(3.1415, 2)` → 3.14 |
| `pow(x, y)` | 幂 | `pow(2, 10)` → 1024 |
| `divmod(a, b)` | 商和余 | `divmod(10, 3)` → (3, 1) |
| `sum(iter)` | 求和 | `sum([1,2,3])` → 6 |
| `min(iter)` | 最小值 | `min([1,5,3])` → 1 |
| `max(iter)` | 最大值 | `max([1,5,3])` → 5 |

### 序列类

| 函数 | 作用 |
|------|------|
| `len(s)` | 长度 |
| `sorted(iter, key, reverse)` | 排序返回新列表 |
| `reversed(seq)` | 反转 |
| `enumerate(iter, start)` | 索引-元素对 |
| `zip(a, b)` | 配对 |
| `map(func, iter)` | 映射 |
| `filter(func, iter)` | 过滤 |
| `all(iter)` | 全部为真 |
| `any(iter)` | 任一为真 |
| `slice(start, stop, step)` | 切片对象 |

### 类型转换类

| 函数 | 作用 |
|------|------|
| `int()`, `float()`, `str()`, `bool()` | 基本类型 |
| `list()`, `tuple()`, `set()`, `dict()` | 容器 |
| `chr()`, `ord()` | 字符/码点 |
| `bin()`, `oct()`, `hex()` | 进制 |
| `bytes()`, `bytearray()` | 字节串 |

### I/O 类

| 函数 | 作用 |
|------|------|
| `print(*args, sep, end, file, flush)` | 输出 |
| `input(prompt)` | 读取一行 |
| `open(file, mode, encoding)` | 打开文件 |
| `format(value, spec)` | 格式化 |

### 对象/反射类

| 函数 | 作用 |
|------|------|
| `type(obj)` | 类型 |
| `isinstance(obj, cls)` | 是否是某类实例 |
| `issubclass(sub, sup)` | 是否是子类 |
| `hasattr(obj, name)` | 是否有属性 |
| `getattr(obj, name, default)` | 获取属性 |
| `setattr(obj, name, value)` | 设置属性 |
| `delattr(obj, name)` | 删除属性 |
| `callable(obj)` | 是否可调用 |
| `id(obj)` | 对象身份（内存地址） |
| `dir(obj)` | 所有属性名 |
| `vars(obj)` | `obj.__dict__` |
| `help(obj)` | 帮助 |

### 高阶函数

| 函数 | 作用 |
|------|------|
| `map(func, *iters)` | 应用函数 |
| `filter(func, iter)` | 过滤 |
| `reduce(func, iter, init)` | 累积（在 functools） |
| `partial(func, *args)` | 偏函数（在 functools） |

### 其他

| 函数 | 作用 |
|------|------|
| `range(start, stop, step)` | 数字序列 |
| `iter(obj)` | 迭代器 |
| `next(iter)` | 下一个元素 |
| `reversed(seq)` | 反向迭代 |
| `hash(obj)` | 哈希值 |
| `repr(obj)` | 开发者字符串 |
| `globals()` | 全局名字字典 |
| `locals()` | 局部名字字典 |

## 二、高频使用例子

```python
# enumerate：同时拿索引和元素
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# zip：配对多个列表
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name} is {age}")
# Alice is 25
# Bob is 30

# all/any
nums = [1, 2, 3, 4, 5]
print(all(x > 0 for x in nums))   # True（全部 > 0）
print(any(x > 10 for x in nums))  # False（没有一个 > 10）

# sorted 高级用法
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
]
by_score = sorted(students, key=lambda s: s["score"], reverse=True)
# Bob(92), Alice(85), Charlie(78)
```

## 三、查看完整列表

```python
import builtins
print([x for x in dir(builtins) if not x.startswith("_")])
```
""",

"module_package": """\
## 一、模块（Module）vs 包（Package）

| 概念 | 含义 | 文件形式 |
|------|------|---------|
| 模块 | 一个 .py 文件 | `utils.py` |
| 包 | 含 `__init__.py` 的目录 | `mypackage/` |
| 库 | 多个包/模块的集合 | 广义概念 |

```
mypackage/                  # 包
├── __init__.py            # 包的初始化（可以为空）
├── module_a.py            # 子模块
├── module_b.py
└── subpackage/            # 子包
    ├── __init__.py
    └── module_c.py
```

## 二、import 的四种方式

```python
# 1. 导入整个模块
import math
print(math.sqrt(16))        # 4.0

# 2. 导入并起别名
import numpy as np
print(np.array([1, 2, 3]))

# 3. 从模块导入特定名字
from math import sqrt, pi
print(sqrt(16))             # 4.0
print(pi)                   # 3.1415926...

# 4. 导入所有（不推荐，会污染命名空间）
from math import *
print(sqrt(16))

# 5. 导入包
import mypackage.module_a
from mypackage import module_a
from mypackage.module_a import some_function
```

## 三、`__init__.py` 的作用

```python
# mypackage/__init__.py

# 1. 标识这是一个包（Python 3.3+ 可以没有，但建议保留）
# 2. 可以写包级初始化代码
print("mypackage 已加载")

# 3. 可以在 `from mypackage import *` 时控制导出哪些名字
__all__ = ["ClassA", "function_b"]

# 4. 简化导入路径
from .module_a import ClassA
from .module_b import function_b
# 这样用户可以 from mypackage import ClassA
```

## 四、`__name__` 变量

```python
# my_module.py
def main():
    print("作为主程序运行")

if __name__ == "__main__":
    main()                  # 只在直接运行本文件时执行
```

```bash
python my_module.py        # 输出 "作为主程序运行"
```

```python
import my_module            # 不输出（因为 __name__ 是 "my_module"）
```

## 五、搜索路径（sys.path）

```python
import sys
print(sys.path)
# ['当前目录', 'site-packages', ...]

# 查看模块位置
import numpy
print(numpy.__file__)       # 'C:\\Python311\\lib\\site-packages\\numpy\\...'

# 添加自定义路径
sys.path.append("/my/custom/path")
```

## 六、自定义模块示例

```python
# utils.py
"""工具模块"""

PI = 3.14159

def add(a, b):
    return a + b

class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, x):
        self.result += x
        return self
```

```python
# main.py
import utils
print(utils.PI)             # 3.14159
print(utils.add(3, 5))      # 8

calc = utils.Calculator()
calc.add(10).add(20)
print(calc.result)          # 30
```

## 七、常用内置模块

| 模块 | 用途 |
|------|------|
| `os` | 操作系统接口 |
| `sys` | Python 解释器 |
| `math` | 数学函数 |
| `random` | 随机数 |
| `datetime` | 日期时间 |
| `json` | JSON 解析 |
| `re` | 正则表达式 |
| `collections` | 高级容器 |
| `itertools` | 迭代工具 |
| `functools` | 函数工具 |
| `pathlib` | 路径处理 |
| `logging` | 日志 |

## 八、安装第三方包（pip）

```bash
# 安装
pip install requests

# 指定版本
pip install requests==2.28.0

# 升级
pip install --upgrade requests

# 卸载
pip uninstall requests

# 查看已安装
pip list

# 国内镜像（快）
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
```

## 九、`__all__` 用来控制 `from xxx import *`

```python
# mymodule.py
__all__ = ["public_func", "PublicClass"]
# private_func 不会被 from xxx import * 导入
```
""",

"custom_exception": """\
## 一、Python 内置异常层级

```
BaseException
├── KeyboardInterrupt      # Ctrl+C
├── SystemExit             # sys.exit()
├── GeneratorExit
└── Exception              # 业务异常都继承这个
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError    # 列表越界
    │   └── KeyError       # 字典无此 key
    ├── TypeError          # 类型错误
    ├── ValueError         # 值错误
    ├── AttributeError     # 属性不存在
    ├── FileNotFoundError  # 文件不存在
    ├── IOError            # I/O 错误
    └── ...
```

## 二、try-except-else-finally

```python
try:
    # 可能出错的代码
    result = 10 / int(input("输入除数："))
except ZeroDivisionError:
    print("不能除以零")
except ValueError as e:
    print(f"输入无效：{e}")
except (TypeError, KeyError) as e:
    print(f"其他错误：{e}")
except Exception as e:    # 兜底（不推荐，能精确就精确）
    print(f"未知错误：{e}")
else:
    # 无异常时执行
    print(f"结果是 {result}")
finally:
    # 无论如何都执行（清理资源）
    print("结束")
```

## 三、抛出异常（raise）

```python
def set_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数")
    if age > 150:
        raise ValueError("年龄超出合理范围")
    print(f"年龄已设置为 {age}")

set_age(-5)     # ValueError: 年龄不能为负数
```

## 四、自定义异常类

```python
class BusinessError(Exception):
    """业务异常基类"""
    def __init__(self, message, code=None):
        super().__init__(message)
        self.message = message
        self.code = code

class InsufficientBalance(BusinessError):
    """余额不足"""
    def __init__(self, balance, amount):
        super().__init__(f"余额 {balance} 不足，需 {amount}")
        self.balance = balance
        self.amount = amount

# 使用
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalance(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 200)
except InsufficientBalance as e:
    print(e)        # 余额 100 不足，需 200
```

## 五、异常的链式抛出（raise from）

```python
try:
    int("abc")
except ValueError as e:
    raise RuntimeError("数据转换失败") from e
# 报错信息会显示原始异常
```

## 六、断言 assert

```python
def divide(a, b):
    assert b != 0, "除数不能为零"    # 调试用
    assert isinstance(a, (int, float)), "a 必须是数字"
    return a / b

divide(10, 0)
# AssertionError: 除数不能为零

# ⚠️ 不要用 assert 做用户输入验证
# 优化模式下 -O 参数会移除 assert
```

## 七、with 语句（上下文管理器）

```python
# 自动关闭文件、自动释放锁
with open("data.txt", "r") as f:
    content = f.read()
# 文件自动关闭（即使中间出错）

# 等价于
f = open("data.txt", "r")
try:
    content = f.read()
finally:
    f.close()
```

## 八、自定义上下文管理器

```python
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = time.time() - self.start
        print(f"耗时 {elapsed:.3f}s")
        return False    # 不吞掉异常

with Timer():
    total = sum(range(10_000_000))
# 耗时 0.123s
```
""",

"closure_decorator": """\
## 一、什么是闭包（Closure）

**闭包** = 函数 + 其引用的外部变量

```python
def outer(msg):
    def inner():
        print(msg)          # 引用了外层函数的变量
    return inner

f = outer("hello")
f()                         # "hello"
del outer                   # 即使 outer 被删，inner 仍能访问 msg
f()                         # "hello"
```

## 二、闭包三要素

1. 函数嵌套
2. 内函数引用外函数的变量
3. 外函数返回内函数

## 三、闭包实战：计数器

```python
def make_counter(start=0, step=1):
    count = [start]      # 用列表避免 nonlocal（list 是可变对象）
    def counter():
        count[0] += step
        return count[0]
    return counter

c1 = make_counter(0, 1)
c2 = make_counter(100, 10)

print(c1(), c1(), c1())     # 1 2 3
print(c2(), c2())           # 110 120
```

## 四、装饰器（Decorator）基础

**装饰器** = 接受函数，返回包装后的函数

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} 执行完毕")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}")

greet("Alice")
# 调用 greet
# Hello, Alice
# greet 执行完毕
```

## 五、装饰器的工作原理

```python
# @my_decorator 等价于
greet = my_decorator(greet)
```

## 六、带参数的装饰器

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi(name):
    print(f"Hi, {name}")

say_hi("Alice")
# Hi, Alice
# Hi, Alice
# Hi, Alice
```

## 七、装饰器链

```python
@bold
@italic
def hello():
    return "Hello"

# 等价于 hello = bold(italic(hello))
```

## 八、`functools.wraps`（保留原函数元信息）

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)           # ← 加这一行
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """问候函数"""
    return f"Hello, {name}"

print(greet.__name__)      # "greet"（用了 wraps）
print(greet.__doc__)       # "问候函数"
```

## 九、类装饰器

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} 已被调用 {self.count} 次")
        return self.func(*args, **kwargs)

@CountCalls
def hello():
    print("Hello!")

hello()
hello()
hello()
# hello 已被调用 1 次
# Hello!
# hello 已被调用 2 次
# Hello!
# hello 已被调用 3 次
# Hello!
```

## 十、实用装饰器例子

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} 耗时 {elapsed:.3f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

slow_function()
# slow_function 耗时 1.001s
```
""",

"functools_wraps": """\
## 一、为什么需要 functools.wraps

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """问候某人"""
    return f"Hello, {name}"

print(greet.__name__)      # "wrapper"（不是 "greet"！）
print(greet.__doc__)       # None
print(greet.__module__)    # 'builtins'
```

## 二、functools.wraps 的修复

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)           # ← 把 func 的元信息复制到 wrapper
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """问候某人"""
    return f"Hello, {name}"

print(greet.__name__)      # "greet"
print(greet.__doc__)       # "问候某人"
print(greet.__module__)    # '__main__'
```

## 三、functools.wraps 复制的属性

`@wraps(func)` 会复制以下属性：

- `__module__`、`__name__`、`__qualname__`、`__annotations__`
- `__doc__`
- `__dict__`（实例字典）
- `__wrapped__`（指向原函数）

## 四、`__wrapped__` 属性

```python
import inspect
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """问候某人"""
    return f"Hello, {name}"

# 通过 __wrapped__ 访问原函数
print(greet.__wrapped__("Alice"))   # "Hello, Alice"
print(inspect.signature(greet))     # (name)
```

## 五、functools 其他实用工具

### lru_cache（记忆化）

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(100))          # 很快（缓存了中间结果）
print(fib.cache_info())   # CacheInfo(hits=98, misses=101, ...)
```

### partial（偏函数）

```python
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)

print(square(5))         # 25
print(cube(5))           # 125
```

### reduce

```python
from functools import reduce
nums = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a + b, nums))    # 15
```

### total_ordering（自动补全比较方法）

```python
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, score):
        self.score = score
    def __eq__(self, other):
        return self.score == other.score
    def __lt__(self, other):
        return self.score < other.score
    # __le__、__gt__、__ge__ 自动生成

s1 = Student(85)
s2 = Student(90)
print(s1 < s2)           # True
print(s1 <= s2)          # True（自动生成）
```

### cmp_to_key（把老式比较函数转 key）

```python
from functools import cmp_to_key

def compare(a, b):
    return len(a) - len(b)    # 按长度排序

words = ["a", "abc", "ab"]
words.sort(key=cmp_to_key(compare))
# ['a', 'ab', 'abc']
```

### cached_property

```python
from functools import cached_property

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def area(self):
        print("计算面积")
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area)    # 计算面积 → 78.5
print(c.area)    # 78.5（不重算，缓存了）
```
""",

"decorator_chain": """\
## 一、装饰器链（Decorator Chaining）

```python
@decorator_a
@decorator_b
@decorator_c
def func():
    pass

# 等价于
func = decorator_a(decorator_b(decorator_c(func)))
```

## 二、执行顺序（自下而上）

```python
def dec_a(func):
    def wrapper(*args, **kwargs):
        print("A 进入")
        result = func(*args, **kwargs)
        print("A 退出")
        return result
    return wrapper

def dec_b(func):
    def wrapper(*args, **kwargs):
        print("B 进入")
        result = func(*args, **kwargs)
        print("B 退出")
        return result
    return wrapper

@dec_a
@dec_b
def hello():
    print("Hello!")

hello()
# A 进入
# B 进入
# Hello!
# B 退出
# A 退出
```

## 三、实用案例：权限+日志+计时

```python
from functools import wraps
import time

def require_login(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get("logged_in"):
            raise PermissionError("请先登录")
        return func(user, *args, **kwargs)
    return wrapper

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] 调用 {func.__name__}({args}, {kwargs})")
        return func(*args, **kwargs)
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"[TIME] {func.__name__} 耗时 {time.time()-start:.3f}s")
        return result
    return wrapper

class User:
    def __init__(self, name, logged_in):
        self.name = name
        self.logged_in = logged_in

@timer
@log_calls
@require_login
def view_profile(user):
    print(f"{user.name} 的个人资料")
    return {"name": user.name}

user = User("Alice", True)
view_profile(user)
# [LOG] 调用 view_profile(({'name': 'Alice', 'logged_in': True},), {})
# Alice 的个人资料
# [TIME] view_profile 耗时 0.001s
```

## 四、带参数的装饰器链

```python
from functools import wraps

def retry(max_attempts=3, delay=0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise
                    print(f"重试 {attempt}/{max_attempts}: {e}")
                    time.sleep(delay)
        return wrapper
    return decorator

def cache(func):
    cache_dict = {}
    @wraps(func)
    def wrapper(*args):
        if args not in cache_dict:
            cache_dict[args] = func(*args)
        return cache_dict[args]
    return wrapper

@retry(max_attempts=3, delay=1)
@cache
def unstable_api():
    import random
    if random.random() < 0.5:
        raise ValueError("API 临时失败")
    return "成功"

print(unstable_api())
```

## 五、类装饰器链

```python
class CountCalls:
    def __init__(self, func):
        wraps(func)(self)      # 让 CountCalls 实例伪装成 func
        self.func = func
        self.count = 0
    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

def timer(cls):
    class Wrapped:
        def __init__(self, *args, **kwargs):
            self._instance = cls(*args, **kwargs)
        def __getattr__(self, name):
            attr = getattr(self._instance, name)
            if callable(attr):
                def timed(*args, **kwargs):
                    start = time.time()
                    result = attr(*args, **kwargs)
                    print(f"[{name}] 耗时 {time.time()-start:.3f}s")
                    return result
                return timed
            return attr
    return Wrapped

# 类装饰器（装饰一个类）
@timer
class MyService:
    def slow_method(self):
        time.sleep(0.5)
        return "done"

s = MyService()
s.slow_method()
# [slow_method] 耗时 0.500s
```

## 六、装饰器调试技巧

```python
# 1. 打印装饰器链
print(func)                    # 显示被装饰后的 wrapper
print(func.__wrapped__)        # 显示原函数

# 2. 用 attrs 排查
for attr in ["__name__", "__doc__", "__wrapped__"]:
    print(f"{attr}: {getattr(func, attr, 'NOT SET')}")

# 3. 调试断点打在 wrapper 里
def wrapper(*args, **kwargs):
    breakpoint()              # 进入交互式调试
    return func(*args, **kwargs)
```
""",

}