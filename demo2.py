import win32gui, win32con, win32api,win32ui
import time
import CommonUtils
import random
import datetime

import async_all

# 体力
power = 200
# 每局消耗体力
consume = 8
# 计划打的局数
maxcount = 9
# 每局消耗时间
consumeTime = 23
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 1.5

successImg = './image/结界突破/success.png'
failImg = './image/结界突破/fail.png'
fail2Img = './image/结界突破/fail2.png'
startImg = './image/结界突破/start.png'
返回按钮Img = './image/结界突破/返回按钮.png'
退出确认按钮Img = './image/结界突破/退出确认按钮.png'
再次挑战按钮Img = './image/结界突破/再次挑战按钮.png'
再次挑战确认按钮Img = './image/结界突破/再次挑战确认按钮.png'


hwnd = win32gui.FindWindow(0, "铁血战士胖虎")


def 开始结界突破() :
    # 设置突破卷数量
    start = datetime.datetime.now()
    print("现在是：" +  str(start))
    print("预计挑战结界 " + str(maxcount) + "局")

    # 读取文件里的挑战坐标
    startAddress = []
    startFile = open('./address/结界突破/挑战坐标.txt')
    for line in startFile.readlines():
        line = line.strip('\n')
        startAddress.append(line)
    startFile.close()

    # 读取文件里的结算坐标
    overAddress = []
    overFile = open('./address/结界突破/结算坐标.txt')
    for line in overFile.readlines():
        line = line.strip('\n')
        overAddress.append(line)
    # 赋值完毕
    overFile.close()

    # 读取文件里的刷新坐标
    flushFile = open('./address/结界突破/刷新坐标.txt')
    flushtAddress = flushFile.read()
    flushX, flushY = flushtAddress.split(',')
    flushFile.close()

    # 用于计算已经攻击过的点
    totalAddress = []


    successTotal = 0
    # 开始执行任务
    for i in range(maxcount):
        print("------------------------")
        print("开始打第 " + str(i + 1) + " 次")


        print('返回退回2次')
        for j in range(2):
            j += 1
            while CommonUtils.openimages(返回按钮Img, hwnd) != 0:
                x, y = CommonUtils.openimages(返回按钮Img, hwnd)
                CommonUtils.click_point_random(x, y, hwnd)
                break
            time.sleep(random.uniform(1.0, 1.5))
            while CommonUtils.openimages(退出确认按钮Img, hwnd) != 0:
                x, y = CommonUtils.openimages(退出确认按钮Img, hwnd)
                CommonUtils.click_point_random(x, y, hwnd)
                break
            time.sleep(random.uniform(8.0, 9.5))

            while CommonUtils.openimages(再次挑战按钮Img, hwnd) != 0:
                x, y = CommonUtils.openimages(再次挑战按钮Img, hwnd)
                CommonUtils.click_point_random(x, y, hwnd)
                break
            time.sleep(random.uniform(1.0, 2.5))

            while CommonUtils.openimages(再次挑战确认按钮Img, hwnd) != 0:
                x, y = CommonUtils.openimages(再次挑战确认按钮Img, hwnd)
                CommonUtils.click_point_random(x, y, hwnd)
                break
            time.sleep(random.uniform(2.0, 3.5))


开始结界突破()