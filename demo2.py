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
power = 200
# 每局消耗体力
consume = 8
# 计划打的局数
maxcount = 30
# 每局消耗时间
consumeTime = 23
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2

successImg = './image/结界突破/success.png'
failImg = './image/结界突破/fail.png'
startImg = './image/结界突破/start.png'
hwndSmall = win32gui.FindWindow(0, "铁血战士胖虎")

def 开始结界突破() :
    hwnd = hwndSmall
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
        i += 1


        # 首先找到挑战坐标 点击  每次挑战坐标全部随机 最后打完刷新
        tempAddr = random.randint(0,8)
        if i%10 == 0 and i != 0 :
            totalAddress = []
            CommonUtils.click_point_random(flushX,flushY,hwnd)
            time.sleep(5)
        # 正常流程

        if i%18 == 0 and i != 0 :
            totalAddress = []
            CommonUtils.click_point_random(flushX,flushY,hwnd)
            time.sleep(5)
        # 正常流程

        if i%29 == 0 and i != 0 :
            totalAddress = []
            CommonUtils.click_point_random(flushX,flushY,hwnd)
            time.sleep(5)
        # 正常流程

        while tempAddr in totalAddress:
            tempAddr = random.randint(0, 8)
        totalAddress.append(tempAddr)
        print(totalAddress)
        print("开始打第 " + str(tempAddr + 1) + " 个点")

    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")



开始结界突破()