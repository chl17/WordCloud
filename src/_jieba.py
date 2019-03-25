import jieba.analyse
import os


def split():
    f = open(os.getcwd() + '\\temp.txt', 'r', encoding='utf-8')
    content = f.readlines()
    stopwords = []
    for stopword in open('stopwords.txt', 'r', encoding='utf-8'):
        stopwords.append(stopword.strip())
    splitData = jieba.cut(''.join(content), cut_all=False, HMM=True)  # 三种模式
    result = ''
    for splitword in splitData:
        if splitword not in stopwords:
            result += splitword + " "
    return result
