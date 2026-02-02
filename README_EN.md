markdown
<div align="center">
  <strong>English</strong> | <a href="README.md">简体中文</a>
</div>

---
# indexdoc-converter Document Conversion Library
**indexdoc-converter** is a Python-based document conversion library, designed to efficiently convert mainstream office documents and web files into Markdown format. It supports the following file types:
- Word documents: **.docx**
- Spreadsheets: **.xlsx, .xls, .ods, .csv, .tsv**
- Web files: **.html, .mhtml, .htm** and web URLs
- PowerPoint presentations: **.pptx**

This library has been published on PyPI (Python Package Index) and can be quickly installed and used via the pip package manager.

[![Python Version](https://img.shields.io/badge/python-3.10+-green.svg)](https://www.python.org/)
[![GitHub Stars](https://img.shields.io/github/stars/indexdoc/indexdoc-converter?style=social)](https://github.com/indexdoc/indexdoc-converter.git)

## Usage
```bash
# Install the library
pip install -U indexdoc-converter # Install the latest version
```
- Minimum Python version required: **Python 3.10**

### Package Structure
```bash
indexdoc-converter/          # Project root directory
├── indexdoc_converter/      # Core package directory
│   ├── __init__.py          # Core code entry
│   ├── docx_to_md.py        # Word to Markdown converter
│   ├── excel_to_md.py       # Excel/Table to Markdown converter
│   ├── html_to_md.py        # HTML to Markdown converter
│   ├── pptx_to_md.py        # PPTX to Markdown converter
│   └── utils/
│       ├── __init__.py
│       ├── FileUtil.py
│       ├── IDUtil.py
│       └── img_to_base64.py
```

### Examples
```python
# Note: import from indexdoc_converter, not indexdoc-converter
from indexdoc_converter.docx_to_md import convert_docx_to_md
from indexdoc_converter.excel_to_md import TableToMarkdown
from indexdoc_converter.html_to_md import convert_to_md
from indexdoc_converter.pptx_to_md import pptx_to_md

# -------------------------------------------Word to Markdown---------------------------------------------------
md_text = convert_docx_to_md(r"C:\Users\xxx\test.docx", False)
with open('./test.md', 'w', encoding='utf-8') as f:
    f.write(md_text)

# -------------------------------------------Excel to Markdown-------------------------------------------------
# Custom parameters example
converter = TableToMarkdown(
    file_title_level=2,  # Markdown heading level for file title, default 1 (#), set to 2 (##) here
    single_row_value_as_title=True,  # Treat a single row of unique values as header, default True
    max_rows=8000,  # Max rows to process, default 6000 (actual: max_rows + 1)
    max_cols=200   # Max columns to process, default 128 (actual: max_cols + 1)
)

# Convert single file
file_path = r"C:\Users\xxx\test.xlsx"
result = converter.convert(file_path)

# blank mode: preserve merged cell structure (content only in top-left cell, others empty)
with open("../tmp/test_blank.md", "w", encoding="utf-8") as f:
    f.write(result['blank'])

# fill mode: fill merged cell content into all merged cells,
# auto-detect header rows, split table blocks, handle empty rows/columns,
# and support parsing merged cells in various table layouts
with open("../tmp/test_fill.md", "w", encoding="utf-8") as f:
    f.write(result['fill'])

# -------------------------------------------PPT to Markdown---------------------------------------------------
ppt_file = r"C:\Users\xxx\test.pptx"
md_path = pptx_to_md(ppt_file)
print(f"Single file conversion completed, MD file path: {md_path}")

# -------------------------------------------Web / HTML to Markdown-----------------------------------------------
# html = "https://news.qq.com/rain/a/20260114A01NI000"
html = "https://www.aituple.com"
# html = "https://www.indexdoc.com"
# html = r"C:\Users\xxx\test.html"
# html = "https://www.indexdoc.com/contact.html"
md = convert_to_md(html, '../tmp/test_html.md')
# md = mhtml_to_markdown(mhtml)
```

## Development
- Python 3.10 or higher

```bash
# Source code repository
https://github.com/indexdoc/indexdoc-batch-generator.git
```

```bash
# Install dependencies quickly
pip install -r requirements.txt

# Using Alibaba Cloud PyPI mirror
pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

## 📞 Author
- Developed by: Hangzhou ZhiyuShu Information Technology Co., Ltd.
- Email: indexdoc@qq.com