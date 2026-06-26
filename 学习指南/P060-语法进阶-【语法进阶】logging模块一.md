---
title: "P60 【语法进阶】logging模块一"
p_no: 60
category: 语法进阶
duration: 394
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P60 【语法进阶】logging模块一

> **课程分类**：语法进阶
> **时长**：394 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

语法进阶阶段，OOP、文件、迭代、多线程、正则、标准库模块。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
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

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）