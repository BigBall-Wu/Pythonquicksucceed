---
title: "P77 【网络爬虫】http和https协议"
p_no: 77
category: 网络爬虫
duration: 470
bvid: BV1rpWjevEip
up: Python官方课程
type: learning-guide
created: 2026-06-24
updated: 2026-06-24
---

# P77 【网络爬虫】http和https协议

> **课程分类**：网络爬虫
> **时长**：470 秒
> **来源**：BV1rpWjevEip - Python官方课程

## 上下文

网络爬虫阶段，从 HTTP 基础到 requests 模块，再到综合案例。

## 课本对应章节

本节内容**书本无对应**，需用 Python 知识库补全。

## 一、课本内容（原书摘录）

> 本节内容书本未涵盖，跳过课本切片。


## 二、知识补全（书本没有的部分）

\
## HTTP vs HTTPS

| 维度 | HTTP | HTTPS |
|------|------|-------|
| 端口 | 80 | 443 |
| 加密 | ❌ 明文 | ✅ TLS/SSL |
| 证书 | 不需要 | 需要 CA 签发 |
| 速度 | 略快 | 略慢（+ TLS 握手） |
| SEO | ❌ 不利 | ✅ 谷歌优先 |

## SSL/TLS 握手流程

```
客户端 → ClientHello（支持的 TLS 版本、加密算法、随机数）
服务器 → ServerHello（选定算法、服务器证书、随机数）
客户端 → 验证证书、生成预主密钥、用公钥加密发送
双方 → 用预主密钥派生出会话密钥
之后 → 用会话密钥加密通信
```

## Python 中处理 HTTPS

```python
import requests

# 默认
r = requests.get("https://api.github.com")

# 跳过证书验证（仅测试）
r = requests.get("https://self-signed.example.com", verify=False)

# 自定义 CA
r = requests.get("https://internal.example.com", verify="/path/to/ca-bundle.crt")

# 客户端证书
r = requests.get("https://example.com", cert=("/path/to/client.crt", "/path/to/client.key"))
```

## 常见 HTTPS 问题

```python
# SSLError: CERTIFICATE_VERIFY_FAILED
# → 证书过期/不受信任

# requests.exceptions.SSLError
# → 检查 verify 参数

# SSL: CERTIFICATE_VERIFY_FAILED
# Mac 上：/Applications/Python\\ 3.x/Install\\ Certificates.command
```

## 三、动手练习

- [ ] 看完本节视频
- [ ] 自己手写一遍示例代码
- [ ] 完成课本对应章节练习（如果有）
- [ ] 尝试修改示例，做小实验
- [ ] 整理笔记（用 WikiLink 链接到相关 Vault 笔记）