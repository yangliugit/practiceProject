# -*- coding=utf-8 -*-
# 注释代码为图片处理为字符图像，下方为整合特定格式的excel
# from PIL import Image
# import argparse
#
#
# # ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# ascii_char = list("MNHQ$OC?7>!:-;. ")
#
#
# def get_char(r, g, b, alpha=256):
#     if alpha == 0:
#         return ' '
#     length = len(ascii_char)
#     gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
#     unit = (256.0 + 1) / length
#     return ascii_char[int(gray / unit)]
#
# if __name__ == '__main__':
#     img = r'F:\trans\asciipng\test.png'
#     width = 160
#     height = 160
#     im = Image.open(img)
#     im = im.resize((width, height), Image.ANTIALIAS)
#
#     txt = ""
#     for i in range(height):
#         for j in range(width):
#             txt += get_char(*im.getpixel((j, i)))
#
#         txt += '\n'
#     print txt
#
#     with open(r'F:\trans\asciipng\output.txt', 'w') as f:
#         f.write(txt)

# -*- coding=utf-8 -*-
# f = open(r'C:\Users\Administrator\Desktop\daxiao.txt', 'w')
# for i in range(2000000):
#     phone = 18626330613 + i
#     f.write(str(phone)+ "\n")
# f.close()


# 将多个Excel文件合并成一个
import xlrd
import xlsxwriter
import os

# 打开一个excel文件
def open_xls(file):
    fh = xlrd.open_workbook(file)
    return fh


# 获取excel中所有的sheet表
def getsheet(fh):
    return fh.sheets()


# 获取sheet表的行数
def getnrows(fh, sheet):
    table = fh.sheets()[sheet]
    return table.nrows


# 读取文件内容并返回行内容
def getFilect(file, shnum):
    fh = open_xls(file)
    table = fh.sheets()[shnum]
    num = table.nrows
    datavalue = []
    for row in range(num):
        rdata = table.row_values(row)
        datavalue.append(rdata)
    datavalue.append('') # 两元素间添加一空格
    return datavalue


# 获取sheet表的个数
def getshnum(fh):
    x = 0
    sh = getsheet(fh)
    for sheet in sh:
        x += 1
    return x


def searchFileOfDir(path, word):
    fpList = []
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        if os.path.isfile(fp) and word in filename:
            fpList.append(fp)
    return fpList


if __name__ == '__main__':
    # 定义要合并的excel文件列表
    path = r'G:\Own\table'
    word = 'keeper'
    allxls = searchFileOfDir(path, word)

    # 存储所有读取的结果
    datavalues = []
    for fl in allxls:
        fh = open_xls(fl)
        x = getshnum(fh)
        for shnum in range(x):
            print("正在读取文件：" + str(fl) + "的第" + str(shnum) + "个sheet表的内容...")
            rvalue = getFilect(fl, shnum)
        datavalues.extend(rvalue)
    rvalue = datavalues

    # 定义最终合并后生成的新文件
    endfile = r'G:\Own\table\ALLexcel.xlsx'
    wb1 = xlsxwriter.Workbook(endfile)
    # 创建一个sheet工作对象
    ws = wb1.add_worksheet()

    format_title = wb1.add_format()  # 定义format格式对象
    format_title.set_border(1)  # 定义format对象单元格边框加粗(1像素)的格式

    format_data = wb1.add_format()  # 定义format_title格式对象
    format_data.set_border(1)  # 定义format_title对象单元格边框加粗(1像素)的格式
    format_data.set_bg_color('#cccccc')  # 定义format_title对象单元格背景颜色为
    format_data.set_align('center')  # 定义format_title对象单元格居中对齐的格式
    format_data.set_bold()  # 定义format_title对象单元格内容加粗的格式

    for a in range(len(rvalue)):
        for b in range(len(rvalue[a])):
            c = rvalue[a][b]
            if c in ('userName', 'tabName', 'colNo', 'colName', 'dataType', 'isNull', 'colComment'):
                ws.write(a, b, c, format_data)
            else:
                ws.write(a, b, c, format_title)
    wb1.close()
    print("文件合并完成")