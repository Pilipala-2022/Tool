import io
import sys
import os
import xml.etree.ElementTree as ET

# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
##anno_path修改为你存放xml文件的位置，最后末尾需要加上/
# old_annotation是修要修改的标签名，new_annotation是修改后的标签名字
anno_path = 'D:/大创/tiny/yolov4-tiny-tf2/VOCdevkit/VOC2007/Annotations/'
jp_path = 'D:/大创/tiny/yolov4-tiny-tf2/VOCdevkit/VOC2007/JPEGImages/'
old_annotation = 'Metal1'
new_annotation = 'Metal'
del_annotations = ['Metal']
# replace = True使用替换功能，False使用删除功能
# CHOICE = 1 为替换功能
# CHOICE = 2 为删除标签
# CHOISE = 3 为删除没有标签信息的xml文件
CHOICE = 3


def _main():
    filelist = os.listdir(anno_path)
    i = 0
    if CHOICE == 1:
        for file in filelist:
            n_ = _Replace_Annotation(file)
            if n_ > 0:
                i += 1
    elif CHOICE == 2:
        for file in filelist:
            n_ = _Del_Annotation(file)
            if n_ > 0:
                i += 1
    elif CHOICE == 3:
        for file in filelist:
            n_ = _Del_Annotation_puls(file)
            if n_ > 0:
                i += 1
    print('the number of xmlfile is :' + str(i))


# 替代标签
def _Replace_Annotation(filepath):
    if os.path.exists(anno_path + filepath) == False:
        print(filepath + ' :not found')
    # 建立xml树状结构
    i = 0
    while Replace_(filepath) == False:
        i += 1

    return i

def Replace_(filepath):
    if os.path.exists(anno_path + filepath) == False:
        print(filepath + ' :not found')
    # 建立xml树状结构
    tree = ET.parse(anno_path + filepath)
    root = tree.getroot()
    # 遍历xml文件 查找'name'
    for annoobject in tree.iter():
        if 'object' in annoobject.tag:
            for element in list(annoobject):
                if 'name' in element.tag:
                    # 替换标签
                    if element.text == old_annotation:
                        element.text = new_annotation
                        print(filepath)
                        # 重新写入xml，使修改生效
                        tree.write(anno_path + filepath, encoding="utf-8", xml_declaration=True)
                        return False


    return True

# 删除标签
def _Del_Annotation(filepath):
    if os.path.exists(anno_path + filepath) == False:
        print(filepath + ' :not found')
    # 建立xml树状结构
    i = 0
    while Delete_(filepath) == False:
        i += 1
    return i

def Delete_(filepath):
    if os.path.exists(anno_path + filepath) == False:
        print(filepath + ' :not found')
    # 建立xml树状结构
    tree = ET.parse(anno_path + filepath)
    # 遍历xml文件 查找'name'
    root = tree.getroot()
    for annoobject in root.iter():
        if 'object' in annoobject.tag:
            for element in list(annoobject):
                if 'name' in element.tag:
                    # 删除标签
                    for anno in del_annotations:
                        if element.text == anno:
                            # 从根节点下删除第一个子节点
                            root.remove(annoobject)
                            print(filepath)
                            # 重新写入xml，使修改生效
                            tree = ET.ElementTree(root)
                            tree.write(anno_path + filepath, encoding="utf-8", xml_declaration=True)
                            return False
    return True


# 删除xml
def _Del_Annotation_puls(filepath):
    if os.path.exists(anno_path + filepath) == False:
        print(filepath + ' :not found')
    # 建立xml树状结构
    i = 0
    if Delete_puls(filepath) == False:
        i += 1
    return i

def Delete_puls(filepath):
    img_name = filepath.split('.')[0] + '.jpg'


    if os.path.exists(anno_path + filepath) == False:
        print(filepath + ' :not found')
    # 建立xml树状结构
    tree = ET.parse(anno_path + filepath)
    # 遍历xml文件 查找'name'
    root = tree.getroot()
    for annoobject in root.iter():
        if 'object' in annoobject.tag:
            return True

    os.remove(anno_path + filepath)
    os.remove(jp_path + img_name)
    print(filepath)
    print(img_name)
    return False

if __name__ == '__main__':
    _main()
