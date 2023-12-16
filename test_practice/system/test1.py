import os


version = input('请输入:')
cmd = fr'{version} --version'    # r表示后面的内容不转义
os.system(cmd)

print('执行完毕')