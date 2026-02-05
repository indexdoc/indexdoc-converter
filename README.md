<div align="center">
  <strong>简体中文</strong> |  <a href="README_EN.md">English</a>
</div>

---
# indexdoc-converter 文档转换工具库
**indexdoc-converter** 是一款基于 Python 开发的文档转换工具库，核心功能为将主流办公文档、网页文件高效转换为 Markdown 格式。各类型文件支持格式如下：
- Word 文档支持 **.docx** ；
- Excel 类表格文档支持 **.xlsx、.xls、.ods、.csv、.tsv** ；
- 网页文件支持 **.html、.mhtml、.htm 及网页url** ；
- PPT 演示文档支持 **.pptx** 。
该工具库现已发布至 PyPI（Python Package Index），可通过 pip 包管理工具快速安装并投入使用。

[![Python Version](https://img.shields.io/badge/python-3.10+-green.svg)](https://www.python.org/)  [![GitHub Stars](https://img.shields.io/github/stars/indexdoc/indexdoc-converter?style=social)](https://github.com/indexdoc/indexdoc-converter.git)  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


##  库的使用
```bash
#库安装
pip install -U indexdoc-converter #下载最新版本库
```
- 若使用该库 python版本最小应为 Python3.10
- 包目录结构

```bash
indexdoc-converter/          # 项目根目录
├── indexdoc_converter/      # 核心包目录
│   ├── __init__.py          # 核心代码
│   ├── docx_to_md.py        # Word转Markdown工具类
│   ├── excel_to_md.py       # Excel转Markdown工具类
│   ├── html_to_md.py        # Html转Markdown工具类
│   ├── pptx_to_md.py        # ppt转Markdown工具类
│   └── utils/
│       ├── __init__.py
│       ├── FileUtil.py
│       ├── IDUtil.py
│       └── img_to_base64.py
```

### 使用示例

```bash
#引用 注意引用为 indexdoc_converter 而不是 indexdoc-converter
from indexdoc_converter.docx_to_md import convert_docx_to_md
from indexdoc_converter.excel_to_md import TableToMarkdown
from indexdoc_converter.html_to_md import convert_to_md
from indexdoc_converter.pptx_to_md import pptx_to_md

 # -------------------------------------------Word转Markdown---------------------------------------------------
    md_text = convert_docx_to_md(r"C:\Users\xxx\测试文档.docx", False)
    with open('./test.md', 'w', encoding='utf-8') as f:
        f.write(md_text)

# -------------------------------------------Excel转Markdown-------------------------------------------------
    # 自定义参数示例
    converter = TableToMarkdown(
        file_title_level=2,  # 文件标题的Markdown层级，默认1（#），这里设为2（##）
        single_row_value_as_title=True,  # 是否将单行唯一值识别为标题，默认True
        max_rows=8000,  # 最大处理行数，默认6000（实际处理行数是max_rows+1）
        max_cols=200  # 最大处理列数，默认128（实际处理列数是max_cols+1）
    )

    # 转换单个文件
    file_path = r"C:\Users\xxx\测试文件.xlsx"
    result = converter.convert(file_path)

    # blank 模式：保留合并单元格的原始样式（只在合并单元格左上角显示内容，其余位置为空）
    with open("../tmp/测试_blank.md", "w", encoding="utf-8") as f:
        f.write(result['blank'])

   # fill 模式：将合并单元格的内容填充到所有合并的单元格中同时还能自动识别表格中的标题行、分割多个表格块，处理空行 / 空列，兼容各种表格格式的合并单元格解析。
    with open("../tmp/测试_fill.md", "w", encoding="utf-8") as f:
        f.write(result['fill'])

# -------------------------------------------ppt转Markdown---------------------------------------------------
    ppt_file = r"C:\Users\xxx\测试文件.pptx"
    md_path = pptx_to_md(ppt_file)
    print(f"单文件转换完成，MD文件路径：{md_path}")

# -------------------------------------------网页文件转Markdown-----------------------------------------------
    # html = "https://news.qq.com/rain/a/20260114A01NI000"
    html = "https://www.aituple.com"
    # html = "https://www.indexdoc.com"
    # html = r"C:\Users\xxx\测试文件.html"
    # html = "https://www.indexdoc.com/contact.html"
    md = convert_to_md(html, '../tmp/测试html.md')
    # md = mhtml_to_markdown(mhtml)
```
###  Word文档
#### 原文档
![主页1](https://github.com/indexdoc/indexdoc-converter/raw/main/Word1.png)
#### 转换后文档
![主页1](https://github.com/indexdoc/indexdoc-converter/raw/main/Word2.png)

###  Excel文档
#### 原文档
![主页1](https://github.com/indexdoc/indexdoc-converter/raw/main/Excel1.png)
#### 转换后文档
![主页1](https://github.com/indexdoc/indexdoc-converter/raw/main/Excel2.png)

###  ppt文档
#### 原文档
![主页1](https://github.com/indexdoc/indexdoc-converter/raw/main/ppt1.png)
#### 转换后文档
![主页1](https://github.com/indexdoc/indexdoc-converter/raw/main/ppt2.png)

###  网页文件
#### 原文档
![主页1](https://github.com/indexdoc/indexdoc-converter/raw/main/html1.png)
#### 转换后文档
![主页1](https://github.com/indexdoc/indexdoc-converter/raw/main/html2.png)

##  二次开发

- Python 3.10+

```bash
#源码地址
https://github.com/indexdoc/indexdoc-converter.git
```
```bash
#快速安装依赖库
pip install -r requirements.txt

# 阿里镜像源
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```


## 📞 作者

- 作者：杭州智予数信息技术有限公司

- 邮箱：indexdoc@qq.com
