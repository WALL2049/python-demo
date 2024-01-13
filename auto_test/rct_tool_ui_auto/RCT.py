# coding:utf-8
# -*- coding: utf-8 -*-

import re

from future.backports.test.ssl_servers import threading
import os
import PySimpleGUI27 as sg
from auto_test.rct_tool_ui_auto import sys
import paramiko
import time
from selenium import webdriver # 导入webdrive这个类
from selenium.webdriver.support.ui import WebDriverWait # 注意区分大小写，导入WebDriverWait等待的类
from selenium.webdriver.support import expected_conditions as EC # es,expected_conditions首字母，方便调用方法。as取一个别名，调方法的话直接EC.
from selenium.webdriver.common.by import By # 通过by进行元素定位
from selenium.webdriver.chrome.options import Options
if 0:
     import re


# 创建浏览器对象
def open_browser(txt):
    # if txt == 'Chrome':
    #     wd = webdriver.Chrome()
    # elif txt == 'Ie':
    #     wd = webdriver.Ie()
    # else:
    #     wd = webdriver.Firefox()
    # return wd
    try:
        wd = getattr(webdriver, txt)()
        # 从webdriver中获取一个名叫txt的属性
        # wd.Chrome
    except Exception as err:
        print(err)
        wd = webdriver.Chrome()
    return wd


# 创建浏览器对象（headless）
def open_browser_headless(txt):
    try:
        opts = Options()
        opts.headless = True  # 设置无头模式
        wd = getattr(webdriver, txt)(options=opts)
        # 从webdriver中获取一个名叫txt的属性
        # wd.Chrome
        # prefs = {
        #     'profile.default_content_setting_values': {
        #         'images': 2
        #     }
        # }
        # opts.add_experimental_option('prefs', prefs)
    except Exception as err:
        print(err)
        wd = webdriver.Chrome()
    return wd

class Key:

    # 创建临时driver
    # wd = webdriver.Chrome()
    # 构造函数用于给self.wd进行初始化
    def __init__(self, txt, viewmod):
        if viewmod == 'headless':
            self.wd = open_browser_headless(txt)
        else:
            self.wd = open_browser(txt)

    # 访问url
    def open(self,url):
        self.wd.get(url)

    # 查找xpath元素
    def locator(self, value):
        # return self.wd.find_element_by_xpath(value)
        return self.wd.find_element(By.XPATH, value)

    # 输入框输入
    def input(self, xpath_, txt):
        self.locator(xpath_).send_keys(txt)

    # 点击
    def click(self, xpath_):
        self.locator(xpath_).click()

    # 等待
    def wait(self, wd, xpath_):
        # time.sleep(time_)
        element = WebDriverWait(wd, 10, 0.2).until(EC.presence_of_element_located((By.XPATH, xpath_)))  # 搜索框元素的显式等待 until判断条件。跟进id进行定位，调用EC条件类
        return element

    # 关闭
    def quit(self):
        self.wd.quit()

    # 刷新窗口句柄
    def refwindow(self):
        windows = self.wd.window_handles
        return windows

    # 切换窗口
    def swch(self, handle):
        self.wd.switch_to.window(handle)

    # 切换frame
    def swch2frame(self, xpath_):
        element2 = self.locator(xpath_)
        self.wd.switch_to.frame(element2)


def thread_it(func):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()

    # 阻塞--卡死界面！
    # t.join()
    return func


def ume_login(key, ume_ip_):
    key.open(ume_ip_)
    key.input('//*[@id="inputUserName"]', 'admin')
    key.input('//*[@id="inputCiphercode"]', 'Zenap_123!@#')
    key.click('//*[@id="loginBut"]')


def ume2click_sta_flow_task( ):
    key.wait(key.wd, '//*[@id="ranume-sta"]/div[2]/div[1]').click()  # 点击STA
    key.swch(key.refwindow()[1])
    key.wait(key.wd, '//*[@id="ranume-sta-ne-trace"]/span').click()  # 点击基站跟踪
    # 输入过滤内容
    time.sleep(1)
    key.swch2frame('//*[@id="page-mainIframe"]')
    key.wait(key.wd,
             '//*[@id="trace_task_list"]/plx-table/div/div/div[1]/plx-table-filter/div/plx-search/div/input').send_keys(
        value['task_name'])
    time.sleep(1)
    # 获取任务状态标志位，是已激活还是未激活
    task_status_flag = key.locator(
        '//*[@id="plx-table-printId-0"]/div[2]/table/tbody/tr/td[5]/plx-table-cell/app-operate-state/div/a[@class]')
    # print task_status_flag.text
    task_status_flag_text = task_status_flag.text  # .decode('utf-8')
    # print task_status_flag_text
    # 判断如果是已激活，点击挂起，等任务状态转变为已挂起，点击激活；如果是已挂起，点击激活
    if task_status_flag_text == '已激活' or task_status_flag_text == 'Activated':
        # print '判断为已激活，需要去激活再激活'
        window.Element('_log_').Update('判断为已激活，需要去激活再激活')
        key.click(
            '/html/body/mt-root/app-event-list/div/div[2]/plx-table/div/div/div[2]/div/div[2]/table/tbody/tr/td[9]/plx-table-cell/app-operate-select/div/button[2]')
        # print '已去激活'
        window.Element('_log_').Update('已去激活')
        time.sleep(10)
        key.click(
            '/html/body/mt-root/app-event-list/div/div[2]/plx-table/div/div/div[2]/div/div[2]/table/tbody/tr/td[9]/plx-table-cell/app-operate-select/div/button[2]')
        # print '已尝试重新激活'
        window.Element('_log_').Update('已尝试重新激活')
        time.sleep(10)
        task_status_flag_text = key.locator(
            '//*[@id="plx-table-printId-0"]/div[2]/table/tbody/tr/td[5]/plx-table-cell/app-operate-state/div/a[@class]').text
        # print (task_status_flag_text == '已激活' or task_status_flag_text == 'Activated')
        if task_status_flag_text == '已激活' or task_status_flag_text == 'Activated':
            # print '已激活成功'
            window.Element('_log_').Update('已激活成功')
        else:
            # print '激活不成功'
            window.Element('_log_').Update('激活不成功')
            key.click(
                '/html/body/mt-root/app-event-list/div/div[2]/plx-table/div/div/div[2]/div/div[2]/table/tbody/tr/td[9]/plx-table-cell/app-operate-select/div/button[2]')
            # print '已再次尝试激活'
            window.Element('_log_').Update('已再次尝试激活')
    else:
        # print '判断为未激活，需要激活'
        window.Element('_log_').Update('判断为未激活，需要激活')
        key.click('//*[@id="start_task_button"]')
        # print '已操作激活'
        window.Element('_log_').Update('已操作激活')

    time.sleep(10)
    key.quit()

def task_start_ume_udp_():
    window.Element('_log_').Update('开始ping包保证连通')
    os.system(value['ping_cmd'])
    ume_login(key, ume_ip_=value['UME_ip'])
    ume2click_sta_flow_task()


def task_ul_tcp_():
    # ping包
    # os.system('ping 66.66.66.8 -S 192.168.223.124 -n 5')
    window.Element('_log_').Update('开始ping包保证连通')
    os.system(value['ping_cmd'])
    window.Element('_log_').Update('ping包完成')
    # 灌包

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(value['bs_ip'], 22, 'itran', 'Itran_2430!@#', timeout=10, compress=True)
    chan = ssh.invoke_shell()
    time.sleep(0.5)
    chan.send('docker ps|grep rct\n ')
    time.sleep(0.5)
    log = chan.recv(65535).decode('ascii')
    log = log.replace(" ", "")
    print(log)
    p = re.compile('173.254.101.100:5000/rct-agent')
    m = p.search(log)
    mstart = m.start()

    chan.send('docker exec -it ' + log[mstart - 12:mstart] + ' /bin/bash\n')
    chan.send('cd ServiceMgr/app/iperf\n')
    time.sleep(0.5)
    window.Element('_log_').Update('登入RCT')
    log = chan.recv(65535).decode('ascii')

    # chan.send('./iperf -s -i 1 -w 2m -p 13111 -P 15\n')
    chan.send(value['ul_tcp_RCT_cmd']+'\n')
    time.sleep(2)
    window.Element('_log_').Update('RCT已开上行收包窗口')
    # os.system('iperf -c 193.254.100.100 -i 1 -w 2m -B 192.168.223.124 -p 13111 -P 10 -t 5400\n')
    # os.system(value['ul_tcp_CMD_cmd']+'\n')
    os.system('start ul_cmd_iperfcmd.bat')
    window.Element('_log_').Update('已运行上行灌包bat脚本')
    print(log)
    time.sleep(900)
    chan.close()
    ssh.close()


def task_dl_tcp_():
    # os.system("iperf -s -i 1 -w 2m -p 13222 -P 15")
    os.system("start kaichuangkou.bat")
    # ping包
    # os.system('ping 66.66.66.8 -S 192.168.223.124 -n 5')
    window.Element('_log_').Update('开始ping包保证连通')
    os.system(value['ping_cmd'])
    # 灌包
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(value['bs_ip'], 22, 'itran', 'Itran_2430!@#', timeout=10, compress=True)
    chan = ssh.invoke_shell()
    time.sleep(0.5)
    chan.send('docker ps|grep rct\n ')
    time.sleep(0.5)
    log = chan.recv(65535).decode('ascii')

    log = log.replace(" ", "")
    print(log)
    p = re.compile('173.254.101.100:5000/rct-agent')
    m = p.search(log)
    mstart = m.start()

    chan.send('docker exec -it ' + log[mstart - 12:mstart] + ' /bin/bash\n')
    chan.send('cd ServiceMgr/app/iperf\n')
    time.sleep(0.5)
    window.Element('_log_').Update('登入RCT')
    log = chan.recv(65535).decode('ascii')

    chan.send(value['dl_tcp_RCT_cmd']+'\n')
    window.Element('_log_').Update('开始下行RCT灌包')
    time.sleep(5)
    print(log)
    time.sleep(900)
    chan.close()
    ssh.close()


def pingbao_32_():
    os.system('start ping_32.bat')


def pingbao_1500_():
    os.system('start ping_1500.bat')


def write_default_value_():
    dtxt_ume_ip = value['UME_ip']
    dtxt_ping_cmd = value['ping_cmd']
    dtxt_task_name = value['task_name']
    dtxt_bs_ip = value['bs_ip']
    dtxt_ul_tcp_RCT_cmd = value['ul_tcp_RCT_cmd']
    dtxt_ul_tcp_CMD_cmd = value['ul_tcp_CMD_cmd']
    dtxt_dl_tcp_CMD_cmd = value['dl_tcp_CMD_cmd']
    dtxt_dl_tcp_RCT_cmd = value['dl_tcp_RCT_cmd']
    dtxt_ping_32_cmd = value['ping_32_cmd']
    dtxt_ping_1500_cmd = value['ping_1500_cmd']
    default_str_='ume_addr:'+dtxt_ume_ip+'\n'+'pingcmd:'+dtxt_ping_cmd+'\n'+'guanbao_task_name:'+dtxt_task_name+'\n'+'jizhan_ip:'+dtxt_bs_ip+'\n'+\
                    'ultcp_RCT_cmd:'+dtxt_ul_tcp_RCT_cmd+'\n'+'ultcp_CMD_cmd:'+dtxt_ul_tcp_CMD_cmd+'\n'+'dltcp_CMD_cmd:'+dtxt_dl_tcp_CMD_cmd+'\n'+\
                    'dltcp_RCT_cmd:'+dtxt_dl_tcp_RCT_cmd+'\n'+'ping_32_cmd:'+dtxt_ping_32_cmd+'\n'+'ping_1500_cmd:'+dtxt_ping_1500_cmd+'\n'
    open('defaultvalue_.txt', 'w').write(default_str_)
    window.Element('_log_').Update('默认参数已写入txt文件')
    open('kaichuangkou.bat', 'w').write(dtxt_dl_tcp_CMD_cmd)
    open('ping_32.bat', 'w').write(dtxt_ping_32_cmd)
    open('ping_1500.bat', 'w').write(dtxt_ping_1500_cmd)
    open('ul_cmd_iperfcmd.bat', 'w').write(dtxt_ul_tcp_CMD_cmd)
    window.Element('_log_').Update('默认参数已输出bat文件')


reload(sys)
sys.setdefaultencoding('utf-8')

# 先从文件中读取默认参数
fread_ = open('defaultvalue_.txt', 'r').read()
dtxt_ume_ip = re.findall('ume_addr:(.*?)\n', fread_)[0]
dtxt_ping_cmd = re.findall('pingcmd:(.*?)\n', fread_)[0]
dtxt_task_name = re.findall('guanbao_task_name:(.*?)\n', fread_)[0]
dtxt_bs_ip = re.findall('jizhan_ip:(.*?)\n', fread_)[0]
dtxt_ul_tcp_RCT_cmd = re.findall('ultcp_RCT_cmd:(.*?)\n', fread_)[0]
dtxt_ul_tcp_CMD_cmd = re.findall('ultcp_CMD_cmd:(.*?)\n', fread_)[0]
dtxt_dl_tcp_CMD_cmd = re.findall('dltcp_CMD_cmd:(.*?)\n', fread_)[0]
dtxt_dl_tcp_RCT_cmd = re.findall('dltcp_RCT_cmd:(.*?)\n', fread_)[0]
dtxt_ping_32_cmd = re.findall('ping_32_cmd:(.*?)\n', fread_)[0]
dtxt_ping_1500_cmd = re.findall('ping_1500_cmd:(.*?)\n', fread_)[0]
# 创建布局

layout = [
    [sg.Text('网管地址'), sg.Text('       '),sg.Input(default_text=dtxt_ume_ip,key='UME_ip')],
    [sg.Text('Ping包命令'), sg.Text('    '),sg.Input(default_text=dtxt_ping_cmd, key='ping_cmd')],
    [sg.Text('灌包任务名'), sg.Text('    '),sg.Input(default_text=dtxt_task_name, key='task_name')],
    [sg.Text('基站ip'), sg.Text('            '),sg.Input(default_text=dtxt_bs_ip,key='bs_ip')],
    [sg.Btn('触发网管UDP灌包任务', key='start_ume_udp_'), sg.Text('', key='_log_',  size=(20,1))],
    [sg.Btn('上行tcp', key='start_ul_tcp_')],
    [sg.Text('RCT'), sg.Text('               '), sg.Input(default_text=dtxt_ul_tcp_RCT_cmd, key='ul_tcp_RCT_cmd')],
    [sg.Text('CMD'), sg.Text('              '), sg.Input(default_text=dtxt_ul_tcp_CMD_cmd, key='ul_tcp_CMD_cmd')],
    [sg.Btn('下行tcp', key='start_dl_tcp_')],
    [sg.Text('CMD'), sg.Text('              '), sg.Input(default_text=dtxt_dl_tcp_CMD_cmd, key='dl_tcp_CMD_cmd')],
    [sg.Text('RCT'), sg.Text('               '),sg.Input(default_text=dtxt_dl_tcp_RCT_cmd, key='dl_tcp_RCT_cmd')],
    [sg.Btn('上下行tcp', key='start_uldl_tcp_')],
    [sg.Btn('ping包32字节', key='start_ping_32_'), sg.Text(''),sg.Input(default_text=dtxt_ping_32_cmd, key='ping_32_cmd')],
    [sg.Btn('ping包1500字节', key='start_ping_1500_'), sg.Input(default_text=dtxt_ping_1500_cmd, key='ping_1500_cmd')],
    [sg.Btn('停止', key='_stop_'),sg.Text('                                                                         '),sg.Btn('写入默认值', key='_write_default_value_')],
    # [sg.Btn('tst', key='_tst_'),sg.Text('tst',key='hua')]
]



# 创建窗口，引入布局，并进行初始化
# 创建时，必须要有一个名称，这个名称会显示在窗口上

window = sg.Window('Baselinetool', layout=layout, finalize=True)
# key = Key('Chrome', 'headless')
while True:  # 创建一个事件循环，否则窗口运行一次就会被关闭
    event, value = window.Read()  # event, value 的值分别是 _LOGIN_ {'_USER_': 'admin', '_PWD_': '123'}

    if event is None:   # 如果事件的值为 None，表示点击了右上角的关闭按钮
        break
    if event == '_stop_':
        os.system('taskkill /f /im iperf.exe')
        os.system('taskkill /f /im cmd.exe')
        os.system('taskkill /f /im ping.exe')
    if event == 'start_ume_udp_':
        key = thread_it(Key('Chrome', 'headless'))
        # threading.Thread(target=task_start_ume_udp_)
        thread_it(task_start_ume_udp_)
    if event == 'start_ul_tcp_':
        thread_it(task_ul_tcp_)
    if event == 'start_dl_tcp_':
        thread_it(task_dl_tcp_)
    if event == 'start_uldl_tcp_':
        thread_it(task_ul_tcp_)
        time.sleep(5)
        thread_it(task_dl_tcp_)
    if event == 'start_ping_32_':
        thread_it(pingbao_32_)
    if event == 'start_ping_1500_':
        thread_it(pingbao_1500_)
    if event == '_write_default_value_':
        thread_it(write_default_value_)
    # if event == '_start_':  # 当获取到事件时，处理逻辑
    #     key = Key('Chrome', '')
    #     print '开始'
    #     ume_login(key, ume_ip_=value['UME_ip'])
    #     ume2click_sta_flow_task()
    #     if value['ul_tcp_flag']==True: #上行tcp
    #         print 'ul_tcp_flag_1'
    #     else:
    #         print 'ul_tcp_flag_0'
    #     if value['dl_tcp_flag']==True: # 下行tcp
    #         print 'dl_tcp_flag_1'
    #     else:
    #         print 'dl_tcp_flag_0'
    #
    #     if value['uldl_tcp_flag']==True: # 上下行同时灌包
    #         print 'uldl_tcp_flag_1'
    #
    #     else:
    #         print 'uldl_tcp_flag_0'
    #
    #     if value['ping_32_flag']==True:
    #         print 'ping_32_flag_1'
    #     else:
    #         print 'ping_32_flag_0'
    #     if value['ping_64_flag']==True:
    #         print 'ping_64_flag_1'
    #     else:
    #         print 'ping_64_flag_0'


window.close()