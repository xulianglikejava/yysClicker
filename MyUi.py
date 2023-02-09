import threading

import PySimpleGUI as sg
import matplotlib
from threading import Thread
import 结界突破大号川源专用
import 六道月之海川源
import 重命名大号


window = sg.Window('python小助手')
matplotlib.use("TkAgg")
sg.ChangeLookAndFeel('GreenTan')
menu_def = [['&使用说明', ['&注意']]]
layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('挑战次数', size=(10, 1)), sg.InputText(49 , key='maxcount')],
    [sg.Button('重命名大号', key='重命名大号'),sg.Button('大号结界突破', key='大号结界突破'),
     sg.Button('月之海', key='月之海')],
    [sg.Submit('处理', key='处理'), sg.Cancel('关闭')],
     [sg.Output(size=(60, 15))],
         ],
window = sg.Window('模板界面', layout, default_element_size=(40, 1), grab_anywhere=False)

while True:
    event, values = window.read()
    maxcount = int(values['maxcount'])
    if event == "重命名大号":
        重命名大号.rename()
    if event == "大号结界突破":
        结界突破大号川源专用.开始结界突破()
    if event == "月之海":
        六道月之海川源.开始六道月之海()




