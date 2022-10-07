import win32gui, win32con, win32api,win32ui
from win32clipboard import *
from PIL import Image
import cv2
import numpy as np
import aircv as ac
import random
import time

import start业原火
import start御灵
import start组队魂土
import start结界突破

hwnd = win32gui.FindWindow(0, "阴阳师 - MuMu模拟器")
import CommonUtils



def test():
    print("准备打什么？")
    print("1--组队魂十")
    print("2--结界突破")
    print("3--业原火")
    print("4--业原火")
    taskid = input("请输入")
    if taskid == 1:
        start组队魂土.开始组队魂土()
    elif taskid == 2:
        start结界突破.开始结界突破()
    elif taskid == 3:
        start业原火.开始业原火()
    elif taskid == 4:
        start御灵.开始御灵()

test()
