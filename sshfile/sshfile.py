import paramiko

# ����SSHClient ʵ������
ssh = paramiko.SSHClient()

# ��������Զ�̻������������
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# ssh����Զ�̻���������Ϊ  ��ַ���˿ڡ��û���������
ssh.connect("192.168.2.100", 22, "byhy", "byhy5200")

# ִ���������Ŀ¼ logs
ssh.exec_command("mkdir logs")

# �ر�ssh����
ssh.close()


cmd = 'ps -ef|grep apiserver |grep -v grep'

# ÿ��ִ������᷵��3�����󣬶�Ӧ��׼���롢��׼�������׼����
stdin, stdout, stderr = ssh.exec_command(cmd)

# �� ��׼�������׼���� �ж�ȡ�ֽ�
outputBytes = stdout.read()+ stderr.read()

# ����Ϊ�ַ���
outputStr = outputBytes.decode('utf8')

print(outstr)

import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.2.100", 22, "byhy", "byhy5200")

# ����Ŀ¼ testdir
ssh.exec_command("mkdir testdir")

# ��һ������ ����Ŀ¼ testdir ���� �鿴��ǰ·��
stdin, stdout, stderr = ssh.exec_command("cd testdir;pwd")
print(stdout.read())

ssh.close()


import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.2.100", 22, "byhy", "byhy5200")

# ��һ��sftp���ӣ�����sftp���Ӷ���
sftp = ssh.open_sftp()

# put�����ϴ��ļ�����1�������Ǳ���·������2��������Զ��·��
sftp.put('install.zip', '/home/byhy/install.zip')

# get���������ļ�����1��������Զ��·������2�������Ǳ���·��
sftp.get('/home/byhy/log.zip', 'd:/log.zip')

# �ر�sftp����
sftp.close()

# �ر�ssh����
ssh.close()