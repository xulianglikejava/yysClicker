import threading

import PySimpleGUI as sg
import matplotlib
from threading import Thread
import 业原火大号
import 组队魂土大小号
import 组队魂土同心队
import 结界突破大号
import 结界突破小号
import 重命名大号
import 重命名小号
from demo2 import stop_thread

window = sg.Window('python小助手')
matplotlib.use("TkAgg")
sg.ChangeLookAndFeel('GreenTan')
menu_def = [['&使用说明', ['&注意']]]
layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('挑战次数', size=(10, 1)), sg.InputText(49 , key='maxcount')],
    [sg.Button('重命名大号', key='重命名大号'),sg.Button('重命名小号', key='重命名小号'),
     sg.Button('大号结界突破', key='大号结界突破'),  sg.Button('小号结界突破', key='小号结界突破')],
    [sg.Button('组队魂土大小号', key='组队魂土大小号'), sg.Button('组队魂土同心队', key='组队魂土同心队'),
     sg.Button('停止组队魂土大小号', key='停止组队魂土大小号'), sg.Button('大号业原火', key='大号业原火')],

    [sg.Button('组队魂土', key='组队魂土'), sg.Button('待开发', key='待开发'),
     sg.Submit('处理', key='处理'), sg.Cancel('关闭')],
     [sg.Output(size=(60, 15))],
         ],

window = sg.Window('模板界面', layout, default_element_size=(40, 1), grab_anywhere=False)

while True:
    event, values = window.read()
    maxcount = int(values['maxcount'])
    if event == "重命名大号":
        重命名大号.rename()
    if event == "重命名小号":
        重命名小号.rename()

    if event == "大号结界突破":
        结界突破大号.开始结界突破()

    if event == "小号结界突破":
        结界突破小号.开始结界突破()

    if event == "组队魂土大小号":
        组队魂土大小号.开始组队魂土(maxcount)

    if event == "组队魂土同心队":
        组队魂土同心队.开始组队魂土(maxcount)

    if event == "停止组队魂土大小号":
        print("停止组队魂土大小号")
        id = threading.get_ident();
        print(id)
        stop_thread(id)


