import PySimpleGUI as sg

dict = {'k1' : 'v1',
        'k2' : 'v1',
        'k3' : 'v3'}

print(dict.items())
print(dict.keys())
print(dict.values())
list=[]
for i in dict:
    list.append(i)

layout=[
    [sg.Combo(list, key='-LB-', size=(30,6), enable_events=True)],
    [sg.T('语言'), sg.In(key='-YY-', size=(25))]
]

window = sg.Window('textUI', layout)

while True:
    event, values = window.read()
    print(event)
    print(sg.Combo.key)
    if event == None:
        break

window.close()
