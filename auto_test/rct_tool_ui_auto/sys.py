# coding=utf-8


# print(sys.argv)
# print(sys.argv[0])
# # print(sys.argv[1])
# # print("第二个参数:%s"%sys.argv[2])
# print("参数个数：%s"%(len(sys.argv)-1))
# print(sys.getdefaultencoding())
# print(sys.getfilesystemencoding())
# print(sys.platform)
# print(sys.version)


# def exitfunc(value):
# 	print(value)
# 	sys.exit(0)
#
# print("hello")
#
# #程序中间过程
#
# try:

# 	sys.exit("sorry, goodbye!")
# except SystemExit:
# 	exitfunc(SystemExit)                  #有异常，捕获并返回异常，结束程序
import sys

item = "sorry, goodbye!"
item = "123"
sys.exit(item)

print("come?")