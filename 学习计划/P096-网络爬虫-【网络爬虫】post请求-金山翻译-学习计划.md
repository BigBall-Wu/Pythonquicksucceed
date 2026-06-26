---
title: "学习计划 P096 【网络爬虫】post请求-金山翻译"
p_no: 96
category: 网络爬虫
created: 2026-06-24
updated: 2026-06-24
type: study-plan
---

# 学习计划 P096　【网络爬虫】post请求-金山翻译

## 一、本节在课程中的位置

| 项目 | 内容 |
|------|------|
| 课程章节 | 第 96 集 / 共 100 集 |
| 分类 | 网络爬虫 |
| 视频时长 | 526 秒（约 9 分钟） |
| 难度 | 中级 |

## 二、为什么先学这一节

POST 请求是爬虫进阶的必备技能。很多 API 和网站功能需要 POST 才能实现：
- 登录表单提交
- 搜索查询
- 翻译服务
- 文件上传

本节通过金山翻译案例，完整展示 POST 请求的使用方法。

## 三、本节要回答的核心问题

1. **POST 请求和 GET 请求的区别？**
2. **如何构造 POST 请求参数？**
3. **金山翻译 API 如何使用？**
4. **如何调试 POST 请求？**
5. **如何处理加密参数？**

## 四、课本对照

本节是**实战案例**，课本无直接对应。需要结合课程视频和知识补全学习。

## 五、具体学习步骤

### 第 1 步：GET vs POST 对比（10 分钟）

```python
# GET vs POST 对比

GET vs POST = """
┌──────────────┬──────────────────┬──────────────────┐
│              │       GET        │       POST      │
├──────────────┼──────────────────┼──────────────────┤
│ 参数位置     │ URL 查询参数      │ 请求体           │
│ 参数大小     │ 有限（2KB）      │ 无限制           │
│ 可见性       │ URL 中可见       │ 不可见           │
│ 缓存         │ 可缓存           │ 不可缓存         │
│ 安全性       │ 低（URL 明文）   │ 较高             │
│ 用途         │ 获取数据         │ 提交数据         │
│ 幂等性       │ 幂等             │ 非幂等           │
└──────────────┴──────────────────┴──────────────────┘
"""

# GET 请求示例
r = requests.get(
    "https://api.example.com/search",
    params={"q": "python", "page": 1}  # 参数在 URL 中
)

# POST 请求示例
r = requests.post(
    "https://api.example.com/submit",
    data={"username": "alice", "password": "secret"}  # 参数在请求体中
)
```

### 第 2 步：金山翻译 API（15 分钟）

```python
import requests

def translate(text, from_lang="en", to_lang="zh"):
    """金山翻译（简化版）"""
    url = "https://ifanyi.iciba.com/index.php"

    # 请求参数
    params = {
        "c": "trans",
        "m": "getTrans",
        "from": from_lang,
        "to": to_lang,
        "query": text,
    }

    # 请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Origin": "https://www.iciba.com",
        "Referer": "https://www.iciba.com/",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
    }

    try:
        response = requests.post(url, data=params, headers=headers, timeout=10)
        result = response.json()

        if result.get("status") == 1:
            return result["content"]["out"]
        else:
            print(f"翻译失败: {result}")
            return None

    except Exception as e:
        print(f"请求失败: {e}")
        return None

# 测试
text = "Hello, world! Python is a great programming language."
translation = translate(text)
print(f"原文: {text}")
print(f"译文: {translation}")
```

### 第 3 步：调试 POST 请求（15 分钟）

```python
import requests

# 调试技巧 1：打印完整请求信息
def debug_post(url, data, headers):
    """调试 POST 请求"""
    print("=" * 50)
    print(f"URL: {url}")
    print(f"Headers: {headers}")
    print(f"Data: {data}")
    print("=" * 50)

    response = requests.post(url, data=data, headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text[:500]}")
    return response

# 调试技巧 2：用 httpbin.org 测试
r = requests.post(
    "https://httpbin.org/post",
    data={"key": "value"},
    headers={"X-Custom": "test"}
)
print(r.json())

# 调试技巧 3：转换为 cURL 命令
# https://curlconverter.com/ 可以把 Python 代码转成 cURL
```

### 第 4 步：翻译器封装（15 分钟）

```python
import requests
import time

class Translator:
    """翻译器类"""

    def __init__(self, from_lang="auto", to_lang="zh"):
        self.from_lang = from_lang
        self.to_lang = to_lang
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...",
        })

    def translate(self, text):
        """翻译文本"""
        url = "https://ifanyi.iciba.com/index.php"

        params = {
            "c": "trans",
            "m": "getTrans",
            "from": self.from_lang,
            "to": self.to_lang,
            "query": text,
        }

        headers = {
            "Origin": "https://www.iciba.com",
            "Referer": "https://www.iciba.com/",
        }

        try:
            response = self.session.post(url, data=params, headers=headers, timeout=10)
            result = response.json()

            if result.get("status") == 1:
                return result["content"]["out"]
            return None

        except Exception as e:
            print(f"翻译失败: {e}")
            return None

    def batch_translate(self, texts, delay=1):
        """批量翻译"""
        results = []
        for i, text in enumerate(texts):
            print(f"[{i+1}/{len(texts)}] 翻译: {text[:30]}...")
            result = self.translate(text)
            results.append(result or "")
            time.sleep(delay)  # 避免请求过快
        return results

# 使用
translator = Translator(from_lang="en", to_lang="zh")
texts = [
    "Hello, world!",
    "Python is great.",
    "I love programming.",
]

translations = translator.batch_translate(texts)
for original, translated in zip(texts, translations):
    print(f"{original} -> {translated}")
```

### 第 5 步：常见翻译 API（10 分钟）

```python
# 常见的免费翻译 API：

翻译 API 对比 = """
1. 有道翻译
   - 免费额度
   - 需要申请 AppKey

2. 百度翻译
   - 有免费额度
   - 需要注册和申请

3. 腾讯翻译
   - 有免费额度
   - 需要 SecretId/SecretKey

4. Google 翻译（被墙）
   - 网页版可能不稳定
   - 官方 API 需要付费

5. DeepL
   - 翻译质量高
   - 有免费额度
"""

# DeepL 示例（推荐）
def deepl_translate(text, api_key="YOUR_API_KEY"):
    """使用 DeepL API 翻译"""
    url = "https://api-free.deepl.com/v2/translate"  # 免费版

    headers = {
        "Authorization": f"DeepL-Auth-Key {api_key}",
    }

    data = {
        "text": text,
        "source_lang": "EN",
        "target_lang": "ZH",
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()["translations"][0]["text"]
```

## 六、这一节要掌握的知识点

- [ ] GET 和 POST 的区别
- [ ] POST 请求参数构造（data/params）
- [ ] 金山翻译 API 使用
- [ ] POST 请求调试技巧
- [ ] 翻译器类封装
- [ ] 常见翻译 API 介绍

## 七、动手练习

### 练习 1：实现多语言翻译

```python
# 实现一个支持多语言的翻译器
def translate_multi(text, source, target):
    """多语言翻译"""
    # 实现代码...
    pass

# 测试
print(translate_multi("Hello", "en", "zh"))
print(translate_multi("你好", "zh", "en"))
print(translate_multi("Bonjour", "fr", "zh"))
```

### 练习 2：批量翻译文件

```python
# 实现一个翻译文件内容的工具
def translate_file(input_file, output_file, source_lang, target_lang):
    """翻译文件内容"""
    # 读取文件
    # 逐行翻译
    # 保存结果
    pass
```

## 八、自测题

- [ ] **Q1**：GET 和 POST 的主要区别是什么？
- [ ] **Q2**：POST 请求的参数放在哪里？
- [ ] **Q3**：金山翻译需要设置哪些请求头？
- [ ] **Q4**：如何调试 POST 请求？
- [ ] **Q5**：批量翻译时为什么要设置延迟？

## 九、参考资料

- 视频 BV1rpWjevEip P96
- 金山词霸：https://www.iciba.com/
- httpbin：https://httpbin.org/

### 选读

- RESTful API 设计：https://restfulapi.net/
- DeepL API：https://www.deepl.com/docs-api/

## 十、关联 Vault 笔记

- [[学习指南/P096-网络爬虫-【网络爬虫】post请求-金山翻译]]
- [[学习计划/P095-网络爬虫-【网络爬虫】使用cookie获取登录后的页面数据-学习计划]]（上一节）
- [[学习计划/P097-网络爬虫-【网络爬虫】session自动携带cookie-学习计划]]（下一节）
- [[index]]

---

> **预计总时长**：65 分钟（视频 9 + 实操 56）
>
> **完成标志**：能用 POST 请求提交数据，能使用翻译 API，能封装翻译器类
