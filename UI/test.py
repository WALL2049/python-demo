import PySimpleGUI as sg

layout= [
[sg.B('中文'), sg.B('English')],
[sg.T('请输入您的基本信息', key='--BEGIN--')],
[sg.T('姓名', key='--NAME--', size=(8,1)), sg.In('例如：李明')],
[sg.T('性别', key='--GENDER--', size=(8,1)), sg.In('')],
[sg.T('年龄', key='--AGE--', size=(8,1)), sg.In('')],
[sg.B('确定', key='--CONFIRM--', size=(8,1)),sg.B('取消', key='--CANCEL--')]

         ]

window= sg.Window("中英文语言转换", layout)

while True:
    event, values= window.read()
    print(event)
    if event == None:
        break
    if event == '--CANCEL--':
        break

    if event == '中文':
        # window['--BEGIN--'].update(value='请输入您的基本信息：')
        window['--BEGIN--'].update('请输入您的基本信息：')
        window['--NAME--'].update('姓名')
        window['--GENDER--'].update('性别')
        window['--AGE--'].update('年龄')
        window['--CONFIRM--'].update('确认')
        window['--CANCEL--'].update('取消')

    if event == 'English':
        window['--BEGIN--'].update('Please input basic information:')
        window['--NAME--'].update('NAME')
        window['--GENDER--'].update('GENDER')
        window['--AGE--'].update('AGE')
        window['--CONFIRM--'].update('CONFIRM')
        window['--CANCEL--'].update('CANCEL')

window.close()


