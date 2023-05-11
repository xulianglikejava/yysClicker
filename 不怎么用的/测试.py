import datetime

import win32gui, win32con, win32api,win32ui

import CommonUtils
import subprocess
import async_all
金币 = '../image/魂土/金币.png'
阴阳师 = '../image/魂土/阴阳师.png'
hwnd = CommonUtils.getSmallHwnd()
探索 = '../image/通用图片/探索.png'
# 模拟器的设备ID
DEVICE_ID = '127.0.0.1:16416'

# 点击的坐标
X_COORDINATE = 500
Y_COORDINATE = 145

def 生成截图(hwnd):
    imgName = str(datetime.datetime.now()).split(".")[0].replace(" ","_").replace(":","_");
    imgName = str(hwnd) + "Snipaste_" + imgName + ".png"
    print(imgName)
    CommonUtils.saveImg(hwnd,imgName)

def 获取余额():
    imgName = str(datetime.datetime.now()).split(".")[0].replace(" ", "_").replace(":", "_");
    imgName = "钱.png"
    CommonUtils.get_money(hwnd,imgName)
def 点击():
    hwnd_list = CommonUtils.getMuMu();
    print(hwnd_list)
    CommonUtils.click_img(阴阳师,hwnd_list[0])
    生成截图(hwnd_list[1])
    CommonUtils.click_img(阴阳师,hwnd_list[1])
    # subprocess.run(['adb', 'connect', DEVICE_ID])
    #
    # # 等待连接建立
    #
    # # 构建adb命令
    # adb_cmd = ['adb', '-s', DEVICE_ID, 'shell', 'input', 'tap', str(X_COORDINATE), str(Y_COORDINATE)]
    #
    # # 执行adb命令
    # subprocess.run(adb_cmd)

点击()

