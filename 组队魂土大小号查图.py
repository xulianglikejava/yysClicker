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
import logging

import async_all

# 体力
power = 350
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
挑战按钮 = './image/魂土/挑战按钮.png'
不可挑战按钮 = './image/魂土/不可挑战按钮.png'
成功 = './image/魂土/成功.png'
成功1 = './image/魂土/成功1.png'
hwndBig = win32gui.FindWindow(0, "铁血战士胖虎")
hwndSmall = win32gui.FindWindow(0, "捉鼠大师小叮当")


def 开始组队魂土() :
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

    for i in range(maxcount):
        print("------------------------")
        print("开始打第 " + str(i + 1) + " 次")
        i += 1

        # 首先找到挑战坐标 点击
        startX, startY, = CommonUtils.openimages(挑战按钮, hwndSmall)
        CommonUtils.click_point_random(startX, startY, hwndSmall)
        time.sleep(random.uniform(0.8, 1.2))
        playCount = 0
        while CommonUtils.openimages(挑战按钮, hwndSmall) != 0:
            print("---没有成功进去挑战!!!---")
            if CommonUtils.openimages(不可挑战按钮, hwndSmall) != 0:
                print('---队友没有进来---')
                return
            playCount = playCount + 1
            if playCount > 5:
                return
            startX, startY, = CommonUtils.openimages(挑战按钮, hwndSmall)
            CommonUtils.click_point_random(startX, startY, hwndSmall)
            time.sleep(random.uniform(1.2, 1.8))
        wait = consumeTime + random.uniform(0.5,0.9)
        print("战斗中间间隔：" + str(wait) + " 秒")
        time.sleep(wait)
        # 打完后点击结算
        flag = 0
        countTime = 0
        while flag == 0:
            if CommonUtils.openimages(成功, hwndSmall) == 0 and CommonUtils.openimages(成功1,hwndSmall) == 0:
                print("等待第 " + str(countTime + 1) + " 次...")
                countTime = countTime + 1
                time.sleep(1)

            elif CommonUtils.openimages(成功, hwndSmall) != 0 or CommonUtils.openimages(成功1,hwndSmall) != 0:
                print("小号找到完成图了")
                time.sleep(random.uniform(1.2, 2.3))
                print("小号点击结算")
                overX, overY = overAddress[random.randint(0, 9)].split(',')
                overXBig, overYBig = overAddress[random.randint(0, 9)].split(',')
                CommonUtils.click_point_random(overX, overY, hwndSmall)
                print("大号点击结算")
                CommonUtils.click_point_random(overXBig, overYBig, hwndBig)
                wait = smallWaitTime + random.uniform(0.3, 1)

                print("结算中间间隔：" + str(wait) + " 秒")
                time.sleep(wait)
                print("小号再点击结算")
                CommonUtils.click_point_random(overX, overY, hwndSmall)
                print("大号再点击结算")
                CommonUtils.click_point_random(overXBig, overYBig, hwndBig)
                # 等待跳转
                time.sleep(2.5 + random.uniform(1.2, 2.5))
                flag = 1
                break;


    startFile.close()
    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")
    # os.system('shutdown -s -t 1')  # 1代表一秒内关机，可自行设置


开始组队魂土()