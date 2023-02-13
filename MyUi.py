import threading

import PySimpleGUI as sg
import matplotlib
from threading import Thread
import 六道月之海mumu
import 结界突破川源
import 重命名大号


window = sg.Window('python小助手')
matplotlib.use("TkAgg")
sg.ChangeLookAndFeel('GreenTan')
menu_def = [['&使用说明', ['&注意']]]
layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Button('月之海', key='月之海'),sg.Button('结界突破', key='结界突破')],
     [sg.Output(size=(60, 15))],
         ],
window = sg.Window('模板界面', layout, default_element_size=(40, 1), grab_anywhere=False)

while True:
    event, values = window.read()

    if event == "月之海":
        六道月之海川源.开始六道月之海()


    if event == "结界突破":
        结界突破川源.开始结界突破()

