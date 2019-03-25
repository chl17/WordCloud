# -*- coding: UTF-8 -*-
import os


def all_path(dirname):
    postfix = ['doc', 'docx', "pdf", 'xls', 'xlsx']  # 设置要保存的文件格式
    fileList = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            # apath.replace('\\', '/')
            if apath.split('.')[-1] in postfix:   # 匹配后缀，只保存所选的文件格式。若要保存全部文件，则注释该句
                try:
                   fileList.append(apath)
                except:
                    pass
    return fileList

