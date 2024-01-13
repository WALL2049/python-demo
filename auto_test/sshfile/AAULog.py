# coding=utf-8
import datetime
import os
import time
import paramiko


class BaseStation:
    def __init__(self, ip, port=22, username="itran", password="Itran_2430!@#"):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password

    def connect_vsw(self):
        # 创建SSHClient 实例对象
        ssh = paramiko.SSHClient()
        # 设置信任远程机器，允许访问
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, self.port, self.username, self.password, timeout=10)

    def connect_vbp(self):
        # 创建SSHClient 实例对象
        ssh = paramiko.SSHClient()
        # 设置信任远程机器，允许访问
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, self.port, self.username, self.password, timeout=10)
        auto_shell = ssh.invoke_shell()
        time.sleep(0.5)
        auto_shell.send("ssh root@192.254.3.48")
        time.sleep(0.5)
        auto_shell.send("Itran_2430!@#$")
        time.sleep(0.5)

    def output_aaulog(self, file_path):
        # 创建SSHClient 实例对象
        ssh = paramiko.SSHClient()
        # 设置信任远程机器，允许访问
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, self.port, self.username, self.password, timeout=10)
        chan = ssh.invoke_shell()
        time.sleep(0.5)
        chan.send("ssh root@192.254.3.48\n")
        time.sleep(0.5)
        chan.send("Itran_2430!@#$\n")
        time.sleep(0.5)
        # chan.send("route\n")
        # time.sleep(0.5)
        chan.send("telnet 200.48.4.7\n")
        time.sleep(0.5)
        chan.send("zte\n")
        time.sleep(0.5)
        chan.send("v2Auth@root\n")
        time.sleep(0.5)
        chan.send("/ushell\n")
        time.sleep(0.5)
        chan.send("ps\n")
        time.sleep(0.5)
        chan.send("pad 113\n")
        time.sleep(0.5)


        for i in range(5):
            chan.send('power_calc 0,0,0,1,4000,1\n')
            time.sleep(0.5)
            log = chan.recv(65535).decode('ascii')
            print(log)
            if not os.path.exists(file_path):
                # os.makedirs(file_path)
                os.mkdir(file_path)
            with open(file_path, "a") as file:
                file.write(str(datetime.datetime.now()) + "\n=========================\n" + log + "\n")
                time.sleep(2)
        chan.close()
        ssh.close()



if __name__ == "__main__":
    file_path = "D:\mts_auto\singlePCC\AAUlog.txt"
    bs = BaseStation("10.230.21.174")
    bs.output_aaulog(file_path)