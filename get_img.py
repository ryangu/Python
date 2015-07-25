# -*- coding:utf-8 -*-
#批量下载某论坛某文章的图片
import re, urllib, random, os, urllib2

list_1=["http://www.yuhuagu.com/duorou/2012/0704/3534.html",]
for n in range(1,3):
    raw_s = "http://www.yuhuagu.com/duorou/2012/0704/3534_%s.html" % n
    list_1.append(raw_s)
print list_1

rootPath = "get_img"
#创建新目录
def mkdir(path):
    path = path.strip()
    isExisted = os.path.exists(path)
    if not isExisted:
        os.makedirs(path)
        return True
    else:
        return False
#存储照片
def saveImg(imageURL,filename,number):
    u = urllib.urlopen(imageURL)
    data = u.read()
    #filename = str(filename) + "/" + str(number) + "." + "jpg" #一定要加文件名，"/"是进入下一目录
    filename = str(filename) + "/%s.jpg" % number #一定要加文件名，"/"是进入下一目录
    filenamePath = rootPath + "/" + filename
    f = open(filenamePath, 'wb')
    f.write(data)
    f.close()

def getImg(html1):
    com_reg = re.compile(r'<p align=.*? src="(.*?)" \/></p>') #正则匹配图片url
    url_list = re.findall(com_reg, html1)
    return url_list

filename = 1
mkdir(rootPath)
for n in list_1:
    s = urllib.urlopen(n)
    html = s.read()
    url_list = getImg(html)
    mkdir(rootPath + "/" + str(filename))
    fileIndex = 1
    for x in url_list:
        saveImg(x,filename,fileIndex)
        fileIndex += 1
    filename += 1




