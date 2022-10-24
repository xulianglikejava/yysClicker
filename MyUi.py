import PySimpleGUI as sg
import matplotlib

import 业原火大号
import 御灵大号
import 组队探索专用
import 组队魂十专用
import 组队魂土
import 结界突破大号
import 结界突破小号
import 重命名大号
import 重命名小号

window = sg.Window('python小助手')
matplotlib.use("TkAgg")
sg.ChangeLookAndFeel('GreenTan')
menu_def = [['&使用说明', ['&注意']]]
layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Button('重命名大号', key='重命名大号'),sg.Button('重命名小号', key='重命名小号'),
     sg.Button('大号结界突破', key='大号结界突破'),  sg.Button('小号结界突破', key='小号结界突破')],
    [sg.Button('组队魂十', key='组队魂十'), sg.Button('组队探索', key='组队探索'),
     sg.Button('大号御灵', key='大号御灵'), sg.Button('大号业原火', key='大号业原火')],
    [sg.Button('组队魂土', key='组队魂土'), sg.Button('待开发', key='待开发'),
     sg.Submit('处理', key='处理'), sg.Cancel('关闭')],
    # [sg.ML(default_text='小助手启动了 ' , size=(50,10), key='showlog',write_only=True, reroute_stdout=False,autoscroll=True)],
    # [sg.Output(size=(60, 15))],
         ],

window = sg.Window('模板界面', layout, default_element_size=(40, 1), grab_anywhere=False)

while True:
    event, values = window.read()
    if event == "重命名大号":
        重命名大号.rename()

    if event == "重命名小号":
        重命名小号.rename()

    if event == "大号结界突破":
        结界突破大号.开始结界突破()

    if event == "小号结界突破":
        结界突破小号.开始结界突破()

    if event == "组队魂十":
        组队魂十专用.开始组队魂十()

    if event == "组队探索":
        组队探索专用.开始组队探索()

    if event == "大号御灵":
        御灵大号.开始御灵()

    if event == "大号业原火":
        业原火大号.开始业原火()

    if event == "组队魂土":
        组队魂土.开始组队魂土()
