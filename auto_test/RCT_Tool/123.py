import os

path = r'C:\Users\123\PycharmProjects\20200302\RCT_Tool'
a = os.listdir(path)        # 默认文件名按字母大小排序
print(a)
b = os.walk(path)

# for dirpath, dirnames, filenames in b:
    # for filename in filenames:
    # print(os.path.join(dirpath, filename))
# for dirpath, dirnames, filenames in b:
#     for dirname in dirnames:
#         print(os.path.join(dirpath, dirname))

