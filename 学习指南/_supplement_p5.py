# -*- coding: utf-8 -*-
"""补全知识库 - 第五批：文件 I/O 进阶 / 系统命令 / 练习题汇总"""
SUPPLEMENT_5 = {

"file_seek": """\
## 一、文件指针（file pointer）

文件对象内部维护一个 **指针**，指向下一个读写位置。

```python
with open("file.txt", "r") as f:
    # 默认从开头
    print(f.tell())            # 0

    content = f.read(5)
    print(f.tell())            # 5（读了 5 个字符）

    f.seek(0)                  # 回到开头
    print(f.tell())            # 0
```

## 二、seek() 详解

```python
f.seek(offset, whence)
# offset：偏移量（字节）
# whence：参考位置
#   0：从文件开头（默认）
#   1：从当前位置
#   2：从文件末尾
```

```python
with open("file.txt", "rb") as f:
    # 从开头偏移
    f.seek(10)                 # 从开头移动 10 字节

    # 从当前位置
    f.seek(5, 1)               # 当前 + 5

    # 从末尾
    f.seek(-5, 2)              # 末尾 - 5（倒数第 5 个字节）

    # 文本模式只支持 whence=0
    # 二进制模式支持 0/1/2
```

## 三、tell() 当前指针位置

```python
with open("file.txt", "r") as f:
    print(f.tell())    # 0
    f.read(10)
    print(f.tell())    # 10
    f.read(5)
    print(f.tell())    # 15
```

## 四、应用：倒序读取

```python
# 倒序读取最后 N 行
def tail(filepath, n=10):
    with open(filepath, "rb") as f:
        # 找到末尾
        f.seek(0, 2)
        size = f.tell()

        # 倒数 n 行大约多少字节（粗略估计）
        block_size = 1024
        lines = []

        while size > 0 and len(lines) <= n:
            read_size = min(block_size, size)
            size -= read_size
            f.seek(size)
            block = f.read(read_size)
            lines = block.decode("utf-8", errors="replace").splitlines() + lines

        return lines[-n:]

print(tail("big.log", 5))
```

## 五、随机访问二进制文件

```python
# 假设有定长记录（如每条 100 字节）
with open("data.bin", "rb") as f:
    # 读第 5 条记录
    record_size = 100
    f.seek(5 * record_size)
    record = f.read(record_size)
```

## 六、文本模式下的换行处理

```python
# 文本模式下，\\r\\n 会被自动转换为 \\n
with open("file.txt", "r") as f:
    content = f.read()
    # Windows 文件读到的是 \\n（统一）

# 想保留原始字节：用二进制模式
with open("file.txt", "rb") as f:
    raw = f.read()
    # Windows: b'...\\r\\n...'
```

## 七、应用：日志文件尾部跟踪

```python
# 像 `tail -f` 一样实时跟踪日志
def follow(filepath):
    with open(filepath, "r") as f:
        f.seek(0, 2)              # 跳到末尾
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line

# 用法
for line in follow("app.log"):
    print(line.rstrip())
```
""",

"venv": """\
## 一、虚拟环境（Virtual Environment）

**虚拟环境**：独立的 Python 环境，每个项目可以有不同版本的库。

## 二、为什么需要虚拟环境

```python
# 项目 A 依赖 requests==2.25.0
# 项目 B 依赖 requests==2.31.0
# 没有虚拟环境 → 冲突！

# 虚拟环境解决：
# /project_a/.venv/  → requests 2.25.0
# /project_b/.venv/  → requests 2.31.0
```

## 三、创建虚拟环境（Python 3.3+）

```bash
# 创建
python -m venv myenv

# 指定 Python 版本
python3.11 -m venv myenv

# 激活（不同系统不同命令）
# Windows (cmd)
myenv\\Scripts\\activate.bat
# Windows (PowerShell)
myenv\\Scripts\\Activate.ps1
# Linux / macOS
source myenv/bin/activate

# 激活后命令行前缀会显示 (myenv)
# (myenv) $ pip install requests

# 退出
deactivate
```

## 四、虚拟环境结构

```
myenv/
├── bin/                  # Linux/Mac 的可执行文件
│   ├── python
│   ├── pip
│   └── activate
├── Scripts/              # Windows 的可执行文件
│   ├── python.exe
│   ├── pip.exe
│   └── activate.bat
├── lib/
│   └── python3.11/
│       └── site-packages/    # 第三方库装这里
└── pyvenv.cfg            # 配置
```

## 五、依赖管理（requirements.txt）

```bash
# 导出依赖
pip freeze > requirements.txt

# 内容示例：
# requests==2.31.0
# urllib3==2.0.7
# certifi==2023.7.22

# 安装依赖
pip install -r requirements.txt
```

## 六、现代化工具（推荐）

### pipenv

```bash
# 安装
pip install pipenv

# 创建虚拟环境 + 安装依赖
pipenv install requests

# 自动生成 Pipfile 和 Pipfile.lock
# 进入环境
pipenv shell
# 运行
pipenv run python script.py
```

### poetry

```bash
# 安装
pip install poetry

# 初始化
poetry init

# 添加依赖
poetry add requests

# 安装所有依赖
poetry install

# 运行
poetry run python script.py
```

### pdm

```bash
# 安装
pip install pdm

# 初始化
pdm init

# 添加依赖
pdm add requests
```

## 七、conda（数据科学常用）

```bash
# 创建
conda create -n myenv python=3.11

# 激活
conda activate myenv

# 安装（conda 源）
conda install numpy pandas matplotlib

# 安装（pip 源）
pip install requests

# 导出
conda env export > environment.yml

# 从文件创建
conda env create -f environment.yml
```

## 八、IDE 集成

### PyCharm

```
Settings → Project → Python Interpreter → 齿轮 → Add → Virtualenv Environment
或 Existing environment → 选择 myenv/Scripts/python.exe
```

### VS Code

```json
// .vscode/settings.json
{
    "python.defaultInterpreterPath": "./myenv/Scripts/python.exe",
    "python.terminal.activateEnvironment": true
}
```

## 九、最佳实践

1. **每个项目一个 venv**：项目根目录 `.venv/`
2. **把 `.venv/` 加进 `.gitignore`**：不提交
3. **提交 `requirements.txt` 或 `pyproject.toml`**：让同事能复现环境
4. **使用工具**：Poetry / PDM 比手动 pip 更现代
5. **定期更新**：每 6 个月升级一次依赖

## 十、Docker（生产级隔离）

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

```bash
docker build -t myapp .
docker run -it myapp python
# 比 venv 更彻底的隔离
```
""",

"os_system": """\
## 一、os.system 执行命令

```python
import os

# 阻塞执行，返回退出码
ret = os.system("ls -la")
print(ret)     # 0 = 成功

# 在 Windows 上
os.system("dir")
```

## 二、subprocess（推荐）

```python
import subprocess

# 1. run（Python 3.5+，最常用）
result = subprocess.run(
    ["ls", "-la"],
    capture_output=True,    # 捕获输出
    text=True,              # 返回字符串而不是 bytes
    timeout=5               # 超时秒数
)
print(result.stdout)        # 标准输出
print(result.stderr)        # 标准错误
print(result.returncode)    # 退出码

# 2. 抛出异常（returncode != 0）
result = subprocess.run(
    ["ls", "/nonexistent"],
    check=True              # 非 0 退出码抛 CalledProcessError
)

# 3. 输入
result = subprocess.run(
    ["grep", "python"],
    input="python is great\\npython rocks\\n",
    capture_output=True,
    text=True
)
print(result.stdout)
```

## 三、os.popen（已废弃，不推荐）

```python
# 旧式 API
output = os.popen("ls -la").read()
```

## 四、shell=True 的风险

```python
import subprocess

# ❌ 危险：命令注入
user_input = "; rm -rf /"
subprocess.run(f"ls {user_input}", shell=True)
# 实际执行：ls ; rm -rf /

# ✅ 安全：传列表
subprocess.run(["ls", user_input], shell=False)
```

## 五、应用案例

```python
import subprocess
import os

# 1. 检查命令是否存在
def command_exists(cmd):
    return subprocess.run(
        ["which", cmd],
        capture_output=True
    ).returncode == 0

# 2. 获取 Git 信息
def git_info():
    result = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        capture_output=True,
        text=True,
        cwd="/path/to/repo"
    )
    return result.stdout.strip()

# 3. 实时流式输出
def run_with_stream(cmd):
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )
    for line in process.stdout:
        print(line, end="")
    process.wait()

# 4. 后台运行
process = subprocess.Popen(
    ["python", "server.py"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    stdin=subprocess.DEVNULL
)
print(f"PID: {process.pid}")
```

## 六、shlex（安全分割命令）

```python
import shlex

# 安全地分割 shell 命令
cmd_str = "ls -la /tmp"
cmd_list = shlex.split(cmd_str)
# ['ls', '-la', '/tmp']

# 处理带空格的文件名
cmd_str = 'cp "my file.txt" /backup/'
cmd_list = shlex.split(cmd_str)
# ['cp', 'my file.txt', '/backup/']
```

## 七、os 模块的系统信息

```python
import os

# CPU 数
os.cpu_count()

# 负载（Unix）
os.getloadavg()

# 当前用户
os.getlogin()
os.getuid()

# 路径分隔符
os.sep            # '/' 或 '\\'
os.extsep         # '.'
os.linesep        # '\\n' 或 '\\r\\n'
os.pathsep        # ':' 或 ';'

# 环境变量
os.environ
os.environb       # bytes 形式

# 磁盘空间
os.statvfs("/") if hasattr(os, "statvfs") else None

# 路径展开
os.path.expanduser("~")
os.path.expandvars("$HOME")
```
""",

"shutil": """\
## 一、shutil 模块（高级文件操作）

```python
import shutil

# 1. 复制文件
shutil.copy("src.txt", "dst.txt")          # 复制 + 权限
shutil.copy2("src.txt", "dst.txt")         # 复制 + 权限 + 元数据（修改时间等）
shutil.copyfile("src.txt", "dst.txt")      # 仅复制内容

# 2. 复制目录
shutil.copytree("src_dir", "dst_dir")      # 递归复制

# 3. 移动 / 重命名
shutil.move("src.txt", "dst.txt")

# 4. 删除目录
shutil.rmtree("dir")                       # 递归删除（慎用！）

# 5. 磁盘使用
total, used, free = shutil.disk_usage("/")
print(f"总：{total // 2**30} GB, 已用：{used // 2**30} GB, 可用：{free // 2**30} GB")
```

## 二、复制函数对比

```python
import shutil

# copyfile vs copy vs copy2
shutil.copyfile("a.txt", "b.txt")  # 仅内容，不保留权限
shutil.copy("a.txt", "b.txt")      # 内容 + 权限
shutil.copy2("a.txt", "b.txt")     # 内容 + 权限 + 元数据（时间戳等）
```

## 三、ignore 模式

```python
import shutil

# 复制时跳过某些文件
def ignore_pyc(dir, files):
    return [f for f in files if f.endswith(".pyc")]

shutil.copytree("src", "dst", ignore=ignore_pyc)

# 用 shutil.ignore_patterns
shutil.copytree("src", "dst", ignore=shutil.ignore_patterns("*.pyc", "__pycache__", ".git"))
```

## 四、压缩与解压

```python
import shutil

# 1. make_archive：创建压缩包
shutil.make_archive(
    "backup",
    "zip",                  # 格式：zip / tar / gztar / bztar / xztar
    root_dir="project",
    base_dir="."
)
# 生成 backup.zip

# 2. unpack_archive：解压
shutil.unpack_archive("backup.zip", "extracted_dir")
```

## 五、which / get_terminal_size

```python
import shutil

# 查找可执行文件
shutil.which("python")
# 'C:\\Python311\\python.exe' 或 '/usr/bin/python'

shutil.which("nonexistent")
# None

# 终端尺寸
cols, rows = shutil.get_terminal_size((80, 24))
print(f"终端：{cols}x{rows}")
```

## 六、chown（修改所有者）

```python
import shutil

# 修改文件所有者（需要 root）
shutil.chown("file.txt", user="alice", group="alice")

# 递归修改
shutil.chown("dir", user="alice", group="alice")
```

## 七、应用：备份脚本

```python
import shutil
import os
from datetime import datetime

def backup(src_dir, backup_dir):
    """增量备份目录"""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # 备份名带时间戳
    name = f"backup_{datetime.now():%Y%m%d_%H%M%S}"
    archive_path = os.path.join(backup_dir, name)

    # 创建压缩包
    shutil.make_archive(archive_path, "zip", root_dir=src_dir)

    # 清理旧备份（保留最近 7 个）
    backups = sorted(os.listdir(backup_dir))
    while len(backups) > 7:
        old = backups.pop(0)
        os.remove(os.path.join(backup_dir, old))

    return archive_path

print(backup("./data", "./backups"))
```
""",

"zipfile": """\
## 一、zipfile 模块

```python
import zipfile

# 1. 读取 zip
with zipfile.ZipFile("archive.zip", "r") as zf:
    # 列出所有文件
    print(zf.namelist())
    # ['file1.txt', 'subdir/file2.py', ...]

    # 文件信息
    for info in zf.infolist():
        print(f"{info.filename}: {info.file_size} bytes, 压缩 {info.compress_size}")

    # 读取单个文件
    content = zf.read("file1.txt")
    print(content.decode())

    # 解压全部
    zf.extractall("extracted_dir")

    # 解压单个文件
    zf.extract("file1.txt", "output_dir")
```

## 二、创建 zip

```python
import zipfile

# 1. 写入文件
with zipfile.ZipFile("new.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    zf.write("file1.txt")                        # 文件
    zf.write("subdir/file2.py")                  # 保留目录结构
    zf.write("README.md", arcname="docs/README.md")  # 重命名
    zf.writestr("hello.txt", "Hello, World!")    # 直接写入字符串

# 2. 追加
with zipfile.ZipFile("existing.zip", "a") as zf:
    zf.write("new_file.txt")

# 3. 多个文件
import os
files_to_zip = ["file1.txt", "file2.txt", "subdir/file3.py"]
with zipfile.ZipFile("batch.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    for file in files_to_zip:
        if os.path.exists(file):
            zf.write(file)
```

## 三、tarfile 模块

```python
import tarfile

# 创建 tar
with tarfile.open("archive.tar.gz", "w:gz") as tf:
    tf.add("file1.txt")
    tf.add("subdir/")

# 列出
with tarfile.open("archive.tar.gz", "r:gz") as tf:
    for member in tf.getmembers():
        print(member.name, member.size)

    # 解压
    tf.extractall("output_dir")
```

## 四、压缩格式对比

| 格式 | 压缩比 | 速度 | 跨平台 | 标准库 |
|------|--------|------|--------|--------|
| zip | 中 | 快 | ✅ | ✅ |
| gzip | 中 | 中 | ✅ | ✅（tar） |
| bz2 | 高 | 慢 | ✅ | ✅（tar） |
| xz | 很高 | 很慢 | ✅ | ✅（tar） |
| 7z | 高 | 中 | 需装 | ❌ |

## 五、加密 ZIP

```python
import zipfile

# 标准库 zipfile 不支持强加密（AES）
# 创建密码保护的 zip（zip 标准弱加密）
with zipfile.ZipFile("encrypted.zip", "w") as zf:
    zf.setpassword(b"my_password")        # 需要时设置密码
    zf.writestr("secret.txt", "机密数据")

# 读取
with zipfile.ZipFile("encrypted.zip", "r") as zf:
    zf.setpassword(b"my_password")
    print(zf.read("secret.txt").decode())

# 强加密：用 pyzipper 库
# pip install pyzipper
```

## 六、压缩整个目录

```python
import zipfile
import os

def zip_directory(src_dir, zip_path):
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, start=os.path.dirname(src_dir))
                zf.write(filepath, arcname)

zip_directory("./myproject", "./backup.zip")
```

## 七、查看压缩包内容（不解压）

```python
import zipfile

with zipfile.ZipFile("archive.zip", "r") as zf:
    # 仅打印文件名
    for name in zf.namelist():
        print(name)

    # 检查文件是否存在
    if "specific.txt" in zf.namelist():
        print("specific.txt 在压缩包里")
```

## 八、应用：解压特定类型

```python
import zipfile
import os

def extract_text_files(zip_path, output_dir):
    """只解压 .txt 文件"""
    with zipfile.ZipFile(zip_path, "r") as zf:
        for name in zf.namelist():
            if name.endswith(".txt") and not name.endswith("/"):
                zf.extract(name, output_dir)
                print(f"解压：{name}")
```
""",

"subprocess": """\
## 一、subprocess 模块

```python
import subprocess

# 1. run（最常用，Python 3.5+）
result = subprocess.run(
    ["ls", "-la"],
    capture_output=True,
    text=True,
    timeout=10
)
print(result.stdout)
print(result.stderr)
print(result.returncode)
```

## 二、捕获输出

```python
import subprocess

# capture_output=True：捕获 stdout 和 stderr
result = subprocess.run(["ls"], capture_output=True, text=True)
print("stdout:", result.stdout)
print("stderr:", result.stderr)

# 只重定向 stdout
result = subprocess.run(
    ["ls"],
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL,    # 丢弃
    text=True
)
```

## 三、传递输入

```python
import subprocess

# 方式 1：字符串
result = subprocess.run(
    ["grep", "python"],
    input="python is great\\npython rocks\\n",
    capture_output=True,
    text=True
)
print(result.stdout)
# python is great
# python rocks

# 方式 2：bytes
result = subprocess.run(
    ["xxd"],
    input=b"hello",
    capture_output=True
)
```

## 四、超时

```python
import subprocess

try:
    result = subprocess.run(
        ["sleep", "10"],
        timeout=3
    )
except subprocess.TimeoutExpired as e:
    print(f"超时：{e}")

# ⚠️ 注意：timeout 不会杀掉子进程（在 Unix 上）
# 想强制杀：用 Popen + kill
```

## 五、检查返回码

```python
import subprocess

# check=True：非 0 退出码抛异常
try:
    result = subprocess.run(
        ["ls", "/nonexistent"],
        capture_output=True,
        check=True
    )
except subprocess.CalledProcessError as e:
    print(f"失败：{e}")
    print(f"返回码：{e.returncode}")
    print(f"stderr：{e.stderr.decode()}")
```

## 六、Popen（高级）

```python
import subprocess

# 实时流式输出
def run_with_live_output(cmd):
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,    # 合并到 stdout
        text=True,
        bufsize=1                    # 行缓冲
    )
    for line in process.stdout:
        print(line, end="")
    ret = process.wait()
    print(f"返回码：{ret}")

run_with_live_output(["ping", "-n", "3", "127.0.0.1"])

# 后台运行
process = subprocess.Popen(
    ["python", "server.py"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    stdin=subprocess.DEVNULL
)
print(f"后台进程 PID：{process.pid}")

# 终止
process.terminate()          # SIGTERM
process.kill()              # SIGKILL
process.wait()              # 等待结束
```

## 七、环境变量

```python
import subprocess
import os

# 继承 + 添加
env = os.environ.copy()
env["MY_VAR"] = "value"

result = subprocess.run(
    ["python", "-c", "import os; print(os.environ.get('MY_VAR'))"],
    env=env,
    capture_output=True,
    text=True
)
print(result.stdout)    # "value"

# 不继承父进程环境
result = subprocess.run(
    ["printenv"],
    env={"ONLY_THIS": "yes"},
    capture_output=True,
    text=True
)
print(result.stdout)    # ONLY_THIS=yes
```

## 八、工作目录

```python
import subprocess

# 在指定目录执行
result = subprocess.run(
    ["ls"],
    cwd="/tmp",
    capture_output=True,
    text=True
)
print(result.stdout)
```

## 九、应用案例

```python
import subprocess

# 1. Git 操作
def git_status():
    return subprocess.run(
        ["git", "status", "--short"],
        capture_output=True,
        text=True,
        cwd="."
    ).stdout

# 2. 文件转换（用外部工具）
def convert_image(input_file, output_file):
    subprocess.run(
        ["ffmpeg", "-i", input_file, output_file],
        check=True
    )

# 3. 并行执行
processes = [
    subprocess.Popen(["cmd1"]),
    subprocess.Popen(["cmd2"]),
]
for p in processes:
    p.wait()

# 4. Shell 管道
result = subprocess.run(
    "ls | grep .py | wc -l",
    shell=True,
    capture_output=True,
    text=True
)
print(f"Python 文件数：{result.stdout.strip()}")
# ⚠️ 注意 shell=True 的安全风险
```

## 十、安全注意事项

```python
import subprocess

# ❌ 危险
user_input = input("文件名：")
subprocess.run(f"rm {user_input}", shell=True)
# 用户输入 "; rm -rf /" → rm ; rm -rf /

# ✅ 安全
subprocess.run(["rm", user_input], shell=False)
# 传列表，不会被 shell 解析

# ✅ 进一步过滤
import re
if not re.match(r"^[a-zA-Z0-9._-]+$", user_input):
    raise ValueError("非法文件名")
subprocess.run(["rm", user_input])
```
""",

"exercise_basic_1": """\
## 一、第 1-2 章练习（环境/变量/字符串/数）

### 1-1. python.org

**题目**：浏览 Python 主页（python.org），找到标题 "The Python Tutorial" 的页面，记录它的 URL。

**答案**：https://docs.python.org/3/tutorial/

### 1-2. 输入字符串

```python
# hello_world.py
print("Hello Python world!")
```

### 1-3. 无穷的技能

**题目**：如果你有无限的时间和精力，你想做什么？

**参考答案**：学习机器学习并用它做医学诊断；写一个改变世界的开源软件；环游世界并把每个地方编程。

### 2-3. 个性化消息

```python
name = "Alice"
print(f"Hello {name}, would you like to learn some Python today?")
```

### 2-4. 调整名字的大小写

```python
name = "aLiCe smITh"
print(name.lower())       # alice smith
print(name.upper())       # ALICE SMITH
print(name.title())       # Alice Smith
```

### 2-5. 名言

```python
quote = '"Whether you think you can, or you think you can\'t -- you\'re right."'
print(f"Henry Ford once said, {quote}")
```

### 2-6. 名言 2

```python
famous_person = "Albert Einstein"
message = '"A person who never made a mistake never tried anything new."'
print(f"{famous_person} once said, {message}")
```

### 2-7. 名字中的空白

```python
name = "  \\tAlice\\nSmith  "
print(f"原：'{name}'")
print(f"lstrip：'{name.lstrip()}'")
print(f"rstrip：'{name.rstrip()}'")
print(f"strip：'{name.strip()}'")
```

### 2-8. 数字 8

```python
print(5 + 3)          # 8
print(10 - 2)         # 8
print(2 * 4)          # 8
print(16 / 2)         # 8.0
print(16 // 2)        # 8（整除）
```

### 2-9. 最喜欢的数字

```python
favorite = 7
print(f"My favorite number is {favorite}.")
```

### 3-4 / 3-5 / 3-6 / 3-7 嘉宾名单（详见第 3 章练习）

```python
guests = ["张三", "李四", "王五"]
for g in guests:
    print(f"亲爱的 {g}, 诚邀您参加晚宴。")
```

## 二、第 3-4 章练习（列表/操作列表）

### 3-1. 姓名

```python
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(name)
```

### 3-2. 问候语

```python
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(f"Hello, {name}!")
```

### 3-3. 自己的列表

```python
transportation = ["Honda motorcycle", "Tesla car", "Bicycle"]
for t in transportation:
    print(f"I would like to own a {t}.")
```

### 4-1. 比萨

```python
pizzas = ["Margherita", "Pepperoni", "Hawaiian"]
for p in pizzas:
    print(f"I like {p} pizza.")
print("I really love pizza!")
```

### 4-2. 动物

```python
animals = ["dog", "cat", "rabbit"]
for a in animals:
    print(f"A {a} would make a great pet.")
print("Any of these animals would make a great pet!")
```

### 4-3. 数到 20

```python
for i in range(1, 21):
    print(i)
```

### 4-4. 一百万

```python
nums = list(range(1, 1_000_001))
print(min(nums))          # 1
print(max(nums))          # 1000000
print(sum(nums))          # 500000500000
```

### 4-5. 一百万求和（计算耗时）

```python
import time
start = time.time()
nums = list(range(1, 1_000_001))
total = sum(nums)
print(f"耗时：{time.time() - start:.3f}s")
```

### 4-6. 奇数

```python
odds = list(range(1, 21, 2))
for n in odds:
    print(n)
```

### 4-7. 3 的倍数

```python
nums = list(range(3, 31, 3))
for n in nums:
    print(n)
```

### 4-8 / 4-9. 立方

```python
cubes = [n**3 for n in range(1, 11)]
for c in cubes:
    print(c)
```

### 4-10. 切片

```python
cubes = [n**3 for n in range(1, 11)]
print("前 3 个：", cubes[:3])
print("中间 3 个：", cubes[4:7])
print("后 3 个：", cubes[-3:])
```

### 4-11. 你的比萨，我的比萨

```python
my_pizzas = ["Margherita", "Pepperoni"]
friend_pizzas = my_pizzas[:]    # 复制而非引用

my_pizzas.append("Hawaiian")
friend_pizzas.append("Vegetarian")

print("My favorite pizzas:")
for p in my_pizzas:
    print(f"- {p}")

print("Friend's favorite pizzas:")
for p in friend_pizzas:
    print(f"- {p}")
```

### 4-13. 自助餐

```python
foods = ("rice", "noodles", "dumplings", "soup", "salad")
for f in foods:
    print(f)
# foods[0] = "bread"     # ❌ 元组不可变
foods = ("bread", "cake") + foods[2:]    # 重新赋值
for f in foods:
    print(f)
```

## 三、第 5-6 章练习（if / 字典）

### 5-1. 条件测试

```python
car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\\nIs car == 'audi'? I predict False.")
print(car == "audi")
```

### 5-3. 外星人颜色

```python
alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points!")
```

### 5-6. 人生阶段

```python
age = 25
if age < 2:
    stage = "婴儿"
elif age < 4:
    stage = "幼儿"
elif age < 13:
    stage = "儿童"
elif age < 20:
    stage = "青少年"
elif age < 65:
    stage = "成年人"
else:
    stage = "老年人"
print(f"你是{stage}。")
```

### 5-8 / 5-9. 用户名管理

```python
usernames = ["admin", "alice", "bob", "charlie", "david"]

for name in usernames:
    if name == "admin":
        print(f"Hello {name}, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")
```

### 6-1. 人

```python
person = {"first_name": "Alice", "last_name": "Smith", "age": 25, "city": "Beijing"}
print(f"{person['first_name']} {person['last_name']}, {person['age']}岁, 来自{person['city']}")
```

### 6-5. 河流

```python
rivers = {"nile": "egypt", "yangtze": "china", "amazon": "brazil"}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
```

### 6-7. 人

```python
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35},
]
for p in people:
    print(f"{p['name']} is {p['age']} years old.")
```

### 6-10. 喜欢的数字

```python
favorite_numbers = {
    "Alice": [3, 7, 42],
    "Bob": [11, 22],
    "Charlie": [99, 1],
}
for name, nums in favorite_numbers.items():
    print(f"{name} 喜欢的数字：{nums}")
```

## 四、第 7 章练习（用户输入/while）

### 7-1. 租车

```python
car = input("What kind of car would you like? ")
print(f"Let me see if I can find you a {car}.")
```

### 7-2. 餐厅订位

```python
party_size = int(input("How many people are in your party? "))
if party_size > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")
```

### 7-4. 比萨配料

```python
prompt = "Enter pizza toppings (type 'quit' to finish): "
while True:
    topping = input(prompt)
    if topping == "quit":
        break
    print(f"Adding {topping} to your pizza.")
```

### 7-5. 电影票

```python
while True:
    age = input("Enter your age (or 'quit'): ")
    if age == "quit":
        break
    age = int(age)
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15
    print(f"Your ticket costs ${price}.")
```

### 7-8. 熟食店

```python
sandwich_orders = ["tuna", "ham", "pastrami", "turkey", "roast beef"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\\nAll sandwiches:")
for s in finished_sandwiches:
    print(f"- {s}")
```
""",

"exercise_basic_2": """\
## 一、第 8 章练习（函数）

### 8-1. 消息

```python
def display_message():
    print("本章学习函数。")

display_message()
```

### 8-2. 喜欢的图书

```python
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Alice in Wonderland")
```

### 8-3. T 恤

```python
def make_shirt(size, message):
    print(f"Making a {size} shirt with message: {message}")

make_shirt("L", "I love Python")
make_shirt(size="M", message="Hello")
```

### 8-5. 城市

```python
def describe_city(city, country="China"):
    print(f"{city} is in {country}.")

describe_city("Beijing")
describe_city("Reykjavik", country="Iceland")
```

### 8-6. 城市名

```python
def city_country(city, country):
    return f"{city.title()}, {country.title()}"

print(city_country("beijing", "china"))
print(city_country("santiago", "chile"))
print(city_country("tokyo", "japan"))
```

### 8-7. 专辑

```python
def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs:
        album["songs"] = songs
    return album

print(make_album("Beatles", "Abbey Road"))
print(make_album("Pink Floyd", "The Wall", songs=26))
```

### 8-9. 魔术师

```python
magicians = ["Alice", "Bob", "Charlie"]

def show_magicians(magicians):
    for m in magicians:
        print(m)

def make_great(magicians):
    for i, m in enumerate(magicians):
        magicians[i] = f"The Great {m}"

make_great(magicians)
show_magicians(magicians)
```

### 8-12. 三明治

```python
def make_sandwich(*items):
    print("Making sandwich with:")
    for item in items:
        print(f"- {item}")

make_sandwich("ham", "cheese")
make_sandwich("turkey", "lettuce", "tomato")
```

### 8-14. 汽车

```python
def make_car(manufacturer, model, **kwargs):
    kwargs["manufacturer"] = manufacturer
    kwargs["model"] = model
    return kwargs

car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)
```

## 二、第 9 章练习（类）

### 9-1. 餐厅

```python
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe(self):
        print(f"{self.name} serves {self.cuisine} cuisine.")

    def open(self):
        print(f"{self.name} is now open!")

    def set_number_served(self, n):
        self.number_served = n

    def increment_number_served(self, n):
        self.number_served += n

r = Restaurant("Beijing Dumpling", "Chinese")
r.describe()
r.open()
r.set_number_served(50)
print(f"Served: {r.number_served}")
```

### 9-3. 用户

```python
class User:
    def __init__(self, first, last, age, location):
        self.first = first
        self.last = last
        self.age = age
        self.location = location

    def describe(self):
        print(f"{self.first} {self.last}, {self.age}, from {self.location}")

    def greet(self):
        print(f"Hello, {self.first}!")

u = User("Alice", "Smith", 25, "Beijing")
u.describe()
u.greet()
```

### 9-4. 就餐人数

```python
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe(self):
        print(f"{self.name} serves {self.cuisine}.")

    def set_number_served(self, n):
        self.number_served = n

    def increment_number_served(self, n):
        self.number_served += n

# 测试
r = Restaurant("test", "test")
r.number_served = 100    # 直接修改
print(r.number_served)   # 100
r.increment_number_served(50)
print(r.number_served)   # 150
```

### 9-6. 冰淇淋小店

```python
class IceCreamStand(Restaurant):
    def __init__(self, name, flavors):
        super().__init__(name, "ice cream")
        self.flavors = flavors

    def show_flavors(self):
        print(f"{self.name} has these flavors:")
        for f in self.flavors:
            print(f"- {f}")

i = IceCreamStand("Cold Stone", ["vanilla", "chocolate", "strawberry"])
i.show_flavors()
```

### 9-9. 电池升级

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

class Battery:
    def __init__(self, size=75):
        self.size = size

    def describe(self):
        print(f"This car has a {self.size}-kWh battery.")

    def get_range(self):
        if self.size <= 75:
            range_miles = 260
        elif self.size <= 100:
            range_miles = 315
        else:
            range_miles = 500
        print(f"Range: {range_miles} miles")

    def upgrade_battery(self):
        if self.size < 100:
            self.size = 100

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

e = ElectricCar("Tesla", "Model S", 2024)
e.battery.describe()
e.battery.get_range()
e.battery.upgrade_battery()
e.battery.describe()
e.battery.get_range()
```

### 9-12. 多个模块

```python
# admin.py
class User:
    pass

class Admin(User):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.privileges = ["can add post", "can delete post"]

    def show_privileges(self):
        print("Privileges:")
        for p in self.privileges:
            print(f"- {p}")
```

### 9-13. 骰子

```python
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

d6 = Die()
results = [d6.roll() for _ in range(10)]
print("10 次掷骰：", results)

d10 = Die(10)
print("d10:", d10.roll())
```

## 三、第 10 章练习（文件/异常）

### 10-1. 学习 Python

```python
with open("learning_python.txt") as f:
    content = f.read()
print(content)
```

### 10-3. 访客

```python
filename = "guest.txt"
with open(filename, "w") as f:
    while True:
        name = input("Enter name (or 'quit'): ")
        if name == "quit":
            break
        f.write(f"{name}\\n")
```

### 10-4. 访客名单

```python
filename = "guest_book.txt"
with open(filename, "a") as f:
    while True:
        name = input("Enter name (or 'quit'): ")
        if name == "quit":
            break
        print(f"Hello {name}, you've been added to the guest book.")
        f.write(f"{name}\\n")
```

### 10-6. 加法运算

```python
try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    print(f"Sum: {a + b}")
except ValueError:
    print("Please enter valid numbers.")
```

### 10-8. 猫和狗

```python
def read_file(filename):
    try:
        with open(filename) as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Sorry, {filename} does not exist.")

read_file("cats.txt")
read_file("dogs.txt")
```

### 10-10. 常见单词

```python
def count_word(filename, word):
    try:
        with open(filename, encoding="utf-8") as f:
            content = f.read()
        return content.lower().count(word.lower())
    except FileNotFoundError:
        print(f"{filename} not found.")
        return 0

print(count_word("alice.txt", "the"))
```

### 10-11. 喜欢的数字

```python
import json

num = input("What's your favorite number? ")
with open("favorite_number.json", "w") as f:
    json.dump(num, f)

# 读取
with open("favorite_number.json") as f:
    print(f"I know your favorite number! It's {json.load(f)}.")
```

### 10-13. 用户字典

```python
import json

def get_stored_username():
    try:
        with open("username.json") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def get_new_username():
    return input("What is your name? ")

def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        with open("username.json", "w") as f:
            json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
```

## 四、第 11 章练习（测试）

### 11-1. 城市函数

```python
# city_functions.py
def city_country(city, country, population=None):
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    return f"{city.title()}, {country.title()}"
```

```python
# test_cities.py
import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")

    def test_city_country_population(self):
        result = city_country("santiago", "chile", 5000000)
        self.assertEqual(result, "Santiago, Chile - population 5000000")

if __name__ == "__main__":
    unittest.main()
```

### 11-3. 雇员

```python
class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount
```

```python
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = Employee("Alice", "Smith", 50000)

    def test_give_default_raise(self):
        self.emp.give_raise()
        self.assertEqual(self.emp.salary, 55000)

    def test_give_custom_raise(self):
        self.emp.give_raise(10000)
        self.assertEqual(self.emp.salary, 60000)

if __name__ == "__main__":
    unittest.main()
```
""",

"exercise_project": """\
## 一、第 12-14 章项目（外星人入侵）

### 12-1. 蓝色天空

```python
import sys
import pygame

class SkyGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Blue Sky")
        self.bg_color = (135, 206, 235)    # 天蓝色

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == "__main__":
    SkyGame().run()
```

### 12-2. 游戏角色

```python
import sys
import pygame

class GameCharacter:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.bg_color = (135, 206, 235)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            # 在屏幕中央画一个红色方块
            pygame.draw.rect(self.screen, (255, 0, 0), (380, 280, 40, 40))
            pygame.display.flip()

GameCharacter().run()
```

### 12-3 / 12-4. 火箭

```python
# rocket_game.py
import sys
import pygame

class Rocket:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("rocket.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Rocket")
        self.bg_color = (135, 206, 235)
        self.rocket = Rocket(self.screen)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.rocket.blitme()
            pygame.display.flip()

if __name__ == "__main__":
    Game().run()
```

### 13-1 / 13-2. 星星

```python
import sys
import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("star.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

class StarGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.bg_color = (0, 0, 30)
        self.stars = pygame.sprite.Group()

        star = Star(self.screen)
        star.rect.x = star.rect.width
        star.rect.y = star.rect.height
        self.stars.add(star)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.stars.draw(self.screen)
            pygame.display.flip()

StarGame().run()
```

## 二、第 15-17 章项目（数据可视化）

### 15-1 / 15-2. 立方

```python
import matplotlib.pyplot as plt

x = range(1, 6)
y = [n**3 for n in x]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(x, y, s=40)

ax.set_title("Cubes", fontsize=20)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
ax.tick_params(labelsize=10)

plt.show()
```

### 15-3 / 15-4. 随机漫步

```python
import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self._get_step()
            y_step = self._get_step()
            if x_step == 0 and y_step == 0:
                continue
            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)

    def _get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

rw = RandomWalk()
rw.fill_walk()

plt.style.use("classic")
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15, c=range(rw.num_points), cmap=plt.cm.Blues)
ax.scatter(0, 0, c="green", s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", s=100)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()
```

### 15-5. 反射

```python
# 改进：去掉坐标轴、突出起终点
# （在 15-4 基础上）
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
```

### 15-7. 两个 D8

```python
import plotly.express as px
import pandas as pd

results = []
for _ in range(1000):
    roll1 = randint(1, 8)
    roll2 = randint(1, 8)
    results.append(roll1 + roll2)

frequencies = [(value, results.count(value)) for value in range(2, 17)]

df = pd.DataFrame(frequencies, columns=["Result", "Frequency"])
fig = px.bar(df, x="Result", y="Frequency", title="两个 D8 掷骰结果分布（1000 次）")
fig.show()
```

### 16-1. 死亡谷

```python
import csv

filename = "data/death_valley_2021_full.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            high = int(row[header_row.index("TMAX")])
            low = int(row[header_row.index("TMIN")])
        except ValueError:
            continue
        dates.append(row[header_row.index("DATE")])
        highs.append(high)
        lows.append(low)

import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
ax.set_title("Death Valley Daily Temperatures, 2021", fontsize=20)
fig.autofmt_xdate()
plt.show()
```

### 16-6. 世界地震

```python
import json
import plotly.express as px

# 读取数据
with open("data/eq_data_30_day_m1.json") as f:
    data = json.load(f)

mags, lons, lats, names = [], [], [], []
for feature in data["features"]:
    mags.append(feature["properties"]["mag"])
    lons.append(feature["geometry"]["coordinates"][0])
    lats.append(feature["geometry"]["coordinates"][1])
    names.append(feature["properties"]["title"])

fig = px.scatter_geo(
    lat=lats, lon=lons, size=mags, title="全球地震分布",
    color=mags, color_continuous_scale="Viridis",
    labels={"color": "震级"}
)
fig.show()
```

### 17-1. python_repos

```python
import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status: {r.status_code}")
response_dict = r.json()

repo_dicts = response_dict["items"]
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

import plotly.express as px
fig = px.bar(x=repo_names, y=stars, labels={"x": "Repository", "y": "Stars"})
fig.show()
```

## 三、第 18-20 章项目（学习笔记）

### 18-1 / 18-2. 新项目

```bash
# 创建虚拟环境
python -m venv ll_env
source llenv/Scripts/activate   # Windows
# 或 source ll_env/bin/activate  # Linux/macOS

pip install django
django-admin startproject learning_log .
python manage.py migrate
python manage.py runserver
```

### 18-5. 拓展模板

```python
# learning_logs/models.py
from django.db import models

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"
```

### 18-6 / 18-7. 模板

```html
<!-- learning_logs/templates/learning_logs/topic.html -->
{% extends "learning_logs/base.html" %}

{% block content %}
<p>Topic: {{ topic }}</p>
<ul>
  {% for entry in entries %}
    <li><p>{{ entry.date_added|date:'M d, Y H:i' }}</p>
        <p>{{ entry.text|linebreaks }}</p>
    </li>
  {% empty %}
    <li>There are no entries for this topic yet.</li>
  {% endfor %}
</ul>
{% endblock content %}
```

### 19-1 / 19-2. 用户注册

```python
# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("learning_logs:index")

    context = {"form": form}
    return render(request, "registration/register.html", context)
```

### 20-1. 其他设置

```python
# learning_log/settings.py
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "learning_logs",
    "users",
]
```

### 20-4. 部署到 Heroku

```bash
# 安装工具
pip install gunicorn django-heroku
pip freeze > requirements.txt

# 创建 Procfile
web: gunicorn learning_log.wsgi

# 创建 runtime.txt
python-3.11.5

# 设置环境变量
heroku config:set DJANGO_SECRET_KEY=xxx
heroku config:set DJANGO_DEBUG=False

# 部署
git push heroku main
heroku run python manage.py migrate
```

## 四、综合项目：待办事项应用（CLI 版）

```python
import json
import os

TODO_FILE = "todos.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE) as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)

def add_todo(text):
    todos = load_todos()
    todos.append({"id": len(todos) + 1, "text": text, "done": False})
    save_todos(todos)
    print(f"✓ Added: {text}")

def list_todos():
    todos = load_todos()
    if not todos:
        print("No todos!")
        return
    for t in todos:
        status = "[x]" if t["done"] else "[ ]"
        print(f"{t['id']}. {status} {t['text']}")

def complete_todo(todo_id):
    todos = load_todos()
    for t in todos:
        if t["id"] == todo_id:
            t["done"] = True
            save_todos(todos)
            print(f"✓ Completed: {t['text']}")
            return
    print(f"Todo #{todo_id} not found")

def delete_todo(todo_id):
    todos = load_todos()
    todos = [t for t in todos if t["id"] != todo_id]
    save_todos(todos)
    print(f"✓ Deleted todo #{todo_id}")

def main():
    while True:
        print("\\n--- Todo App ---")
        print("1. Add  2. List  3. Complete  4. Delete  5. Quit")
        choice = input("Choice: ")
        if choice == "1":
            text = input("Todo text: ")
            add_todo(text)
        elif choice == "2":
            list_todos()
        elif choice == "3":
            tid = int(input("Todo ID: "))
            complete_todo(tid)
        elif choice == "4":
            tid = int(input("Todo ID: "))
            delete_todo(tid)
        elif choice == "5":
            break

if __name__ == "__main__":
    main()
```
""",

}