import PySimpleGUI as sg

# sg.theme_previewer()
# print(sg.theme_list())
sg.theme('LightGreen1')
sg.Popup('弹窗演示')
# print(sg.theme_button_color())
sg.theme_button_color(('black', 'white'))      # 按键文字颜色，和按键背景色
sg.Popup('弹窗演示，改变颜色')




# 2)定义布局，确定行数
layout = [
    [sg.Text(i) for i in 'abcd'],
    [[sg.In(i)] for i in ['北京','上海','广州','深圳']]
    # [[sg.InputText(i)] for i in ['北京','上海','广州','深圳']]
]
# 3)创建窗口
window = sg.Window('PySimpleUI学习', layout)

# 4)事件循环
while True:
    event, values = window.read()
    if event == None:  # 窗口关闭事件
        break
    # if event= sg.WIN_CLOSED:  # 窗口关闭事件
    #     break
    if event == 'a':    # 判断事件是否发生
            print('点击了a')  #事件发生时要处理执行的任务
            sg.Popup('执行a任务')
# 5)关闭窗口
window.close()

