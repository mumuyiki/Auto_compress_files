
# 🗄️ Auto_compress_files

一个基于 **Python** 的小工具，可以将 **任意文件** 打包为单个大小不超过1g的zip文件
支持几乎所有文件格式

---

## 🤷‍♂️ 这个脚本有什么用？

一些聊天软件 不支持发送1g以上的文件 使用它可以拆分为很多小压缩包

## 🤷‍♂️ 为什么不用分卷压缩

不得不承认 分卷压缩在大部分场景下是最优解 但大部分小白并不知道什么是分卷压缩 很多小白连目录的概念都不清楚 与其让他们下载压缩包 放到同一目录下解压 不如告诉他们 分别打开 然后分别解压

---


## ⚙️ 使用方法

1. 使用你喜欢的编辑器打开 `Auto_compress_files.py`
2. 修改脚本开头的 **配置项**：
3. 关于 **”核心数设定“** 根据你cpu的核心来填写就好 例如i5-12400 是6个P核 0个E核 就填写6 

   ```python
   # 配置项
   source_dir = r"C:\Users\xuan\Desktop\file" #原目录
   output_dir = r"C:\Users\xuan\Desktop\zipfiles" #输出目录
   max_size = 1024 * 1024 * 1024  # 每个ZIP最大1GB
   num_workers = 6  # 核心数设定
   ```
4. 保存后运行脚本：

   ```bash
   python Auto_compress_files.py
   ```
