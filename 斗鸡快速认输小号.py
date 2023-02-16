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
maxcount = 20
# 每局消耗时间
consumeTime = 5
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2
战斗 = './image/斗鸡/战斗.png'
返回 = './image/斗鸡/返回.png'
确认 = './image/斗鸡/确认.png'
取消 = './image/斗鸡/取消.png'
hwnd = CommonUtils.getSmallHwnd()


def 开始斗鸡() :
    start = datetime.datetime.now()
    print("现在是：" +  str(start))
    print("预计组队挑战斗鸡 " + str(maxcount) + "局")
    # 读取文件里的结算坐标
    overAddress = []
    overFile = open('./address/斗鸡/结算坐标.txt')
    for line in overFile.readlines():
        line = line.strip('\n')
        overAddress.append(line)
    # 赋值完毕

    for i in range(maxcount):
        print("------------------------")
        print("开始打第 " + str(i + 1) + " 次")
        i += 1

        # 首先找到挑战坐标 点击
        while CommonUtils.openimages(战斗, hwnd) != 0:
            startX, startY, = CommonUtils.openimages(战斗, hwnd)
            CommonUtils.click_point_random(startX, startY, hwnd)
            time.sleep(random.uniform(0.8, 1.2))
        playCount = 0


        # 打完后点击结算
        flag = 0
        countTime = 0
        while flag == 0:
            if CommonUtils.openimages(取消, hwnd) != 0:
                print("等待第 " + str(countTime + 1) + " 次...")
                countTime = countTime + 1
                time.sleep(3)

            elif CommonUtils.openimages(返回, hwnd) != 0 and CommonUtils.openimages(取消, hwnd) == 0:
                print("找到对手了")
                time.sleep(random.uniform(5.2, 5.8))
                print("退出")
                CommonUtils.click_img_no_retry(返回, hwnd)
                time.sleep(random.uniform(2.2, 2.8))
                print("确认")
                while CommonUtils.openimages(确认, hwnd) == 0:
                    CommonUtils.click_img_no_retry(返回, hwnd)
                CommonUtils.click_img(确认, hwnd)
                time.sleep(random.uniform(2.2, 2.8))
                overX, overY = overAddress[random.randint(0, 9)].split(',')
                print("点击结算")
                CommonUtils.click_point_random(overX, overY, hwnd)
                time.sleep(random.uniform(3.2, 4.8))

                flag = 1
                break;


    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")
    # os.system('shutdown -s -t 1')  # 1代表一秒内关机，可自行设置


开始斗鸡()