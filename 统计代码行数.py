import os
import sys


def getfilelist(filepath):
    filelist = os.listdir(filepath)  # 获取filepath文件夹下的所有的文件,filepath必须要是绝对路径
    files = []
    for filename in filelist:
        folder = os.path.join(filepath, filename)  # get folder abspath
        if os.path.isdir(folder):
            # Recursion遍历所有子文件夹,extend() #函数用于在列表末尾一次性追加另一个序列中的多个值
            files.extend(getfilelist(folder))

        else:
            if os.path.splitext(folder)[1] == '.py' or os.path.splitext(folder)[1] == '.cpp' or os.path.splitext(folder)[1] == '.c':
                files.append(folder)
    return files


def Countline(file):
    value = dict()
    count = 0
    fh = open(file, encoding='utf-8', errors='ignore')
    for lines in fh.readlines():  # readlines() 读取文件所有内容，按行为单位放到一个列表中，返回list类型。
        if lines.startswith("//") or lines.startswith("#"):
            continue
        count += 1
    value[file] = count
    return value


filepath1 = "d:\\pythoncode"  # python path needs two \
filepath2 = "d:\\c_code"
totalline = 0
for everyfile in getfilelist(filepath1) + getfilelist(filepath2):
    print(Countline(everyfile))
    totalline += Countline(everyfile)[everyfile]
print("The totalline is", totalline)
