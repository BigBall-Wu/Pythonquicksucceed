# -*- coding: utf-8 -*-
"""补全知识库 - 第四批：正则/标准库模块"""
SUPPLEMENT_4 = {

"regex_basics": """\
## 一、re 模块基础

```python
import re

# 1. 匹配（match）：从开头匹配
m = re.match(r"hello", "hello world")
print(m.group())     # "hello"
print(m.span())      # (0, 5)

# 2. 搜索（search）：找第一个匹配
m = re.search(r"world", "hello world")
print(m.group())     # "world"

# 3. 全文搜索（findall）：找所有匹配
results = re.findall(r"\\d+", "I have 2 apples and 5 oranges")
print(results)       # ['2', '5']

# 4. 全文搜索（finditer）：返回迭代器
for m in re.finditer(r"\\d+", "abc 123 def 456"):
    print(f"匹配 {m.group()} 在 {m.span()}")
# 匹配 123 在 (4, 7)
# 匹配 456 在 (12, 15)
```

## 二、元字符

| 字符 | 含义 | 例子 |
|------|------|------|
| `.` | 任意单个字符（除换行） | `a.c` 匹配 "abc"、"axc" |
| `^` | 行首 | `^Hello` 匹配行首的 Hello |
| `$` | 行尾 | `end$` 匹配行尾的 end |
| `*` | 0+ 次 | `ab*` 匹配 "a"、"ab"、"abb" |
| `+` | 1+ 次 | `ab+` 匹配 "ab"、"abb"，不匹配 "a" |
| `?` | 0 或 1 次 | `ab?` 匹配 "a"、"ab" |
| `{n}` | n 次 | `a{3}` 匹配 "aaa" |
| `{n,m}` | n 到 m 次 | `a{2,4}` 匹配 "aa"、"aaa"、"aaaa" |
| `[]` | 字符集 | `[abc]` 匹配任一 |
| `[^]` | 否定字符集 | `[^abc]` 匹配非 abc |
| `|` | 或 | `cat|dog` 匹配 cat 或 dog |
| `()` | 分组 | `(abc)+` 匹配 "abcabc" |
| `\\` | 转义 | `\\.` 匹配字面点 |

## 三、字符类简写

| 简写 | 等价 | 含义 |
|------|------|------|
| `\\d` | `[0-9]` | 数字 |
| `\\D` | `[^0-9]` | 非数字 |
| `\\w` | `[a-zA-Z0-9_]` | 单词字符 |
| `\\W` | `[^a-zA-Z0-9_]` | 非单词字符 |
| `\\s` | `[ \\t\\n\\r\\f\\v]` | 空白 |
| `\\S` | `[^ \\t\\n\\r\\f\\v]` | 非空白 |
| `\\b` | - | 单词边界 |
| `\\B` | - | 非单词边界 |

## 四、常用模式

```python
# 邮箱
email_pat = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
re.match(email_pat, "alice@example.com")    # 匹配

# 手机号（中国）
phone_pat = r"^1[3-9]\\d{9}$"
re.match(phone_pat, "13812345678")           # 匹配

# IP 地址
ip_pat = r"^((25[0-5]|2[0-4]\\d|[01]?\\d\\d?)\\.){3}(25[0-5]|2[0-4]\\d|[01]?\\d\\d?)$"
re.match(ip_pat, "192.168.1.1")             # 匹配

# URL
url_pat = r"^https?://[^\\s]+$"

# 身份证号（简单）
id_pat = r"^\\d{17}[\\dXx]$"

# 日期
date_pat = r"^\\d{4}-\\d{1,2}-\\d{1,2}$"
```

## 五、re 模块函数

```python
import re

# 替换
re.sub(r"\\d+", "X", "I have 2 apples and 5 oranges")
# "I have X apples and X oranges"

# 分割
re.split(r"[,;\\s]+", "a,b;c  d")
# ['a', 'b', 'c', 'd']

# 编译（提高性能）
pattern = re.compile(r"\\d+")
print(pattern.findall("a1 b22 c333"))
# ['1', '22', '333']
```

## 六、贪婪 vs 非贪婪

```python
# 贪婪（默认）：尽可能多匹配
re.findall(r"<.+>", "<a><b>")
# ['<a><b>']

# 非贪婪（加 ?）：尽可能少匹配
re.findall(r"<.+?>", "<a><b>")
# ['<a>', '<b>']
```

## 七、原始字符串 r"..."

```python
# 普通字符串中 \\d 需要两个反斜杠
re.match("\\d+", "123")

# 原始字符串更清晰
re.match(r"\\d+", "123")

# 不用 r 前缀的坑
text = "C:\\Users\\name"
print(re.findall("\\\\", text))    # 需要 4 个反斜杠
print(re.findall(r"\\", text))     # 只需要 2 个
```
""",

"regex_quantifier": """\
## 一、量词详解

```python
import re

# 1. *  ：0 或多次
re.findall(r"ab*", "a ab abb abbb")     # ['a', 'ab', 'abb', 'abbb']

# 2. +  ：1 或多次
re.findall(r"ab+", "a ab abb")          # ['ab', 'abb']

# 3. ?  ：0 或 1 次
re.findall(r"ab?", "a ab abb")          # ['a', 'ab', 'ab']

# 4. {n} ：恰好 n 次
re.findall(r"\\d{3}", "123 4567 89")     # ['123', '456']

# 5. {n,} ：至少 n 次
re.findall(r"\\d{2,}", "1 12 123 1234") # ['12', '123', '1234']

# 6. {n,m} ：n 到 m 次
re.findall(r"\\d{2,3}", "1 12 123 1234")
# ['12', '123', '123']

# 7. *? +? ?? {n,m}? ：非贪婪
```

## 二、贪婪 vs 非贪婪

```python
import re

text = "<h1>title</h1><p>content</p>"

# 贪婪：.* 尽可能多
m = re.search(r"<.*>", text)
print(m.group())      # "<h1>title</h1><p>content</p>"（整个）

# 非贪婪：.*? 尽可能少
m = re.search(r"<.*?>", text)
print(m.group())      # "<h1>"（第一个标签）
```

## 三、字符集

```python
import re

# [abc]：匹配 a、b、c 任一
re.findall(r"[abc]", "aabbccdd")         # ['a', 'a', 'b', 'b', 'c', 'c']

# [a-z]：匹配 a 到 z
re.findall(r"[a-z]+", "Hello World 123") # ['ello', 'orld']

# [0-9]：匹配数字
re.findall(r"[0-9]+", "abc123def456")    # ['123', '456']

# [^abc]：匹配非 a、b、c
re.findall(r"[^a-z]+", "abc123def")      # ['123']

# 预定义字符类
re.findall(r"\\d+", "abc123")            # ['123']
re.findall(r"\\w+", "hello_world!")      # ['hello_world']
re.findall(r"\\s+", "a  b\\tc\\nd")      # ['  ', '\\t', '\\n']
```

## 四、边界匹配

```python
import re

# \\b：单词边界
re.findall(r"\\bcat\\b", "cat cats scatter")
# ['cat']（只匹配独立的 cat）

# \\B：非单词边界
re.findall(r"\\Bcat\\B", "scatter")
# ['cat']（scatter 中间的 cat）

# ^ 和 $（行首/行尾）
re.findall(r"^\\w+", "hello\\nworld")
# ['hello']（每行的开头）

# 配合 re.MULTILINE
re.findall(r"^\\w+", "hello\\nworld", re.MULTILINE)
# ['hello', 'world']
```

## 五、实际例子

```python
import re

# 1. 提取数字
text = "订单 #12345，金额 $99.99，日期 2024-06-24"
nums = re.findall(r"\\d+\\.?\\d*", text)
# ['12345', '99.99', '2024', '06', '24']

# 2. 验证密码强度
# 至少 8 位，包含大小写字母和数字
pwd_pat = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).{8,}$"
re.match(pwd_pat, "Abc12345")           # 匹配

# 3. 提取 URL
text = "访问 https://www.example.com 或 http://test.org"
urls = re.findall(r"https?://[^\\s]+", text)
# ['https://www.example.com', 'http://test.org']

# 4. 提取标签
text = "Hello #python #regex @alice"
tags = re.findall(r"#\\w+", text)
# ['#python', '#regex']
```

## 六、性能优化

```python
import re

# 1. 预编译（多次使用时性能提升 5-10 倍）
pattern = re.compile(r"\\d+")
for line in big_text.split("\\n"):
    pattern.findall(line)

# 2. 避免灾难性回溯
# ❌ (a+)+  在 "aaaaaaaaaaaab" 上很慢
# ✅ a+       等价但更快

# 3. 用具体字符类代替 .
re.findall(r"[^>]+", text)      # 比 .+ 快
```

## 七、常用 flags

```python
import re

# re.IGNORECASE / re.I ：忽略大小写
re.findall(r"hello", "HELLO Hello", re.IGNORECASE)

# re.MULTILINE / re.M ：^ $ 匹配每行
re.findall(r"^\\w+", "a\\nb", re.MULTILINE)

# re.DOTALL / re.S ：. 匹配换行
re.findall(r".+", "a\\nb", re.DOTALL)

# re.VERBOSE / re.X ：允许注释
pattern = re.compile(r"""
    \\d+           # 数字
    [a-z]+         # 字母
""", re.VERBOSE)
```
""",

"regex_group": """\
## 一、分组基础

```python
import re

# () 创建分组
m = re.match(r"(\\d+)-(\\d+)", "123-456")
print(m.group(0))    # "123-456"（完整匹配）
print(m.group(1))    # "123"（第 1 组）
print(m.group(2))    # "456"（第 2 组）
print(m.groups())    # ('123', '456')
```

## 二、命名分组

```python
import re

m = re.match(r"(?P<year>\\d{4})-(?P<month>\\d{2})-(?P<day>\\d{2})", "2024-06-24")
print(m.group("year"))      # "2024"
print(m.group("month"))     # "06"
print(m.group("day"))       # "24"
print(m.groupdict())        # {'year': '2024', 'month': '06', 'day': '24'}
```

## 三、反向引用

```python
import re

# \\1 引用第一组
text = "abc abc def def"
re.findall(r"(\\w+) \\1", text)
# ['abc', 'def']

# 命名引用 (?P=name)
m = re.match(r"(?P<word>\\w+) (?P=word)", "hello hello")
print(m.group())         # "hello hello"

# 验证 HTML 标签
re.findall(r"<(\\w+)>.*?</\\1>", "<b>bold</b> <i>italic</i>")
# ['b', 'i']
```

## 四、非捕获分组

```python
import re

# (?:...) 不捕获
m = re.match(r"(?:\\d{4})-(\\d{2})-(\\d{2})", "2024-06-24")
print(m.groups())    # ('06', '24')（年没捕获）

# 应用：提高性能、不污染组号
```

## 五、断言（零宽匹配）

### 前瞻断言

```python
import re

# (?=...) ：后面是
re.findall(r"\\w+(?=\\s*\\d)", "abc123 def456")
# ['abc', 'def']

# 密码必须包含数字
re.findall(r"\\w*(?=\\d)", "abc123")
# ['abc']

# (?!...) ：后面不是
re.findall(r"\\w+(?!\\d)", "abc123 def456 xyz")
# ['23', '56']（数字结尾的不要）
```

### 后顾断言

```python
import re

# (?<=...) ：前面是
re.findall(r"(?<=\\$)\\d+", "$100 $200")
# ['100', '200']

# (?<!...) ：前面不是
re.findall(r"(?<!\\$)\\d+", "$100 200")
# ['200']（$100 被排除）
```

## 六、常见分组技巧

```python
import re

# 1. 提取日期
date = "Today is 2024-06-24"
m = re.search(r"(\\d{4})-(\\d{2})-(\\d{2})", date)
year, month, day = m.groups()

# 2. 提取 KV
text = "name=Alice age=25 city=Beijing"
pairs = re.findall(r"(\\w+)=(\\w+)", text)
# [('name', 'Alice'), ('age', '25'), ('city', 'Beijing')]

# 转为 dict
d = dict(pairs)
# {'name': 'Alice', 'age': '25', 'city': 'Beijing'}

# 3. 解析 URL
url = "https://www.example.com:8080/path?key=value"
m = re.match(r"(\\w+)://([^:/]+)(?::(\\d+))?([^?]*)\\?(.*)", url)
protocol, host, port, path, query = m.groups()

# 4. 替换带分组
text = "John Smith"
re.sub(r"(\\w+) (\\w+)", r"\\2, \\1", text)
# "Smith, John"
```

## 七、re.sub 高级用法

```python
import re

# 1. 用函数处理匹配项
def repl(m):
    return m.group().upper()

re.sub(r"\\w+", repl, "hello world")
# "HELLO WORLD"

# 2. 用命名组替换
text = "2024-06-24"
re.sub(r"(?P<y>\\d{4})-(?P<m>\\d{2})-(?P<d>\\d{2})",
       r"\\g<d>/\\g<m>/\\g<y>", text)
# "24/06/2024"

# 3. 替换并转换大小写
re.sub(r"\\b\\w+\\b", lambda m: m.group().upper(), "hello world")
# "HELLO WORLD"
```

## 八、复杂匹配示例

```python
import re

# 提取 Markdown 标题
md = "# Title\\n## Subtitle\\n### Subsubtitle"
re.findall(r"^(#{1,6})\\s+(.+)$", md, re.MULTILINE)
# [('#', 'Title'), ('##', 'Subtitle'), ('###', 'Subsubtitle')]

# 解析 CSV 行（简单）
csv_line = '"Alice","25","alice@example.com"'
re.findall(r'"([^"]*)"', csv_line)
# ['Alice', '25', 'alice@example.com']

# 提取 IPv4
ips = re.findall(r"\\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b", text)
```
""",

"regex_greedy": """\
## 一、贪婪（Greedy） vs 非贪婪（Lazy）

正则默认是 **贪婪的**：尽可能多匹配。

```python
import re

text = "<h1>title</h1>"

# 贪婪：.* 匹配到最后一个 >
m = re.search(r"<.*>", text)
print(m.group())      # "<h1>title</h1>"（整个字符串）

# 非贪婪：.*? 遇到第一个 > 就停
m = re.search(r"<.*?>", text)
print(m.group())      # "<h1>"（只匹配开始标签）
```

## 二、所有量词都有非贪婪版本

| 贪婪 | 非贪婪 | 含义 |
|------|--------|------|
| `*` | `*?` | 0+ 次 |
| `+` | `+?` | 1+ 次 |
| `?` | `??` | 0 或 1 次 |
| `{n}` | `{n}?` | n 次 |
| `{n,}` | `{n,}?` | 至少 n 次 |
| `{n,m}` | `{n,m}?` | n 到 m 次 |

## 三、实战例子

```python
import re

# 1. 提取 HTML 标签内容
html = "<b>bold</b><i>italic</i>"
re.findall(r"<(\\w+)>(.+?)</\\1>", html)
# [('b', 'bold'), ('i', 'italic')]

# 2. 提取 div 内容（贪婪会出错）
text = "<div>first</div><div>second</div>"
re.findall(r"<div>(.+)</div>", text)        # ['first</div><div>second']（错！）
re.findall(r"<div>(.+?)</div>", text)       # ['first', 'second']（对！）

# 3. JSON 字符串（简化）
text = '"name": "Alice", "age": 25'
re.findall(r'"(\\w+)":\\s*"([^"]+)"', text)
# 贪婪模式没问题（这里没歧义）

# 4. 注释提取
code = "/* 注释 1 */ code /* 注释 2 */"
re.findall(r"/\\*(.+?)\\*/", code)
# [' 注释 1 ', ' 注释 2 ']
```

## 四、回溯灾难（Catastrophic Backtracking）

```python
import re
import time

# ❌ 危险：嵌套量词
pattern = r"^(a+)+$"

# 测试灾难性回溯
text = "a" * 30 + "!"
start = time.time()
re.match(pattern, text)
print(f"耗时：{time.time()-start:.3f}s")
# 可能非常慢！

# ✅ 解决：去掉冗余量词
pattern = r"^a+$"
```

**如何避免**：

1. **不要嵌套量词**：`(a+)+` → `a+`
2. **使用占有量词**（Python 3.11+）：`(a+)++` （实验性）
3. **使用原子组**（Python 不直接支持，可用 lookahead 模拟）：`(?=(a+))\\1`

## 五、原子组（Atomic Group）模拟

Python 标准 `re` 不支持原子组，但可以用 lookahead 模拟：

```python
import re

# (?=(...))\\1 ：先看前面是不是匹配，但不前进；然后匹配回 \\1
text = "abcabcabc"
re.findall(r"(?=(abc))\\1+", text)
# 不会过度匹配

# 实际用途：避免回溯
pattern = r"(?=(a+))\\1+$"
```

## 六、原生字符串 r"..."

```python
import re

# 不加 r：双反斜杠
pattern = "\\d+\\.\\d+"
re.findall(pattern, "1.5 2.0")

# 加 r：单反斜杠，更清晰
pattern = r"\\d+\\.\\d+"
re.findall(pattern, "1.5 2.0")
# 推荐：永远用 r"..."
```

## 七、贪婪模式的正确使用

```python
import re

# 1. 提取最后一段路径
url = "/a/b/c/d/file.txt"
re.findall(r".*/(.+)", url)
# ['file.txt']（贪婪到最后一个 /）

# 2. 提取键值对（贪婪没问题）
text = 'name="Alice Smith" age="25"'
re.findall(r'(\\w+)="([^"]+)"', text)
# [('name', 'Alice Smith'), ('age', '25')]

# 3. 替换多个空白为一个
text = "a  b   c"
re.sub(r"\\s+", " ", text)
# "a b c"
```

## 八、调试正则

```python
import re

# 1. 用 regex101.com 在线调试
# 2. print(re.compile(pattern).pattern)  # 查看最终模式
# 3. 用 named group 增强可读性

pattern = r"""
    (?P<protocol>\\w+):         # 协议
    //
    (?P<host>[^/]+)             # 主机
    (?P<path>.*)                # 路径
"""

re.match(pattern, "https://example.com/path", re.VERBOSE)
```
""",

"os_module": """\
## 一、os.path 模块

```python
import os.path as path

# 1. 路径拼接
p = path.join("dir", "subdir", "file.txt")
# Windows: 'dir\\subdir\\file.txt'
# Linux/Mac: 'dir/subdir/file.txt'

# 2. 拆分路径
path.split("/a/b/c.txt")       # ('/a/b', 'c.txt')
path.splitext("file.txt")      # ('file', '.txt')
path.dirname("/a/b/c.txt")     # '/a/b'
path.basename("/a/b/c.txt")    # 'c.txt'

# 3. 获取信息
path.exists("/etc/passwd")     # True/False
path.isfile("/etc/passwd")     # True/False
path.isdir("/etc")             # True/False
path.getsize("/etc/passwd")    # 字节数
path.getmtime("/etc/passwd")   # 修改时间戳

# 4. 绝对路径
path.abspath("file.txt")       # 当前工作目录 + file.txt
path.realpath("file.txt")      # 解析符号链接
path.normpath("/a//b/../c")    # '/a/c'

# 5. 分割驱动器（Windows）
path.splitdrive("C:\\Users\\name")
# ('C:', '\\Users\\name')

# 6. 同名检查
path.commonpath(["/a/b", "/a/c"])  # '/a'
path.commonprefix(["/a/b", "/a/c"])  # '/a/'（注意区别）
```

## 二、os 模块常用功能

```python
import os

# 1. 当前工作目录
print(os.getcwd())         # '/f/学习模块/百科全书'
os.chdir("/tmp")           # 切换

# 2. 列出目录
files = os.listdir(".")    # ['a.py', 'b.txt', 'subdir/']
# 用 pathlib 更现代：
# list(Path('.').iterdir())

# 3. 创建/删除目录
os.mkdir("newdir")                 # 单层
os.makedirs("a/b/c", exist_ok=True)  # 多层（递归）
os.rmdir("newdir")                 # 只能删空目录
os.removedirs("a/b/c")             # 递归删（必须空）

# 4. 删除文件
os.remove("file.txt")              # 删文件

# 5. 重命名
os.rename("old.txt", "new.txt")
os.replace("old.txt", "new.txt")   # 跨设备也可

# 6. 文件信息
stat = os.stat("file.txt")
print(stat.st_size, stat.st_mtime, stat.st_mode)

# 7. 环境变量
os.environ["HOME"]                 # 读取
os.environ["MY_VAR"] = "value"     # 设置
print(os.getenv("PATH", "default"))

# 8. 执行命令
os.system("ls -la")               # 阻塞，输出到终端
ret = os.popen("ls").read()        # 返回字符串
```

## 三、os.walk 遍历目录

```python
import os

for root, dirs, files in os.walk("."):
    # root：当前路径
    # dirs：子目录列表（可修改来跳过）
    # files：文件列表
    print(f"{root}:")
    for f in files:
        print(f"  {f}")
    # 跳过隐藏目录
    dirs[:] = [d for d in dirs if not d.startswith(".")]
```

## 四、os.path 跨平台注意

```python
import os.path

# ❌ 不要硬编码斜杠
"dir\\subdir\\file.txt"

# ✅ 用 os.path.join
os.path.join("dir", "subdir", "file.txt")

# 或者用 pathlib（更现代）
from pathlib import Path
p = Path("dir") / "subdir" / "file.txt"
```

## 五、文件权限

```python
import os
import stat

# 检查
mode = os.stat("file.txt").st_mode
print(stat.filemode(mode))        # '-rw-r--r--'

# 修改
os.chmod("file.txt", 0o755)       # rwxr-xr-x
```
""",

"os_module_advanced": """\
## 一、os.scandir（比 listdir 高效）

```python
import os

# 普通 listdir：每个文件单独 stat
files = os.listdir(".")

# scandir：返回 DirEntry，包含缓存的 stat
with os.scandir(".") as entries:
    for entry in entries:
        print(f"{entry.name}: {'dir' if entry.is_dir() else 'file'}, "
              f"size={entry.stat().st_size}")
```

## 二、os.fdopen / os.dup（文件描述符）

```python
import os

# 文件描述符（底层 I/O）
fd = os.open("file.txt", os.O_RDWR | os.O_CREAT)
try:
    # 读取
    data = os.read(fd, 1024)
    # 写入
    os.write(fd, b"hello")
finally:
    os.close(fd)

# 复制文件描述符
fd2 = os.dup(fd)
os.close(fd)
# fd2 仍然有效
```

## 三、os 模块的系统调用

```python
import os

# 进程相关
print(os.getpid())          # 当前进程 PID
print(os.getppid())         # 父进程 PID
os._exit(0)                 # 立即退出（不清理）
# vs sys.exit()              # 抛出 SystemExit，可捕获

# 用户/组
print(os.getuid(), os.getgid())      # Linux/Mac
print(os.getlogin())                  # 当前登录用户名

# 环境
os.environ["NEW_VAR"] = "value"
print(os.path.expanduser("~"))       # 用户主目录
print(os.path.expandvars("$HOME"))   # 展开环境变量

# 路径分隔符
print(os.sep)             # '/' 或 '\\'
print(os.linesep)         # '\\n' 或 '\\r\\n'
print(os.name)            # 'posix' 或 'nt'
```

## 四、os.spawn（启动子进程）

```python
import os

# os.spawnl：参数列表
ret = os.spawnl(os.P_WAIT, "/bin/ls", "ls", "-la")
print(f"返回：{ret}")

# os.spawnv：参数数组
ret = os.spawnv(os.P_NOWAIT, "/bin/ls", ["ls", "-la"])
# 不等待，立即返回
```

## 五、os 模块的临时文件

```python
import os
import tempfile

# 用 tempfile 创建临时文件（推荐）
import tempfile
fd, path = tempfile.mkstemp(suffix=".txt", prefix="myapp_")
print(f"创建临时文件：{path}")
os.write(fd, b"temp data")
os.close(fd)
# 用完删除
os.unlink(path)
```

## 六、文件锁（仅 Unix）

```python
import os
import fcntl

# 文件锁（Unix 专属）
fd = os.open("file.txt", os.O_RDWR)
try:
    fcntl.flock(fd, fcntl.LOCK_EX)    # 排他锁
    # 修改文件
    fcntl.flock(fd, fcntl.LOCK_UN)    # 解锁
finally:
    os.close(fd)
```

## 七、os.path 与 pathlib 对比

```python
import os
from pathlib import Path

# os.path 风格
p = os.path.join("dir", "file.txt")
b = os.path.basename(p)
exists = os.path.exists(p)

# pathlib 风格
p = Path("dir") / "file.txt"
b = p.name
exists = p.exists()

# pathlib 优势：
# - 链式调用
# - 跨平台统一
# - 内置方法丰富
```

## 八、综合示例：递归查找文件

```python
import os

def find_files(root, pattern):
    """递归查找匹配 pattern 的文件"""
    matches = []
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if pattern in filename:
                matches.append(os.path.join(dirpath, filename))
    return matches

# 查找所有 .py 文件
py_files = find_files(".", ".py")
print(f"找到 {len(py_files)} 个 Python 文件")
```
""",

"sys_module": """\
## 一、sys 模块速查

```python
import sys

# 1. 命令行参数
sys.argv         # ['script.py', 'arg1', 'arg2']
# 退出码
sys.exit(0)      # 正常退出
sys.exit(1)      # 异常退出

# 2. Python 路径
sys.path         # 模块搜索路径（list）
sys.path.append("/my/modules")

# 3. Python 版本
sys.version      # '3.11.5 (main, ...)'
sys.version_info # sys.version_info(major=3, minor=11, micro=5, ...)
sys.platform     # 'win32' / 'linux' / 'darwin'

# 4. 模块缓存
sys.modules      # 已加载的模块字典

# 5. 标准输入输出
sys.stdout       # 标准输出
sys.stderr       # 标准错误
sys.stdin        # 标准输入

# 6. 内存管理
sys.getrefcount(obj)    # 引用计数
sys.getsizeof(obj)      # 对象字节大小
sys.getrecursionlimit() # 递归深度限制

# 7. 异常信息
sys.exc_info()   # (type, value, traceback)
sys.last_traceback  # 最后异常

# 8. 整数缓存
sys.int_info     # 整数信息
sys.float_info   # 浮点信息
```

## 二、sys.argv 命令行参数

```python
# script.py
import sys

print(f"脚本名：{sys.argv[0]}")
print(f"参数个数：{len(sys.argv) - 1}")

if len(sys.argv) > 1:
    print(f"第一个参数：{sys.argv[1]}")

# 运行：python script.py hello world
# 输出：
# 脚本名：script.py
# 参数个数：2
# 第一个参数：hello
```

**更复杂的解析用 argparse**：

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name", help="你的名字")
parser.add_argument("--age", type=int, default=18)
args = parser.parse_args()

print(f"{args.name}, {args.age}")
```

## 三、sys.path 模块搜索路径

```python
import sys

# 查看
for p in sys.path:
    print(p)
# ''
# '/usr/lib/python311.zip'
# '/usr/lib/python3.11'
# '/usr/lib/python3.11/lib-dynload'
# '/usr/lib/python3.11/site-packages'

# 添加
sys.path.insert(0, "/my/custom/path")   # 优先搜索
sys.path.append("/another/path")        # 最后搜索

# PYTHONPATH 环境变量（在 shell 里设）
# export PYTHONPATH=/my/modules
```

## 四、sys.stdin/stdout/stderr

```python
import sys

# 重定向
sys.stdout.write("hello\\n")

# 重定向到文件
with open("output.txt", "w") as f:
    sys.stdout = f
    print("这行写到文件里")
    sys.stdout = sys.__stdout__    # 恢复
```

## 五、sys.exit 退出码

```python
import sys

# 0 = 成功
# 非 0 = 失败
sys.exit(0)        # 正常退出
sys.exit(1)        # 出错退出
sys.exit("Error")  # 打印消息并以 1 退出

# 抛 SystemExit（可捕获）
try:
    sys.exit(1)
except SystemExit as e:
    print(f"捕获到退出：{e.code}")
```

## 六、sys.excepthook 自定义异常处理

```python
import sys

def custom_excepthook(exc_type, exc_value, exc_tb):
    print(f"😱 出错了：{exc_type.__name__}: {exc_value}")

sys.excepthook = custom_excepthook

# 测试
1 / 0
# 😱 出错了：ZeroDivisionError: division by zero
```

## 七、sys.modules 模块缓存

```python
import sys

# 已加载的模块
import json
import os

print("json" in sys.modules)     # True
print(json.__name__)             # "json"

# 重新加载（开发时调试用）
import importlib
importlib.reload(json)

# 移除
del sys.modules["json"]
```

## 八、sys.getsizeof 对象大小

```python
import sys

print(sys.getsizeof(0))           # 28
print(sys.getsizeof("hello"))     # 54
print(sys.getsizeof([1,2,3]))     # 88
print(sys.getsizeof({"a": 1}))    # 232
```

## 九、sys.setrecursionlimit 递归深度

```python
import sys

# 默认 1000 层
sys.setrecursionlimit(10000)     # 提高限制（小心栈溢出）

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# 注意：递归太深会 RecursionError
```
""",

"time_module": """\
## 一、time 模块

```python
import time

# 1. 时间戳（自 1970-01-01 起的秒数）
t = time.time()              # 1719234567.123456
print(t)

# 2. 结构化时间（struct_time）
local_t = time.localtime()    # 本地时间
utc_t = time.gmtime()         # UTC 时间
print(local_t.tm_year)        # 2024
print(local_t.tm_hour)        # 14

# 3. 格式化字符串
time.strftime("%Y-%m-%d %H:%M:%S")           # '2024-06-24 14:30:00'
time.strftime("%Y年%m月%d日")                  # '2024年06月24日'

# 4. 解析字符串
time.strptime("2024-06-24", "%Y-%m-%d")
# time.struct_time(tm_year=2024, tm_mon=6, tm_mday=24, ...)

# 5. 休眠
time.sleep(1)                # 休眠 1 秒

# 6. 性能计时
start = time.time()
do_something()
elapsed = time.time() - start
print(f"耗时 {elapsed:.3f}s")
```

## 二、格式化符号

| 符号 | 含义 | 例子 |
|------|------|------|
| `%Y` | 4 位年 | 2024 |
| `%y` | 2 位年 | 24 |
| `%m` | 月（01-12） | 06 |
| `%d` | 日（01-31） | 24 |
| `%H` | 时（00-23） | 14 |
| `%I` | 时（01-12） | 02 |
| `%M` | 分（00-59） | 30 |
| `%S` | 秒（00-59） | 45 |
| `%p` | AM/PM | PM |
| `%a` | 星期缩写 | Mon |
| `%A` | 星期全称 | Monday |
| `%b` | 月份缩写 | Jun |
| `%B` | 月份全称 | June |
| `%j` | 一年中的第几天 | 176 |
| `%U` | 一年中的第几周（周日为第一天） | 25 |
| `%W` | 一年中的第几周（周一为第一天） | 25 |
| `%c` | 本地日期时间 | Mon Jun 24 14:30:00 2024 |
| `%x` | 本地日期 | 06/24/24 |
| `%X` | 本地时间 | 14:30:00 |
| `%z` | 时区偏移 | +0800 |

## 三、struct_time 字段

```python
import time

t = time.localtime()
print(t.tm_year)      # 年
print(t.tm_mon)       # 月 (1-12)
print(t.tm_mday)      # 日 (1-31)
print(t.tm_hour)      # 时 (0-23)
print(t.tm_min)       # 分 (0-59)
print(t.tm_sec)       # 秒 (0-61, 处理闰秒)
print(t.tm_wday)      # 周几 (0=周一)
print(t.tm_yday)      # 一年中第几天 (1-366)
print(t.tm_isdst)     # 是否夏令时
```

## 四、时间戳与结构化时间互转

```python
import time

# 时间戳 → 结构化
ts = 1719234567.123
t = time.localtime(ts)
print(t.tm_year)      # 2024

# 结构化 → 时间戳
t = time.localtime()
ts = time.mktime(t)

# UTC 时间戳
utc_ts = time.time()           # 当前 UTC 时间戳
```

## 五、高精度计时

```python
import time

# perf_counter：最高精度
start = time.perf_counter()
time.sleep(0.001)
elapsed = time.perf_counter() - start
print(f"耗时 {elapsed:.6f}s")

# monotonic：单调时间（不受系统时间修改影响）
start = time.monotonic()
time.sleep(0.5)
print(f"耗时 {time.monotonic() - start:.3f}s")

# process_time：进程 CPU 时间
start = time.process_time()
do_cpu_work()
print(f"CPU 耗时 {time.process_time() - start:.3f}s")
```

## 六、datetime 模块（推荐）

time 模块偏底层，实际项目更推荐用 datetime：

```python
from datetime import datetime, timedelta

# 当前时间
now = datetime.now()           # 2024-06-24 14:30:00.123456
utc_now = datetime.utcnow()    # UTC

# 创建特定时间
d = datetime(2024, 6, 24, 14, 30, 0)

# 格式化
now.strftime("%Y-%m-%d %H:%M:%S")

# 解析
d = datetime.strptime("2024-06-24", "%Y-%m-%d")

# 时间运算
tomorrow = now + timedelta(days=1)
next_week = now + timedelta(weeks=1)
diff = tomorrow - now          # timedelta

# 时间戳转换
ts = now.timestamp()           # → float
d = datetime.fromtimestamp(ts) # → datetime
```

## 七、性能对比

```python
import time

n = 1_000_000

# time.time() 的调用开销
start = time.time()
for _ in range(n):
    time.time()
print(f"time.time(): {time.time() - start:.3f}s")

# perf_counter
start = time.perf_counter()
for _ in range(n):
    time.perf_counter()
print(f"perf_counter: {time.perf_counter() - start:.3f}s")
# perf_counter 更精确
```
""",

"time_format": """\
## 一、struct_time 字段

```python
import time

t = time.localtime()
# t.tm_year    年（4 位）
# t.tm_mon     月（1-12）
# t.tm_mday    日（1-31）
# t.tm_hour    时（0-23）
# t.tm_min     分（0-59）
# t.tm_sec     秒（0-61，处理闰秒）
# t.tm_wday    周几（0=周一，6=周日）
# t.tm_yday    一年中第几天（1-366）
# t.tm_isdst   是否夏令时（-1=未知）
```

## 二、strftime 详细格式

```python
import time

t = time.localtime()

# 日期
time.strftime("%Y-%m-%d")           # 2024-06-24
time.strftime("%y%m%d")             # 240624
time.strftime("%d/%m/%Y")           # 24/06/2024（欧洲格式）

# 时间
time.strftime("%H:%M:%S")           # 14:30:45
time.strftime("%I:%M:%S %p")        # 02:30:45 PM（12 小时制）
time.strftime("%H:%M")              # 14:30

# 完整
time.strftime("%Y-%m-%d %H:%M:%S")  # 2024-06-24 14:30:45
time.strftime("%c")                  # Mon Jun 24 14:30:45 2024

# 自定义
time.strftime("Today is %A, %B %d, %Y")
# Today is Monday, June 24, 2024

# 中文
time.strftime("%Y年%m月%d日 %H时%M分%S秒")
# 2024年06月24日 14时30分45秒

# ISO 8601
time.strftime("%Y-%m-%dT%H:%M:%S")  # 2024-06-24T14:30:45
```

## 三、strptime 解析

```python
import time

# 解析 ISO 格式
t = time.strptime("2024-06-24", "%Y-%m-%d")

# 解析中文
t = time.strptime("2024年06月24日", "%Y年%m月%d日")

# 解析自定义
t = time.strptime("24/06/2024", "%d/%m/%Y")

# 解析 12 小时制
t = time.strptime("02:30:45 PM", "%I:%M:%S %p")
```

## 四、datetime 高级用法

```python
from datetime import datetime, timedelta, timezone

# 当前时间
now = datetime.now()
print(now.isoformat())          # '2024-06-24T14:30:45.123456'

# 时区
utc = timezone.utc
beijing = timezone(timedelta(hours=8))

dt = datetime.now(beijing)
print(dt.tzinfo)                # UTC+08:00

# 格式化
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%Y年%m月%d日"))

# 解析
dt = datetime.strptime("2024-06-24", "%Y-%m-%d")
dt = datetime.fromisoformat("2024-06-24T14:30:00")

# 时间运算
yesterday = now - timedelta(days=1)
next_year = now + timedelta(days=365)
two_hours_later = now + timedelta(hours=2)

# 差值
diff = next_year - now
print(diff.days, diff.seconds)

# 时间戳
ts = now.timestamp()              # float
dt = datetime.fromtimestamp(ts)   # 本地时区
dt = datetime.utcfromtimestamp(ts) # UTC

# 比较
if now > yesterday:
    print("now is after yesterday")

# 提取分量
print(now.year, now.month, now.day)
print(now.weekday())              # 周几（0=周一）
print(now.isoweekday())           # 周几（1=周一，7=周日）
print(now.date())                 # date 部分
print(now.time())                 # time 部分
```

## 五、时区处理（Python 3.9+ zoneinfo）

```python
from datetime import datetime
from zoneinfo import ZoneInfo

# 列出所有时区
from zoneinfo import available_timezones
print("Asia/Shanghai" in available_timezones())    # True

# 切换时区
shanghai = ZoneInfo("Asia/Shanghai")
tokyo = ZoneInfo("Asia/Tokyo")
nyc = ZoneInfo("America/New_York")

dt = datetime.now(shanghai)
print(dt.astimezone(tokyo))      # 转东京时间
print(dt.astimezone(nyc))        # 转纽约时间
```

## 六、时间运算示例

```python
from datetime import datetime, timedelta

# 计算年龄
birth = datetime(2000, 1, 1)
today = datetime.now()
age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

# 计算下个工作日
def next_weekday(d):
    while d.weekday() >= 5:  # 周末
        d += timedelta(days=1)
    return d

# 计算两个时间间隔
start = datetime(2024, 1, 1)
end = datetime(2024, 12, 31)
diff = end - start
print(f"全年 {diff.days} 天")

# 倒计时到周末
now = datetime.now()
days_to_weekend = 5 - now.weekday()
if days_to_weekend < 0:
    days_to_weekend += 7
print(f"距周末还有 {days_to_weekend} 天")
```
""",

"logging_module": """\
## 一、logging 模块基础

```python
import logging

# 1. 基本使用
logging.basicConfig(level=logging.DEBUG)
logging.debug("调试信息")
logging.info("一般信息")
logging.warning("警告")
logging.error("错误")
logging.critical("严重错误")
```

## 二、日志级别

| 级别 | 数值 | 用途 |
|------|------|------|
| `DEBUG` | 10 | 详细诊断信息 |
| `INFO` | 20 | 确认程序运行正常 |
| `WARNING` | 30 | 警告，但程序能继续 |
| `ERROR` | 40 | 严重问题 |
| `CRITICAL` | 50 | 致命错误 |

## 三、basicConfig 配置

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="app.log",
    filemode="a"  # 追加（默认）
)

logging.info("程序启动")
# 写入 app.log：
# 2024-06-24 14:30:00 - root - INFO - 程序启动
```

## 四、Logger 对象（推荐）

```python
import logging

# 1. 获取 logger
logger = logging.getLogger(__name__)   # 用模块名
logger.setLevel(logging.DEBUG)

# 2. 添加 handler
# 输出到控制台
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter("%(name)s - %(levelname)s - %(message)s"))
logger.addHandler(console)

# 输出到文件
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)

# 3. 使用
logger.debug("调试")
logger.info("信息")
logger.warning("警告")
```

## 五、Formatter 字段

| 字段 | 含义 |
|------|------|
| `%(name)s` | Logger 名 |
| `%(levelname)s` | 级别名 |
| `%(levelno)d` | 级别数字 |
| `%(pathname)s` | 文件路径 |
| `%(filename)s` | 文件名 |
| `%(funcName)s` | 函数名 |
| `%(lineno)d` | 行号 |
| `%(asctime)s` | 时间（可格式化） |
| `%(message)s` | 日志消息 |
| `%(exc_info)s` | 异常信息 |
| `%(threadName)s` | 线程名 |
| `%(process)d` | 进程 PID |

## 六、实战：完整 logging 配置

```python
import logging
from logging.handlers import RotatingFileHandler

# 配置
def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 控制台（只显示 INFO+）
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    logger.addHandler(console)

    # 文件（所有级别，含滚动）
    file_handler = RotatingFileHandler(
        "app.log",
        maxBytes=10 * 1024 * 1024,    # 10 MB
        backupCount=5,                # 保留 5 个备份
        encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

logger = setup_logging()
logger.info("程序启动")
```

## 七、在类中使用

```python
import logging

class UserService:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def login(self, username):
        self.logger.info(f"用户 {username} 尝试登录")
        if not self._validate(username):
            self.logger.warning(f"用户 {username} 验证失败")
            return False
        self.logger.info(f"用户 {username} 登录成功")
        return True

    def _validate(self, username):
        return username == "admin"

service = UserService()
service.login("alice")
service.login("admin")
```

## 八、logging vs print

| 维度 | print | logging |
|------|-------|---------|
| 开关 | 不能关 | 可以按级别控制 |
| 输出目标 | 标准输出 | 任意（文件、网络） |
| 时间戳 | 没有 | 自动 |
| 模块/函数 | 没有 | 自动 |
| 线程信息 | 没有 | 自动 |
| 性能 | 慢 | 快（懒格式化） |

```python
# 推荐习惯
# ❌ 用 print 调试
print("here")
print(f"value: {value}")

# ✅ 用 logging
logger.debug("here")
logger.debug(f"value: {value}")
```
""",

"logging_config": """\
## 一、配置文件方式

### dictConfig（推荐）

```python
import logging
import logging.config

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {
            "format": "%(levelname)s: %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "app.log",
            "mode": "a",
            "level": "DEBUG",
            "formatter": "standard",
            "encoding": "utf-8",
        },
        "rotating": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "app.log",
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 5,
            "level": "DEBUG",
            "formatter": "standard",
            "encoding": "utf-8",
        },
    },
    "loggers": {
        "": {  # root
            "handlers": ["console", "file"],
            "level": "DEBUG",
        },
        "myapp": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,    # 不传给 root
        },
    },
}

logging.config.dictConfig(LOGGING_CONFIG)

logger = logging.getLogger("myapp.module")
logger.info("启动")
```

### fileConfig（从 ini 文件）

```ini
# logging.conf
[loggers]
keys=root,myapp

[handlers]
keys=console,file

[formatters]
keys=standard

[logger_root]
level=DEBUG
handlers=console

[logger_myapp]
level=INFO
handlers=console
qualname=myapp

[handler_console]
class=StreamHandler
level=INFO
formatter=standard
args=(sys.stdout,)

[handler_file]
class=FileHandler
level=DEBUG
formatter=standard
args=('app.log', 'a')

[formatter_standard]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
```

```python
import logging
import logging.config

logging.config.fileConfig("logging.conf")
logger = logging.getLogger("myapp")
```

## 二、过滤器

```python
import logging

class SensitiveFilter(logging.Filter):
    """过滤掉密码等敏感信息"""
    def filter(self, record):
        if "password" in record.msg.lower():
            record.msg = record.msg.replace("password=xxx", "password=***")
        return True

logger = logging.getLogger()
logger.addFilter(SensitiveFilter())

logger.info("User logged in with password=secret123")
# "User logged in with password=***"
```

## 三、上下文日志（传递额外字段）

```python
import logging

# 使用 LoggerAdapter
logger = logging.getLogger(__name__)
adapter = logging.LoggerAdapter(logger, {"user_id": "unknown"})

# 设置上下文
adapter.extra = {"user_id": "alice"}
adapter.info("操作执行")

# 输出
# INFO:__main__:操作执行
# （但 user_id 不会自动显示）

# 自定义 Formatter 显示
formatter = logging.Formatter("%(asctime)s [%(user_id)s] %(message)s")
```

## 四、异常日志

```python
import logging

logger = logging.getLogger(__name__)

try:
    1 / 0
except ZeroDivisionError:
    logger.exception("除以零错误")    # 自动附加 traceback

    # 或手动
    logger.error("除以零错误", exc_info=True)
```

## 五、第三方日志库（高级）

```python
# loguru：更简单
from loguru import logger

logger.add("app.log", rotation="500 MB", retention="10 days")
logger.info("Hello, World!")
logger.error("出错了")

# 结构化日志（structlog）
import structlog
log = structlog.get_logger()
log.info("user_logged_in", user_id=123, ip="192.168.1.1")
# 输出：user_logged_in user_id=123 ip=192.168.1.1
```

## 六、性能优化

```python
import logging

logger = logging.getLogger(__name__)

# ❌ 即使禁用也会计算 f-string
logger.debug(f"Value: {expensive_function()}")

# ✅ 懒格式化（推荐）
logger.debug("Value: %s", expensive_function())

# ✅ 条件判断（更激进）
if logger.isEnabledFor(logging.DEBUG):
    logger.debug(f"Value: {expensive_function()}")
```

## 七、日志最佳实践

1. **用模块级 logger**：`logger = logging.getLogger(__name__)`
2. **不要在库代码里配置 handler**：让用户决定
3. **避免重复日志**：配置时设 `disable_existing_loggers: False` + `propagate: False`
4. **用文件 + 控制台双输出**：控制台看实时，文件查历史
5. **用滚动日志**：避免单个文件过大
6. **结构化字段**：方便后续解析（JSON logs）
""",

"random_module": """\
## 一、random 模块基础

```python
import random

# 1. 随机浮点数
random.random()             # [0, 1) 之间的浮点数
random.uniform(1, 10)        # [1, 10] 之间的浮点数

# 2. 随机整数
random.randint(1, 10)        # [1, 10] 之间的整数（包含两端）
random.randrange(0, 100, 2)  # [0, 100) 之间的偶数（range 风格）

# 3. 随机序列
random.choice([1, 2, 3, 4, 5])     # 随机选一个
random.choices([1, 2, 3], k=2)    # 随机选 k 个（可重复）
random.sample([1, 2, 3, 4], 2)    # 随机选 k 个（不重复）

# 4. 打乱序列
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)          # 原地打乱
print(lst)
```

## 二、种子（可重复随机）

```python
import random

# 设置种子
random.seed(42)
print(random.random())       # 0.6394267984578837

random.seed(42)
print(random.random())       # 0.6394267984578837（一样）

# 默认种子是系统时间
random.seed()
```

**用途**：
- 调试随机代码（固定种子让 bug 可重现）
- 单元测试
- 蒙特卡洛模拟

## 三、常用场景

### 1. 随机密码

```python
import random
import string

def gen_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%"
    return ''.join(random.choice(chars) for _ in range(length))

print(gen_password())        # "aB3$kL9pQ!m2"
```

### 2. 洗牌（Fisher-Yates）

```python
import random

def fisher_yates(lst):
    for i in range(len(lst) - 1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]
    return lst

print(fisher_yates([1,2,3,4,5]))
# 注意：random.shuffle 内部就是这个算法
```

### 3. 加权随机

```python
import random

items = ["apple", "banana", "cherry"]
weights = [0.5, 0.3, 0.2]      # 概率

# 单选
choice = random.choices(items, weights=weights, k=1)[0]

# 多选
choices = random.choices(items, weights=weights, k=10)
# 按概率分布抽取
```

### 4. 随机抽样

```python
import random

# 不重复抽样
population = list(range(100))
sample = random.sample(population, 10)    # 抽 10 个

# 分层抽样（按比例）
groups = {
    "A": ["a1", "a2", "a3"],
    "B": ["b1", "b2"],
    "C": ["c1", "c2", "c3", "c4"],
}
for g, items in groups.items():
    k = max(1, len(items) // 2)
    sample = random.sample(items, k)
```

## 四、secrets 模块（密码学安全）

```python
import secrets

# 1. 安全随机整数
secrets.randbelow(100)           # [0, 100)
secrets.randbits(32)             # 32 位随机整数

# 2. 安全随机字节
token = secrets.token_bytes(16)  # 16 字节（128 位）
hex_token = secrets.token_hex(16)  # 32 字符的十六进制

# 3. 安全 URL 安全 token
url_token = secrets.token_urlsafe(16)

# 4. 对比（防止时序攻击）
secrets.compare_digest(a, b)     # 恒定时间比较

# 应用：API token、密码重置链接、session ID
```

## 五、UUID（通用唯一标识符）

```python
import uuid

# UUID v1：基于时间 + MAC 地址
u1 = uuid.uuid1()

# UUID v4：完全随机（最常用）
u4 = uuid.uuid4()

# UUID v5：基于名字 + 命名空间
u5 = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")

# 转字符串
str(u4)              # '12345678-1234-4abc-9def-123456789012'

# 从字符串解析
u = uuid.UUID("12345678-1234-4abc-9def-123456789012")
```

## 六、random 性能与陷阱

```python
import random

# 1. random 不是密码学安全的！用 secrets 替代
# ❌ random.random()   # 可预测
# ✅ secrets.token_hex()  # 不可预测

# 2. 性能
import time

n = 1_000_000
start = time.time()
for _ in range(n):
    random.random()
print(f"random.random: {time.time() - start:.3f}s")

start = time.time()
for _ in range(n):
    secrets.token_hex(16)
print(f"secrets.token_hex: {time.time() - start:.3f}s")
# secrets 慢约 10 倍（但安全）
```

## 七、应用案例

```python
import random

# 1. 抽奖
participants = ["Alice", "Bob", "Charlie", "David", "Eve"]
winners = random.sample(participants, 3)
print(f"中奖者：{winners}")

# 2. 模拟掷骰子
def roll_dice(n=2):
    return [random.randint(1, 6) for _ in range(n)]

# 3. 随机点名
students = ["张三", "李四", "王五", "赵六"]
print(f"今天回答问题的是：{random.choice(students)}")

# 4. 蒙特卡洛求 π
def monte_carlo_pi(n=1_000_000):
    inside = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x*x + y*y < 1:
            inside += 1
    return 4 * inside / n

print(f"π ≈ {monte_carlo_pi():.6f}")
```
""",

}