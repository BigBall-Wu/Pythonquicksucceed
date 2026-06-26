---
title: "P19 【语法基础】函数、return返回值与形参实参"
p_no: 19
category: 语法基础
duration: 1563
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P19 【语法基础】函数、return返回值与形参实参

> **课程分类**：语法基础
> **时长**：1563 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

语法基础阶段，从安装到容器、函数、装饰器。

## 课本对应章节

本节在《Python编程：从入门到实践》第 2 版中的对应位置：

- 8.1　定义函数
- 8.2　传递实参
- 8.3　返回值

## 一、课本内容（原书摘录）

## 8.1　定义函数

下面是一个打印问候语的简单函数，名为`greet_user()`
 ：

**

```
❶ def greet_user():
❷     """显示简单的问候语。"""
❸     print("Hello!")

❹ greet_user()
```

本例演示了最简单的函数结构。❶处的代码行使用关键字`def`
 来告诉Python，你要定义一个函数。这是****
 ，向Python指出了函数名，还可能在圆括号内指出函数为完成任务需要什么样的信息。在这里，函数名为`greet_user()`
 ，它不需要任何信息就能完成工作，因此括号是空的（即便如此，括号也必不可少）。最后，定义以冒号结尾。

紧跟在`def greet_user():`
 后面的所有缩进行构成了函数体。❷处的文本是称为****
 （docstring）的注释，描述了函数是做什么的。文档字符串用三引号括起，Python使用它们来生成有关程序中函数的文档。

代码行`print("Hello!")`
 （见❸）是函数体内的唯一一行代码，因此`greet_user()`
 只做一项工作：打印`Hello!`
 。

要使用这个函数，可调用它。****
 让Python执行函数的代码。要****
 函数，可依次指定函数名以及用圆括号括起的必要信息，如❹处所示。由于这个函数不需要任何信息，调用它时只需输入`greet_user()`
 即可。和预期一样，它打印`Hello!`
 ：

```
Hello!
```

### 8.1.1　向函数传递信息

只需稍作修改，就可让函数`greet_user()`
 不仅向用户显示`Hello!`
 ，还将用户的名字作为抬头。为此，可在函数定义`def greet_user()`
 的括号内添加`username`
 。通过在这里添加`username`
 ，可让函数接受你给`username`
 指定的任何值。现在，这个函数要求你调用它时给`username`
 指定一个值。调用`greet_user()`
 时，可将一个名字传递给它，如下所示：

```
def greet_user(username):
    """显示简单的问候语。"""
    print(f"Hello, {username.title()}!")

greet_user('jesse')
```

代码`greet_user('jesse')`
 调用函数`greet_user()`
 ，并向它提供执行函数调用`print()`
 所需的信息。这个函数接受你传递给它的名字，并向这个人发出问候：

```
Hello, Jesse!
```

同样，`greet_user('sarah')`
 调用函数`greet_user()`
 并向它传递`'sarah'`
 ，从而打印`Hello, Sarah!`
 。可根据需要调用函数`greet_user()`
 任意次，调用时无论传入什么名字，都将生成相应的输出。

### 8.1.2　实参和形参

前面定义函数`greet_user()`
 时，要求给变量`username`
 指定一个值。调用这个函数并提供这种信息（人名）时，它将打印相应的问候语。

在函数`greet_user()`
 的定义中，变量`username`
 是一个****
 （parameter），即函数完成工作所需的信息。在代码`greet_user('jesse')`
 中，值`'jesse'`
 是一个****
 （argument），即调用函数时传递给函数的信息。调用函数时，将要让函数使用的信息放在圆括号内。在`greet_user('jesse')`
 中，将实参`'jesse'`
 传递给了函数`greet_user()`
 ，这个值被赋给了形参`username`
 。

> 注意
>  　大家有时候会形参、实参不分，因此如果你看到有人将函数定义中的变量称为实参或将函数调用中的变量称为形参，不要大惊小怪。

> 动手试一试
> 
> 
> 练习8-1：消息
>  　编写一个名为display_message()
>  的函数，它打印一个句子，指出你在本章学的是什么。调用这个函数，确认显示的消息正确无误。
> 
> 练习8-2：喜欢的图书
>  　编写一个名为favorite_book()
>  的函数，其中包含一个名为title
>  的形参。这个函数打印一条消息，下面是一个例子。
> One of my favorite books is Alice in Wonderland.
> 调用这个函数，并将一本图书的名称作为实参传递给它。


<!-- source: text/part0000_split_064.html -->


---

## 8.2　传递实参

函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。向函数传递实参的方式很多：可使用****
 ，这要求实参的顺序与形参的顺序相同；也可使用****
 ，其中每个实参都由变量名和值组成；还可使用列表和字典。下面依次介绍这些方式。

### 8.2.1　位置实参

调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。为此，最简单的关联方式是基于实参的顺序。这种关联方式称为****
 。

为明白其中的工作原理，来看一个显示宠物信息的函数。这个函数指出一个宠物属于哪种动物以及它叫什么名字，如下所示：

**

```
❶ def describe_pet(animal_type, pet_name):
      """显示宠物的信息。"""
      print(f"\nI have a {animal_type}.")
      print(f"My {animal_type}'s name is {pet_name.title()}.")

❷ describe_pet('hamster', 'harry')
```

这个函数的定义表明，它需要一种动物类型和一个名字（见❶）。调用`describe_pet()`
 时，需要按顺序提供一种动物类型和一个名字。例如，在刚才的函数调用中，实参`'hamster'`
 被赋给形参`animal_type`
 ，而实参`'harry'`
 被赋给形参`pet_name`
 （见❷）。在函数体内，使用了这两个形参来显示宠物的信息。

输出描述了一只名为Harry的仓鼠：

```
I have a hamster.
My hamster's name is Harry.
```

1. 多次调用函数

可以根据需要调用函数任意次。要再描述一个宠物，只需再次调用describe_pet()
 即可：

def describe_pet(animal_type, pet_name):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

第二次调用describe_pet()
 函数时，向它传递了实参'dog'
 和'willie'
 。与第一次调用时一样，Python将实参'dog'
 关联到形参animal_type
 ，并将实参'willie'
 关联到形参pet_name
 。与前面一样，这个函数完成了任务，但打印的是一条名为Willie的小狗的信息。至此，有一只名为Harry的仓鼠，还有一条名为Willie的小狗：

I have a hamster.
My hamster's name is Harry.

I have a dog.
My dog's name is Willie.

多次调用函数是一种效率极高的工作方式。只需在函数中编写一次描述宠物的代码，然后每当需要描述新宠物时，都调用该函数并向它提供新宠物的信息。即便描述宠物的代码增加到了10行，依然只需使用一行调用函数的代码，就可描述一个新宠物。
在函数中，可根据需要使用任意数量的位置实参，Python将按顺序将函数调用中的实参关联到函数定义中相应的形参。
2. 位置实参的顺序很重要

使用位置实参来调用函数时，如果实参的顺序不正确，结果可能出乎意料：

def describe_pet(animal_type, pet_name):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')

在这个函数调用中，先指定名字，再指定动物类型。由于实参'harry'
 在前，这个值将赋给形参animal_type
 。同理，'hamster'
 将赋给形参pet_name
 。结果是有一个名为Hamster的harry：

I have a harry.
My harry's name is Hamster.

如果你得到的结果像上面一样可笑，请确认函数调用中实参的顺序与函数定义中形参的顺序一致。

### 8.2.2　关键字实参

****
 是传递给函数的名称值对。因为直接在实参中将名称和值关联起来，所以向函数传递实参时不会混淆（不会得到名为Hamster的harry这样的结果）。关键字实参让你无须考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。

下面来重新编写pets.py，在其中使用关键字实参来调用`describe_pet()`
 ：

```
def describe_pet(animal_type, pet_name):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
```

函数`describe_pet()`
 还和之前一样，但调用这个函数时，向Python明确地指出了各个实参对应的形参。看到这个函数调用时，Python知道应该将实参`'hamster'`
 和`'harry'`
 分别赋给形参`animal_type`
 和`pet_name`
 。输出正确无误，指出有一只名为Harry的仓鼠。

关键字实参的顺序无关紧要，因为Python知道各个值该赋给哪个形参。下面两个函数调用是等效的：

```
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
```

> 注意
>  　使用关键字实参时，务必准确指定函数定义中的形参名。

### 8.2.3　默认值

编写函数时，可给每个形参指定****
 。在调用函数中给形参提供了实参时，Python将使用指定的实参值；否则，将使用形参的默认值。因此，给形参指定默认值后，可在函数调用中省略相应的实参。使用默认值可简化函数调用，还可清楚地指出函数的典型用法。

例如，如果你发现调用`describe_pet()`
 时，描述的大多是小狗，就可将形参`animal_type`
 的默认值设置为`'dog'`
 。这样，调用`describe_pet()`
 来描述小狗时，就可不提供这种信息：

```
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
```

这里修改了函数`describe_pet()`
 的定义，在其中给形参`animal_type`
 指定了默认值`'dog'`
 。这样，调用这个函数时，如果没有给`animal_type`
 指定值，Python就将把这个形参设置为`'dog'`
 ：

```
I have a dog.
My dog's name is Willie.
```

请注意，在这个函数的定义中，修改了形参的排列顺序。因为给`animal_type`
 指定了默认值，无须通过实参来指定动物类型，所以在函数调用中只包含一个实参——宠物的名字。然而，Python依然将这个实参视为位置实参，因此如果函数调用中只包含宠物的名字，这个实参将关联到函数定义中的第一个形参。这就是需要将`pet_name`
 放在形参列表开头的原因。

现在，使用这个函数的最简单方式是在函数调用中只提供小狗的名字：

```
describe_pet('willie')
```

这个函数调用的输出与前一个示例相同。只提供了一个实参`'willie'`
 ，这个实参将关联到函数定义中的第一个形参`pet_name`
 。由于没有给`animal_type`
 提供实参，Python将使用默认值`'dog'`
 。

如果要描述的动物不是小狗，可使用类似于下面的函数调用：

```
describe_pet(pet_name='harry', animal_type='hamster')
```

由于显式地给`animal_type`
 提供了实参，Python将忽略这个形参的默认值。

> 注意
>  　使用默认值时，必须先在形参列表中列出没有默认值的形参，再列出有默认值的实参。这让Python依然能够正确地解读位置实参。

### 8.2.4　等效的函数调用

鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式。请看下面对函数`describe_pet()`
 的定义，其中给一个形参提供了默认值：

```
def describe_pet(pet_name, animal_type='dog'):
```

基于这种定义，在任何情况下都必须给`pet_name`
 提供实参。指定该实参时可采用位置方式，也可采用关键字方式。如果要描述的动物不是小狗，还必须在函数调用中给`animal_type`
 提供实参。同样，指定该实参时可以采用位置方式，也可采用关键字方式。

下面对这个函数的所有调用都可行：

```
# 一条名为Willie的小狗。
describe_pet('willie')
describe_pet(pet_name='willie')

# 一只名为Harry的仓鼠。
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
```

这些函数调用的输出与前面的示例相同。

> 注意
>  　使用哪种调用方式无关紧要，只要函数调用能生成你期望的输出就行。使用对你来说最容易理解的调用方式即可。

### 8.2.5　避免实参错误

等你开始使用函数后，如果遇到实参不匹配错误，不要大惊小怪。你提供的实参多于或少于函数完成工作所需的信息时，将出现实参不匹配错误。例如，如果调用函数`describe_pet()`
 时没有指定任何实参，结果将如何呢？

```
def describe_pet(animal_type, pet_name):
    """显示宠物的信息。"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet()
```

Python发现该函数调用缺少必要的信息，traceback指出了这一点：

```
  Traceback (most recent call last):
❶   File "pets.py", line 6, in <module>
❷     describe_pet()
❸ TypeError: describe_pet() missing 2 required positional arguments: 'animal_
  type' and 'pet_name'
```

在❶处，traceback指出了问题出在什么地方，让我们能够回过头去找出函数调用中的错误。在❷处，指出了导致问题的函数调用。在❸处，traceback指出该函数调用少了两个实参，并指出了相应形参的名称。如果这个函数存储在一个独立的文件中，我们也许无须打开这个文件并查看函数的代码，就能重新正确地编写函数调用。

Python读取函数的代码并指出需要为哪些形参提供实参，这提供了极大的帮助。这也是应该给变量和函数指定描述性名称的另一个原因：如果这样做了，那么无论对于你，还是可能使用你编写的代码的其他任何人来说，Python提供的错误消息都将更帮助。

如果提供的实参太多，将出现类似的traceback，帮助你确保函数调用和函数定义匹配。

> 动手试一试
> 
> 
> 练习8-3：T恤
>  　编写一个名为make_shirt()
>  的函数，它接受一个尺码以及要印到T恤上的字样。这个函数应打印一个句子，概要地说明T恤的尺码和字样。
> 使用位置实参调用该函数来制作一件T恤，再使用关键字实参来调用这个函数。
> 
> 练习8-4：大号T恤
>  　修改函数make_shirt()
>  ，使其在默认情况下制作一件印有“I love Python”字样的大号T恤。调用这个函数来制作：一件印有默认字样的大号T恤，一件印有默认字样的中号T恤，以及一件印有其他字样的T恤（尺码无关紧要）。
> 
> 练习8-5：城市
>  　编写一个名为describe_city()
>  的函数，它接受一座城市的名字以及该城市所属的国家。这个函数应打印一个简单的句子，下面是一个例子。
> Reykjavik is in Iceland.
> 给用于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。


<!-- source: text/part0000_split_065.html -->


---

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

> 本节由课本内容为主，无额外补全。


## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）