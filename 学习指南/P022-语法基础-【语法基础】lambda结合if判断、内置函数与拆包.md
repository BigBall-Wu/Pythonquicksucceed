---
title: "P22 【语法基础】lambda结合if判断、内置函数与拆包"
p_no: 22
category: 语法基础
duration: 2776
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P22 【语法基础】lambda结合if判断、内置函数与拆包

> **课程分类**：语法基础
> **时长**：2776 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

语法基础阶段，从安装到容器、函数、装饰器。

## 课本对应章节

本节在《Python编程：从入门到实践》第 2 版中的对应位置：

- 8.3　返回值

## 一、课本内容（原书摘录）

## 8.3　返回值

函数并非总是直接显示输出，它还可以处理一些数据，并返回一个或一组值。函数返回的值称为****
 。在函数中，可使用`return`
 语句将值返回到调用函数的代码行。返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。

### 8.3.1　返回简单值

下面来看一个函数，它接受名和姓并返回整洁的姓名：

**

```
❶ def get_formatted_name(first_name, last_name):
      """返回整洁的姓名。"""
❷     full_name = f"{first_name} {last_name}"
❸     return full_name.title()

❹ musician = get_formatted_name('jimi', 'hendrix')
  print(musician)
```

函数`get_formatted_name()`
 的定义通过形参接受名和姓（见❶）。它将姓和名合而为一，在中间加上一个空格，并将结果赋给变量`full_name`
 （见❷）。然后，将`full_name`
 的值转换为首字母大写格式，并将结果返回到函数调用行（见❸）。

调用返回值的函数时，需要提供一个变量，以便将返回的值赋给它。在这里，将返回值赋给了变量`musician`
 （见❹）。输出为整洁的姓名：

```
Jimi Hendrix
```

原本只需编写下面的代码就可输出整洁的姓名，相比于此，前面做的工作好像太多了：

```
print("Jimi Hendrix")
```

但在需要分别存储大量名和姓的大型程序中，像`get_formatted_name()`
 这样的函数非常有用。可以分别存储名和姓，每当需要显示姓名时都调用这个函数。

### 8.3.2　让实参变成可选的

有时候，需要让实参变成可选的，这样使用函数的人就能只在必要时提供额外的信息。可使用默认值来让实参变成可选的。

例如，假设要扩展函数`get_formatted_name()`
 ，使其同时处理中间名。为此，可将其修改成类似于下面这样：

```
def get_formatted_name(first_name, middle_name, last_name):
    """返回整洁的姓名。"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
```

只要同时提供名、中间名和姓，这个函数就能正确运行。它根据这三部分创建一个字符串，在适当的地方加上空格，并将结果转换为首字母大写格式：

```
John Lee Hooker
```

并非所有的人都有中间名，但如果调用这个函数时只提供了名和姓，它将不能正确运行。为了让中间名变成可选的，可给形参`middle_name`
 指定一个空的默认值，并在用户没有提供中间名时不使用这个形参。为让`get_formatted_name()`
 在没有提供中间名时依然可行，可将形参`middle_name`
 的默认值设置为空字符串，并将其移到形参列表的末尾：

```
❶ def get_formatted_name(first_name, last_name, middle_name=''):
      """返回整洁的姓名。"""
❷     if middle_name:
          full_name = f"{first_name} {middle_name} {last_name}"
❸     else:
          full_name = f"{first_name} {last_name}"
      return full_name.title()

  musician = get_formatted_name('jimi', 'hendrix')
  print(musician)

❹ musician = get_formatted_name('john', 'hooker', 'lee')
  print(musician)
```

在本例中，姓名是根据三个可能提供的部分创建的。由于人都有名和姓，因此在函数定义中首先列出了这两个形参。中间名是可选的，因此在函数定义中最后列出该形参，并将其默认值设置为空字符串（见❶）。

在函数体中，检查是否提供了中间名。Python将非空字符串解读为`True`
 ，因此如果函数调用中提供了中间名，`if middle_name`
 将为`True`
 （见❷）。如果提供了中间名，就将名、中间名和姓合并为姓名，再将其修改为首字母大写格式，并返回到函数调用行。在函数调用行，将返回的值赋给变量`musician`
 ，然后这个变量的值被打印出来。如果没有提供中间名，`middle_name`
 将为空字符串，导致`if`
 测试未通过，进而执行`else`
 代码块（见❸）：只使用名和姓来生成姓名，并将格式设置好的姓名返回给函数调用行。在函数调用行，将返回的值赋给变量`musician`
 ，然后这个变量的值被打印出来。

调用这个函数时，如果只想指定名和姓，调用起来将非常简单。如果还要指定中间名，就必须确保它是最后一个实参，这样Python才能正确地将位置实参关联到形参（见❹）。

这个修改后的版本不仅适用于只有名和姓的人，而且适用于还有中间名的人：

```
Jimi Hendrix
John Lee Hooker
```

可选值让函数能够处理各种不同的情形，同时确保函数调用尽可能简单。

### 8.3.3　返回字典

函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。例如，下面的函数接受姓名的组成部分，并返回一个表示人的字典：

**

```
  def build_person(first_name, last_name):
      """返回一个字典，其中包含有关一个人的信息。"""
❶     person = {'first': first_name, 'last': last_name}
❷     return person

  musician = build_person('jimi', 'hendrix')
❸ print(musician)
```

函数`build_person()`
 接受名和姓，并将这些值放到字典中（见❶）。存储`first_name`
 的值时，使用的键为`'first'`
 ，而存储`last_name`
 的值时，使用的键为`'last'`
 。最后，返回表示人的整个字典（见❷）。在❸处，打印这个返回的值，此时原来的两项文本信息存储在一个字典中：

```
{'first': 'jimi', 'last': 'hendrix'}
```

这个函数接受简单的文本信息，并将其放在一个更合适的数据结构中，让你不仅能打印这些信息，还能以其他方式处理它们。当前，字符串`'jimi'`
 和`'hendrix'`
 被标记为名和姓。你可以轻松地扩展这个函数，使其接受可选值，如中间名、年龄、职业或其他任何要存储的信息。例如，下面的修改让你能存储年龄：

```
def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人的信息。"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
```

在函数定义中，新增了一个可选形参`age`
 ，并将其默认值设置为特殊值`None`
 （表示变量没有值）。可将`None`
 视为占位值。在条件测试中，`None`
 相当于`False`
 。如果函数调用中包含形参`age`
 的值，这个值将被存储到字典中。在任何情况下，这个函数都会存储人的姓名，但可进行修改，使其同时存储有关人的其他信息。

### 8.3.4　结合使用函数和while
 循环

可将函数同本书前面介绍的任何Python结构结合起来使用。例如，下面将结合使用函数`get_formatted_name()`
 和`while`
 循环，以更正式的方式问候用户。下面尝试使用名和姓跟用户打招呼：

**

```
  def get_formatted_name(first_name, last_name):
      """返回整洁的姓名。"""
      full_name = f"{first_name} {last_name}"
      return full_name.title()

  # 这是一个无限循环！
  while True:
❶     print("\nPlease tell me your name:")
      f_name = input("First name: ")
      l_name = input("Last name: ")

      formatted_name = get_formatted_name(f_name, l_name)
      print(f"\nHello, {formatted_name}!")
```

在本例中，使用的是`get_formatted_name()`
 的简单版本，不涉及中间名。`while`
 循环让用户输入姓名：依次提示用户输入名和姓（见❶）。

但这个`while`
 循环存在一个问题：没有定义退出条件。请用户提供一系列输入时，该在什么地方提供退出途径呢？要让用户能够尽可能容易地退出，因此每次提示用户输入时，都应提供退出途径。每次提示用户输入时，都使用`break`
 语句提供退出循环的简单途径：

```
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名。"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
```

我们添加了一条消息来告诉用户如何退出，然后在每次提示用户输入时，都检查他输入的是否是退出值。如果是，就退出循环。现在，这个程序将不断地问候，直到用户输入的姓或名为`'q'`
 ：

```
Please tell me your name:
(enter 'q' at any time to quit)
First name: eric
Last name: matthes

Hello, Eric Matthes!

Please tell me your name:
(enter 'q' at any time to quit)
First name: q
```

> 动手试一试
> 
> 
> 练习8-6：城市名
>  　编写一个名为city_country()
>  的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面的字符串：
> 
> "Santiago, Chile"
> 
> 至少使用三个城市国家对来调用这个函数，并打印它返回的值。
> 
> 练习8-7：专辑
>  　编写一个名为make_album()
>  的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
> 给函数make_album()
>  添加一个默认值为None
>  的可选形参，以便存储专辑包含的歌曲数。如果调用这个函数时指定了歌曲数，就将该值添加到表示专辑的字典中。调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
> 
> 练习8-8：用户的专辑
>  　在为完成练习8-7编写的程序中，编写一个while
>  循环，让用户输入专辑的歌手和名称。获取这些信息后，使用它们来调用函数make_album()
>  并将创建的字典打印出来。在这个while
>  循环中，务必提供退出途径。


<!-- source: text/part0000_split_066.html -->



## 二、知识补全（书本没有的部分）

\
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

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）