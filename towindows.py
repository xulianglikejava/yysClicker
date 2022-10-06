import win32gui, win32con, win32api,win32ui
from win32clipboard import *
from PIL import Image
import cv2
import numpy as np
import aircv as ac
from math import pow
import random

hwnd = win32gui.FindWindow(0, "阴阳师 - MuMu模拟器" )


def click_point(x, y):
    long_position = win32api.MAKELONG(x, y)#模拟鼠标指针 传送到指定坐标
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)#模拟鼠标按下
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)#模拟鼠标弹起


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
    # im_PIL.save("im_PIL.png") #保存
    im_PILs=cv2.cvtColor(np.array(im_PIL),cv2.COLOR_RGB2BGR)
    # pil转换格式到opencv
    return im_PILs

def openimages(template):
    """
    传入需要匹配的原图路径,返回值为,
    """
    templates = ac.imread(template)
    # 进行比对
    #  match_results = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    match_result = ac.find_template(makeimg(),templates,0.9)
    if match_result is not None:
        # 返回右上角的顶点，以及左下角的底点
    #    return match_result['rectangle'][0],match_result['rectangle'][3]
        x1 = random.randint(match_result['rectangle'][0][0],match_result['rectangle'][3][0])
        y1 = random.randint(match_result['rectangle'][0][1],match_result['rectangle'][3][1])
        print(x1,y1)
        return x1,y1
    else:
        return 0

def movwwindow(x1,y1):
        """
        关于移动窗口的的方法
        示例movwwindow(10,10)
        """
        #  获取句柄
        hwnd = win32gui.FindWindow(0, "阴阳师 - MuMu模拟器")
        # 固定大小
        x2 = 978   #宽
        y2 = 587   #高
        win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST, x1, y1, x2, y2, win32con.SWP_SHOWWINDOW)
        #需要地点窗口位置置于底层
        return 1
        #关于窗口的代码
