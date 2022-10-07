import win32gui, win32con, win32api,win32ui
from win32clipboard import *
from PIL import Image
import cv2
import numpy as np
import aircv as ac
import random
import time
hwnd = win32gui.FindWindow(0, "阴阳师 - MuMu模拟器")
import CommonUtils
# hwnd = win32gui.FindWindow(0, "雷电模拟器")

a1 = "./image/28/11.png"
# 主页困28的入
a2 = "./image/kun28/a2.png"
# 识别探索入库
a3 = "./image/kun28/a3.png"
# 攻击小图
a3s = "./image/kun28/a3-1.png"
# 优先识别boss
a4 = "./image/kun28/a4.png"
# 结束1
a4s = "./image/kun28/a4-1.png"
# 结束时2
a5 = "./image/kun28/a5.png"
# 打完的小纸盒
a6 = "./image/kun28/a6.png"
# 点击返回按钮后的确定按钮
imagesList = [a1,a2,a3,a3s,a4,a4s,a5,a6]

# 简单点击事件
def click_point(x, y):
    # 模拟鼠标指针 传送到指定坐标
    long_position = win32api.MAKELONG(x, y)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    time.sleep(random.random(0.02 , 0.08))
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)


def makeimg():
    """
    后台截屏函数,并返回opencv的对象
    """
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bot - top
    #返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    hWndDC = win32gui.GetWindowDC(hwnd)
    #创建设备描述表
    mfcDC = win32ui.CreateDCFromHandle(hWndDC)
    #创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()
    #创建位图对象准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    #为bitmap开辟存储空间
    saveBitMap.CreateCompatibleBitmap(mfcDC,width,height)
    #将截图保存到saveBitMap中
    saveDC.SelectObject(saveBitMap)
    # 保存bitmap到内存设备描述表
    saveDC.BitBlt((0,0), (width,height), mfcDC, (0, 0), win32con.SRCCOPY)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    im_PIL = Image.frombuffer('RGB',(bmpinfo['bmWidth'],bmpinfo['bmHeight']),bmpstr,'raw','BGRX',0,1)
    im_PIL.save("screen.png") #保存
    im_PILs=cv2.cvtColor(np.array(im_PIL),cv2.COLOR_RGB2BGR)
    # pil转换格式到opencv
    return im_PILs

def openimages(template):
    """
    传入需要匹配的原图路径,返回值为,
    """
    templates = ac.imread(template)
    # 进行比对
    # templates = cv2.imread(template, cv2.IMREAD_UNCHANGED)
    # match_results = cv2.matchTemplate(source, templates, cv2.TM_CCOEFF_NORMED)
    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match_results)
    match_result = ac.find_template(makeimg(),templates,0.6)
    if match_result is not None:
        # 返回右上角的顶点，以及左下角的底点
    #    return match_result['rectangle'][0],match_result['rectangle'][3]
        x1 = random.randint(match_result['rectangle'][0][0],match_result['rectangle'][3][0])
        y1 = random.randint(match_result['rectangle'][0][1],match_result['rectangle'][3][1])
        print(x1,y1)
        return x1,y1
    else:
        return 0

def test():
    successImg = './image/结界突破/success.png'
    failImg = './image/结界突破/fail.png'
    startImg = './image/结界突破/start.png'
    print(CommonUtils.openimages(successImg))
    print(CommonUtils.openimages(failImg))

test()
