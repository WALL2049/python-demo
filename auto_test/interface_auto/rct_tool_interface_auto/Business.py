# -*- coding: utf-8 -*-
import subprocess
import re
import time
import paramiko


class Bussiness_Type:
    def __init__(self,GNB_IP, UE_CORE_IP, PORT):
        self.GNB_IP = GNB_IP
        self.ue_core_ip = UE_CORE_IP
        self.ue_pc_ip = '192.168.254.190'
        self.pdn_core_ip = '99.99.99.9'
        self.port = PORT
        self.pdn_ip = ''
        self._ssh = None
        self._chan = None
        self._ssh_pdn = None
        self._chan_pdn = None

    #result=1表示ping不通，result=0标识ping通
    def Ping(self):
        cmd = "ping " + self.pdn_core_ip + " -S " + self.ue_pc_ip
        #print(cmd)
        result = subprocess.run(cmd, shell=False)
        #print(result.returncode)
        return result
    #RCT灌包
    def login(self):
        self._ssh = paramiko.SSHClient()
        self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._ssh.connect(self.GNB_IP, 22, 'itran', 'Itran_2430!@#')
        self._chan = self._ssh.invoke_shell()
        self._chan.keep_this = self._ssh

    def login_pdn(self):
        self._ssh_pdn = paramiko.SSHClient()
        self._ssh_pdn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._ssh_pdn.connect('10.230.6.9', 22, 'root', 'Aa888888@')
        self._chan_pdn = self._ssh_pdn.invoke_shell()
        self._chan_pdn.keep_this = self._ssh_pdn

    def exec_cmd(self, cmd_list, timeout=1):
        if not isinstance(cmd_list, list):
            cmd_list = [cmd_list]
        for cmd in cmd_list:
            self._chan.send(cmd + '\n')
            time.sleep(timeout)
        result = self._chan.recv(99999)
        print(result)
        return result

    def exec_cmd_pdn(self, cmd_list, timeout=1):
        if not isinstance(cmd_list, list):
            cmd_list = [cmd_list]
        for cmd in cmd_list:
            self._chan_pdn.send(cmd + '\n')
            time.sleep(timeout)
        result = self._chan_pdn.recv(99999)
        print(result)
        return result

    def logout(self):
        if self._ssh and self._chan:
            self._ssh = None
            self._chan = None

    def logout_pdn(self):
        if self._ssh_pdn and self._chan_pdn:
            self._ssh_pdn = None
            self._chan_pdn = None

    def rct_udp_cmd(self):
        self.exec_cmd("docker exec -ti `docker ps | grep rct-agent-1 | awk '{print $1}'` sh")
        self.exec_cmd("cd ServiceMgr/app/iperf")
        self.exec_cmd("./iperf -u -c " + self.ue_core_ip + " -i 1 -p " + self.port + " -b 2200m -t 300 -l 1350 -P 1")
        time.sleep(300)
        self.exec_cmd("exit")

    def rct_tcp_cmd(self):
        self.exec_cmd("docker exec -ti `docker ps | grep rct-agent-1 | awk '{print $1}'` sh")
        self.exec_cmd("cd ServiceMgr/app/iperf")
        self.exec_cmd("./iperf  -c " + self.ue_core_ip + " -w 1m -p " + self.port + " -P 10 -t 300 -i 1")
        time.sleep(300)
        self.exec_cmd("exit")

    def pdn_udp_cmd(self):
        self.exec_cmd_pdn("./iperf -u -c " + self.ue_core_ip + " -i 1 -p " + self.port + " -b 2200m -t 300 -l 1350 -P 1 -B 99.99.99.9")
        time.sleep(300)
        self.exec_cmd_pdn("exit")

    def pdn_tcp_cmd(self):
        self.exec_cmd_pdn("./iperf  -c " + self.ue_core_ip + " -w 1m -p " + self.port + " -P 10 -t 300 -i 1 -B 99.99.99.9")
        time.sleep(300)
        self.exec_cmd_pdn("exit")

    def start_udp_rct(self):
        self.__init__(self.GNB_IP, self.ue_core_ip, self.port)
        self.login()
        self.rct_udp_cmd()
        self.logout()

    def start_tcp_rct(self):
        self.__init__(self.GNB_IP, self.ue_core_ip, self.port)
        self.login()
        self.rct_tcp_cmd()
        self.logout()

    def start_udp_pdn(self):
        self.__init__(self.GNB_IP, self.ue_core_ip, self.port)
        self.login_pdn()
        self.pdn_udp_cmd()
        self.logout_pdn()

    def start_tcp_pdn(self):
        self.__init__(self.GNB_IP, self.ue_core_ip, self.port)
        self.login_pdn()
        self.pdn_tcp_cmd()
        self.logout_pdn()