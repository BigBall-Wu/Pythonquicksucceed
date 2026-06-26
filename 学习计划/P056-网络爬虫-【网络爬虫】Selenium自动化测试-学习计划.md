---
title: P056-网络爬虫-【网络爬虫】Selenium自动化测试-学习计划
created: 2026-06-24
updated: 2026-06-24
type: permanent
tags: [python, 网络爬虫, Selenium]
summary: 掌握Selenium自动化浏览器操作与JavaScript渲染页面抓取
---

# P056 - 网络爬虫：Selenium 自动化测试

## 本节知识点总览

| 知识点 | 难度 | 重要度 | 课本定位 |
|--------|------|--------|----------|
| Selenium 基础 | ⭐⭐ | ⭐⭐⭐ | L3965-L3995 |
| 元素定位 | ⭐⭐ | ⭐⭐⭐ | L4000-L4035 |
| 等待策略 | ⭐⭐ | ⭐⭐⭐ | L4040-L4075 |
| JavaScript 处理 | ⭐⭐ | ⭐⭐ | L4080-L4115 |

---

## 一、Selenium 基础

### 1.1 安装

```bash
# 安装 Selenium
pip install selenium

# 下载浏览器驱动
# Chrome: https://chromedriver.chromium.org/
# Firefox: https://github.com/mozilla/geckodriver/releases
# Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

# 确保驱动版本与浏览器版本匹配
```

### 1.2 基本使用

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 配置 Chrome 选项
options = Options()
options.add_argument("--headless")  # 无头模式
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 启动浏览器
service = Service("C:/path/to/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# 访问网页
driver.get("https://www.example.com")

# 获取页面标题
print(driver.title)

# 获取页面源码
print(driver.page_source)

# 关闭浏览器
driver.quit()
```

---

## 二、元素定位

### 2.1 八种定位方式

```python
from selenium.webdriver.common.by import By

# ID 定位
element = driver.find_element(By.ID, "username")
elements = driver.find_elements(By.ID, "username")

# NAME 定位
element = driver.find_element(By.NAME, "password")

# CLASS NAME 定位
element = driver.find_element(By.CLASS_NAME, "btn-primary")

# TAG NAME 定位
element = driver.find_element(By.TAG_NAME, "input")

# LINK TEXT 定位
element = driver.find_element(By.LINK_TEXT, "查看更多")

# PARTIAL LINK TEXT 定位
element = driver.find_element(By.PARTIAL_LINK_TEXT, "更多")

# XPATH 定位
element = driver.find_element(By.XPATH, "//input[@id='username']")

# CSS SELECTOR 定位
element = driver.find_element(By.CSS_SELECTOR, "input#username")
```

### 2.2 XPath 高级定位

```python
# 绝对路径
element = driver.find_element(By.XPATH, "/html/body/div[2]/form/input")

# 相对路径
element = driver.find_element(By.XPATH, "//form/input")

# 属性定位
element = driver.find_element(By.XPATH, "//input[@type='text']")
element = driver.find_element(By.XPATH, "//input[@type='text' and @name='username']")

# 文本定位
element = driver.find_element(By.XPATH, "//button[text()='登录']")
element = driver.find_element(By.XPATH, "//a[contains(text(),'更多')]")

# 父元素定位
element = driver.find_element(By.XPATH, "//input[@id='username']/parent::div")

# 兄弟元素定位
element = driver.find_element(By.XPATH, "//input[@id='username']/following-sibling::input")
```

---

## 三、元素操作

### 3.1 基本操作

```python
# 输入文本
element.send_keys("hello")

# 清空输入框
element.clear()

# 点击
element.click()

# 获取元素文本
text = element.text

# 获取属性值
value = element.get_attribute("href")

# 判断元素是否可见
is_visible = element.is_displayed()

# 判断元素是否启用
is_enabled = element.is_enabled()

# 判断元素是否选中（checkbox/radio）
is_selected = element.is_selected()
```

### 3.2 表单操作

```python
from selenium.webdriver.support.ui import Select

# 文本输入
username = driver.find_element(By.NAME, "username")
username.send_keys("admin")

# 密码输入
password = driver.find_element(By.NAME, "password")
password.send_keys("password")

# 下拉框选择
select = Select(driver.find_element(By.NAME, "country"))
select.select_by_value("CN")           # 按值选择
select.select_by_visible_text("中国")  # 按文本选择
select.select_by_index(1)               # 按索引选择

# 单选框
radio = driver.find_element(By.XPATH, "//input[@name='gender' and @value='male']")
radio.click()

# 复选框
checkbox = driver.find_element(By.ID, "agree")
if not checkbox.is_selected():
    checkbox.click()

# 提交表单
driver.find_element(By.XPATH, "//button[@type='submit']").click()
```

### 3.3 鼠标操作

```python
from selenium.webdriver.common.action_chains import ActionChains

# 悬停
element = driver.find_element(By.ID, "dropdown")
ActionChains(driver).move_to_element(element).perform()

# 右键点击
ActionChains(driver).context_click(element).perform()

# 双击
ActionChains(driver).double_click(element).perform()

# 拖拽
source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")
ActionChains(driver).drag_and_drop(source, target).perform()

# 组合操作
ActionChains(driver).click(element).send_keys("text").perform()
```

### 3.4 键盘操作

```python
from selenium.webdriver.common.keys import Keys

# 输入
element.send_keys("hello")

# 特殊键
element.send_keys(Keys.RETURN)    # 回车
element.send_keys(Keys.ENTER)     # 回车
element.send_keys(Keys.TAB)       # Tab
element.send_keys(Keys.ESCAPE)   # ESC

# 全选
element.send_keys(Keys.CONTROL, "a")
element.send_keys(Keys.CONTROL, "c")  # 复制
element.send_keys(Keys.CONTROL, "v")  # 粘贴
```

---

## 四、等待策略

### 4.1 显式等待

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 等待元素可见
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "element_id"))
)

# 等待元素可点击
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "button_id"))
)

# 等待元素存在于 DOM
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@id='content']"))
)

# 等待文本出现
element = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "status"), "完成")
)

# 等待新窗口打开
main_window = driver.window_handles[0]
WebDriverWait(driver, 10).until(EC.new_window_is_opened(main_window))
```

### 4.2 常见等待条件

```python
# 判断条件
EC.title_is("页面标题")
EC.title_contains("页面标题")
EC.url_contains("example.com")
EC.url_to_be("https://...")

# 元素条件
EC.presence_of_element_located((By.ID, "id"))
EC.visibility_of_element_located((By.ID, "id"))
EC.invisibility_of_element_located((By.ID, "id"))
EC.element_to_be_clickable((By.ID, "id"))
EC.staleness_of(element)  # 等待元素从 DOM 移除

# 多个元素
EC.presence_of_all_elements_located((By.CLASS_NAME, "item"))

# 自定义条件
def wait_for_element(driver):
    element = driver.find_element(By.ID, "target")
    return element if element.is_displayed() else None

element = WebDriverWait(driver, 10).until(wait_for_element)
```

### 4.3 隐式等待

```python
# 设置全局隐式等待（只设置一次）
driver.implicitly_wait(10)  # 10 秒

# 隐式等待会在每次查找元素时生效，直到元素出现或超时
element = driver.find_element(By.ID, "dynamic_content")
```

---

## 五、JavaScript 处理

### 5.1 执行 JavaScript

```python
# 执行 JavaScript 代码
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 滚动到元素
element = driver.find_element(By.ID, "target")
driver.execute_script("arguments[0].scrollIntoView();", element)

# 获取页面高度
height = driver.execute_script("return document.body.scrollHeight")

# 处理动态加载内容
driver.execute_script("window.scrollBy(0, 500);")

# 等待 JavaScript 执行
driver.set_script_timeout(10)
```

### 5.2 处理动态内容

```python
# 滚动加载
def scroll_to_load(driver, scroll_pause=1):
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# 无限滚动
def infinite_scroll(driver):
    while True:
        # 滚动
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        
        # 检查是否有"加载更多"按钮
        try:
            load_more = driver.find_element(By.XPATH, "//button[contains(text(),'加载更多')]")
            load_more.click()
            time.sleep(2)
        except:
            break
```

### 5.3 处理 Shadow DOM

```python
# Shadow DOM 访问
shadow_host = driver.find_element(By.ID, "shadow_host")
shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
shadow_element = shadow_root.find_element(By.CSS_SELECTOR, "button")

# 嵌套 Shadow DOM
shadow_root1 = driver.execute_script("return arguments[0].shadowRoot", shadow_host1)
shadow_host2 = shadow_root1.find_element(By.CSS_SELECTOR, "#shadow_host2")
shadow_root2 = driver.execute_script("return arguments[0].shadowRoot", shadow_host2)
```

---

## 六、实战案例

### 6.1 登录并抓取数据

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_and_scrape(url, username, password):
    options = Options()
    options.add_argument("--headless")
    
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    try:
        # 等待登录表单加载
        wait = WebDriverWait(driver, 10)
        
        # 输入用户名
        wait.until(EC.presence_of_element_located((By.NAME, "username")))
        driver.find_element(By.NAME, "username").send_keys(username)
        
        # 输入密码
        driver.find_element(By.NAME, "password").send_keys(password)
        
        # 点击登录
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        
        # 等待页面跳转
        wait.until(EC.url_changes(url))
        
        # 抓取数据
        items = []
        elements = driver.find_elements(By.CSS_SELECTOR, ".item")
        for el in elements:
            items.append({
                "title": el.find_element(By.CSS_SELECTOR, ".title").text,
                "price": el.find_element(By.CSS_SELECTOR, ".price").text
            })
        
        return items
    
    finally:
        driver.quit()
```

### 6.2 截图与页面信息

```python
# 截图
driver.save_screenshot("screenshot.png")
driver.find_element(By.ID, "element").screenshot("element.png")

# 获取窗口大小
print(driver.get_window_size())

# 获取当前 URL 和标题
print(driver.current_url)
print(driver.title)

# 前进/后退
driver.back()
driver.forward()
driver.refresh()
```

---

## 七、注意事项

### 7.1 性能优化

```python
# 不要滥用 sleep，使用显式等待
# time.sleep(5)  # ❌ 不好

# WebDriverWait(driver, 10).until(...)  # ✅ 好

# 关闭图片加载（加速）
options.add_experimental_option("prefs", {
    "profile.managed_default_content_settings.images": 2
})
```

### 7.2 异常处理

```python
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException
)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "content"))
    )
except TimeoutException:
    print("等待超时")
except NoSuchElementException:
    print("元素不存在")
```

### 7.3 代理设置

```python
options = Options()
options.add_argument("--proxy-server=http://proxy.example.com:8080")
```

---

## 八、课本重点标注

**《Python编程：从入门到实践》第3版 核心段落：**

| 章节 | 页码 | 重点内容 |
|------|------|----------|
| 15.1 | ~330 | Selenium 基础 |
| 15.2 | ~335 | 元素定位 |
| 15.3 | ~340 | 等待与交互 |

---

## 九、易错点与避坑指南

1. **驱动版本不匹配**：确保 Chrome/Firefox 和驱动版本一致
2. **元素未加载完成**：使用显式等待
3. **iframe 嵌套**：需要先切换到 iframe
4. **动态 ID**：不要依赖动态生成的 ID
5. **隐式等待过长**：会影响所有查找操作

---

## 十、学习成果检验

- [ ] 掌握 Selenium 安装和配置
- [ ] 能使用八种元素定位方式
- [ ] 能进行表单操作和交互
- [ ] 掌握显式等待和隐式等待
- [ ] 能执行 JavaScript 代码
- [ ] 能处理 Shadow DOM
- [ ] 能处理动态加载内容
