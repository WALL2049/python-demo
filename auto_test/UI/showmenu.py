import PySimpleGUI as sg
import os

mean = [
    ['file(&F)', ['new::new', 'open::open', '!save as', 'exit']],    # 快捷键：alt+F,注意key的设定
    ['edit(&E)', ['cut', 'copy', 'delete', '---', '!paste', 'find']],      # 注意分割线’---‘
    ['view(&V)', ['1::1', '!2', '3']]     # 注意'!'禁用，通常在事件触发后使用该功能
]
a = 'ping 192.168.3.1'
layout = [
    [sg.Menu(mean)],
    [sg.B('执行Ping包命令', key='ping_cmd'), sg.In(default_text=a, key='input123', size=(25))],
    [[sg.In()] for i in range(5)]
]



window = sg.Window('菜单演示', layout)

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == None:
        break
    if event == 'new::new':
        sg.popup('您点击了new!')
    if event == 'ping_cmd':
        os.system(values['input123'])


window.close()

