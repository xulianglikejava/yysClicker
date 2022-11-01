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
power = 392
# 每局消耗体力
consume = 8
# 计划打的局数
maxcount = 0
# 每局消耗时间
consumeTime = 24
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2

hwnd = win32gui.FindWindow(0, "铁血战士胖虎")

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
        CommonUtils.click_point_random(startX,startY,hwnd)
        wait = consumeTime + random.uniform(0.5,0.9)
        print("战斗中间间隔：" + str(wait) + " 秒")
        time.sleep(wait)
        # 打完后点击结算
        print("点击结算")
        overX,overY = overAddress[random.randint(0,9)].split(',')
        CommonUtils.click_point_random(overX,overY,hwnd)
        wait = smallWaitTime + random.uniform(1.2, 1.4)
        print("结算中间间隔：" + str(wait) + " 秒")
        time.sleep(wait)
        print("再点击结算")
        CommonUtils.click_point_random(overX,overY,hwnd)
        # 等待跳转
        time.sleep(bigWaitTime + random.uniform(0.1,0.3))


    startFile.close()
    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")


开始组队魂土()

