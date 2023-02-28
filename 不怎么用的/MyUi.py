import PySimpleGUI as sg
import matplotlib
from 不怎么用的 import 结界突破川源

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

