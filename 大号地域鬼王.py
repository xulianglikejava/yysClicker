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

import async_all

# 体力
power = 392
# 每局消耗体力
consume = 8
# 计划打的局数
maxcount = 2
# 每局消耗时间
consumeTime = 80
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2

# 图片素材
探索Img = './image/通用图片/探索.png'
地域鬼王Img = './image/地域鬼王/地域鬼王.png'
筛选Img = './image/地域鬼王/筛选.png'
挑战Img = './image/地域鬼王/挑战.png'
准备Img = './image/地域鬼王/准备.png'
收藏按钮Img = './image/地域鬼王/收藏按钮.png'
收藏挑战1Img = './image/地域鬼王/收藏挑战1.png'
收藏挑战2Img = './image/地域鬼王/收藏挑战2.png'
红蛋蛋1Img = './image/地域鬼王/红蛋蛋1.png'
红蛋蛋2Img = './image/地域鬼王/红蛋蛋2.png'
红蛋蛋3Img = './image/地域鬼王/红蛋蛋3.png'
叉叉Img = './image/地域鬼王/叉叉.png'

hwnd = win32gui.FindWindow(0, "铁血战士胖虎")

# 读取文件里的挑战坐标
startAddress = []
startFile = open('./address/地域鬼王/鬼王坐标.txt')
for line in startFile.readlines():
    line = line.strip('\n')
    startAddress.append(line)
startFile.close()
# 读取文件里的结算坐标
overAddress = []
overFile = open('./address/地域鬼王/结算坐标.txt')
for line in overFile.readlines():
    line = line.strip('\n')
    overAddress.append(line)
# 赋值完毕
overFile.close()

# 读取文件里的红蛋坐标
redAddress = []
redFile = open('./address/地域鬼王/红蛋坐标.txt')
for line in redFile.readlines():
    line = line.strip('\n')
    redAddress.append(line)
# 赋值完毕
redFile.close()

# 读取文件里的关闭坐标
closeAddress = []
closeFile = open('./address/地域鬼王/关闭坐标.txt')
for line in closeFile.readlines():
    line = line.strip('\n')
    closeAddress.append(line)
# 赋值完毕
closeFile.close()

def 开始打地域鬼王() :
    start = datetime.datetime.now()
    print("现在是：" +  str(start))
    print("开始打地域鬼王")
    print('点击探索')

    # CommonUtils.click_point_random(833,200, hwnd)

    if CommonUtils.openimages(探索Img, hwnd) != 0 :
        x, y = CommonUtils.openimages(探索Img, hwnd)
        CommonUtils.click_point_random(x,y,hwnd)
    time.sleep(random.uniform(1.1, 2.5))

    print('点击地域鬼王图标')
    if CommonUtils.openimages(地域鬼王Img, hwnd) != 0:
        x, y = CommonUtils.openimages(地域鬼王Img, hwnd)
        CommonUtils.click_point_random(x, y, hwnd)
    time.sleep(random.uniform(1.1, 2.5))

    # 开始执行任务
    for i in range(maxcount):
        print("------------------------")
        print("开始打第 " + str(i + 1) + " 次")
        print('点击筛选')
        while CommonUtils.openimages(筛选Img, hwnd) != 0:
            x, y = CommonUtils.openimages(筛选Img, hwnd)
            CommonUtils.click_point_random(x, y, hwnd)
            break
        time.sleep(random.uniform(2.0, 2.5))
        print('收藏')
        while CommonUtils.openimages(收藏按钮Img, hwnd) != 0:
            x, y = CommonUtils.openimages(收藏按钮Img, hwnd)
            CommonUtils.click_point_random(x, y, hwnd)
            break
        time.sleep(random.uniform(2.0, 2.5))

        if i == 0 :
            print('收藏挑战1')
            while CommonUtils.openimages(收藏挑战1Img, hwnd) != 0:
                x, y = CommonUtils.openimages(收藏挑战1Img, hwnd)
                CommonUtils.click_point_random(x, y, hwnd)
                break
            time.sleep(random.uniform(2.0, 2.5))
        elif i == 1 :
            print('收藏挑战2')
            while CommonUtils.openimages(收藏挑战2Img, hwnd) != 0:
                x, y = CommonUtils.openimages(收藏挑战2Img, hwnd)
                CommonUtils.click_point_random(x, y, hwnd)
                break
            time.sleep(random.uniform(2.0, 2.5))
        print('挑战')
        while CommonUtils.openimages(挑战Img, hwnd) != 0:
            x, y = CommonUtils.openimages(挑战Img, hwnd)
            CommonUtils.click_point_random(x, y, hwnd)
            break
        time.sleep(random.uniform(4.0, 5.5))
        print('准备')
        while CommonUtils.openimages(准备Img, hwnd) != 0:
            x, y = CommonUtils.openimages(准备Img, hwnd)
            CommonUtils.click_point_random(x, y, hwnd)
            break
        time.sleep(consumeTime + random.uniform(2.0, 2.5))
        while CommonUtils.openimages(红蛋蛋1Img, hwnd) != 0:
            print('战斗结束')
            overX, overY = overAddress[random.randint(0, 9)].split(',')
            print("点击结算")
            CommonUtils.click_point_random(overX, overY, hwnd)
            time.sleep(random.uniform(2.1, 2.5))
            print("再点击结算")
            CommonUtils.click_point_random(overX, overY, hwnd)
            time.sleep(random.uniform(2.1, 3.5))
            break
        print('点击红蛋1')
        while CommonUtils.openimages(红蛋蛋1Img, hwnd) != 0:
            x, y = CommonUtils.openimages(红蛋蛋1Img, hwnd)
            CommonUtils.click_point_random(x, y, hwnd)
            time.sleep( random.uniform(2.0, 2.5))
            x, y = overAddress[random.randint(0, 9)].split(',')
            print("点击结算")
            CommonUtils.click_point_random(x, y, hwnd)
            break
        time.sleep(random.uniform(2.0, 2.5))
        print('点击红蛋2')
        while CommonUtils.openimages(红蛋蛋2Img, hwnd) != 0:
            x, y = CommonUtils.openimages(红蛋蛋2Img, hwnd)
            CommonUtils.click_point_random(x, y, hwnd)
            time.sleep( random.uniform(2.0, 2.5))
            x, y = overAddress[random.randint(0, 9)].split(',')
            print("点击结算")
            CommonUtils.click_point_random(x, y, hwnd)
            break
        time.sleep(random.uniform(2.0, 2.5))
        print('点击红蛋3')
        while CommonUtils.openimages(红蛋蛋3Img, hwnd) != 0:
            x, y = CommonUtils.openimages(红蛋蛋3Img, hwnd)
            CommonUtils.click_point_random(x, y, hwnd)
            time.sleep(  random.uniform(2.0, 2.5))
            x, y = overAddress[random.randint(0, 9)].split(',')
            print("点击结算")
            CommonUtils.click_point_random(x, y, hwnd)
            break
        time.sleep(random.uniform(2.0, 2.5))
        print('点击叉叉')
        while CommonUtils.openimages(叉叉Img, hwnd) != 0:
            x, y = CommonUtils.openimages(叉叉Img, hwnd)
            CommonUtils.click_point_random(x, y, hwnd)
            break

        i += 1


    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")



开始打地域鬼王()
