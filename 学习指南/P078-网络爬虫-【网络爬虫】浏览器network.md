---
title: "P78 【网络爬虫】浏览器network"
p_no: 78
category: 网络爬虫
duration: 455
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P78 【网络爬虫】浏览器network

> **课程分类**：网络爬虫
> **时长**：455 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

网络爬虫阶段，从 HTTP 基础到 requests 模块，再到综合案例。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
## 浏览器 F12 抓包

### Chrome DevTools Network 面板

打开方式：`F12` → `Network` 面板

### 关键列

| 列 | 含义 |
|------|------|
| Name | 请求名 |
| Status | 状态码 |
| Type | 类型（xhr/fetch/img） |
| Initiator | 发起者 |
| Size | 大小 |
| Time | 耗时 |

### 过滤请求

- `XHR`：只看 AJAX 请求（API）
- `JS`：JavaScript
- `Img`：图片
- `Doc`：HTML
- `WS`：WebSocket

### 查看请求详情

点击请求 → 看 Headers / Preview / Response / Cookies / Timing

**Headers 面板**：
- General：URL、方法、状态码
- Response Headers：响应头
- Request Headers：请求头（**最重要的**）
- Query String Parameters：URL 参数

**Response 面板**：原始响应内容

### 复制为 cURL

右键请求 → Copy → Copy as cURL (bash)

```bash
curl 'https://api.example.com/data' \\
  -H 'User-Agent: Mozilla/5.0 ...' \\
  -H 'Authorization: Bearer xxx' \\
  -H 'Cookie: session=abc' \\
  --data-raw '{"key":"value"}'
```

转 Python requests：

```python
import requests

headers = {
    "User-Agent": "Mozilla/5.0 ...",
    "Authorization": "Bearer xxx",
    "Cookie": "session=abc",
}

response = requests.post(
    "https://api.example.com/data",
    headers=headers,
    json={"key": "value"}
)
```

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）