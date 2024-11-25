import datetime
import os

import win32gui, win32con, win32api,win32ui
from PIL import Image
import cv2
import numpy as np
import aircv as ac
import random
import time


child_handles = []
SmallHwnd = 0
new_dir = "../Snipaste/"

加成按钮 = './image/通用图片/加成.png'
加成启动 = './image/通用图片/加成启动.png'
加成坐标 = './address/通用坐标/加成按钮坐标.txt'
邀请 = './image/通用图片/邀请.png'
邀请好友 = './image/通用图片/邀请好友.png'
队友 = './image/通用图片/队友.png'
接受邀请 = './image/通用图片/接受邀请.png'

# 简单漂移点击事件
def click_point_random(x,y,hwnd):
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

# 无偏移点击
def click_point(x,y,hwnd):
    # 模拟鼠标指针 传送到指定坐标
    # print("点击的坐标为：" + str(x) + "," + str(y))
    long_position = win32api.MAKELONG(x, y)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    time.sleep(random.uniform(0.08 , 0.20))
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)
def click_point_random_clear(x,y,hwnd):
    # 模拟鼠标指针 传送到指定坐标
    # 随机一下
    random1 = random.randint(0,10)
    if random1 > 5 :
        x = int(x) + random.randint(0,4)
        y = int(y) - random.randint(0,3)
    else:
        x = int(x) - random.randint(0,4)
        y = int(y) + random.randint(0,3)
    # print("点击的坐标为：" + str(x) + "," + str(y))
    long_position = win32api.MAKELONG(x, y)
    hwnd = win32gui.FindWindow(0, "阴阳师 - MuMu模拟器")
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    time.sleep(random.uniform(0.02 , 0.08))
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)
# 对窗口进行后台截图 并返回信息
def makeimg(hwnd):
    """
    后台截屏函数,并返回opencv的对象
    """
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    width = 540
    height = 960
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
    # pil转换格式到opencv
    win32gui.DeleteObject(saveBitMap.GetHandle())
    mfcDC.DeleteDC()
    saveDC.DeleteDC()
    im_PILs = cv2.cvtColor(np.array(im_PIL), cv2.COLOR_RGB2BGR)
    # pil转换格式到opencv
    return im_PILs

def saveImg(hwnd,ImgName):
    """
    后台截屏函数,并返回opencv的对象
    """
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    width = 540
    height = 960
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
    if not os.path.isdir(new_dir):
        os.makedirs(new_dir)
    im_PIL.save(new_dir+ImgName)
    # pil转换格式到opencv
    win32gui.DeleteObject(saveBitMap.GetHandle())
    mfcDC.DeleteDC()
    saveDC.DeleteDC()
    im_PILs = cv2.cvtColor(np.array(im_PIL), cv2.COLOR_RGB2BGR)

    # pil转换格式到opencv
    return im_PILs

# 传入小图信息 然后截屏里找大图 最后返回x，y坐标
def openimages(template,hwnd):
    """
    传入需要匹配的原图路径,返回值为,
    """
    # templates = ac.imread(template)
    templates = cv2.imdecode(np.fromfile(template, dtype=np.uint8), -1)  # 读取中文路径及名称

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
def winfun(hwnd, lparam):
    s = win32gui.GetWindowText(hwnd)
    if len(s) > 3:
        child_handles.clear()
        child_handles.append(hwnd)
    return 1
def getBigHwnd():
    hwnd = win32gui.FindWindow(None, "铁血战士胖虎")
    win32gui.EnumChildWindows(hwnd, winfun, None)
    return child_handles[0]
def getSmallHwnd():
    hwnd = win32gui.FindWindow(None, "捉鼠大师小叮当")
    win32gui.EnumChildWindows(hwnd, winfun, None)
    return child_handles[0]
# 直接点图，包含错误重试
def click_img(img,hwnd):
    startX, startY, = openimages(img, hwnd)
    click_point_random(startX, startY, hwnd)
    time.sleep(random.uniform(2.2, 2.8))
    playCount = 0
    while openimages(img, hwnd) != 0:
        print("---没有成功点击!!!---")
        playCount = playCount + 1
        if playCount > 3:
            return
        startX, startY, = openimages(img, hwnd)
        click_point_random(startX, startY, hwnd)
        time.sleep(random.uniform(2.2, 2.8))
# 直接点图，无错误重试
def click_img_no_retry(img,hwnd):
    startX, startY, = openimages(img, hwnd)
    click_point(startX, startY, hwnd)
    time.sleep(random.uniform(2.2, 2.8))
# 商店购买产品
def click_img_buy(img,hwnd):
    startX, startY, = openimages(img, hwnd)
    click_point_random(startX, startY, hwnd)
    time.sleep(random.uniform(2.2, 2.8))
# 打完怪选技能
def click_img_select(img,hwnd):
    startX, startY, = openimages(img, hwnd)
    startY = startY + 280
    click_point_random(startX, startY, hwnd)
    time.sleep(random.uniform(2.2, 2.8))
    playCount = 0
    while openimages(img, hwnd) != 0:
        print("---没有成功点击!!!---")
        playCount = playCount + 1
        if playCount > 10:
            return
        startX, startY, = openimages(img, hwnd)
        startY = startY + 280
        click_point_random(startX, startY, hwnd)
        time.sleep(random.uniform(2.2, 2.8))
# 打完怪选符咒
def click_img_select_fz(img,hwnd):
    startX, startY, = openimages(img, hwnd)
    startY = startY + 183
    if startY > 500 :
        startY = random.randint(445,455)
    click_point(startX, startY, hwnd)
    time.sleep(random.uniform(2.2, 2.8))
    playCount = 0
    while openimages(img, hwnd) != 0:
        print("---没有成功点击!!!---")
        playCount = playCount + 1
        if playCount > 10:
            return
        startX, startY, = openimages(img, hwnd)
        startY = startY + 183
        if startY > 500:
            startY = random.randint(445, 455)
        click_point(startX, startY, hwnd)
        time.sleep(random.uniform(2.2, 2.8))


def getBigHwndMuMu():
    hwnd = win32gui.FindWindow(0, "抖音-记录美好生活 - Google Chrome")
    return hwnd
def getSmallHwndMuMu():
    hwnd = win32gui.FindWindow(0, "#N1 阴阳师 - MuMu模拟器")
    return hwnd

def getMuMu():
    hwnd_list = []
    win32gui.EnumWindows(callback, hwnd_list)
    return hwnd_list


def callback(hwnd, extra):
    if "铁血战士胖虎" in win32gui.GetWindowText(hwnd):
        extra.append(hwnd)



def 生成截图(hwnd):
    imgName = str(datetime.datetime.now()).split(".")[0].replace(" ","_").replace(":","_");
    imgName = "Snipaste_" + imgName + ".png"
    print(imgName)
    saveImg(hwnd,imgName)

def 打开御魂经验加成(hwndSmall,hwndBig):
    # 读取文件里的结算坐标
    clickAddress = []
    overFile = open(加成坐标,'r', encoding='utf-8')
    for line in overFile.readlines():
        line = line.strip('\n')
        clickAddress.append(line)
    # 赋值完毕
    overFile.close()
    # 加成坐标
    # 御魂加成
    itemXSmall, itemYSmall = clickAddress[3].split(',')
    itemXSmall = int(itemXSmall)
    itemYSmall = int(itemYSmall)
    # 经验50%加成
    exp50XSmall, exp50YSmall = clickAddress[5].split(',')
    exp50XSmall = int(exp50XSmall)
    exp50YSmall = int(exp50YSmall)
    # 经验100%加成
    exp100XSmall, exp100YSmall = clickAddress[7].split(',')
    exp100XSmall = int(exp100XSmall)
    exp100YSmall = int(exp100YSmall)
    print("小号打开加成页面")
    click_img_no_retry(加成按钮, hwndSmall)
    print("大号打开加成页面")
    click_img_no_retry(加成按钮, hwndBig)
    time.sleep(random.uniform(0.6, 1));
    if openimages(加成启动, hwndSmall) == 0:
        print("小号打开御魂加成")
        click_point(itemXSmall, itemYSmall, hwndSmall)
    if openimages(加成启动, hwndBig) == 0:
        print("大号打开御魂加成")
        click_point(itemXSmall, itemYSmall, hwndBig)
        time.sleep(random.uniform(0.6, 1));
        print("大号打开经验50%加成")
        click_point(exp50XSmall, exp50YSmall, hwndBig)
        time.sleep(random.uniform(0.6, 1));
        print("大号打开经验100%加成")
        click_point(exp100XSmall, exp100YSmall, hwndBig)
        time.sleep(random.uniform(0.6, 1));
    print("小号关闭加成页面")
    click_img_no_retry(加成按钮, hwndSmall)
    print("大号关闭加成页面")
    click_img_no_retry(加成按钮, hwndBig)


def 打开御魂加成(hwndSmall,hwndBig):
    # 读取文件里的结算坐标
    clickAddress = []
    overFile = open(加成坐标,'r', encoding='utf-8')
    for line in overFile.readlines():
        line = line.strip('\n')
        clickAddress.append(line)
    # 赋值完毕
    overFile.close()
    # 加成坐标
    # 御魂加成
    itemXSmall, itemYSmall = clickAddress[3].split(',')
    itemXSmall = int(itemXSmall)
    itemYSmall = int(itemYSmall)
    print("小号打开加成页面")
    click_img_no_retry(加成按钮, hwndSmall)
    print("大号打开加成页面")
    click_img_no_retry(加成按钮, hwndBig)
    time.sleep(random.uniform(0.6, 1));
    if openimages(加成启动, hwndSmall) == 0:
        print("小号打开御魂加成")
        click_point(itemXSmall, itemYSmall, hwndSmall)
    if openimages(加成启动, hwndBig) == 0:
        print("大号打开御魂加成")
        click_point(itemXSmall, itemYSmall, hwndBig)
        time.sleep(random.uniform(0.6, 1));
    print("小号关闭加成页面")
    click_img_no_retry(加成按钮, hwndSmall)
    print("大号关闭加成页面")
    click_img_no_retry(加成按钮, hwndBig)


def 关闭加成(hwndSmall,hwndBig):
    # 读取文件里的结算坐标
    clickAddress = []
    overFile = open(加成坐标, 'r', encoding='utf-8')
    for line in overFile.readlines():
        line = line.strip('\n')
        clickAddress.append(line)
    # 赋值完毕
    overFile.close()
    print("小号打开加成菜单")
    click_img_no_retry(加成按钮, hwndSmall)
    print("大号打开加成菜单")
    click_img_no_retry(加成按钮, hwndBig)
    time.sleep(random.uniform(0.6, 1));
    print("小号关闭加成")
    while openimages(加成启动, hwndSmall) != 0:
        click_img_no_retry(加成启动,hwndSmall)
        time.sleep(random.uniform(0.6, 1));

    print("大号关闭加成")
    while openimages(加成启动, hwndBig) != 0:
        click_img_no_retry(加成启动,hwndBig)
        time.sleep(random.uniform(0.6, 1));
    print("小号关闭加成菜单")
    click_img_no_retry(加成按钮, hwndSmall)
    print("大号关闭加成菜单")
    click_img_no_retry(加成按钮, hwndBig)

def 邀请队友(hwndSmall,hwndBig):
    click_img_no_retry(邀请, hwndSmall)
    time.sleep(random.uniform(0.6, 1));
    click_img_no_retry(队友, hwndSmall)
    time.sleep(random.uniform(2.6, 3));
    click_img(邀请好友, hwndSmall)
    time.sleep(random.uniform(0.6, 1));
    click_img(接受邀请, hwndBig)



