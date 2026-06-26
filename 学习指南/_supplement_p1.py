# -*- coding: utf-8 -*-
"""补全知识库：每个 key 对应一段 markdown 内容（书本没有的知识点）。
格式：key -> md_text
"""
SUPPLEMENT = {

# ===== 课前篇 =====
"course_overview": """\
## 一、学习路线图（7 天速成是宣传，学习周期建议 8-12 周）

| 阶段 | 周数 | 学习内容 | 配套书本章节 |
|------|------|---------|-------------|
| 入门 | 1-2 | 起步 / 变量 / if / 循环 / 字符串 | 第 1-2 章 |
| 基础 | 3-4 | 列表 / 字典 / 函数 / 类 / 文件 | 第 3-10 章 |
| 进阶 | 5-6 | 测试代码 / 异常 / 调试 | 第 10-11 章 |
| 项目 | 7-9 | 外星人入侵 / 数据可视化 / Web | 第 12-20 章 |
| 拓展 | 10-12 | 爬虫 / 自动化办公 / 数据分析 | 本课程 + 课外 |

## 二、Python 能做什么（按就业方向）

- **Web 后端**：Django、Flask、FastAPI（本课程未涉及 → 课外学）
- **数据分析**：pandas、numpy、matplotlib（书第 15-17 章）
- **爬虫**：requests、Scrapy、Selenium（本课 P72+）
- **自动化办公**：openpyxl、python-docx、pyautogui（**本书无**，需课外学）
- **AI/机器学习**：PyTorch、TensorFlow、scikit-learn（**本书无**）
- **脚本工具**：os、shutil、subprocess（本课 P55-P68）

## 三、学习心态

1. **不要追求"7 天速成"**：7 天只能学完基础语法，做不了项目
2. **必须动手敲代码**：看视频 ≠ 学会，每节视频看完要自己重写一遍
3. **错误是最好的老师**：遇到 bug 先自己读，再搜索引擎，最后问人
4. **做项目 > 学语法**：语法是工具，项目才能整合工具
""",

"pycharm_install": """\
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
""",

"hello_world": """\
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
""",

"debug_print": """\
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
""",

"variable_naming": """\
## 一、变量与标识符的本质

**Python 变量是指向对象的"标签"**（不是"盒子"装数据）：

```python
a = [1, 2, 3]
b = a         # b 不是 a 的副本，b 和 a 指向同一个列表
b.append(4)
print(a)      # [1, 2, 3, 4] ← a 也被改了！
```

要真正复制：

```python
import copy
b = a.copy()          # 浅拷贝（一层）
b = a[:]              # 浅拷贝（切片）
b = list(a)           # 浅拷贝（构造）
b = copy.deepcopy(a)  # 深拷贝（嵌套也复制）
```

## 二、标识符命名规则

### 硬性规则（违反会报错）

1. 只能含字母、数字、下划线
2. 不能以数字开头
3. 不能用关键字（`if`、`for`、`class` 等）
4. 区分大小写（`Name` ≠ `name`）

### 软性规范（PEP 8 推荐）

| 类型 | 风格 | 例子 |
|------|------|------|
| 变量 | snake_case | `user_name`, `total_count` |
| 函数 | snake_case | `get_user()`, `calculate_sum()` |
| 类 | PascalCase | `UserAccount`, `HttpClient` |
| 常量 | UPPER_SNAKE | `MAX_SIZE`, `PI = 3.14` |
| 模块 | snake_case | `utils.py`, `data_loader.py` |
| 私有 | 前缀下划线 | `_internal_value`, `__private_attr` |

### 命名要"自解释"

```python
# ❌ 差：缩写难懂
a = 86400
n = 0
tmp = []

# ✅ 好：见名知意
SECONDS_PER_DAY = 86400
user_count = 0
pending_requests = []
```

## 三、Python 关键字

```python
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
#  'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
#  'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
#  'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
#  'while', 'with', 'yield']
```
""",

"fstring": """\
## 一、f-string 详解（Python 3.6+）

**f-string** 是 Python 3.6 引入的字符串格式化方法，比 `format()` 和 `%` 都简洁：

```python
name = "Alice"
age = 25

# 三种格式化方式
print("Name: %s, Age: %d" % (name, age))            # C 风格（过时）
print("Name: {}, Age: {}".format(name, age))         # format 方法
print(f"Name: {name}, Age: {age}")                  # ✅ f-string（推荐）
```

### f-string 内嵌表达式

```python
# 数学运算
a, b = 10, 3
print(f"{a} + {b} = {a + b}")          # 10 + 3 = 13

# 函数调用
import math
print(f"π ≈ {math.pi:.4f}")            # π ≈ 3.1416

# 三元运算符
score = 85
print(f"{'及格' if score >= 60 else '不及格'}")  # 及格

# 调用方法
name = "alice"
print(f"{name.upper()}")                # ALICE
```

### 格式说明符

```python
# 数字精度
print(f"{3.1415926:.2f}")              # 3.14
print(f"{3.1415926:.4f}")              # 3.1416

# 宽度对齐（用于表格）
for i, name in enumerate(["Alice", "Bob", "Charlie"]):
    print(f"{i:3d} | {name:<10} | {len(name):3d}")
#   0 | Alice      |   5
#   1 | Bob        |   3
#   2 | Charlie    |   7

# 千分位分隔符
print(f"{1234567890:,}")                # 1,234,567,890
print(f"{1234567890:,.2f}")             # 1,234,567,890.00

# 百分比
print(f"{0.876:.1%}")                   # 87.6%

# 不同进制
print(f"{255:#x}")                       # 0xff（十六进制）
print(f"{8:#o}")                         # 0o10（八进制）
print(f"{10:#b}")                        # 0b1010（二进制）

# 填充
print(f"{42:05d}")                       # 00042
print(f"{'hi':*^10}")                    # ****hi****
```

### 调试专用 f-string（Python 3.8+）

```python
x = 10
y = [1, 2, 3]

# 传统
print(f"x = {x}, y = {y}")

# 调试专用（自动加等号，显示变量名+值）
print(f"{x=}, {y=}")                    # x=10, y=[1, 2, 3]

# 带格式
print(f"{x=:,}, {y=!r}")                # x=10, y=[1, 2, 3]
```

## 二、其他格式化方法对比

| 方法 | 优点 | 缺点 |
|------|------|------|
| f-string | 简洁、可读、可内嵌表达式 | Python 3.6+ 才支持 |
| `str.format()` | Python 2/3 兼容 | 写起来啰嗦 |
| `%` 格式化 | C 程序员熟悉 | 类型多时易错、过时 |
| `Template` | 用户输入安全 | 功能最少 |

## 三、大数下划线（Python 3.6+）

```python
# 以前
a = 1000000000000
b = 0.000000001

# 现在（可读性更好）
a = 1_000_000_000_000   # 一万亿
b = 0.000_000_001        # 一纳米
print(a, b)              # 1000000000000 1e-09
```
""",

"operator_input": """\
## 一、算术运算符全表

| 运算符 | 含义 | 例子 | 结果 |
|--------|------|------|------|
| `+` | 加 | `5 + 3` | 8 |
| `-` | 减 | `5 - 3` | 2 |
| `*` | 乘 | `5 * 3` | 15 |
| `/` | 除（浮点） | `7 / 2` | 3.5 |
| `//` | 整除 | `7 // 2` | 3 |
| `%` | 取模（余） | `7 % 2` | 1 |
| `**` | 幂 | `2 ** 10` | 1024 |

```python
# 常见陷阱
print(-7 // 2)      # -4（向下取整，不是 -3）
print(int(-3.5))    # -3
import math
print(math.floor(-3.5))   # -4（真向下取整）
print(math.trunc(-3.5))   # -3（截断小数部分）

# 字符串/列表的 +
print("Hello" + " " + "World")   # "Hello World"
print([1, 2] + [3, 4])           # [1, 2, 3, 4]

# 字符串/列表的 *
print("ab" * 3)                  # "ababab"
print([0] * 5)                   # [0, 0, 0, 0, 0]
```

## 二、赋值运算符

```python
# 复合赋值
x = 10
x += 5    # x = x + 5  → 15
x -= 3    # x = x - 3  → 12
x *= 2    # x = x * 2  → 24
x /= 4    # x = x / 4  → 6.0
x //= 2   # x = x // 2 → 3.0
x **= 2   # x = x ** 2 → 9.0

# 海象运算符（Python 3.8+）：赋值并返回值
if (n := len("hello")) > 3:
    print(f"长度 {n} 大于 3")
# 输出：长度 5 大于 3
```

## 三、input 函数详解

```python
# 基本用法
name = input("请输入你的名字：")    # 阻塞等待用户输入
print(f"你好，{name}！")

# 注意：input 总是返回字符串！
age = input("年龄：")
print(type(age))   # <class 'str'>
# 必须转换
age = int(input("年龄："))

# 多值输入（一行多个）
a, b = input("输入两个数（空格分隔）：").split()
a, b = int(a), int(b)
print(f"a + b = {a + b}")

# 列表输入
nums = list(map(int, input("输入多个数：").split()))
```

## 四、转义字符

```python
# 常用转义
print("He said: \\"Hello\\"")      # He said: "Hello"
print('It\\'s a book.')              # It's a book.
print("Line 1\\nLine 2")             # 换行
print("Col1\\tCol2")                 # Tab
print("C:\\\\Users\\\\name")          # 路径：C:\\Users\\name

# 原始字符串（不转义）
print(r"C:\\Users\\name\\Desktop")    # 原样输出
# 用于正则表达式、文件路径特别方便

# 不转义的多行字符串
print("""第一行
第二行""")
```
""",

}