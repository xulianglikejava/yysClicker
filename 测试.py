import datetime

import win32gui, win32con, win32api,win32ui

import CommonUtils
import async_all

hwnd = win32gui.FindWindow(0, "阴阳师 - MuMu模拟器")



def 生成截图(hwnd):
    imgName = str(datetime.datetime.now()).split(".")[0].replace(" ","_").replace(":","_");
    imgName = "Snipaste_" + imgName + ".png"
    print(imgName)
    CommonUtils.saveImg(hwnd,imgName)


