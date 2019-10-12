#!/usr/bin/python
# encoding: UTF-8
import re

f=open("3.txt",'r',encoding='utf-8')
f=f.read()
# make Chinese text clean
def clean_zh_text(text):#正则化处理， compile之后需要匹配的内容可以自行添加，该代码只保留了字母，数字，句号和中文以及换行符
    # keep English, digital and Chinese
    comp = re.compile('[^A-Z^a-z^0-9^\u3002\u4e00-\u9fa5.\n]')
    return comp.sub('', text)
if __name__ == '__main__':
    #版本一 以句号为节点划分数据
    text_zh = f
clean_str = ' '.join(text_zh.split())#将字符串先通过split转为数组，再转回字符串，目的是把
text2 = clean_zh_text(clean_str)
for i in range(len(text2)):
    if text2[i] =="。":
        text2 = text2[:i+1]+"\n"+text2[i+1:]
print (text2)

with open("清洗.txt","w") as g:
        g.write(text2)

#版本二 以空行为节点划分数据。
a = clean_zh_text(text_zh)
with open("test3.txt","w") as g:
        g.write(a)

s = []
f=open("test3.txt",'r')
for lines in f:
    if lines.strip() == '':
        ls = lines
    elif lines.strip() != '':
        ls = lines.strip()
        if ls.find('第') == 0:#检测第字是否在首段，此处灵活多变，用户可以根据需要的关键词进行划分
           ls = ls +'\n'

    s.append(ls)
f.close()
print(s)
f1 = open('result1.txt','w')#该txt事先在相应路径创好以便导出数据
for j in s:
    f1.write(j)
f1.close()