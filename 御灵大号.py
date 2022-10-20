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
power = 192
# 每局消耗体力
consume = 8
# 计划打的局数
maxcount = 50
# 每局消耗时间
consumeTime = 50
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2

hwndBig = win32gui.FindWindow(0, "铁血战士胖虎")
# hwnd = win32gui.FindWindow(0, "MuMu模拟器")
successImg = './image/御灵/success.png'
failImg = './image/御灵/fail.png'
startImg = './image/御灵/start.png'


def 开始御灵() :
    hwnd = CommonUtils.get_child_windows(hwndBig)

    # 设置挑战次数
    start = datetime.datetime.now()
    print("现在是：" +  str(start))
    print("预计挑战御灵 " + str(maxcount) + "局")

    # 读取文件里的结算坐标
    overAddress = []
    overFile = open('./address/御灵/结算坐标.txt')
    for line in overFile.readlines():
        line = line.strip('\n')
        overAddress.append(line)
    # 赋值完毕
    overFile.close()

    # 用于计算已经攻击过的点
    totalAddress = []

    # 开始执行任务
    for i in range(maxcount):
        print("------------------------")
        print("开始打第 " + str(i + 1 ) + " 次")
        i += 1
        startX,startY, = CommonUtils.openimages(startImg,hwnd)
        CommonUtils.click_point_random(startX, startY,hwnd)
        # 一把打完至少要120秒
        time.sleep(consumeTime)
        flag = 0
        # 循环截图 判断是否打完
        while flag == 0 :
            if CommonUtils.openimages(successImg,hwnd) == 0 and CommonUtils.openimages(failImg,hwnd) == 0:
                print("战斗还没结束...")
                time.sleep(5)
            else :
                overX, overY = overAddress[random.randint(0, 9)].split(',')
                print("点击结算")
                CommonUtils.click_point_random(overX, overY,hwnd)
                time.sleep(smallWaitTime + random.uniform(0.2,0.5))
                CommonUtils.click_point_random(overX, overY,hwnd)
                flag = 1
                break;
        time.sleep(bigWaitTime + random.uniform(0.2,0.6))

    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")



