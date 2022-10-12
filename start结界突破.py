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
maxcount = 0
# 每局消耗时间
consumeTime = 23
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2

hwnd = win32gui.FindWindow(0, "阴阳师 - MuMu模拟器")
# hwnd = win32gui.FindWindow(0, "MuMu模拟器")
successImg = './image/结界突破/success.png'
failImg = './image/结界突破/fail.png'
startImg = './image/结界突破/start.png'


def 开始结界突破() :
    # 设置突破卷数量
    maxcount = 6
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
        tempAddr = random.randint(0,9)
        if i%9 == 0 and i != 0 :
            totalAddress = []
            CommonUtils.click_point_random(flushX,flushY)
            time.sleep(5)
        # 正常流程

        while tempAddr in totalAddress:
            tempAddr = random.randint(0, 9)
        totalAddress.append(tempAddr)
        print("开始打第 " + str(tempAddr + 1) + " 个点")
        startX, startY, againX, againY = startAddress[tempAddr].split(',')
        CommonUtils.click_point_random(startX,startY)
        time.sleep(random.uniform(2.1,2.9))

        if CommonUtils.openimages(startImg) == 0:
            CommonUtils.click_point_random(startX, startY)
        if CommonUtils.openimages(startImg) != 0:
            againX, againY = CommonUtils.openimages(startImg)
            CommonUtils.click_point_random(againX, againY)

        # 一把打完至少要三十秒
        time.sleep(25)
        # 循环找图用的
        flag = 0
        # 由于计算等待次数
        countTime = 0

        # 循环截图 判断是否打完
        while flag == 0 :

            if CommonUtils.openimages(successImg) == 0 and CommonUtils.openimages(failImg) == 0:
                print("等待第 " + str(countTime + 1 ) + " 次...")
                countTime = countTime + 1
                time.sleep(5)
                if countTime > 15 :
                    overX, overY = overAddress[random.randint(0, 9)].split(',')
                    print("等不下去了，随便点一点")
                    break;


            elif CommonUtils.openimages(successImg) != 0 :
                # 如果成功 那么成功次数加一  加一后再计算是否是第三次 如果是得多点次
                successTotal = successTotal + 1
                overX, overY = overAddress[random.randint(0, 9)].split(',')
                print("点击结算")
                print("已经成功打完了第" + str(successTotal + 1 ) + " 次...")
                CommonUtils.click_point_random(overX, overY)
                if successTotal != 0 and successTotal % 3 == 0 :
                    print("点击弹窗胜利")
                    CommonUtils.click_point_random(overX, overY)
                flag = 1
                break;
            elif CommonUtils.openimages(failImg) != 0:
                overX, overY = overAddress[random.randint(0, 9)].split(',')
                print("点击结算")
                CommonUtils.click_point_random(overX, overY)
                flag = 1
                break;

        time.sleep(bigWaitTime + random.uniform(1.4,2.5))

    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")


开始结界突破()

