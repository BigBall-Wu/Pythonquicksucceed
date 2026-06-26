---
title: "P57 【语法进阶】sys模块"
p_no: 57
category: 语法进阶
duration: 441
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P57 【语法进阶】sys模块

> **课程分类**：语法进阶
> **时长**：441 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

语法进阶阶段，OOP、文件、迭代、多线程、正则、标准库模块。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
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

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）