---
title: "P2 【语法基础】Python、PyCharm的安装与相关配置"
p_no: 2
category: 语法基础
duration: 2503
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P2 【语法基础】Python、PyCharm的安装与相关配置

> **课程分类**：语法基础
> **时长**：2503 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

语法基础阶段，从安装到容器、函数、装饰器。

## 课本对应章节

本节在《Python编程：从入门到实践》第 2 版中的对应位置：

- 1.1　搭建编程环境
- 1.2　在不同操作系统中搭建Python编程环境
- 1.4　解决安装问题
- 1.5　从终端运行Python程序
- 1.6　小结

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

## 1.4　解决安装问题

如果无法运行程序hello_world.py，可尝试如下几个解决方法，这些通用方法适用于所有编程问题。

- 程序存在严重错误时，Python将显示traceback，即错误报告。Python会仔细研究文件，试图找出其中的问题。trackback可能会提供线索，让你知道是什么问题让程序无法运行。
- 离开计算机，先休息一会儿再尝试。别忘了，语法在编程中非常重要，即便是少一个冒号、引号不匹配或括号不匹配，都可能导致程序无法正确运行。请再次阅读本章的相关内容，并重新审视你编写的代码，看看能否找出错误。
- 推倒重来。你也许不需要卸载任何软件，但删除文件hello_world.py并重新创建它也许是合理的选择。
- 让别人在你的计算机或其他计算机上按本章的步骤重做一遍，并仔细观察。你可能遗漏了一小步，而别人刚好没有遗漏。
- 请懂Python的人帮忙。当你有这样的想法时，可能发现在你认识的人当中就有人使用Python。
- 本章的安装说明在本书主页上：ituring.cn/book/2784。对你来说，在线版也许更合适，因为可以复制并粘贴其中的代码。
- 到网上寻求帮助。附录C提供了很多在线资源，如论坛或在线聊天网站，你可以在这些地方请求解决过相同问题的人提供解决方案。

不要担心这会打扰经验丰富的程序员。每个程序员都遇到过问题，大多数程序员很乐意帮助你正确地设置系统。只要能清晰地说明你要做什么、尝试了哪些方法及其结果，就很可能有人能够帮到你。正如前言中指出的，Python社区对初学者非常友好。

任何现代计算机都能够运行Python。前期的问题可能令人沮丧，但很值得你花时间去解决。能够运行hello_world.py后，你就可以开始学习Python了，而且编程工作会更有趣，也更令人愉快。


<!-- source: text/part0000_split_020.html -->


---

## 1.5　从终端运行Python程序

你编写的大多数程序将直接在文本编辑器中运行，但有时候从终端运行程序很有用。例如，你可能想直接运行既有的程序。

在任何安装了Python的系统上都可以这样做，前提是你知道如何进入程序文件所在的目录。为尝试这样做，请确保将文件hello_world.py存储到了桌面的文件夹python_work中。

### 1.5.1　在Windows系统中从终端运行Python程序

在命令窗口中，可以使用终端命令`cd`
 （表示change directory，即****
 ）在文件系统中导航。使用命令`dir`
 （表示directory，即****
 ）可以显示当前目录中的所有文件。

为运行程序hello_world.py，请打开一个新的终端窗口，并执行下面的命令：

```
❶ C:\> cd Desktop\python_work
❷ C:\Desktop\python_work> dir
  hello_world.py
❸ C:\Desktop\python_work> python hello_world.py
  Hello Python world!
```

这里使用了命令`cd`
 来切换到文件夹Desktop\python_work（见❶）。接下来，使用命令`dir`
 来确认这个文件夹中包含文件hello_world.py（见❷）。最后，使用命令`python hello_world.py`
 来运行这个文件（见❸）。

大多数程序可直接从编辑器运行，但待解决的问题比较复杂时，你编写的程序可能需要从终端运行。

### 1.5.2　在Linux和macOS系统中从终端运行Python程序

在Linux和macOS系统中，从终端运行Python程序的方式相同。在终端会话中，可以使用终端命令`cd`
 （表示change directory，即****
 ）在文件系统中导航。使用命令`ls`
 （表示list，即****
 ）可以显示当前目录中所有未隐藏的文件。

为运行程序hello_world.py，请打开一个新的终端窗口，并执行下面的命令：

```
❶ ~$ cd Desktop/python_work/
❷ ~/Desktop/python_work$ ls
  hello_world.py
❸ ~/Desktop/python_work$ python hello_world.py
  Hello Python world!
```

这里使用了命令`cd`
 来切换到文件夹Desktop/python_work（见❶）。接下来，使用命令`ls`
 来确认这个文件夹中包含文件hello_world.py（见❷）。最后，使用命令`python hello_world.py`
 来运行这个文件（见❸）。

就这么简单。要运行Python程序，只需使用命令`python`
 （或`python3`
 ）即可。

> 动手试一试
> 
> 本章的练习都是探索性的，但从第2章开始将要求你用那一章学到的知识来解决问题。
> 
> 练习1-1：python.org
>  　浏览Python主页，寻找你感兴趣的主题。你对Python越熟悉，这个网站对你来说就越有用。
> 
> 练习1-2：输入错误
>  　打开你刚创建的文件hello_world.py，在代码中添加一个输入错误，再运行这个程序。输入错误会引发错误吗？你能理解显示的错误消息吗？你能添加一个不会导致错误的输入错误吗？你凭什么认为它不会导致错误？
> 
> 练习1-3：无穷的技艺
>  　如果你有无穷多种编程技艺，你打算开发什么样的程序呢？你就要开始学习编程了。如果心中有目标，就能立即将新学到的技能付诸应用，现在正是草拟目标的大好时机。将想法记录下来是个不错的习惯，这样每当需要开始新项目时，都可参考它们。现在请花点时间描绘三个你想创建的程序。


<!-- source: text/part0000_split_021.html -->


---

## 1.6　小结

在本章中，你大致了解了Python，并在自己的系统中安装了Python。你还安装了一个文本编辑器，以简化Python代码的编写工作。你学习了如何在终端会话中运行Python代码片段，并运行了第一个程序——hello_world.py。你还大致了解了如何解决安装问题。

在下一章，你将学习如何在Python程序中使用各种数据和变量。


<!-- source: text/part0000_split_022.html -->

# 第 2 章　变量和简单数据类型

> 在本章中，你将学习可在Python程序中使用的各种数据，还将学习如何在程序中使用变量来表示这些数据。


<!-- source: text/part0000_split_023.html -->



## 二、知识补全（书本没有的部分）

\
## 一、PyCharm 与 VS Code 选哪个

| 维度 | PyCharm | VS Code |
|------|---------|---------|
| 安装包 | 大（~500MB） | 小（~80MB） |
| 启动速度 | 慢 | 快 |
| 智能提示 | 专业级 | 需装 Pylance |
| 调试器 | 内置 | 需装插件 |
| 远程开发 | 专业版收费 | 免费 |
| 学习曲线 | 中等 | 友好 |

**建议**：初学者用 PyCharm Community（免费），熟练后转 VS Code。

## 二、PyCharm 必装配置

1. **Python 解释器**：Settings → Project → Python Interpreter → 选择系统 Python 或 venv
2. **代码风格**：Settings → Editor → Code Style → Python → 选 PEP 8
3. **字体**：推荐 JetBrains Mono 或 Fira Code（带连字）
4. **插件**：
   - `.ignore`：.gitignore 高亮
   - `Key Promoter X`：快捷键提示
   - `Chinese Language Pack`（可选）

## 三、常见 Bug 与排错

```python
# Bug 1：缩进错误（IndentationError）
def foo():
print("hello")  # ❌ IndentationError

def foo():
    print("hello")  # ✅

# Bug 2：语法错误（SyntaxError）
if x = 5:  # ❌ SyntaxError: assignment 不能用在条件里
if x == 5:  # ✅

# Bug 3：Tab 与空格混用（TabError）
def foo():
    print("hello")  # 这里用了 Tab
    print("world")  # 这里用了 4 个空格 → TabError
# 解决：Settings → Editor → Code Style → Python → 勾 "Use tab character" 取消，改用空格

# Bug 4：NameError（变量未定义）
print(x)  # ❌ NameError: name 'x' is not defined
x = 10
print(x)  # ✅
```

## 四、排错流程

1. **看报错信息最后一行**：告诉你哪一行、什么错
2. **往上读 traceback**：找到调用链
3. **打断点**：在出错行前一行打断点，单步执行
4. **print 大法**：在可疑位置 print 变量值
5. **搜索引擎**：复制报错最后一行粘贴到 Google（**别用百度**，技术问题 Google 质量高 10 倍）

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）