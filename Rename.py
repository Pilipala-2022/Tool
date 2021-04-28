# -*- coding: UTF-8 -*-
'''
    Create by 谢昊璋 on 2021/4/26 22:03 
'''
# coding = utf-8
import os

# 文件路径
# path = "D:/RM2021/test/"
path = "D:/RM2021/1/"

# 标号起点
count = 1

# 获取该目录下所有文件，存入列表中
fileList = os.listdir(path)

n = 0
for i in fileList:

    old_name = path + fileList[n]
    new_name= path + "Img" + str(count) + ".jpg"

    print(i)

    os.rename(old_name, new_name)  # 用os模块中的rename方法对文件改名
    print(i, '======>', new_name)
    n += 1
    count += 1
print("总共处理{}张图片".format(n))