---
title: "P4 【语法基础】debug、注释与输出函数"
p_no: 4
category: 语法基础
duration: 1642
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P4 【语法基础】debug、注释与输出函数

> **课程分类**：语法基础
> **时长**：1642 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

语法基础阶段，从安装到容器、函数、装饰器。

## 课本对应章节

本节在《Python编程：从入门到实践》第 2 版中的对应位置：

- 2.5　注释
- 1.3　运行Hello World程序

## 一、课本内容（原书摘录）

## 2.5　注释

在大多数编程语言中，注释是一项很有用的功能。本书前面编写的程序中都只包含Python代码，但随着程序越来越大、越来越复杂，就应在其中添加说明，对你解决问题的方法进行大致的阐述。****
 让你能够使用自然语言在程序中添加说明。

### 2.5.1　如何编写注释

在Python中，注释用井号（`#`
 ）标识。井号后面的内容都会被Python解释器忽略，如下所示：

**

```
# 向大家问好。
print("Hello Python people!")
```

Python解释器将忽略第一行，只执行第二行。

```
Hello Python people!
```

### 2.5.2　该编写什么样的注释

编写注释的主要目的是阐述代码要做什么，以及是如何做的。在开发项目期间，你对各个部分如何协同工作了如指掌，但过段时间后，有些细节你可能不记得了。当然，你总是可以通过研究代码来确定各个部分的工作原理，但通过编写注释以清晰的自然语言对解决方案进行概述，可节省很多时间。

要成为专业程序员或与其他程序员合作，就必须编写有意义的注释。当前，大多数软件是合作编写的，编写者可能是同一家公司的多名员工，也可能是众多致力于同一个开源项目的人员。训练有素的程序员都希望代码中包含注释，因此你最好从现在开始就在程序中添加描述性注释。作为新手，最值得养成的习惯之一就是在代码中编写清晰、简洁的注释。

如果不确定是否要编写注释，就问问自己：在找到合理的解决方案之前，考虑了多个解决方案吗？如果答案是肯定的，就编写注释对你的解决方案进行说明吧。相比回过头去再添加注释，删除多余的注释要容易得多。从现在开始，本书的示例都将使用注释来阐述代码的工作原理。

> 动手试一试
> 
> 
> 练习2-10：添加注释
>  　选择你编写的两个程序，在每个程序中至少添加一条注释。如果程序太简单，实在没有什么需要说明的，就在程序文件开头加上你的姓名和当前日期，再用一句话阐述程序的功能。


<!-- source: text/part0000_split_028.html -->


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
## 一、注释的三种形式

```python
# 1. 单行注释：以 # 开头，到行末结束
# 这是单行注释
x = 1  # 行尾注释

# 2. 多行注释：用三引号字符串（实际是字符串，不是真注释）
"""
这是
多行注释
"""

# 3. 文档字符串（docstring）：用于函数/类/模块说明
def add(a, b):
    """计算两数之和（这是函数的 docstring）"""
    return a + b
```

**注释的最佳实践**：

- ✅ **解释"为什么"** 而不是"是什么"
  ```python
  # ❌ 差：把 i 加 1
  i += 1

  # ✅ 好：跳过标题行（每 100 个数据点显示一次进度）
  i += 1
  ```
- ✅ **保持更新**：代码改了注释也要改
- ❌ **不要写显而易见的注释**

## 二、print 调试法（最实用的调试技巧）

```python
# 在可疑位置插入 print
def divide(a, b):
    print(f"[DEBUG] a={a}, b={b}")  # 调试输出
    if b == 0:
        return None
    return a / b

result = divide(10, 0)
print(f"[DEBUG] result={result}")
```

**进阶：使用 logging 模块代替 print**（生产代码必学）

```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("调试信息")
logger.info("一般信息")
logger.warning("警告")
logger.error("错误")
```

## 三、Python 调试器 pdb

```python
# 在代码中打断点
import pdb; pdb.set_trace()  # Python 3.7 以下
breakpoint()  # Python 3.7+ 推荐

# 进入调试模式后可用命令：
# n (next)      下一步
# s (step)      进入函数
# c (continue)  继续到下一个断点
# p x           打印变量 x
# q             退出
```

**PyCharm 调试**：直接点行号左侧打断点，比 pdb 友好 10 倍。

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）