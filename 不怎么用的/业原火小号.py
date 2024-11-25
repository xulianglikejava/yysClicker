import win32gui
import time
from 不怎么用的 import CommonUtils
import random
import datetime

# 体力
power = 200
# 每局消耗体力
consume = 8
# 计划打的局数
maxcount = 30
# 每局消耗时间
consumeTime = 40
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2

hwnd = win32gui.FindWindow(0, "捉鼠大师小叮当")
successImg = './image/业原火/success.png'
failImg = './image/业原火/fail.png'
startImg = './image/业原火/start.png'


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
        print("开始打第 " + str(i) + " 次")
        i += 1
        startX,startY, = CommonUtils.openimages(startImg, hwnd)
        CommonUtils.click_point_random(startX, startY, hwnd)
        # 一把打完至少要120秒
        time.sleep(consumeTime)
        flag = 0
        # 循环截图 判断是否打完
        while flag == 0 :
            if CommonUtils.openimages(successImg, hwnd) == 0 and CommonUtils.openimages(failImg, hwnd) == 0:
                print("战斗还没结束...")
                time.sleep(5)
            else :
                overX, overY = overAddress[random.randint(0, 9)].split(',')
                print("点击结算")
                CommonUtils.click_point_random(overX, overY, hwnd)
                time.sleep(smallWaitTime + random.uniform(0.2,0.5))
                CommonUtils.click_point_random(overX, overY, hwnd)
                flag = 1
                break;
        time.sleep(bigWaitTime + random.uniform(0.2,0.6))

    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")

开始业原火()

