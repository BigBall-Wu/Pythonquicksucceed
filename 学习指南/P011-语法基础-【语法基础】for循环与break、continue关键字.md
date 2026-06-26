---
title: "P11 【语法基础】for循环与break、continue关键字"
p_no: 11
category: 语法基础
duration: 1764
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P11 【语法基础】for循环与break、continue关键字

> **课程分类**：语法基础
> **时长**：1764 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

语法基础阶段，从安装到容器、函数、装饰器。

## 课本对应章节

本节在《Python编程：从入门到实践》第 2 版中的对应位置：

- 4.1　遍历整个列表
- 4.2　避免缩进错误

## 一、课本内容（原书摘录）

## 4.1　遍历整个列表

你经常需要遍历列表的所有元素，对每个元素执行相同的操作。例如，在游戏中，可能需要将每个界面元素平移相同的距离；对于包含数字的列表，可能需要对每个元素执行相同的统计运算；在网站中，可能需要显示文章列表中的每个标题。需要对列表中的每个元素都执行相同的操作时，可使用Python中的`for`
 循环。

假设我们有一个魔术师名单，需要将其中每个魔术师的名字都打印出来。为此，可以分别获取名单中的每个名字，但这种做法会导致多个问题。例如，如果名单很长，将包含大量重复的代码。另外，每当名单的长度发生变化时，都必须修改代码。通过使用`for`
 循环，可以让Python去处理这些问题。

下面使用`for`
 循环来打印魔术师名单中的所有名字：

**

```
❶ magicians = ['alice', 'david', 'carolina']
❷ for magician in magicians:
❸     print(magician)
```

首先，像第3章那样定义一个列表（见❶）。接下来，定义一个`for`
 循环（见❷）。这行代码让Python从列表`magicians`
 中取出一个名字，并将其与变量`magician`
 相关联。最后，让Python打印前面赋给变量`magician`
 的名字（见❸）。这样，对于列表中的每个名字，Python都将重复执行❷处和❸处的代码行。你可以这样解读这些代码：对于列表`magicians`
 中的每位魔术师，都将其名字打印出来。输出很简单，就是列表中所有的名字：

```
alice
david
carolina
```

### 4.1.1　深入研究循环

循环这种概念很重要，因为它是让计算机自动完成重复工作的常见方式之一。例如，在前面magicians.py中使用的简单循环里，Python将首先读取其中的第一行代码：

```
for magician in magicians:
```

这行代码让Python获取列表`magicians`
 中的第一个值`'alice'`
 ，并将其与变量`magician`
 相关联。接下来，Python读取下一行代码：

```
    print(magician)
```

它让Python打印`magician`
 的值，依然是`'alice'`
 。鉴于该列表还包含其他值，Python返回到循环的第一行：

```
for magician in magicians:
```

Python获取列表中的下一个名字'david'，并将其与变量magician相关联，再执行下面这行代码：

```
    print(magician)
```

Python再次打印变量`magician`
 的值，当前为`'david'`
 。接下来，Python再次执行整个循环，对列表中的最后一个值`'carolina'`
 进行处理。至此，列表中没有其他的值了，因此Python接着执行程序的下一行代码。在这个示例中，`for`
 循环后面没有其他代码，因此程序就此结束。

刚开始使用循环时请牢记，对列表中的每个元素，都将执行循环指定的步骤，而不管列表包含多少个元素。如果列表包含一百万个元素，Python就重复执行指定的步骤一百万次，且通常速度非常快。

另外，编写`for`
 循环时，可以给依次与列表中每个值相关联的临时变量指定任意名称。然而，选择描述单个列表元素的有意义名称大有裨益。例如，对于小猫列表、小狗列表和一般性列表，像下面这样编写`for`
 循环的第一行代码是不错的选择：

```
for cat in cats:
for dog in dogs:
for item in list_of_items:
```

这些命名约定有助于你明白`for`
 循环中将对每个元素执行的操作。使用单数和复数式名称，可帮助你判断代码段处理的是单个列表元素还是整个列表。

### 4.1.2　在for
 循环中执行更多操作

在`for`
 循环中，可对每个元素执行任何操作。下面来扩展前面的示例，对于每位魔术师，都打印一条消息，指出他的表演太精彩了。

**

```
  magicians = ['alice', 'david', 'carolina']
  for magician in magicians:
❶     print(f"{magician.title()}, that was a great trick!")
```

相比于前一个示例，唯一的不同是为每位魔术师打印了一条以其名字为抬头的消息（见❶）。这个循环第一次迭代时，变量`magician`
 的值为`'alice'`
 ，因此Python打印的第一条消息的抬头为`'Alice'`
 ；第二次迭代时，消息的抬头为`'David'`
 ；第三次迭代时，抬头为`'Carolina'`
 。

下面的输出表明，对于列表中的每位魔术师，都打印了一条个性化消息：

```
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
```

在`for`
 循环中，想包含多少行代码都可以。在代码行`for magician in magicians`
 后面，每个缩进的代码行都是循环的一部分，将针对列表中的每个值都执行一次。因此，可对列表中的每个值执行任意次数的操作。

下面再添加一行代码，告诉每位魔术师，我们期待他的下一次表演：

```
  magicians = ['alice', 'david', 'carolina']
  for magician in magicians:
      print(f"{magician.title()}, that was a great trick!")
❶     print(f"I can't wait to see your next trick, {magician.title()}.\n")
```

两个函数调用`print()`
 都缩进了，因此它们都将针对列表中的每位魔术师执行一次。第二个函数调用`print()`
 中的换行符`"\n"`
 （见❶）在每次迭代结束后都插入一个空行，从而整洁地将针对各位魔术师的消息编组：

```
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

David, that was a great trick!
I can't wait to see your next trick, David.

Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
```

在`for`
 循环中，想包含多少行代码都可以。实际上，你会发现使用`for`
 循环对每个元素执行众多不同的操作很有用。

### 4.1.3　在for
 循环结束后执行一些操作

`for`
 循环结束后怎么办呢？通常，你需要提供总结性输出或接着执行程序必须完成的其他任务。

在`for`
 循环后面，没有缩进的代码都只执行一次，不会重复执行。下面来打印一条向全体魔术师致谢的消息，感谢他们的精彩表演。想要在打印给各位魔术师的消息后面打印一条给全体魔术师的致谢消息，需要将相应的代码放在`for`
 循环后面，且不缩进：

```
  magicians = ['alice', 'david', 'carolina']
  for magician in magicians:
      print(f"{magician.title()}, that was a great trick!")
      print(f"I can't wait to see your next trick, {magician.title()}.\n")

❶ print("Thank you, everyone. That was a great magic show!")
```

你在前面看到了，开头两个函数调用`print()`
 针对列表中的每位魔术师重复执行。然而，第三个函数调用`print()`
 没有缩进（见❶），因此只执行一次：

```
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

David, that was a great trick!
I can't wait to see your next trick, David.

Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

Thank you, everyone. That was a great magic show!
```

使用`for`
 循环处理数据是一种对数据集执行整体操作的不错方式。例如，你可能使用`for`
 循环来初始化游戏：遍历角色列表，将每个角色显示到屏幕上。然后在循环后面添加一个不缩进的代码块，在屏幕上绘制所有角色后显示一个Play Now按钮。


<!-- source: text/part0000_split_038.html -->


---

## 4.2　避免缩进错误

Python根据缩进来判断代码行与前一个代码行的关系。在前面的示例中，向各位魔术师显示消息的代码行是`for`
 循环的一部分，因为它们缩进了。Python通过使用缩进让代码更易读。简单地说，它要求你使用缩进让代码整洁而结构清晰。在较长的Python程序中，你将看到缩进程度各不相同的代码块，从而对程序的组织结构有大致的认识。

开始编写必须正确缩进的代码时，需要注意一些常见的****
 。例如，程序员有时候会将不需要缩进的代码块缩进，而对于必须缩进的代码块却忘了缩进。查看这样的错误示例有助于你以后避开它们，以及在它们出现在程序中时进行修复。

下面来看一些较为常见的缩进错误。

### 4.2.1　忘记缩进

对于位于`for`
 语句后面且属于循环组成部分的代码行，一定要缩进。如果忘记缩进， Python会提醒你：

**

```
  magicians = ['alice', 'david', 'carolina']
  for magician in magicians:
❶ print(magician)
```

函数调用`print()`
 （见❶）应缩进却没有缩进。Python没有找到期望缩进的代码块时，会让你知道哪行代码有问题。

```
File "magicians.py", line 3
  print(magician)
      ^
IndentationError: expected an indented block
```

通常，将紧跟在`for`
 语句后面的代码行缩进，可消除这种缩进错误。

### 4.2.2　忘记缩进额外的代码行

有时候，循环能够运行且不会报告错误，但结果可能出人意料。试图在循环中执行多项任务，却忘记缩进其中的一些代码行时，就会出现这种情况。

例如，如果忘记缩进循环中的第二行代码（它告诉每位魔术师，我们期待其下次表演），就会出现这种情况：

```
  magicians = ['alice', 'david', 'carolina']
  for magician in magicians:
      print(f"{magician.title()}, that was a great trick!")
❶ print(f"I can't wait to see your next trick, {magician.title()}.\n")
```

第二个函数调用`print()`
 （见❶）原本需要缩进，但Python发现`for`
 语句后面有一行代码是缩进的，因此没有报告错误。最终的结果是，对于列表中的每位魔术师，都执行了第一个函数调用`print()`
 ，因为它缩进了；而第二个函数调用`print()`
 没有缩进，因此只在循环结束后执行一次。由于变量`magician`
 的终值为`'carolina'`
 ，结果只有她收到了消息“looking forward to the next trick”：

```
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
```

这是一个****
 。从语法上看，这些Python代码是合法的，但由于存在逻辑错误，结果并不符合预期。如果你预期某项操作将针对每个列表元素都执行一次，但它总共只执行了一次，请确定需要将一行还是多行代码缩进。

### 4.2.3　不必要的缩进

如果你不小心缩进了无须缩进的代码行，Python将指出这一点：

**

```
  message = "Hello Python world!"
❶     print(message)
```

函数调用`print()`
 （见❶）无须缩进，因为它并非循环的组成部分。因此Python将指出这种错误：

```
  File "hello_world.py", line 2
    print(message)
    ^
IndentationError: unexpected indent
```

为避免意外缩进错误，请只缩进需要缩进的代码。在前面编写的程序中，只有要在`for`
 循环中对每个元素执行的代码需要缩进。

### 4.2.4　循环后不必要的缩进

如果不小心缩进了应在循环结束后执行的代码，这些代码将针对每个列表元素重复执行。在有些情况下，这可能导致Python报告语法错误，但在大多数情况下，这只会导致逻辑错误。

例如，如果不小心缩进了感谢全体魔术师精彩表演的代码行，结果将如何呢？

**

```
  magicians = ['alice', 'david', 'carolina']
  for magician in magicians:
      print(f"{magician.title()}, that was a great trick!")
      print(f"I can't wait to see your next trick, {magician.title()}.\n")

❶ print("Thank you everyone, that was a great magic show!")
```

由于❶处的代码行缩进了，它将针对列表中的每位魔术师执行一次，如下所示：

```
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

Thank you everyone, that was a great magic show!
David, that was a great trick!
I can't wait to see your next trick, David.

Thank you everyone, that was a great magic show!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

Thank you everyone, that was a great magic show!
```

这也是一个逻辑错误，与4.2.2节的错误类似。Python不知道你的本意，只要代码符合语法，它就会运行。如果原本只应执行一次的操作执行了多次，可能要对执行该操作的代码取消缩进。

### 4.2.5　遗漏了冒号

`for`
 语句末尾的冒号告诉Python，下一行是循环的第一行。

```
  magicians = ['alice', 'david', 'carolina']
❶ for magician in magicians
      print(magician)
```

如果不小心遗漏了冒号，如❶所示，将导致语法错误，因为Python不知道你意欲何为。这种错误虽然易于消除，但并不那么容易发现。程序员为找出这样的单字符错误，花费的时间多得令人惊讶。此类错误之所以难以发现，是因为通常在人们的意料之外。

> 动手试一试
> 
> 
> 练习4-1：比萨
>  　想出至少三种你喜欢的比萨，将其名称存储在一个列表中，再使用for
>  循环将每种比萨的名称打印出来。
> 
> 
> 修改这个for
>  循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。对于每种比萨，都显示一行输出，下面是一个例子。
> I like pepperoni pizza.
>  
> 
> 
> 在程序末尾添加一行代码，它不在for
>  循环中，指出你有多喜欢比萨。输出应包含针对每种比萨的消息，还有一个总结性句子，下面是一个例子。
> I really love pizza!
>  
> 
> 
> 
> 练习4-2：动物
>  　想出至少三种有共同特征的动物，将其名称存储在一个列表中，再使用for
>  循环将每种动物的名称打印出来。
> 
> 
> 修改这个程序，使其针对每种动物都打印一个句子，下面是一个例子。
> A dog would make a great pet.
>  
> 
> 
> 在程序末尾添加一行代码，指出这些动物的共同之处，如打印下面这样的句子。
> Any of these animals would make a great pet!


<!-- source: text/part0000_split_039.html -->



## 二、知识补全（书本没有的部分）

> 本节由课本内容为主，无额外补全。


## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）