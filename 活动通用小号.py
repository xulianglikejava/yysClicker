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
maxcount = 150
# 每局消耗时间
consumeTime = 33
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2
# hwnd = win32gui.FindWindow(0, "铁血战士胖虎")
hwnd = CommonUtils.getSmallHwnd()
successImg = './image/活动通用/success.png'
success1Img = './image/活动通用/success1.png'
failImg = './image/活动通用/fail.png'
startImg = './image/活动通用/start.png'


def 开始挑战活动() :
    # 设置挑战次数
    start = datetime.datetime.now()
    print("现在是：" +  str(start))
    print("预计挑战活动 " + str(maxcount) + "局")

    # 读取文件里的结算坐标
    overAddress = []
    overFile = open('./address/活动通用/结算坐标.txt')
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
        print("开始打第 " + str(i+1) + " 次")
        i += 1
        startX,startY, = CommonUtils.openimages(startImg,hwnd)
        CommonUtils.click_point_random(startX, startY,hwnd)
        time.sleep(random.uniform(0.8, 1.2))
        playCount = 0
        while CommonUtils.openimages(startImg, hwnd) != 0:
            print("---没有成功进去挑战!!!---")
            playCount = playCount + 1
            if playCount > 3:
                return
            startX, startY, = CommonUtils.openimages(startImg, hwnd)
            CommonUtils.click_point_random(startX, startY, hwnd)
            time.sleep(random.uniform(1.0, 1.2))

        # 一把打完至少要120秒
        time.sleep(consumeTime)
        flag = 0
        # 循环截图 判断是否打完
        while flag == 0 :
            if CommonUtils.openimages(successImg,hwnd) == 0 or CommonUtils.openimages(success1Img,hwnd) == 0  :
                print("战斗还没结束...")
                time.sleep(3)
            else :
                overX, overY = overAddress[random.randint(0, 9)].split(',')
                print("点击结算")
                CommonUtils.click_point_random(overX, overY,hwnd)
                time.sleep(1 + random.uniform(0.5,0.8))
                # 检查一下
                print("检查一下")
                if CommonUtils.openimages(successImg, hwnd) != 0 or CommonUtils.openimages(success1Img, hwnd) != 0:
                    print("没有点成功啊")
                else:
                    flag = 1
                    break;
        time.sleep(2 + random.uniform(1.0,2.0))

    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")

开始挑战活动()

