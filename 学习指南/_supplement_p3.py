# -*- coding: utf-8 -*-
"""补全知识库 - 第三批：OOP 高级 / 迭代生成器 / 多线程协程"""
SUPPLEMENT_3 = {

"mro": """\
## 一、MRO（Method Resolution Order）方法解析顺序

**问题**：多继承时，同名方法该调哪个父类的？

```python
class A:
    def show(self):
        print("A.show")

class B(A):
    def show(self):
        print("B.show")

class C(A):
    def show(self):
        print("C.show")

class D(B, C):
    pass

d = D()
d.show()         # B.show（D → B → C → A）
```

## 二、C3 线性化算法

Python 使用 **C3 线性化** 确定 MRO：

```python
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>,
#  <class '__main__.A'>, <class 'object'>)
```

## 三、super() 的工作原理

```python
class A:
    def show(self):
        print("A.show")

class B(A):
    def show(self):
        print("B.show")
        super().show()         # 调用 MRO 中下一个

class C(A):
    def show(self):
        print("C.show")
        super().show()

class D(B, C):
    def show(self):
        print("D.show")
        super().show()         # → B.show → C.show → A.show

d = D()
d.show()
# D.show
# B.show
# C.show
# A.show
```

## 四、新式类 vs 经典类（Python 2 遗留）

```python
# Python 3 默认所有类都继承 object（新式类）
class MyClass:
    pass

# 等价于
class MyClass(object):
    pass
```

## 五、菱形继承问题

```
    A
   / \\
  B   C
   \\ /
    D
```

**经典类**：深度优先（A→B→A→C→A）
**新式类**：C3 线性化（A→B→C→A）

新式类更合理：每个父类只调用一次。

## 六、抽象基类（ABC）

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

# s = Shape()      # ❌ TypeError: 不能实例化抽象类
c = Circle(5)
print(c.area())         # 78.5
```

## 七、Mixin 模式

```python
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class User(JSONMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

u = User("Alice", 25)
print(u.to_json())      # {"name": "Alice", "age": 25}
```
""",

"polymorphism_static": """\
## 一、多态（Polymorphism）

**多态**：同样的方法调用，在不同对象上有不同行为。

```python
class Cat:
    def speak(self):
        return "喵"

class Dog:
    def speak(self):
        return "汪"

class Duck:
    def speak(self):
        return "嘎"

# 同样的调用，不同表现
animals = [Cat(), Dog(), Duck()]
for animal in animals:
    print(animal.speak())
# 喵 汪 嘎
```

### 鸭子类型（Duck Typing）

```python
# 不需要继承关系，只要"看起来像鸭子"就行
class Robot:
    def speak(self):
        return "哔哔"

animals.append(Robot())      # 也能加入列表
animals[-1].speak()          # "哔哔"
```

## 二、静态方法 @staticmethod

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# 调用（不需要实例）
print(MathUtils.add(3, 5))       # 8

# 也可以从实例调用（但没必要）
m = MathUtils()
print(m.add(3, 5))              # 8

# 静态方法不能访问 self/cls
```

## 三、类方法 @classmethod

```python
class User:
    count = 0                    # 类属性

    def __init__(self, name):
        self.name = name
        User.count += 1

    @classmethod
    def get_count(cls):
        return cls.count         # 访问类属性

    @classmethod
    def from_dict(cls, data):
        """工厂方法：从字典创建实例"""
        return cls(data["name"])

u1 = User("Alice")
u2 = User("Bob")
print(User.get_count())          # 2

# 工厂方法
data = {"name": "Charlie"}
u3 = User.from_dict(data)
print(u3.name)                  # Charlie
```

## 四、@staticmethod vs @classmethod vs 实例方法

| 装饰器 | 第一个参数 | 访问 self? | 访问 cls? | 用途 |
|--------|----------|-----------|---------|------|
| 无 | self | ✅ | ✅ | 普通实例方法 |
| `@staticmethod` | 无 | ❌ | ❌ | 工具函数 |
| `@classmethod` | cls | ⚠️（通过 cls） | ✅ | 工厂方法、类级操作 |

## 五、属性 @property

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius   # 私有约定

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半径不能为负")
        self._radius = value

c = Circle(5)
print(c.radius)              # 5（调用 getter）
c.radius = 10                # 调用 setter
# c.radius = -1              # ValueError

# 比显式方法更 Pythonic
# c.get_radius() / c.set_radius(10)
```

## 六、super() 在多态中的用法

```python
class Animal:
    def speak(self):
        raise NotImplementedError

class Cat(Animal):
    def speak(self):
        return "喵"

class PersianCat(Cat):       # 波斯猫，继承 Cat
    def speak(self):
        parent_sound = super().speak()
        return f"{parent_sound}（波斯猫）"

p = PersianCat()
print(p.speak())             # "喵（波斯猫）"
```
""",

"magic_methods_1": """\
## 一、魔法方法（Dunder Methods）

**魔法方法**：以双下划线 `__` 开头和结尾的方法，由 Python 解释器在特定场景自动调用。

## 二、构造与析构

```python
class MyClass:
    def __new__(cls, *args, **kwargs):
        # 创建实例（很少用）
        print("__new__ 被调用")
        return super().__new__(cls)

    def __init__(self, value):
        # 初始化实例
        self.value = value
        print(f"__init__ 被调用，value={value}")

    def __del__(self):
        # 析构（垃圾回收时调用）
        print("__del__ 被调用，对象被销毁")

obj = MyClass(42)
del obj
# __new__ 被调用
# __init__ 被调用，value=42
# __del__ 被调用，对象被销毁
```

## 三、字符串表示

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"           # 面向用户

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"      # 面向开发者

p = Point(1, 2)
print(p)             # Point(1, 2)        （调用 __str__）
print(repr(p))       # Point(x=1, y=2)    （调用 __repr__）
```

## 四、比较运算符

```python
class Student:
    def __init__(self, score):
        self.score = score

    def __eq__(self, other):
        return self.score == other.score
    def __lt__(self, other):
        return self.score < other.score
    def __le__(self, other):
        return self.score <= other.score

s1 = Student(85)
s2 = Student(90)
print(s1 == s2)      # False
print(s1 < s2)       # True
print(s1 <= s2)      # True

# 其他比较方法
# __ne__ 不等于
# __gt__ 大于
# __ge__ 大于等于
```

## 五、算术运算符

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)           # Vector(4, 6)
print(v1 - v2)           # Vector(-2, -2)
print(v1 * 3)            # Vector(3, 6)

# 其他运算符
# __truediv__ / __floordiv__ / __mod__ 除法 / 取模
# __pow__ 幂运算
# __neg__ / __pos__ / __abs__ 一元运算
# __matmul__ @ 运算符（NumPy 用）
```

## 六、容器方法

```python
class MyList:
    def __init__(self, items):
        self.items = list(items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        del self.items[index]

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        return iter(self.items)

ml = MyList([1, 2, 3])
print(len(ml))           # 3
print(ml[0])             # 1
ml[1] = 20
print(ml[1])             # 20
print(2 in ml)           # False（20 是 2 吗？不是）
for x in ml:
    print(x)             # 1 20 3
```

## 七、可调用对象

```python
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x + self.n

add5 = Adder(5)
print(add5(10))          # 15（实例像函数一样调用）
print(callable(add5))    # True
```

## 八、上下文管理器

```python
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        print(f"耗时 {time.time() - self.start:.3f}s")
        return False

with Timer():
    sum(range(10_000_000))
# 耗时 0.05s
```
""",

"magic_methods_2": """\
## 一、属性访问

```python
class Dynamic:
    def __getattr__(self, name):
        """属性未找到时调用"""
        return f"动态属性: {name}"

    def __setattr__(self, name, value):
        """设置属性时调用"""
        print(f"设置 {name} = {value}")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        print(f"删除 {name}")
        super().__delattr__(name)

d = Dynamic()
d.x = 10                 # "设置 x = 10"
print(d.x)               # 10
print(d.undefined)       # "动态属性: undefined"
```

## 二、描述符（Descriptor）

```python
class Validator:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not (self.min_val <= value <= self.max_val):
            raise ValueError(f"值必须在 {self.min_val}-{self.max_val}")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

class Person:
    age = Validator(0, 150)

p = Person()
p.age = 25                # OK
# p.age = 200              # ValueError
print(p.age)              # 25
```

## 三、可哈希对象

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

p = Point(1, 2)
d = {p: "origin"}        # 可以作为字典 key
print(d[Point(1, 2)])     # "origin"
```

**注意**：定义了 `__eq__` 后默认 `__hash__` 变 None（不可哈希）。需要显式定义。

## 四、bool 转换

```python
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

ml_empty = MyList([])
ml_full = MyList([1, 2, 3])

print(bool(ml_empty))    # False（__len__ 返回 0）
print(bool(ml_full))     # True

# 或者自定义 __bool__
class AlwaysTrue:
    def __bool__(self):
        return True

print(bool(AlwaysTrue()))    # True
```

## 五、pickle 序列化

```python
import pickle

class MyClass:
    def __init__(self, data):
        self.data = data

    def __getstate__(self):
        """pickle 时调用"""
        return {"data": self.data}

    def __setstate__(self, state):
        """unpickle 时调用"""
        self.data = state["data"]

obj = MyClass([1, 2, 3])
data = pickle.dumps(obj)
restored = pickle.loads(data)
print(restored.data)       # [1, 2, 3]
```

## 六、运算符重载总结

| 运算符 | 方法 |
|--------|------|
| `+` | `__add__` |
| `-` | `__sub__` |
| `*` | `__mul__` |
| `/` | `__truediv__` |
| `//` | `__floordiv__` |
| `%` | `__mod__` |
| `**` | `__pow__` |
| `==` | `__eq__` |
| `<` | `__lt__` |
| `<=` | `__le__` |
| `>` | `__gt__` |
| `>=` | `__ge__` |
| `!=` | `__ne__` |
| `len(x)` | `__len__` |
| `str(x)` | `__str__` |
| `repr(x)` | `__repr__` |
| `bool(x)` | `__bool__` |
| `hash(x)` | `__hash__` |
| `x[key]` | `__getitem__` |
| `x[key] = v` | `__setitem__` |
| `del x[key]` | `__delitem__` |
| `item in x` | `__contains__` |
| `iter(x)` | `__iter__` |
| `next(x)` | `__next__` |
| `x()` | `__call__` |
| `with x` | `__enter__`, `__exit__` |
""",

"iterable_iterator": """\
## 一、迭代器协议

Python 的 `for` 循环背后是 **迭代器协议**：

```python
for x in [1, 2, 3]:
    print(x)
# 等价于
it = iter([1, 2, 3])      # __iter__
while True:
    try:
        x = next(it)      # __next__
        print(x)
    except StopIteration:
        break
```

## 二、可迭代对象 vs 迭代器

| 概念 | 定义 | 方法 |
|------|------|------|
| 可迭代对象（Iterable） | 可以用 `for` 遍历 | 实现 `__iter__`（返回迭代器） |
| 迭代器（Iterator） | 记住遍历位置 | 实现 `__iter__` 和 `__next__` |

```python
# list 是可迭代对象，但不是迭代器
nums = [1, 2, 3]
print(hasattr(nums, "__iter__"))   # True
print(hasattr(nums, "__next__"))   # False

# iter() 把可迭代对象变成迭代器
it = iter(nums)
print(hasattr(it, "__next__"))     # True

# 迭代器是一次性的
nums2 = list(it)        # [1, 2, 3]
nums3 = list(it)        # []（已经耗尽）
```

## 三、迭代器状态

迭代器内部维护：

- 当前遍历位置
- 已遍历过的元素（不保存）

```python
it = iter([1, 2, 3])
print(next(it))     # 1
print(next(it))     # 2
print(next(it))     # 3
print(next(it))     # StopIteration
```

## 四、内置可迭代对象

所有能用 `for` 的对象都是 Iterable：

- 容器：`list`, `tuple`, `set`, `dict`, `str`
- 文件对象（`open()` 返回）
- 生成器（generator）
- `range()` 返回的对象
- `zip()`, `map()`, `filter()` 返回的对象

## 五、判断对象是否可迭代

```python
from collections.abc import Iterable, Iterator

def is_iterable(obj):
    return isinstance(obj, Iterable)

def is_iterator(obj):
    return isinstance(obj, Iterator)

print(is_iterable([1, 2, 3]))      # True
print(is_iterator([1, 2, 3]))     # False
print(is_iterator(iter([1, 2])))  # True
print(is_iterable(open("file.txt")))  # True
```

## 六、迭代器 vs 生成器

- 迭代器：类，需要自己实现 `__iter__` 和 `__next__`
- 生成器：函数 + yield，更简洁

```python
# 迭代器：写起来繁琐
class Counter:
    def __init__(self, max):
        self.max = max
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= self.max:
            raise StopIteration
        self.n += 1
        return self.n

# 生成器：一行搞定
def counter(max):
    n = 0
    while n < max:
        n += 1
        yield n
```
""",

"custom_iterator": """\
## 一、自定义迭代器（类方式）

```python
class Fibonacci:
    """斐波那契数列迭代器"""
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        self.count += 1
        self.a, self.b = self.b, self.a + self.b
        return self.a

# 使用
fib = Fibonacci(10)
for n in fib:
    print(n, end=" ")
# 1 1 2 3 5 8 13 21 34 55
```

## 二、自定义可迭代对象（更常见）

```python
class MyRange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        n = self.start
        while n < self.end:
            yield n       # 生成器方式
            n += self.step

# 使用
for i in MyRange(0, 10, 2):
    print(i, end=" ")
# 0 2 4 6 8
```

## 三、反向迭代

```python
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 0
        while n <= self.start:
            yield n
            n += 1

# 正向
for i in Countdown(5):
    print(i, end=" ")
# 5 4 3 2 1

# 反向
for i in reversed(Countdown(5)):
    print(i, end=" ")
# 0 1 2 3 4 5
```

## 四、迭代器的链式操作

```python
from itertools import chain, islice

# chain：连接多个迭代器
a = [1, 2, 3]
b = ["a", "b", "c"]
for x in chain(a, b):
    print(x, end=" ")
# 1 2 3 a b c

# islice：切片
nums = iter(range(100))
for x in islice(nums, 5, 10):
    print(x, end=" ")
# 5 6 7 8 9
```

## 五、迭代器的"惰性求值"

迭代器是 **惰性** 的：只在需要时计算下一个值。

```python
# 列表推导式：立即计算所有
squares = [x ** 2 for x in range(10_000_000)]   # 占用大量内存

# 生成器表达式：惰性
squares_gen = (x ** 2 for x in range(10_000_000))  # 几乎不占内存

# 用 next() 一个个取值
print(next(squares_gen))    # 0
print(next(squares_gen))    # 1
```

## 六、iter(callable, sentinel) 模式

```python
# iter(callable, sentinel)：每次调用 callable，返回 sentinel 时停止
# 经典应用：读取固定大小的块

with open("big_file.txt") as f:
    for chunk in iter(lambda: f.read(1024), ""):
        process(chunk)
# 每次读 1024 字节，读到空字符串时停止
```

## 七、什么时候需要自定义迭代器

- 数据量大到不能放进内存（用生成器/迭代器）
- 需要自定义遍历顺序
- 实现数据结构（树、图的遍历）
- 实现惰性计算
""",

"generator_yield": """\
## 一、生成器（Generator）是什么

**生成器** = 包含 `yield` 的函数 → 自动返回迭代器

```python
def count_up_to(n):
    i = 0
    while i < n:
        yield i
        i += 1

# 调用不会执行函数体，而是返回一个生成器
gen = count_up_to(5)
print(type(gen))        # <class 'generator'>

# 每次 next() 执行到下一个 yield
print(next(gen))        # 0
print(next(gen))        # 1
print(list(gen))        # [2, 3, 4]
```

## 二、yield 的工作原理

```python
def simple_gen():
    print("Start")
    yield 1
    print("After first yield")
    yield 2
    print("After second yield")
    yield 3
    print("End")

gen = simple_gen()
print("调用 next(gen):")
print(next(gen))        # Start → 1
print("---")
print(next(gen))        # After first yield → 2
print("---")
print(next(gen))        # After second yield → 3
```

## 三、生成器 vs 普通函数

| 特性 | 普通函数 | 生成器 |
|------|---------|--------|
| 返回 | 单个值 | 迭代器 |
| 调用次数 | 一次 | 多次（next 一次执行到下一个 yield） |
| 内存 | 一开始就计算所有 | 惰性，按需计算 |
| 状态 | 每次调用重置 | 暂停/恢复 |

## 四、生成器表达式

```python
# 列表推导式
squares_list = [x ** 2 for x in range(10)]      # 立即生成列表

# 生成器表达式（用圆括号）
squares_gen = (x ** 2 for x in range(10))       # 惰性

print(next(squares_gen))   # 0
print(sum(squares_gen))    # 285（继续消费剩余的）
```

## 五、send() / throw() / close()

生成器可以从外部发送值、抛异常、关闭：

```python
def echo():
    while True:
        received = yield
        print(f"收到：{received}")

gen = echo()
next(gen)                  # 启动生成器
gen.send("hello")          # 收到：hello
gen.send("world")          # 收到：world

gen.close()                # 关闭（再 next 会抛 StopIteration）
# gen.send("x")             # StopIteration
```

```python
# throw 在生成器内抛异常
def gen_with_exception():
    try:
        yield 1
        yield 2
    except ValueError:
        print("捕获到 ValueError")
        yield 99

g = gen_with_exception()
next(g)                    # 1
g.throw(ValueError, "test")  # 捕获到 ValueError → 99
```

## 六、yield from（委托生成器）

```python
# 不用 yield from
def chain(*iterables):
    for it in iterables:
        for item in it:
            yield item

# 用 yield from（更简洁）
def chain(*iterables):
    for it in iterables:
        yield from it

print(list(chain([1, 2], "ab", (3, 4))))
# [1, 2, 'a', 'b', 3, 4]
```

## 七、生成器的双向通信（高级）

```python
def running_average():
    total = 0
    count = 0
    while True:
        value = yield total / count if count else 0
        total += value
        count += 1

avg = running_average()
next(avg)                  # 启动
print(avg.send(10))        # 10.0
print(avg.send(20))        # 15.0
print(avg.send(30))        # 20.0
```

## 八、生成器的优点

1. **节省内存**：流式处理大数据
2. **惰性计算**：按需产生值
3. **代码简洁**：比手写迭代器类短
4. **自然支持管道**：`yield from` 串联

## 九、常见陷阱

```python
# ❌ 生成器只能消费一次
gen = (x for x in range(3))
print(list(gen))           # [0, 1, 2]
print(list(gen))           # []

# ✅ 需要重新创建
gen = (x for x in range(3))
print(list(gen))           # [0, 1, 2]

# ❌ 生成器内不能 return value
# def gen():
#     return 1             # ❌ SyntaxError in generator
#     yield 1

# ✅ 用 raise StopIteration(value) 结束
def gen():
    yield 1
    yield 2
    # 隐式 return
```
""",

"threading_basics": """\
## 一、线程（Thread）基础

**线程** 是进程内的执行单元，共享进程的内存。

```python
import threading
import time

def worker(name, duration):
    print(f"线程 {name} 开始")
    time.sleep(duration)
    print(f"线程 {name} 结束")

# 创建线程
t1 = threading.Thread(target=worker, args=("A", 2))
t2 = threading.Thread(target=worker, args=("B", 3))

# 启动
t1.start()
t2.start()

# 等待完成
t1.join()
t2.join()

print("所有线程结束")
```

## 二、线程 vs 进程

| 特性 | 线程 | 进程 |
|------|------|------|
| 内存 | 共享 | 独立 |
| 创建开销 | 小 | 大 |
| 通信 | 容易（共享变量） | 难（需要 IPC） |
| GIL 限制 | ✅ 受影响 | ❌ 不受影响 |
| 适用 | I/O 密集 | CPU 密集 |

## 三、GIL（全局解释器锁）

**GIL** 是 CPython 的特性：同一时刻只有一个线程能执行 Python 字节码。

```python
# CPU 密集任务：多线程反而更慢（线程切换开销）
import threading

def cpu_heavy(n):
    while n > 0:
        n -= 1

# 单线程
t = time.time()
cpu_heavy(10_000_000)
print(f"单线程：{time.time()-t:.2f}s")

# 多线程（不会更快！）
t = time.time()
threads = [threading.Thread(target=cpu_heavy, args=(10_000_000,)) for _ in range(2)]
for t in threads: t.start()
for t in threads: t.join()
print(f"双线程：{time.time()-t:.2f}s")
```

**为什么有 GIL**：避免内存管理的竞争条件。绕过办法：多进程、C 扩展、asyncio。

## 四、守护线程

```python
import threading
import time

def daemon_task():
    while True:
        print("守护线程运行中...")
        time.sleep(1)

t = threading.Thread(target=daemon_task, daemon=True)
t.start()

time.sleep(3)
print("主程序结束，守护线程自动终止")
```

## 五、线程数量控制

```python
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def task(n):
    time.sleep(1)
    return n ** 2

# 方式 1：手动管理
threads = []
for i in range(5):
    t = threading.Thread(target=task, args=(i,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()

# 方式 2：线程池（推荐）
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, i) for i in range(5)]
    for f in futures:
        print(f.result())
```

## 六、线程局部数据

```python
import threading

# 每个线程独立的变量
thread_local = threading.local()

def get_id():
    if not hasattr(thread_local, "id"):
        thread_local.id = threading.get_ident()
    return thread_local.id

def worker():
    print(f"线程 {get_id()}")

t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)
t1.start(); t2.start()
t1.join(); t2.join()
```
""",

"thread_sync_gil": """\
## 一、线程同步问题

多个线程同时修改共享变量会导致 **竞态条件**：

```python
import threading

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads: t.start()
for t in threads: t.join()

print(counter)    # 不是 200000（可能更少）
```

**原因**：`counter += 1` 实际是三步（读、加、写），中间会被其他线程打断。

## 二、互斥锁（Lock）

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:            # 加锁
            counter += 1      # 临界区
        # 自动解锁

threads = [threading.Thread(target=increment) for _ in range(2)]
for t in threads: t.start()
for t in threads: t.join()

print(counter)    # 200000（正确）
```

## 三、死锁

**死锁**：两个锁互相等待对方释放。

```python
import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def task1():
    with lock_a:
        time.sleep(0.1)
        with lock_b:           # 等 lock_b
            print("task1 done")

def task2():
    with lock_b:
        time.sleep(0.1)
        with lock_a:           # 等 lock_a（已被 task1 持有）
            print("task2 done")

# 永远卡住！
```

**避免死锁**：

1. 按固定顺序获取锁
2. 用 `try/finally` 而非 `with`
3. 设置超时

```python
# 用 try/finally 加超时
lock_a.acquire(timeout=1)
try:
    lock_b.acquire(timeout=1)
    try:
        # 临界区
        pass
    finally:
        lock_b.release()
finally:
    lock_a.release()
```

## 四、可重入锁（RLock）

同一个线程可以多次获取同一个 RLock：

```python
lock = threading.RLock()

def recursive_func(n):
    with lock:
        if n > 0:
            recursive_func(n - 1)

recursive_func(3)    # 普通 Lock 会死锁
```

## 五、条件变量（Condition）

```python
import threading

items = []
condition = threading.Condition()

def consumer():
    with condition:
        while not items:
            condition.wait()        # 等待通知
        item = items.pop(0)
        print(f"消费：{item}")

def producer():
    with condition:
        items.append("apple")
        condition.notify()          # 通知等待者

threading.Thread(target=consumer).start()
threading.Thread(target=producer).start()
```

## 六、信号量（Semaphore）

控制同时访问资源的线程数：

```python
import threading
import time

sem = threading.Semaphore(3)        # 最多 3 个并发

def task(i):
    with sem:
        print(f"线程 {i} 获取资源")
        time.sleep(1)
        print(f"线程 {i} 释放资源")

threads = [threading.Thread(target=task, args=(i,)) for i in range(10)]
for t in threads: t.start()
for t in threads: t.join()
```

## 七、GIL 与多线程性能

```python
import threading
import multiprocessing
import time

def cpu_task(n):
    while n > 0:
        n -= 1

def benchmark_single():
    cpu_task(50_000_000)

def benchmark_threaded():
    t1 = threading.Thread(target=cpu_task, args=(25_000_000,))
    t2 = threading.Thread(target=cpu_task, args=(25_000_000,))
    t1.start(); t2.start()
    t1.join(); t2.join()

def benchmark_multiprocess():
    p1 = multiprocessing.Process(target=cpu_task, args=(25_000_000,))
    p2 = multiprocessing.Process(target=cpu_task, args=(25_000_000,))
    p1.start(); p2.start()
    p1.join(); p2.join()

# 结果（典型）：
# 单线程：1.5s
# 双线程：1.5s（一样！GIL 限制）
# 双进程：0.8s（更快，真并行）
```

## 八、什么时候用多线程 vs 多进程

| 场景 | 选择 |
|------|------|
| I/O 密集（网络请求、文件读写） | 多线程 |
| CPU 密集（数值计算、图像处理） | 多进程 |
| 共享状态多 | 多线程（共享变量） |
| 隔离性要求高 | 多进程 |
""",

"multiprocessing": """\
## 一、多进程基础

```python
import multiprocessing
import time

def worker(name, duration):
    print(f"进程 {name} 开始")
    time.sleep(duration)
    print(f"进程 {name} 结束")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=worker, args=("A", 2))
    p2 = multiprocessing.Process(target=worker, args=("B", 3))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("所有进程结束")
```

**注意**：在 Windows/macOS 上多进程代码必须放在 `if __name__ == "__main__":` 下。

## 二、进程池（Pool）

```python
import multiprocessing

def square(n):
    return n * n

if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        # map：阻塞
        results = pool.map(square, [1, 2, 3, 4, 5])
        print(results)            # [1, 4, 9, 16, 25]

        # apply_async：非阻塞
        async_results = [pool.apply_async(square, (i,)) for i in range(5)]
        results = [r.get() for r in async_results]
        print(results)
```

## 三、ProcessPoolExecutor（更现代的接口）

```python
from concurrent.futures import ProcessPoolExecutor

def square(n):
    return n * n

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(square, [1, 2, 3, 4, 5]))
        print(results)
```

## 四、进程间通信

### Queue

```python
import multiprocessing

def producer(q):
    for i in range(5):
        q.put(i)
        print(f"放入 {i}")

def consumer(q):
    while True:
        try:
            item = q.get(timeout=1)
            print(f"取出 {item}")
        except:
            break

if __name__ == "__main__":
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,))
    p1.start(); p2.start()
    p1.join(); p2.join()
```

### Pipe

```python
import multiprocessing

def sender(conn):
    conn.send("hello from sender")
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=sender, args=(child_conn,))
    p.start()
    print(parent_conn.recv())    # "hello from sender"
    p.join()
```

### Shared Value/Array

```python
import multiprocessing

def increment(counter, lock):
    for _ in range(100):
        with lock:
            counter.value += 1

if __name__ == "__main__":
    counter = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()

    processes = [multiprocessing.Process(target=increment, args=(counter, lock))
                 for _ in range(4)]
    for p in processes: p.start()
    for p in processes: p.join()

    print(counter.value)    # 400
```

## 五、Manager（共享复杂对象）

```python
import multiprocessing

def update_dict(d, key, value):
    d[key] = value

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        d = manager.dict()
        processes = [multiprocessing.Process(target=update_dict, args=(d, k, v))
                     for k, v in [("a", 1), ("b", 2), ("c", 3)]]
        for p in processes: p.start()
        for p in processes: p.join()
        print(dict(d))      # {'a': 1, 'b': 2, 'c': 3}
```
""",

"process_communication": """\
## 一、进程间通信（IPC）方式

| 方式 | 适用 | 特点 |
|------|------|------|
| Queue | 多数情况 | 线程/进程安全，FIFO |
| Pipe | 两个进程 | 双向通信，速度快 |
| Shared Memory | 大数据共享 | Value/Array |
| Manager | 复杂对象 | 跨进程共享 dict/list |
| Socket | 不同主机 | 网络通信 |

## 二、Queue 详解

```python
import multiprocessing
import time

def producer(q):
    for i in range(10):
        q.put(f"item-{i}")
        print(f"放入 item-{i}")
        time.sleep(0.1)
    q.put(None)        # 哨兵，通知结束

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"处理 {item}")

if __name__ == "__main__":
    q = multiprocessing.Queue(maxsize=3)    # 有界队列
    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,))
    p1.start(); p2.start()
    p1.join(); p2.join()
```

## 三、Pipe 详解

```python
import multiprocessing

def worker(conn):
    while True:
        msg = conn.recv()
        if msg == "stop":
            conn.send("stopped")
            break
        result = msg.upper()
        conn.send(result)
    conn.close()

if __name__ == "__main__":
    parent, child = multiprocessing.Pipe(duplex=True)
    p = multiprocessing.Process(target=worker, args=(child,))
    p.start()

    parent.send("hello")
    print(parent.recv())    # "HELLO"

    parent.send("world")
    print(parent.recv())    # "WORLD"

    parent.send("stop")
    print(parent.recv())    # "stopped"
    p.join()
```

## 四、共享内存 Value 和 Array

```python
import multiprocessing
import time

def worker(shared_array, lock):
    for i in range(len(shared_array)):
        with lock:
            shared_array[i] = shared_array[i] ** 2

if __name__ == "__main__":
    arr = multiprocessing.Array('i', [1, 2, 3, 4, 5], lock=True)
    lock = multiprocessing.Lock()

    p = multiprocessing.Process(target=worker, args=(arr, lock))
    p.start()
    p.join()

    print(list(arr))    # [1, 4, 9, 16, 25]
```

## 五、Manager

```python
import multiprocessing

def worker(d):
    d["count"] += 1
    d["items"].append(d["count"])

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        d = manager.dict({"count": 0, "items": []})
        processes = [multiprocessing.Process(target=worker, args=(d,))
                     for _ in range(5)]
        for p in processes: p.start()
        for p in processes: p.join()
        print(dict(d))
        # {'count': 5, 'items': [1, 2, 3, 4, 5]}
```

## 六、跨主机通信（Socket）

```python
# 服务端
import socket
import threading

def handle_client(conn, addr):
    print(f"连接来自 {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data.upper())
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9999))
server.listen()
print("监听 9999 端口...")

while True:
    conn, addr = server.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()
```

```python
# 客户端
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))

client.send("hello".encode())
print(client.recv(1024).decode())    # "HELLO"
client.close()
```

## 七、选择 IPC 方式的建议

```python
# 单机、同步：Queue（最常用）
# 单机、双向：Pipe
# 单机、共享大数据：Shared Memory
# 单机、共享复杂对象：Manager
# 跨主机：Socket / RPC（gRPC, XML-RPC）
```
""",

"thread_implementation": """\
## 一、继承 Thread 类

```python
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, duration):
        super().__init__()
        self.name = name
        self.duration = duration

    def run(self):                          # 必须实现 run 方法
        print(f"线程 {self.name} 开始")
        time.sleep(self.duration)
        print(f"线程 {self.name} 结束")

t = MyThread("Worker-1", 2)
t.start()
t.join()
```

## 二、传递参数

```python
class MyThread(threading.Thread):
    def __init__(self, name, *args, **kwargs):
        super().__init__()
        self.name = name
        self.args = args
        self.kwargs = kwargs

    def run(self):
        print(f"{self.name}: args={self.args}, kwargs={self.kwargs}")

t = MyThread("T1", 1, 2, 3, key="value")
t.start()
t.join()
# T1: args=(1, 2, 3), kwargs={'key': 'value'}
```

## 三、线程返回值

线程默认不返回值。常用三种方法：

### 方法 1：共享变量

```python
import threading

class MyThread(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.result = None

    def run(self):
        self.result = self.n ** 2

t = MyThread(10)
t.start()
t.join()
print(t.result)    # 100
```

### 方法 2：Queue

```python
import threading
import queue

result_queue = queue.Queue()

def worker(n):
    result_queue.put(n ** 2)

t = threading.Thread(target=worker, args=(10,))
t.start()
t.join()
print(result_queue.get())    # 100
```

### 方法 3：concurrent.futures（推荐）

```python
from concurrent.futures import ThreadPoolExecutor

def square(n):
    return n ** 2

with ThreadPoolExecutor() as executor:
    future = executor.submit(square, 10)
    print(future.result())    # 100

    # map：批量
    results = executor.map(square, [1, 2, 3, 4, 5])
    print(list(results))      # [1, 4, 9, 16, 25]
```

## 四、回调

```python
from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    time.sleep(1)
    return n * 2

def callback(future):
    print(f"任务完成，结果：{future.result()}")

with ThreadPoolExecutor() as executor:
    future = executor.submit(task, 10)
    future.add_done_callback(callback)
    # 主线程继续做其他事...

    # 如果想等待
    future.result()
```

## 五、异常处理

```python
from concurrent.futures import ThreadPoolExecutor

def task(n):
    if n < 0:
        raise ValueError("n 不能为负")
    return n ** 2

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(task, x) for x in [1, -1, 2]]
    for f in futures:
        try:
            print(f.result())
        except Exception as e:
            print(f"任务出错：{e}")
```

## 六、线程安全的数据结构

```python
import queue

# queue.Queue 是线程安全的
q = queue.Queue()
# q.put(item)   # 入队
# q.get()       # 出队（阻塞直到有元素）
# q.task_done() # 标记任务完成
# q.join()      # 等待所有任务完成

# 优先级队列
pq = queue.PriorityQueue()
pq.put((3, "task-3"))
pq.put((1, "task-1"))
pq.put((2, "task-2"))

while not pq.empty():
    print(pq.get())    # 数字小的优先
```

## 七、定时器（Timer）

```python
import threading

def hello():
    print("Hello!")

t = threading.Timer(3.0, hello)    # 3 秒后执行
t.start()
# 3 秒后：Hello!

t.cancel()    # 取消定时器（未执行时有效）
```
""",

"mutex_lock": """\
## 一、互斥锁（Mutex / Lock）

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        lock.acquire()
        try:
            counter += 1
        finally:
            lock.release()

# 推荐写法（with 语句）
def increment_better():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment_better) for _ in range(2)]
for t in threads: t.start()
for t in threads: t.join()

print(counter)    # 200000
```

## 二、可重入锁（RLock）

```python
import threading

# 同一个线程可以多次获取，普通 Lock 会死锁
lock = threading.RLock()

def func():
    with lock:
        with lock:          # 第二次获取不会死锁
            print("OK")

func()
```

## 三、死锁演示与解决

### 死锁演示

```python
import threading
import time

a = threading.Lock()
b = threading.Lock()

def task1():
    with a:
        time.sleep(0.1)
        with b:             # 等 b（被 task2 持有）
            print("task1")

def task2():
    with b:
        time.sleep(0.1)
        with a:             # 等 a（被 task1 持有）
            print("task2")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t1.start(); t2.start()
# 卡死
```

### 解决方法 1：固定加锁顺序

```python
def task1():
    with a:                  # 先 a
        with b:              # 后 b
            print("task1")

def task2():
    with a:                  # 也先 a
        with b:              # 也后 b
            print("task2")
```

### 解决方法 2：tryLock + 超时

```python
def task_with_timeout():
    while True:
        if a.acquire(timeout=1):
            try:
                if b.acquire(timeout=1):
                    try:
                        print("成功")
                        return
                    finally:
                        b.release()
            finally:
                a.release()
        time.sleep(0.1)
```

## 四、读写锁（threading.RWLock 不在标准库）

需要自己实现或用第三方库：

```python
import threading

class RWLock:
    def __init__(self):
        self._readers = 0
        self._lock = threading.Lock()
        self._can_read = threading.Condition(self._lock)
        self._can_write = threading.Condition(self._lock)
        self._writer = False

    def acquire_read(self):
        with self._lock:
            while self._writer:
                self._can_read.wait()
            self._readers += 1

    def release_read(self):
        with self._lock:
            self._readers -= 1
            if self._readers == 0:
                self._can_write.notify_all()

    def acquire_write(self):
        with self._lock:
            while self._writer or self._readers > 0:
                self._can_write.wait()
            self._writer = True

    def release_write(self):
        with self._lock:
            self._writer = False
            self._can_read.notify_all()
            self._can_write.notify_all()
```

## 五、原子操作（threading.atomic）

Python 没有原子的 `++` 操作。但某些操作天然原子：

```python
# ✅ 原子操作（单条字节码）
x = 1              # LOAD_CONST 1 / STORE_NAME x
x = y              # LOAD_NAME y / STORE_NAME x
lst.append(1)      # LOAD_METHOD / CALL

# ❌ 非原子（read-modify-write）
x += 1             # LOAD / BINARY_ADD / STORE（三步）
```

## 六、condition（条件变量）

```python
import threading

queue = []
MAX = 5
cv = threading.Condition()

def producer():
    with cv:
        while len(queue) >= MAX:
            cv.wait()
        queue.append(1)
        cv.notify()

def consumer():
    with cv:
        while not queue:
            cv.wait()
        queue.pop()
        cv.notify()

# 生产者-消费者模式
```

## 七、Event（事件）

```python
import threading

event = threading.Event()

def waiter():
    print("等待事件...")
    event.wait()           # 阻塞直到 set()
    print("事件已触发")

def setter():
    import time
    time.sleep(2)
    event.set()            # 触发

threading.Thread(target=waiter).start()
threading.Thread(target=setter).start()
# 2 秒后输出 "事件已触发"
```

## 八、Barrier（屏障）

```python
import threading

barrier = threading.Barrier(3)    # 3 个线程都到达后才继续

def worker(name):
    print(f"{name} 到达屏障")
    barrier.wait()                  # 等待其他线程
    print(f"{name} 继续执行")

threads = [threading.Thread(target=worker, args=(f"T{i}",)) for i in range(3)]
for t in threads: t.start()
for t in threads: t.join()
```
""",

"greenlet": """\
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
""",

"gevent": """\
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
""",

}