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
import os

# 体力
power = 96
# 每局消耗体力
consume = 4
# 计划打的局数
maxcount = 0
# 每局消耗时间
consumeTime = 33
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2


hwndSmall = win32gui.FindWindow(0, "捉鼠大师小叮当")
hwndBig = win32gui.FindWindow(0, "铁血战士胖虎")


def 开始组队魂十(hwndSmall,hwndBig) :

    maxcount = math.floor(power/consume)
    start = datetime.datetime.now()
    print("现在是：" +  str(start))
    print("预计组队挑战魂十 " + str(maxcount) + "局")
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
        print("开始打第 " + str(i + 1) + " 次")
        i += 1

        # 首先找到挑战坐标 点击
        CommonUtils.click_point_random(startX,startY,hwndSmall)
        wait = consumeTime + random.uniform(0.5,0.9)
        print("战斗中间间隔：" + str(wait) + " 秒")
        time.sleep(wait)
        # 打完后点击结算
        print("小号点击结算")
        overX,overY = overAddress[random.randint(0,9)].split(',')
        overXBig,overYBig = overAddress[random.randint(0,9)].split(',')
        CommonUtils.click_point_random(overX,overY,hwndSmall)
        print("大号点击结算")
        CommonUtils.click_point_random(overXBig,overYBig,hwndBig)
        wait = smallWaitTime + random.uniform(1.2, 1.4)

        print("结算中间间隔：" + str(wait) + " 秒")
        time.sleep(wait)
        print("小号再点击结算")
        CommonUtils.click_point_random(overX,overY,hwndSmall)
        print("大号再点击结算")
        CommonUtils.click_point_random(overXBig,overYBig,hwndBig)

        # 等待跳转
        time.sleep(bigWaitTime + random.uniform(0.2,0.6))


    startFile.close()
    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")
    # os.system('shutdown -s -t 1')  # 1代表一秒内关机，可自行设置


开始组队魂十(hwndSmall,hwndBig)

