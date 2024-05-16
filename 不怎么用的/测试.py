import datetime

from 不怎么用的 import CommonUtils

金币 = '../image/魂土/金币.png'
阴阳师 = '../image/魂土/阴阳师.png'
hwnd = CommonUtils.getSmallHwnd()
hwndBig = CommonUtils.getBigHwnd()
hwndSmall = CommonUtils.getSmallHwnd()
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
    CommonUtils.saveImg(hwnd, imgName)


生成截图(CommonUtils.getBigHwnd())

