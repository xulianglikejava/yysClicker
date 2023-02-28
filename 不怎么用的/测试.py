import datetime

import win32gui, win32con, win32api,win32ui

import CommonUtils
import async_all

hwnd = CommonUtils.getBigHwnd()

def 生成截图(hwnd):
    imgName = str(datetime.datetime.now()).split(".")[0].replace(" ","_").replace(":","_");
    imgName = "Snipaste_" + imgName + ".png"
    print(imgName)
    CommonUtils.saveImg(hwnd,imgName)

def 获取余额():
    imgName = str(datetime.datetime.now()).split(".")[0].replace(" ", "_").replace(":", "_");
    imgName = "钱.png"
    CommonUtils.get_money(hwnd,imgName)

获取余额()

