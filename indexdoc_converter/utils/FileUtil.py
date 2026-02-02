import os
def get_filepath_shortname_suffix(file_url):
    """
    获取文件路径， 文件名， 后缀名
    :param file_url:
    :return:
    """
    filepath, tmpfilename = os.path.split(file_url)
    shotname, extension = os.path.splitext(tmpfilename)
    return filepath, shotname, extension

def get_file_suffix(file_url):
    return os.path.splitext(file_url)[-1].lower()

def get_file_name_without_suffix(file_url):
    return os.path.splitext(file_url)[-2]


def detect_encoding(file_path: str) -> str:
    """
    稳定版编码检测
    核心思路：实际读取测试比理论检测更可靠
    """
    encodings_to_try = [
        'utf-8',        # 必须包含
        'gb18030',      # 最全中文支持
        'utf-8-sig',    # 必须包含
        'big5',         # 台湾繁体，极少数情况
        'utf-16',       # 极少数情况
        'cp1252',       # Windows西欧
        'latin1',       # 最兼容的回退
    ]

    for encoding in encodings_to_try:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                # 读取前1KB测试，不消耗太多资源
                f.read(1024)
                # 如果测试读取成功，返回该编码
                # print(encoding)
                return encoding
        except UnicodeDecodeError:
            continue
    #默认返回utf-8
    return 'utf-8'
