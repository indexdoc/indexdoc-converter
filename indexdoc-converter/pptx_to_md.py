import pptx2md
from pathlib import Path
import os
import tempfile

from utils import IDUtil

def pptx_to_md(pptx_file):
    md_file_path = Path(tempfile.gettempdir()) / f"{IDUtil.get_uuid()}.md"
    config = pptx2md.ConversionConfig(
        pptx_path=pptx_file,
        output_path=md_file_path,
        image_dir=Path(tempfile.gettempdir()),
        disable_notes=True  # 根据需求选择是否禁用备注页
    )
    pptx2md.convert(config)
    return md_file_path

def batch_pptx_to_md(input_dir: str, output_dir: str = None, image_dir: str = None):
    """
    使用指定的输入目录中的所有 .pptx 文件，并将它们转换为 Markdown 文件。

    Args:
        input_dir (str): 包含 PPTX 文件的文件夹路径
        output_dir (str, optional): 输出 Markdown 文件的文件夹。若为 None，则输出到与 PPTX 相同位置
        image_dir (str, optional): 图片保存目录。如果需要导出图片的话设置此项
    """
    input_path = Path(input_dir)
    if not input_path.exists() or not input_path.is_dir():
        raise ValueError(f"输入目录不存在或不是文件夹: {input_dir}")

    # 如果没有指定输出目录，则默认为输入目录
    if output_dir is None:
        output_path = input_path
    else:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

    # 如果需要导出图片，创建图片目录
    if image_dir:
        img_path = Path(image_dir)
        img_path.mkdir(parents=True, exist_ok=True)
    else:
        img_path = None

    pptx_files = list(input_path.glob("*.pptx"))
    if not pptx_files:
        print(f"在 {input_dir} 中未找到 .pptx 文件")
        return

    print(f"发现 {len(pptx_files)} 个 PPTX 文件，开始转换...")

    for pptx_file in pptx_files:
        try:
            md_file = output_path / f"{pptx_file.stem}.md"

            config = pptx2md.ConversionConfig(
                pptx_path=pptx_file,
                output_path=md_file,
                image_dir=img_path,
                disable_notes=True  # 根据需求选择是否禁用备注页
            )

            print(f"正在转换: {pptx_file.name} → {md_file.name}")

            pptx2md.convert(config)
            print(f"✅ 成功: {md_file.name}")
        except Exception as e:
            print(f"❌ 失败: {pptx_file.name} - {e}")

    print("批量转换完成！")


if __name__ == "__main__":
    # 你可以在这里直接设置路径，或者通过命令行参数传递
    input_folder = r'D:\测试目录_全面\ppt'  # 替换为你的PPTX文件夹路径
    output_folder = './markdown_out'  # 可选，设为None则输出到原目录
    image_folder = './markdown_out/images'  # 如果你需要导出图片，设置此路径；否则保持None

    batch_pptx_to_md(input_folder, output_folder, image_folder)
