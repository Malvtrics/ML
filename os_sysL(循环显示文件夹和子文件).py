##循环显示文件夹和下面的子文件

import os,sys

def dir_s(path,tab):
    path = os.path.abspath(path)
    files = os.listdir(path)
    for f in files:
        print("\t"*tab + f) 
        subpath = os.path.join(path,f)
        if os.path.isdir(subpath):
            dir_s(subpath,tab+1)

dir_s('C:\\Users\\mengwang\\Desktop\\GPMA\\Other\\Python',0)
