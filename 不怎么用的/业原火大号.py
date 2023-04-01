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
maxcount = 22
# 每局消耗时间
consumeTime = 75
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2

hwnd = CommonUtils.getBigHwnd()
successImg = '../image/业原火/success.png'
failImg = '../image/业原火/fail.png'
startImg = '../image/业原火/start.png'


def 开始业原火() :
    # 设置挑战次数
    start = datetime.datetime.now()
    print("现在是：" +  str(start))
    print("预计挑战业原火 " + str(maxcount) + "局")

    # 读取文件里的结算坐标
    overAddress = []
    overFile = open('../address/业原火/结算坐标.txt')
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
        print("开始打第 " + str(i + 1) + " 次")
        i += 1
        # 首先找到挑战坐标 点击
        startX, startY, = CommonUtils.openimages(startImg, hwnd)
        CommonUtils.click_point_random(startX, startY, hwnd)
        time.sleep(random.uniform(0.8, 1.2))
        playCount = 0
        while CommonUtils.openimages(startImg, hwnd) != 0:
            print("---没有成功进去挑战!!!---")
            playCount = playCount + 1
            if playCount > 5:
                return
            startX, startY, = CommonUtils.openimages(startImg, hwnd)
            CommonUtils.click_point_random(startX, startY, hwnd)
            time.sleep(random.uniform(1.2, 1.8))
        # 一把打完至少要120秒
        time.sleep(consumeTime)
        flag = 0
        # 循环截图 判断是否打完
        while flag == 0 :
            if CommonUtils.openimages(successImg,hwnd) == 0 :
                print("战斗还没结束...")
                time.sleep(2)
            if CommonUtils.openimages(successImg,hwnd) != 0 :
                overX, overY = overAddress[random.randint(0, 9)].split(',')
                while CommonUtils.openimages(successImg, hwnd) != 0:
                    print("点击结算")
                    CommonUtils.click_point_random(overX, overY, hwnd)
                    time.sleep(random.uniform(1.2,1.6))
                    flag = 1
        time.sleep(smallWaitTime +random.uniform(1.2, 1.6))

    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")

开始业原火()

