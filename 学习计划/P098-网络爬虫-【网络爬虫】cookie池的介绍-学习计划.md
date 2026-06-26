---
title: "学习计划 P098 【网络爬虫】cookie池的介绍"
p_no: 98
category: 网络爬虫
created: 2026-06-24
updated: 2026-06-24
type: study-plan
---

# 学习计划 P098　【网络爬虫】cookie池的介绍

## 一、本节在课程中的位置

| 项目 | 内容 |
|------|------|
| 课程章节 | 第 98 集 / 共 100 集 |
| 分类 | 网络爬虫 |
| 视频时长 | 313 秒（约 5 分钟） |
| 难度 | 中级 |

## 二、为什么先学这一节

Cookie 池是高级反封策略之一。当单一账号/ Cookie 容易被封禁时，使用 Cookie 池可以：
- 分散请求来源，降低单个账号风险
- 模拟多个用户行为
- 提高爬虫的稳定性和持久性
- 实现更高效的数据采集

## 三、本节要回答的核心问题

1. **什么是 Cookie 池？**
2. **Cookie 池的工作原理？**
3. **如何实现 Cookie 池？**
4. **如何维护 Cookie 池？**
5. **Cookie 池的最佳实践？**

## 四、课本对照

本节内容**书本未涵盖**。高级反爬策略属于进阶知识，需要靠课程视频 + 知识补全学习。

## 五、具体学习步骤

### 第 1 步：Cookie 池概念（10 分钟）

```python
# Cookie 池原理：

Cookie池原理 = """
┌─────────────────────────────────────────────────────┐
│                   Cookie 池                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐           │
│  │Cookie 1 │  │Cookie 2 │  │Cookie 3 │  ...      │
│  │(Alice)  │  │(Bob)   │  │(Charlie)│           │
│  └────┬────┘  └────┬────┘  └────┬────┘           │
│       │            │            │                 │
│       └────────────┼────────────┘                 │
│                    ↓                               │
│              random.choice()                        │
│                    ↓                               │
│         ┌─────────────────┐                        │
│         │ 随机获取一个    │                        │
│         │ Cookie 使用     │                        │
│         └─────────────────┘                        │
└─────────────────────────────────────────────────────┘

优势：
- 分散请求来源
- 降低单个 Cookie 被封概率
- 提高爬虫稳定性
"""
```

### 第 2 步：基础 Cookie 池实现（15 分钟）

```python
import random
import requests

class CookiePool:
    """Cookie 池"""

    def __init__(self, cookies_list=None):
        """
        cookies_list: Cookie 字典列表
        格式: [{'sid': 'xxx', 'user': 'alice'}, ...]
        """
        self.cookies_list = cookies_list or []

    def add(self, cookies):
        """添加 Cookie"""
        if cookies not in self.cookies_list:
            self.cookies_list.append(cookies)

    def get_random(self):
        """随机获取一个 Cookie"""
        if not self.cookies_list:
            raise ValueError("Cookie 池为空")
        return random.choice(self.cookies_list)

    def get_session(self):
        """获取一个带随机 Cookie 的 Session"""
        session = requests.Session()
        cookies = self.get_random()
        session.cookies.update(cookies)
        return session

    def __len__(self):
        return len(self.cookies_list)

# 使用示例
pool = CookiePool([
    {"session": "alice_001", "user_id": "1"},
    {"session": "bob_002", "user_id": "2"},
    {"session": "charlie_003", "user_id": "3"},
])

print(f"Cookie 池大小: {len(pool)}")

# 获取随机 Cookie
cookies = pool.get_random()
print(f"随机 Cookie: {cookies}")

# 获取带 Cookie 的 Session
session = pool.get_session()
print(f"Session Cookie: {dict(session.cookies)}")
```

### 第 3 步：Cookie 池管理器（15 分钟）

```python
import json
import time
from pathlib import Path

class CookiePoolManager:
    """Cookie 池管理器"""

    def __init__(self, storage_file="cookie_pool.json"):
        self.storage_file = Path(storage_file)
        self.cookies = self._load()

    def _load(self):
        """加载 Cookie 池"""
        if self.storage_file.exists():
            with open(self.storage_file, encoding="utf-8") as f:
                return json.load(f)
        return []

    def _save(self):
        """保存 Cookie 池"""
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump(self.cookies, f, ensure_ascii=False, indent=2)

    def add(self, cookie, max_age=None):
        """
        添加 Cookie

        参数：
            cookie: Cookie 字典
            max_age: 有效期（秒），None 表示永不过期
        """
        # 添加时间戳
        cookie["added_at"] = time.time()
        if max_age:
            cookie["expires_at"] = time.time() + max_age
        else:
            cookie["expires_at"] = None

        self.cookies.append(cookie)
        self._save()

    def remove(self, index):
        """移除指定索引的 Cookie"""
        if 0 <= index < len(self.cookies):
            self.cookies.pop(index)
            self._save()

    def get_valid(self):
        """获取所有有效（非过期）的 Cookie"""
        now = time.time()
        return [
            c for c in self.cookies
            if c.get("expires_at") is None or c["expires_at"] > now
        ]

    def get_random_valid(self):
        """随机获取一个有效 Cookie"""
        valid = self.get_valid()
        if not valid:
            return None
        return random.choice(valid)

    def cleanup_expired(self):
        """清理过期的 Cookie"""
        before = len(self.cookies)
        self.cookies = self.get_valid()
        after = len(self.cookies)
        self._save()
        return before - after

    def get_stats(self):
        """获取统计信息"""
        valid = self.get_valid()
        expired = len(self.cookies) - len(valid)
        return {
            "total": len(self.cookies),
            "valid": len(valid),
            "expired": expired,
        }

# 使用
manager = CookiePoolManager("my_cookie_pool.json")

# 添加 Cookie
manager.add({"session": "test_001", "user": "test"}, max_age=3600)

# 获取统计
print(manager.get_stats())

# 清理过期
removed = manager.cleanup_expired()
print(f"清理了 {removed} 个过期 Cookie")
```

### 第 4 步：高级 Cookie 池（15 分钟）

```python
import random
import requests
import time
from collections import defaultdict

class AdvancedCookiePool:
    """高级 Cookie 池（带状态追踪）"""

    def __init__(self):
        self.cookies = []
        self.failed_count = defaultdict(int)  # 失败次数
        self.last_used = defaultdict(float)  # 上次使用时间

    def add(self, cookies):
        """添加 Cookie"""
        self.cookies.append(cookies)

    def get_random(self, prefer_valid=True):
        """获取 Cookie（优先选择失败少、最近未用的）"""
        if prefer_valid:
            # 过滤掉失败次数过多的
            candidates = [c for c in self.cookies if self.failed_count[id(c)] < 3]
            if not candidates:
                candidates = self.cookies
        else:
            candidates = self.cookies

        # 按权重选择（失败少权重高）
        weights = []
        for c in candidates:
            weight = max(1, 5 - self.failed_count[id(c)])
            weights.append(weight)

        selected = random.choices(candidates, weights=weights)[0]
        self.last_used[id(selected)] = time.time()
        return selected

    def mark_success(self, cookies):
        """标记成功"""
        self.failed_count[id(cookies)] = 0

    def mark_failure(self, cookies):
        """标记失败"""
        self.failed_count[id(cookies)] += 1

    def get_healthy(self):
        """获取健康的 Cookie（失败次数少）"""
        return [c for c in self.cookies if self.failed_count[id(c)] < 3]


class CookiePoolSession:
    """Cookie 池 + Session 组合"""

    def __init__(self, pool):
        self.pool = pool

    def request(self, method, url, **kwargs):
        """带 Cookie 池的请求"""
        cookies = self.pool.get_random()

        # 更新 kwargs 中的 cookies
        if "cookies" in kwargs:
            kwargs["cookies"].update(cookies)
        else:
            kwargs["cookies"] = cookies

        session = requests.Session()
        try:
            response = session.request(method, url, **kwargs)

            if response.status_code < 400:
                self.pool.mark_success(cookies)
                return response
            else:
                self.pool.mark_failure(cookies)
                return response

        except Exception as e:
            self.pool.mark_failure(cookies)
            raise
```

### 第 5 步：最佳实践（10 分钟）

```python
# Cookie 池最佳实践：

最佳实践 = """
1. Cookie 来源
   - 多个注册账号
   - 账号轮换注册
   - 购买/租用（不推荐）

2. 维护策略
   - 定期刷新 Cookie
   - 监控 Cookie 有效性
   - 及时移除失效 Cookie

3. 使用策略
   - 随机选择 + 权重
   - 失败自动切换
   - 控制使用频率

4. 法律风险
   - 使用 Cookie 池可能违反网站 TOS
   - 仅用于合法目的
   - 尊重网站规则
"""

# ⚠️ 重要提醒：
重要提醒 = """
Cookie 池可能涉及以下风险：

1. 账号被封
   - 同一 IP 多账号容易关联
   - 异常行为被检测

2. 法律风险
   - 违反网站服务条款
   - 可能侵犯用户隐私
   - 滥用可能违法

3. 技术风险
   - Cookie 有效期短
   - 需要持续维护
   - 成本较高

建议：优先使用官方 API 或付费服务
"""

# 合规替代方案
合规方案 = """
1. 官方 API（如有）
2. 付费数据服务
3. 授权数据合作
4. 公开数据集
"""
```

## 六、这一节要掌握的知识点

- [ ] Cookie 池的概念和原理
- [ ] 基础 Cookie 池实现
- [ ] Cookie 池管理器（持久化、过期清理）
- [ ] 高级 Cookie 池（权重、状态追踪）
- [ ] Cookie 池最佳实践
- [ ] 法律风险和合规建议

## 七、动手练习

### 练习 1：实现 Cookie 池

```python
# 实现一个 Cookie 池类
class MyCookiePool:
    """自定义 Cookie 池"""

    def __init__(self):
        # 初始化...
        pass

    def add(self, cookies):
        # 添加 Cookie...
        pass

    def get_random(self):
        # 随机获取...
        pass

    def remove_invalid(self):
        # 移除无效 Cookie...
        pass
```

### 练习 2：实现 Cookie 管理器

```python
# 实现一个带过期清理的 Cookie 管理器
class CookieManager:
    """Cookie 管理器"""

    def __init__(self, storage_path):
        # 初始化...
        pass

    def save(self, cookies):
        # 保存 Cookie...
        pass

    def load(self):
        # 加载 Cookie...
        pass

    def cleanup(self):
        # 清理过期...
        pass
```

## 八、自测题

- [ ] **Q1**：什么是 Cookie 池？
- [ ] **Q2**：Cookie 池相比单个 Cookie 有什么优势？
- [ ] **Q3**：如何实现 Cookie 过期清理？
- [ ] **Q4**：Cookie 池有哪些法律风险？
- [ ] **Q5**：有哪些合规替代方案？

## 九、参考资料

- 视频 BV1rpWjevEip P98
- requests 文档：https://docs.python-requests.org/

### 选读

- 反爬策略汇总：https://github.com/chenjiandongx/anti-anti-spider
- 爬虫伦理：https://www.sciencedirect.com/science/article/pii/S0167739X1930010X

## 十、关联 Vault 笔记

- [[学习指南/P098-网络爬虫-【网络爬虫】cookie池的介绍]]
- [[学习计划/P097-网络爬虫-【网络爬虫】session自动携带cookie-学习计划]]（上一节）
- [[学习计划/P099-网络爬虫-【网络爬虫】代理ip介绍-学习计划]]（下一节）
- [[index]]

---

> **预计总时长**：65 分钟（视频 5 + 实操 60）
>
> **完成标志**：能理解 Cookie 池原理，能实现 Cookie 池类，能进行 Cookie 管理和维护
