# 微软docx2pdf

https://superuser.com/questions/1523869/batch-convert-docx-files-to-pdf

stackexchange 里找到的回答。

使用pip 安装 docx2pdf , 帮助页面：


```pwsh
Scripts> docx2pdf

usage: docx2pdf [-h] [--keep-active] [--version] input [output]

Example Usage:

Convert single docx file in-place from myfile.docx to myfile.pdf:
    docx2pdf myfile.docx

Batch convert docx folder in-place. Output PDFs will go in the same folder:
    docx2pdf myfolder/

Convert single docx file with explicit output filepath:
    docx2pdf input.docx output.docx

Convert single docx file and output to a different explicit folder:
    docx2pdf input.docx output_dir/

Batch convert docx folder. Output PDFs will go to a different explicit folder:
    docx2pdf input_dir/ output_dir/

positional arguments:
  input          input file or folder. batch converts entire folder or convert single file
  output         output file or folder

options:
  -h, --help     show this help message and exit
  --keep-active  prevent closing word after conversion
  --version      display version and exit

```


速度非常快，效果不错。属于跨平台docx文件转换为pdf的比较好的工具了。

