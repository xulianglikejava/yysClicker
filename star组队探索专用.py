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
power = 230
# 每局消耗体力
consume = 3
# 计划打的局数
maxcount = 0
# 每局消耗时间
consumeTime = 13
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2

# hwnd = win32gui.FindWindow(0, "阴阳师 - MuMu模拟器")
hwndBig = win32gui.FindWindow(0, "铁血战士胖虎")
hwndSmall = win32gui.FindWindow(0, "捉鼠大师小叮当")


# 图片素材
successImg = './image/探索/success.png'
startImg = './image/探索/start.png'
fightImg = './image/探索/fight.png'
fightImg2 = './image/探索/fight2.png'
giftImg = './image/探索/gift.png'
sureImg = './image/探索/sure.png'
makesureImg = './image/探索/makesure.png'


def 开始组队探索() :
    maxcount = math.floor(power/consume)
    start = datetime.datetime.now()
    print("现在是：" +  str(start))
    print("预计组队挑战探索 " + str(maxcount) + "局")

    # 读取文件里的结算坐标
    overAddress = []
    overFile = open('./address/探索/结算坐标.txt')
    for line in overFile.readlines():
        line = line.strip('\n')
        overAddress.append(line)
    # 赋值完毕
    overFile.close()

    # 读取文件里的走动坐标
    moveAddress = []
    moveFile = open('./address/探索/移动坐标.txt')
    for line in moveFile.readlines():
        line = line.strip('\n')
        moveAddress.append(line)
    # 赋值完毕
    moveFile.close()


    # 开始执行任务
    for i in range(maxcount):
        print("------------------------")
        print("开始打第 " + str(i + 1) + " 次")

        # 首先找到挑战坐标 点击
        if CommonUtils.openimages(startImg, hwndSmall) != 0:
            smallX,smallY = CommonUtils.openimages(startImg, hwndSmall)
            CommonUtils.click_point_random(smallX,smallY,hwndSmall)
            time.sleep(random.uniform(3.1, 4.9))
            continue

        # 如果有找到战斗坐标 点击
        if CommonUtils.openimages(fightImg2, hwndSmall) != 0:
            smallX, smallY = CommonUtils.openimages(fightImg2, hwndSmall)
            CommonUtils.click_point_random(smallX, smallY, hwndSmall)
            time.sleep(random.uniform(1.1, 2.9) + consumeTime)

            # 打完后点击结算
            print("小号点击结算")
            overX, overY = overAddress[random.randint(0, 9)].split(',')
            overXBig, overYBig = overAddress[random.randint(0, 9)].split(',')
            CommonUtils.click_point_random(overX, overY, hwndSmall)
            print("大号点击结算")
            CommonUtils.click_point_random(overXBig, overYBig, hwndBig)

            time.sleep(random.uniform(1.2, 1.9))
            print("小号再点击结算")
            CommonUtils.click_point_random(overX, overY, hwndSmall)
            print("大号再点击结算")
            CommonUtils.click_point_random(overXBig, overYBig, hwndBig)
            # 结束一次循环
            i += 1


            continue

        # 如果有找到战斗坐标 点击
        if CommonUtils.openimages(fightImg, hwndSmall) != 0:
            smallX, smallY = CommonUtils.openimages(fightImg, hwndSmall)
            CommonUtils.click_point_random(smallX, smallY, hwndSmall)
            time.sleep(random.uniform(1.1, 2.9) + consumeTime)

            # 打完后点击结算
            print("小号点击结算")
            overX, overY = overAddress[random.randint(0, 9)].split(',')
            overXBig, overYBig = overAddress[random.randint(0, 9)].split(',')
            CommonUtils.click_point_random(overX, overY, hwndSmall)
            print("大号点击结算")
            CommonUtils.click_point_random(overXBig, overYBig, hwndBig)

            time.sleep(random.uniform(1.0, 2.2))
            print("小号再点击结算")
            CommonUtils.click_point_random(overX, overY, hwndSmall)

            print("大号再点击结算")
            CommonUtils.click_point_random(overX, overY, hwndBig)
            # 结束一次循环
            i += 1

            continue



        # 如果有小纸人 把小纸人都点掉
        while CommonUtils.openimages(giftImg, hwndSmall) != 0:
            smallX, smallY = CommonUtils.openimages(giftImg, hwndSmall)
            CommonUtils.click_point_random(smallX, smallY, hwndSmall)
            time.sleep(random.uniform(1.1, 2.9) )
            overX, overY = overAddress[random.randint(0, 9)].split(',')
            CommonUtils.click_point_random(overX, overY, hwndSmall)

            # 如果有小纸人 把小纸人都点掉
            while CommonUtils.openimages(giftImg, hwndBig) != 0:
                smallX, smallY = CommonUtils.openimages(giftImg, hwndBig)
                CommonUtils.click_point_random(smallX, smallY, hwndBig)
                time.sleep(random.uniform(1.1, 2.9))
                overX, overY = overAddress[random.randint(0, 9)].split(',')
                CommonUtils.click_point_random(overX, overY, hwndBig)
                time.sleep(random.uniform(1.1, 2.9))

            # 小号邀请大号
            while CommonUtils.openimages(sureImg, hwndSmall) != 0:
                smallX, smallY = CommonUtils.openimages(sureImg, hwndSmall)
                CommonUtils.click_point_random(smallX, smallY, hwndSmall)
                time.sleep(random.uniform(1.1, 2.9))
                # 小号邀请大号
                while CommonUtils.openimages(makesureImg, hwndBig) != 0:
                    BigX, BigY = CommonUtils.openimages(makesureImg, hwndBig)
                    # 大号同意邀请
                    CommonUtils.click_point_random(BigX, BigY, hwndBig)
                    time.sleep(random.uniform(1.1, 2.9))
                    continue

            continue

        # 寻找新的怪物
        while CommonUtils.openimages(fightImg, hwndSmall) == 0:
            # 模拟人物走动,走到近头
            print("模拟人物走动,走到近头")

            moveX,moveY = moveAddress[0].split(',')
            CommonUtils.click_point_random(moveX, moveY, hwndSmall)
            time.sleep(random.uniform(1.1, 2.9) + smallWaitTime)
            continue





    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")


开始组队探索()

