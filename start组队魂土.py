import math
import win32gui, win32con, win32api,win32ui
from PIL import Image
import cv2
import numpy as np
import aircv as ac
import time
import CommonUtils
import random
import datetime

# 体力
power = 92
# 每局消耗体力
consume = 8
# 计划打的局数
maxcount = 0
# 每局消耗时间
consumeTime = 23
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2

hwnd = win32gui.FindWindow(0, "阴阳师 - MuMu模拟器")
# hwnd = win32gui.FindWindow(0, "MuMu模拟器")

# 简单点击事件
def click_point(x,y):
    # 模拟鼠标指针 传送到指定坐标
    long_position = win32api.MAKELONG(x, y)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    time.sleep(random.random(0.02 , 0.08))
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)

# 简单点击事件
def click_point_random(x,y):
    # 模拟鼠标指针 传送到指定坐标
    # 随机一下
    random1 = random.randint(0,10)
    if random1 > 5 :
        x = int(x) + random.randint(0,4)
        y = int(y) - random.randint(0,3)
    else:
        x = int(x) - random.randint(0,4)
        y = int(y) + random.randint(0,3)
    print("点击的坐标为：" + str(x) + "," + str(y))
    long_position = win32api.MAKELONG(x, y)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    time.sleep(random.uniform(0.02 , 0.08))
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)

# 对窗口进行后台截图 并返回信息
def makeimg(self):
    """
    后台截屏函数,并返回opencv的对象
    """
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bot - top
    # 返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    hWndDC = win32gui.GetWindowDC(hwnd)
    # 创建设备描述表
    mfcDC = win32ui.CreateDCFromHandle(hWndDC)
    # 创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建位图对象准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 为bitmap开辟存储空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    # 将截图保存到saveBitMap中
    saveDC.SelectObject(saveBitMap)
    # 保存bitmap到内存设备描述表
    saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    im_PIL = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
    # im_PIL.save("screen.png")  # 保存
    im_PILs = cv2.cvtColor(np.array(im_PIL), cv2.COLOR_RGB2BGR)
    # pil转换格式到opencv
    return im_PILs

# 传入小图信息 然后截屏里找大图 最后返回x，y坐标
def openimages(template):
    """
    传入需要匹配的原图路径,返回值为,
    """
    templates = ac.imread(template)
    # 进行比对
    # templates = cv2.imread(template, cv2.IMREAD_UNCHANGED)
    # match_results = cv2.matchTemplate(source, templates, cv2.TM_CCOEFF_NORMED)
    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match_results)
    match_result = ac.find_template(makeimg(hwnd), templates, 0.6)
    if match_result is not None:
        # 返回右上角的顶点，以及左下角的底点
        #    return match_result['rectangle'][0],match_result['rectangle'][3]
        x1 = random.randint(match_result['rectangle'][0][0], match_result['rectangle'][3][0])
        y1 = random.randint(match_result['rectangle'][0][1], match_result['rectangle'][3][1])
        return x1, y1
    else:
        return 0


def 开始组队魂土() :
    maxcount = math.floor(power/consume)
    start = datetime.datetime.now()
    print("现在是：" +  str(start))
    print("预计组队挑战魂土 " + str(maxcount) + "局")
    # 读取文件里的挑战坐标
    startFile = open('./address/组队魂土/挑战坐标.txt')
    startAddress = startFile.read()
    startX,startY = startAddress.split(',')
    startFile.close()

    # 读取文件里的结算坐标
    overAddress = []
    overFile = open('./address/组队魂土/结算坐标.txt')
    for line in overFile.readlines():
        line = line.strip('\n')
        overAddress.append(line)
    # 赋值完毕

    # 开始执行任务
    for i in range(maxcount):
        print("------------------------")
        print("开始打第 " + str(i) + " 次")
        i += 1

        # 首先找到挑战坐标 点击
        click_point_random(startX,startY)
        wait = consumeTime + random.uniform(0.5,0.9)
        print("战斗中间间隔：" + str(wait) + " 秒")
        time.sleep(wait)
        # 打完后点击结算
        print("点击结算")
        overX,overY = overAddress[random.randint(0,9)].split(',')
        click_point_random(overX,overY)
        wait = smallWaitTime + random.uniform(1.2, 1.4)
        print("结算中间间隔：" + str(wait) + " 秒")
        time.sleep(wait)
        print("再点击结算")
        click_point_random(overX,overY)
        # 等待跳转
        time.sleep(bigWaitTime + random.uniform(0.2,0.6))


    startFile.close()
    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")


开始组队魂土()

