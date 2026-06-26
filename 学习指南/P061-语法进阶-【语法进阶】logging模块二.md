---
title: "P61 【语法进阶】logging模块二"
p_no: 61
category: 语法进阶
duration: 553
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P61 【语法进阶】logging模块二

> **课程分类**：语法进阶
> **时长**：553 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

语法进阶阶段，OOP、文件、迭代、多线程、正则、标准库模块。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
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

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）