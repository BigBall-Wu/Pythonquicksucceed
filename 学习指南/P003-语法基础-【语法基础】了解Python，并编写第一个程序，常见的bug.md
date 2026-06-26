---
title: "P3 【语法基础】了解Python，并编写第一个程序，常见的bug"
p_no: 3
category: 语法基础
duration: 1746
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P3 【语法基础】了解Python，并编写第一个程序，常见的bug

> **课程分类**：语法基础
> **时长**：1746 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

语法基础阶段，从安装到容器、函数、装饰器。

## 课本对应章节

本节在《Python编程：从入门到实践》第 2 版中的对应位置：

- 1.1　搭建编程环境
- 1.2　在不同操作系统中搭建Python编程环境
- 1.3　运行Hello World程序

## 一、课本内容（原书摘录）

## 1.1　搭建编程环境

在不同的操作系统中，Python存在细微的差别，因此有几点你需要牢记在心。本节将确保你的系统正确安装Python。

### 1.1.1　Python版本

每种编程语言都会随着新概念和新技术的推出而不断发展，Python开发者也在一直致力于丰富和强化其功能。本书编写期间的最新版本为Python 3.7，但只要你安装了Python 3.6或更高的版本，就能运行本书中的所有代码。在本节中，你将核实系统是否安装了Python，以及是否需要安装更新的版本。附录A提供了详尽的指南，指导你在各种主流操作系统中安装最新版本的Python。

有些较老的Python项目依然使用Python 2，但你应该使用Python 3。如果你的系统安装了Python 2，很可能是为了支持系统需要的一些旧程序。你应保留它，并安装更新的版本以便学习本书。

### 1.1.2　运行Python代码片段

Python自带一个在终端窗口中运行的解释器，让你无须保存并运行整个程序就能尝试运行Python代码片段。

本书将以如下方式列出代码片段：

```
❶ >>> print("Hello Python interpreter!")
  Hello Python interpreter!
```

提示符`>>>`
 表明正在使用终端窗口，而加粗的文本表示需要你输入之后按回车键来执行的代码。本书的大多数示例是独立的小程序，你将在编辑器中执行它们，因为大多数代码也是这样编写出来的。然而，为高效地演示一些基本概念，需要在Python终端会话中执行一系列代码片段。只要代码清单中包含三个右尖括号（如❶所示），就意味着代码是在终端会话中执行的，而输出也是来自终端会话的。稍后将演示如何在Python解释器中编写代码。

此外，你还要安装一款文本编辑器，并使用它来完成学习编程的标准操作——编写一个简单的Hello World程序。长期以来，编程界都认为刚接触一门新语言时，如果首先使用它来编写一个在屏幕上显示消息“Hello world!”的程序，将给你带来好运。这种程序虽然简单，却有其用途：如果它能够在你的系统上正确运行，那么你编写的任何Python程序也都将正确运行。

### 1.1.3　Sublime Text简介

Sublime Text是一款简单的文本编辑器，可以在任何现代操作系统中安装。你几乎能直接在Sublime Text中执行所有程序。在Sublime Text中执行程序时，代码将在其内嵌的终端会话中运行，让你能够轻松地看到输出。

Sublime Text是一款适合初学者的编辑器，但很多专业编程人员也在使用它。在学习Python的过程中熟练掌握Sublime Text之后，可继续使用它来编写复杂的大型项目。Sublime Text的许可条件非常宽松，可以一直免费使用，但如果你喜欢它并想长期使用，其开发者会要求你购买许可证。

附录B介绍了其他几种文本编辑器，如果你想知道还有哪些编辑器可供使用，现在就应该读一读。如果你想马上动手编程，可先使用Sublime Text，等有了一些编程经验后再考虑使用其他编辑器。本章稍后将引导你在当前使用的操作系统中安装Sublime Text。


<!-- source: text/part0000_split_017.html -->


---

## 1.2　在不同操作系统中搭建Python编程环境

Python是一种跨平台的编程语言，这意味着它能够运行在所有主流操作系统中。在所有安装了Python的现代计算机上，都能够运行你编写的任何Python程序。然而，在不同的操作系统中，安装Python的方法存在细微的差别。

在本节中，你将学习如何在自己的系统中安装Python。首先要检查系统是否安装了较新的Python版本，如果没有，就进行安装；然后是安装Sublime Text。在不同的操作系统中搭建Python编程环境时，只有这两步存在差别。

接下来，你将运行Hello World程序，并排除各种故障。我将详细介绍如何在各种操作系统中完成这些任务，让你能够搭建一个对初学者友好的Python编程环境。

### 1.2.1　在Windows系统中搭建Python编程环境

Windows系统并非都默认安装了Python，因此你可能需要安装它，再安装Sublime Text。

1. 安装Python

首先，检查你的系统是否安装了Python。为此，在“开始”菜单中输入command
 并按回车以打开一个命令窗口；也可以按住Shift键并右击桌面，选择“在此处打开命令窗口”1
 。在终端窗口中输入python
 （全部小写）并按回车：如果出现了Python提示符（>>>
 ），就说明系统安装了Python；如果出现一条错误消息，指出python
 是无法识别的命令，就说明没有安装Python。
如果出现后一种情况或者安装的Python版本低于3.6，就需要下载Windows Python安装程序。为此，请访问Python官方网站主页。将鼠标指向Download链接，你将看到一个用于下载最新版本Python的按钮。单击该按钮，这将根据你的系统自动下载正确的安装程序。下载安装程序后，运行它。请务必选中复选框Add Python（版本号）to PATH（例如图1-1），这让你能够更轻松地配置系统。

图1-1　确保选中复选框Add Python（版本号） to PATH
2. 在终端会话中运行Python

打开一个命令窗口，并在其中执行命令python
 。如果出现了Python提示符（>>>
 ），就说明Windows找到了你刚安装的Python版本。

C:\> python
Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit
(AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>

注意
 　如果没有看到类似的输出，请参阅附录A中更详尽的安装说明。

在Python会话中执行下面的命令，并确认看到了输出“Hello Python interpreter!”。

>>> print("Hello Python interpreter!")
Hello Python interpreter!
>>>

每当要运行Python代码片段时，都请打开一个命令窗口并启动Python终端会话。要关闭该终端会话，可按Ctrl + Z、再按回车键，也可执行命令exit()
 。
3. 安装Sublime Text

要下载Sublime Text安装程序，可访问Sublime Text网站主页，单击Download链接，并查找Windows安装程序。下载安装程序后运行它，并接受所有的默认设置。

在Windows 10系统中，可如此打开PowerShell窗口。——编者注

### 1.2.2　在macOS系统中搭建Python编程环境

大多数macOS系统默认安装了Python。确定安装了Python后，你还需安装Sublime Text，并确保其配置正确无误。

1. 检查是否安装了Python 3

在文件夹Applications/Utilities中，选择Terminal，打开一个终端窗口；也可以按Command + 空格键，再输入terminal
 并按回车。为确定是否安装了Python，请执行命令python
 （请注意，其中的p
 是小写的），这也将在终端窗口中启动Python，让你能够输入Python命令。输出类似于下面这样，它指出了安装的Python版本；最后的>>>
 是提示符，让你能够输入Python命令。

$ python
Python 2.7.15 (default, Aug 17 2018, 22:39:05)
[GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)] on darwin
Type "help", "copyright", "credits", or "license" for more information.
>>>

上述输出表明，当前计算机默认使用的Python版本为Python 2.7.15。看到上述输出后，如果要退出Python并返回到终端窗口，可按Ctrl + D或执行命令exit()
 。
要检查系统是否安装了Python 3，可尝试执行命令python3
 。可能会出现一条错误消息，这意味着没有安装任何Python 3版本。如果输出指出安装了Python 3.6或更高的版本，可以直接跳过下一小节。如果系统没有安装Python 3，就需要手动安装它。注意，请将本书中所有的命令python
 都替换为命令python3
 ，这样才能使用Python 3（而不是Python 2）。Python 2和Python 3的差别非常大，如果你使用Python 2来运行本书的代码，肯定会遇到麻烦。
如果系统默认安装的是低于Python 3.6的版本，请按下一小节的说明安装最新版本。
2. 安装最新的Python版本

要下载Python安装程序，可访问Python网站主页。将鼠标指向Download链接，你将看到一个用于下载最新版本Python的按钮。单击该按钮，这将根据你的系统自动下载正确的安装程序。下载安装程序后，运行它。
运行安装程序后，在终端提示符下执行如下命令：

$  python3 --version
Python 3.7.2

输出应该类似于上面这样。如果确实如此，就可以开始尝试使用Python了，但请务必将本书中的每个命令python
 都替换为python3
 。
3. 在终端会话中运行Python代码

现在可以打开终端窗口并执行命令python3
 ，再尝试运行Python代码片段。请在终端会话中输入如下代码行并按回车：

>>> print("Hello Python interpreter!")
Hello Python interpreter!
>>>

消息将直接输出到当前终端窗口中。别忘了，要关闭Python解释器，可按Ctrl + D或执行命令exit()
 。
4. 安装Sublime Text

要安装编辑器Sublime Text，需要下载安装程序。为此，可访问Sublime Text网站主页，单击链接Download，并查找macOS安装程序。下载安装程序后运行它，再将Sublime Text图标拖放到文件夹Applications中。

### 1.2.3　在Linux系统中搭建Python编程环境

Linux系统是为编程而设计的，因此大多数Linux计算机默认安装了Python。编写和维护Linux的人认为，你很可能会使用这种系统进行编程，他们也鼓励你这样做。因此，要在这种系统中编程，你几乎不用安装什么软件，只需要修改一些设置。

1. 检查Python版本

在你的系统中运行应用程序Terminal（如果你使用的是Ubuntu，可按Ctrl + Alt + T），打开一个终端窗口。为确定安装的是哪个Python版本，请执行命令python3
 （请注意，其中的p
 是小写的）。如果安装了Python，这个命令将启动Python解释器。输出类似于下面这样，它指出了安装的Python版本；最后的>>>
 是提示符，让你能够输入Python命令。

$ python3
Python 3.7.2 (default, Dec 27 2018, 04:01:51)
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>

上述输出表明，当前计算机默认使用的Python版本为Python 3.7.2。看到上述输出后，如果要退出Python并返回到终端窗口，可按Ctrl + D或执行命令exit()
 。务必将本书中的每个命令python
 都替换为python3
 。
要运行本书的代码，必须使用Python 3.6或更高的版本。如果系统安装的是低于Python 3.6的版本，请参阅附录A，了解如何安装最新版。
2. 在终端会话中运行Python代码

现在可打开终端窗口并执行命令python3
 ，再尝试运行Python代码片段。检查Python版本时，你就这样做过。下面再次这样做，然后在终端会话中输入如下代码并按回车：

>>> print("Hello Python interpreter!")
Hello Python interpreter!
>>>

消息将直接打印到当前终端窗口中。别忘了，要关闭Python解释器，可按Ctrl + D或执行命令exit()
 。
3. 安装Sublime Text

在Linux系统中，可通过Ubuntu Software Center来安装Sublime Text。为此，单击菜单中的Ubuntu Software图标并查找Sublime Text，再通过单击来安装它。


<!-- source: text/part0000_split_018.html -->


---

## 1.3　运行Hello World程序

安装较新版本的Python和Sublime Text后，就可以编写并运行你的第一个Python程序了。这样做之前，需要设置Sublime Text，确保它使用系统中正确的Python版本。然后，就可以编写并运行Hello World程序了。

### 1.3.1　配置Sublime Text以使用正确的Python版本

如果在你的系统中执行命令`python`
 时启动的是Python 3，就无须做任何配置，直接跳到下一节即可。如果需要执行命令`python3`
 来启动Python，就需要配置Sublime Text，使其使用正确的Python版本来运行你编写的程序。

为此，单击Sublime Text图标以启动它，也可在搜索栏中输入Sublime Text来找到它再启动。选择菜单Tools ▶ Build System ▶ New Build System，新建一个配置文件。删除该文件中的所有内容，再输入如下内容：

**

**

```
{
    "cmd": ["python3", "-u", "$file"],
}
```

这段代码让Sublime Text使用命令`python3`
 来运行Python程序。将这个文件保存到Sublime Text默认打开的文件夹中，并将其命名为Python3.sublime-build。

### 1.3.2　运行程序hello_world.py

编写第一个程序前，在系统中创建一个名为python_work的文件夹，用于存储你开发的项目。文件名和文件夹名称最好使用小写字母，并使用下划线代替空格，因为Python采用了这些命名约定。

启动Sublime Text，再选择菜单File ▶ Save As将Sublime Text创建的空文件存储到文件夹python_work中，并将其命名为hello_world.py。文件扩展名.py告诉Sublime Text，文件中的代码是使用Python编写的，这能让它知道如何运行这个程序，并以有帮助的方式突出其中的代码。

保存这个文件后，在其中输入如下代码行：

**

```
print("Hello Python world!")
```

在你的系统中，如果能使用命令`python`
 来启动Python 3，可以选择菜单Tools ▶ Build或按Ctrl + B（在macOS系统中为Command + B）来运行程序。如果需要像前一节那样配置Sublime Text，请选择菜单Tools ▶ Build System ▶ Python 3来运行这个程序。从此以后，你就可以选择菜单Tools ▶ Build或按Ctrl + B（或Command + B）来运行程序了。

在Sublime Text的底部，将出现一个终端窗口，其中包含如下输出：

```
Hello Python world!
[Finished in 0.1s]
```

如果看不到上述输出，可能是因为这个程序出了点问题。请检查你输入的每个字符。是否不小心将`print`
 的首字母大写了？是否遗漏了引号或圆括号？编程语言的语法非常严格，只要不满足要求，就会报错。如果你无法运行这个程序，请参阅下一节的建议。


<!-- source: text/part0000_split_019.html -->



## 二、知识补全（书本没有的部分）

\
## 一、第一个程序的完整解析

```python
print("Hello Python world!")
```

### 拆解这行代码

| 部分 | 类型 | 含义 |
|------|------|------|
| `print` | 函数名 | Python 内置函数，把内容输出到控制台 |
| `(` | 运算符 | 函数调用开始 |
| `"Hello Python world!"` | 字符串字面量 | 用双引号括起的文本 |
| `)` | 运算符 | 函数调用结束 |

### 等价的几种写法

```python
print("Hello Python world!")           # 双引号
print('Hello Python world!')           # 单引号
print("""Hello Python world!""")       # 三引号（可跨行）
print('''Hello Python world!''')       # 三单引号
```

**单/双/三引号的区别**：

- 单引号和双引号等价，**只是用于在字符串里包含另一种引号**：
  ```python
  print("It's a book.")    # ✅ 字符串里包含单引号
  print('It\'s a book.')   # ✅ 用转义字符
  ```
- 三引号可以跨多行：
  ```python
  msg = """第一行
  第二行
  第三行"""
  ```

### print 函数详细参数

```python
print(*objects, sep=' ', end='\\n', file=sys.stdout, flush=False)
```

| 参数 | 默认 | 含义 |
|------|------|------|
| `*objects` | 无 | 任意多个要打印的对象 |
| `sep` | `' '` | 对象之间的分隔符 |
| `end` | `'\\n'` | 打印结束后的字符 |
| `file` | `sys.stdout` | 输出目标 |
| `flush` | `False` | 是否立即刷新缓冲 |

**实用例子**：

```python
# sep：自定义分隔符
print("Python", "Java", "C++", sep=" | ")
# 输出：Python | Java | C++

# end：自定义结尾（不换行）
print("Loading", end="")
for i in range(3):
    print(".", end="", flush=True)
    import time; time.sleep(0.5)
print()  # 最后换行
# 输出：Loading...

# 多参数
name = "Alice"
age = 25
print("Name:", name, "Age:", age)
# 输出：Name: Alice Age: 25
```

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）