import PySimpleGUI as sg

a = '这里是默认文本'
layout = [
    [sg.Text('网管地址',size=(8,1)),sg.Input(default_text=a,key='UME_ip')],
    [sg.Text('Ping包命令',size=(8,1)),sg.Input(default_text=a, key='ping_cmd')],
    [sg.Text('灌包任务名',size=(8,1)),sg.Input(default_text=a, key='task_name')],
    [sg.Text('基站ip',size=(8,1)),sg.Input(key='bs_ip')],
    [sg.Btn('触发网管UDP灌包任务', key='start_ume_udp_'), sg.Text('', key='_log_',  size=(20,1))],
    [sg.Btn('上行tcp', key='start_ul_tcp_')],
    [sg.Text('RCT',size=(8,1)),sg.Input(key='ul_tcp_RCT_cmd')],
    [sg.Text('CMD',size=(8,1)), sg.Input(key='ul_tcp_CMD_cmd')],
    [sg.Btn('下行tcp', key='start_dl_tcp_')],
    [sg.Text('CMD',size=(8,1)), sg.Input(key='dl_tcp_CMD_cmd')],
    [sg.Text('RCT',size=(8,1)), sg.Input(key='dl_tcp_RCT_cmd')],
    [sg.Btn('上下行tcp', key='start_uldl_tcp_')],
    [sg.Btn('ping包32字节', key='start_ping_32_'), sg.Text(''),sg.Input(key='ping_32_cmd')],
    [sg.Btn('ping包1500字节', key='start_ping_1500_'), sg.Input(key='ping_1500_cmd')],
    [sg.Btn('停止', key='_stop_'),sg.Text('                                                                         '),sg.Btn('写入默认值', key='_write_default_value_')],
    # [sg.Btn('tst', key='_tst_'),sg.Text('tst',key='hua')]
]



# 创建窗口，引入布局，并进行初始化
# 创建时，必须要有一个名称，这个名称会显示在窗口上

window = sg.Window('Baselinetool', layout=layout, finalize=True)
# key = Key('Chrome', 'headless')
while True:  # 创建一个事件循环，否则窗口运行一次就会被关闭
    event, value = window.Read()  # event, value 的值分别是 _LOGIN_ {'_USER_': 'admin', '_PWD_': '123'}
    print(event)
    print('-------------')
    print(value)
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

window.close()