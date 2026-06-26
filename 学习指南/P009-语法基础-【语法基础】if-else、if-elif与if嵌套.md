---
title: "P9 【语法基础】if-else、if-elif与if嵌套"
p_no: 9
category: 语法基础
duration: 1546
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P9 【语法基础】if-else、if-elif与if嵌套

> **课程分类**：语法基础
> **时长**：1546 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

语法基础阶段，从安装到容器、函数、装饰器。

## 课本对应章节

本节在《Python编程：从入门到实践》第 2 版中的对应位置：

- 5.3　if

## 一、课本内容（原书摘录）

## 5.3　if
 语句

理解条件测试后，就可以开始编写`if`
 语句了。`if`
 语句有很多种，选择使用哪种取决于要测试的条件数。前面讨论条件测试时，列举了多个`if`
 语句示例，下面更深入地讨论这个主题。

### 5.3.1　简单的if
 语句

最简单的`if`
 语句只有一个测试和一个操作：

```
if conditional_test:
    do something
```

第一行可包含任何条件测试，而在紧跟在测试后面的缩进代码块中，可执行任何操作。如果条件测试的结果为`True`
 ，Python就会执行紧跟在`if`
 语句后面的代码，否则Python将忽略这些代码。

假设有一个表示某人年龄的变量，而你想知道这个人是否符合投票的年龄，可使用如下代码：

**

```
  age = 19
❶ if age >= 18:
❷     print("You are old enough to vote!")
```

在❶处，Python检查变量`age`
 的值是否大于或等于18。答案是肯定的，因此Python执行❷处缩进的函数调用`print()`
 ：

```
You are old enough to vote!
```

在`if`
 语句中，缩进的作用与在`for`
 循环中相同。如果测试通过了，将执行`if`
 语句后面所有缩进的代码行，否则将忽略它们。

在紧跟`if`
 语句后面的代码块中，可根据需要包含任意数量的代码行。下面在一个人符合投票年龄时再打印一行输出，问他是否登记了：

```
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
```

条件测试通过了，而且两个函数调用`print()`
 都缩进了，因此它们都将执行：

```
You are old enough to vote!
Have you registered to vote yet?
```

如果`age`
 的值小于18，这个程序将不会有任何输出。

### 5.3.2　if-else
 语句

我们经常需要在条件测试通过时执行一个操作，在没有通过时执行另一个操作。在这种情况下，可使用Python提供的`if-else`
 语句。`if-else`
 语句块类似于简单的`if`
 语句，但其中的`else`
 语句让你能够指定条件测试未通过时要执行的操作。

下面的代码在一个人符合投票年龄时显示与前面相同的消息，在不符合时显示一条新消息：

```
  age = 17
❶ if age >= 18:
      print("You are old enough to vote!")
      print("Have you registered to vote yet?")
❷ else:
      print("Sorry, you are too young to vote.")
      print("Please register to vote as soon as you turn 18!")
```

如果❶处的条件测试通过了，就执行第一组缩进的函数调用`print()`
 。如果测试结果为`False`
 ，就执行❷处的`else`
 代码块。这次`age`
 小于18，条件测试未通过，因此执行`else`
 代码块中的代码：

```
Sorry, you are too young to vote.
Please register to vote as soon as you turn 18!
```

上述代码之所以可行，是因为只存在两种情形：要么符合投票年龄，要么不符合。`if-else`
 结构非常适合用于让Python执行两种操作之一的情形。在这样简单的`if-else`
 结构中，总是会执行两个操作中的一个。

### 5.3.3　if-elif-else
 结构

我们经常需要检查超过两个的情形，为此可使用Python提供的`if-elif-else`
 结构。Python只执行`if-elif-else`
 结构中的一个代码块。它依次检查每个条件测试，直到遇到通过了的条件测试。测试通过后，Python将执行紧跟在它后面的代码，并跳过余下的测试。

在现实世界中，很多情况下需要考虑的情形超过两个。例如，来看一个根据年龄段收费的游乐场：

- 4岁以下免费；
- 4～18岁收费25美元；
- 18岁（含）以上收费40美元。

如果只使用一条`if`
 语句，该如何确定门票价格呢？下面的代码确定一个人所属的年龄段，并打印一条包含门票价格的消息：

**

```
  age = 12

❶ if age < 4:
      print("Your admission cost is $0.")
❷ elif age < 18:
      print("Your admission cost is $25.")
❸ else:
      print("Your admission cost is $40.")
```

❶处的`if`
 测试检查一个人是否不满4岁。如果是，Python就打印一条合适的消息，并跳过余下测试。❷处的`elif`
 代码行其实是另一个`if`
 测试，仅在前面的测试未通过时才会运行。在这里，我们知道这个人不小于4岁，因为第一个测试未通过。如果这个人未满18岁，Python将打印相应的消息，并跳过`else`
 代码块。如果`if`
 测试和`elif`
 测试都未通过，Python将运行❸处`else`
 代码块中的代码。

在本例中，❶处测试的结果为`False`
 ，因此不执行其代码块。然而，第二个测试的结果为`True`
 （12小于18），因此执行其代码块。输出为一个句子，向用户指出门票价格：

```
Your admission cost is $25.
```

只要年龄超过17岁，前两个测试就都不能通过。在这种情况下，将执行`else`
 代码块，指出门票价格为40美元。

为了让代码更简洁，可不在`if-elif-else`
 代码块中打印门票价格，而只在其中设置门票价格，并在它后面添加一个简单的函数调用`print()`
 ：

```
  age = 12

  if age < 4:
❶     price = 0
  elif age < 18:
❷     price = 25
  else:
❸     price = 40

❹ print(f"Your admission cost is ${price}.")
```

❶处、❷处和❸处的代码行像前一个示例那样，根据人的年龄设置变量`price`
 的值。在`if-elif-else`
 结构中设置`price`
 的值后，一条未缩进的函数调用`print()`
 ❹会根据这个变量的值打印一条消息，指出门票的价格。

这些代码的输出与前一个示例相同，但`if-elif-else`
 结构的作用更小：它只确定门票价格，而不是在确定门票价格的同时打印一条消息。除效率更高外，这些修订后的代码还更容易修改：要调整输出消息的内容，只需修改一个而不是三个函数调用`print()`
 。

### 5.3.4　使用多个elif
 代码块

可根据需要使用任意数量的`elif`
 代码块。例如，假设前述游乐场要给老年人打折，可再添加一个条件测试，判断顾客是否符合打折条件。下面假设对于65岁（含）以上的老人，可半价（即20美元）购买门票：

```
  age = 12

  if age < 4:
      price = 0
  elif age < 18:
      price = 25
❶ elif age < 65:
      price = 40
❷ else:
      price = 20

  print(f"Your admission cost is ${price}.")
```

这些代码大多未变。第二个`elif`
 代码块（见❶）通过检查确定年龄不到65岁后，才将门票价格设置为全票价格——40美元。请注意，在`else`
 代码块（见❷）中，必须将所赋的值改为20，因为仅当年龄超过65岁（含）时，才会执行这个代码块。

### 5.3.5　省略else
 代码块

Python并不要求`if-elif`
 结构后面必须有`else`
 代码块。在有些情况下，`else`
 代码块很有用；而在其他一些情况下，使用一条`elif`
 语句来处理特定的情形更清晰：

```
  age = 12

  if age < 4:
      price = 0
  elif age < 18:
      price = 25
  elif age < 65:
      price = 40
❶ elif age >= 65:
      price = 20

  print(f"Your admission cost is ${price}.")
```

❶处的`elif`
 代码块在顾客的年龄超过65岁（含）时，将价格设置为20美元。这比使用`else`
 代码块更清晰些。经过这样的修改后，每个代码块都仅在通过了相应的测试时才会执行。

`else`
 是一条包罗万象的语句，只要不满足任何`if`
 或`elif`
 中的条件测试，其中的代码就会执行。这可能引入无效甚至恶意的数据。如果知道最终要测试的条件，应考虑使用一个`elif`
 代码块来代替`else`
 代码块。这样就可以肯定，仅当满足相应的条件时，代码才会执行。

### 5.3.6　测试多个条件

`if-elif-else`
 结构功能强大，但仅适合用于只有一个条件满足的情况：遇到通过了的测试后，Python就跳过余下的测试。这种行为很好，效率很高，让你能够测试一个特定的条件。

然而，有时候必须检查你关心的所有条件。在这种情况下，应使用一系列不包含`elif`
 和`else`
 代码块的简单`if`
 语句。在可能有多个条件为`True`
 且需要在每个条件为`True`
 时都采取相应措施时，适合使用这种方法。

下面再来看看前面的比萨店示例。如果顾客点了两种配料，就需要确保在其比萨中包含这些配料：

**

```
❶ requested_toppings = ['mushrooms', 'extra cheese']

❷ if 'mushrooms' in requested_toppings:
      print("Adding mushrooms.")
❸ if 'pepperoni' in requested_toppings:
      print("Adding pepperoni.")
❹ if 'extra cheese' in requested_toppings:
      print("Adding extra cheese.")

  print("\nFinished making your pizza!")
```

首先创建一个列表，其中包含顾客点的配料（见❶）。❷处的`if`
 语句检查顾客是否点了配料蘑菇（mushrooms）。如果点了，就打印一条确认消息。❸处检查配料辣香肠（pepperoni）的代码也是一个简单的`if`
 语句，而不是`elif`
 或`else`
 语句。因此不管前一个测试是否通过，都将进行这个测试。❹处的代码检查顾客是否要求多加芝士（extra cheese）。不管前两个测试的结果如何，都会执行这些代码。每当这个程序运行时，都会执行这三个独立的测试。

因为本例检查了每个条件，所以将在比萨中添加蘑菇并多加芝士：

```
Adding mushrooms.
Adding extra cheese.

Finished making your pizza!
```

如果像下面这样转而使用`if-elif-else`
 结构，代码将不能正确运行，因为有一个测试通过后，就会跳过余下的测试：

```
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
```

第一个测试检查列表中是否包含`'mushrooms'`
 。它通过了，因此将在比萨中添加蘑菇。然而，Python将跳过`if-elif-else`
 结构中余下的测试，不再检查列表中是否包含`'pepperoni'`
 和`'extra cheese'`
 。结果是，将添加顾客点的第一种配料，但不会添加其他配料：

```
Adding mushrooms.

Finished making your pizza!
```

总之，如果只想执行一个代码块，就使用`if-elif-else`
 结构；如果要执行多个代码块，就使用一系列独立的`if`
 语句。

> 动手试一试
> 
> 
> 练习5-3：外星人颜色
>  　假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color
>  的变量，并将其赋值为'green'
>  、'yellow'
>  或'red'
>  。
> 
> 编写一条if
>  语句，检查外星人是否是绿色的。如果是，就打印一条消息，指出玩家获得了5分。
> 编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）。
> 
> 
> 练习5-4：外星人颜色2
>  　像练习5-3那样设置外星人的颜色，并编写一个if-else
>  结构。
> 
> 如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5分。
> 如果外星人不是绿色的，就打印一条消息，指出玩家获得了10分。
> 编写这个程序的两个版本，在一个版本中执行if
>  代码块，在另一个版本中执行else
>  代码块。
> 
> 
> 练习5-5：外星人颜色3
>  　将练习5-4中的if-else
>  结构改为if-elif-else
>  结构。
> 
> 如果外星人是绿色的，就打印一条消息，指出玩家获得了5分。
> 如果外星人是黄色的，就打印一条消息，指出玩家获得了10分。
> 如果外星人是红色的，就打印一条消息，指出玩家获得了15分。
> 编写这个程序的三个版本，分别在外星人为绿色、黄色和红色时打印一条消息。
> 
> 
> 练习5-6：人生的不同阶段
>  　设置变量age
>  的值，再编写一个if-elif-else
>  结构，根据age
>  的值判断一个人处于人生的哪个阶段。
> 
> 如果年龄小于2岁，就打印一条消息，指出这个人是婴儿。
> 如果年龄为2（含）～4岁，就打印一条消息，指出这个人是幼儿。
> 如果年龄为4（含）～13岁，就打印一条消息，指出这个人是儿童。
> 如果年龄为13（含）～20岁，就打印一条消息，指出这个人是青少年。
> 如果年龄为20（含）～65岁，就打印一条消息，指出这个人是成年人。
> 如果年龄超过65岁（含），就打印一条消息，指出这个人是老年人。
> 
> 
> 练习5-7：喜欢的水果
>  　创建一个列表，其中包含你喜欢的水果，再编写一系列独立的if
>  语句，检查列表中是否包含特定的水果。
> 
> 将该列表命名为favorite_fruits
>  ，并在其中包含三种水果。
> 
> 编写5条if
>  语句，每条都检查某种水果是否包含在列表中。如果是，就打印一条消息，下面是一个例子。
> You really like bananas!


<!-- source: text/part0000_split_048.html -->



## 二、知识补全（书本没有的部分）

> 本节由课本内容为主，无额外补全。


## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）