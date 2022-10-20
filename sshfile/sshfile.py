import paramiko

# 创建SSHClient 实例对象
ssh = paramiko.SSHClient()

# 设置信任远程机器，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# ssh连接远程机器，参数为  地址、端口、用户名、密码
ssh.connect("192.168.2.100", 22, "byhy", "byhy5200")

# 执行命令，创建目录 logs
ssh.exec_command("mkdir logs")

# 关闭ssh连接
ssh.close()


cmd = 'ps -ef|grep apiserver |grep -v grep'

# 每次执行命令会返回3个对象，对应标准输入、标准输出、标准错误
stdin, stdout, stderr = ssh.exec_command(cmd)

# 从 标准输出、标准错误 中读取字节
outputBytes = stdout.read()+ stderr.read()

# 解码为字符串
outputStr = outputBytes.decode('utf8')

print(outstr)

import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.2.100", 22, "byhy", "byhy5200")

# 创建目录 testdir
ssh.exec_command("mkdir testdir")

# 用一行命令 进入目录 testdir 并且 查看当前路径
stdin, stdout, stderr = ssh.exec_command("cd testdir;pwd")
print(stdout.read())

ssh.close()


import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.2.100", 22, "byhy", "byhy5200")

# 打开一个sftp连接，返回sftp连接对象
sftp = ssh.open_sftp()

# put方法上传文件，第1个参数是本地路径，第2个参数是远程路径
sftp.put('install.zip', '/home/byhy/install.zip')

# get方法下载文件，第1个参数是远程路径，第2个参数是本地路径
sftp.get('/home/byhy/log.zip', 'd:/log.zip')

# 关闭sftp连接
sftp.close()

# 关闭ssh连接
ssh.close()