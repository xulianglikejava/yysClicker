import time
from 不怎么用的 import CommonUtils
import random
import datetime

# 体力
power = 200
# 每局消耗体力
consume = 8
# 计划打的局数
maxcount = 150
# 每局消耗时间
consumeTime = 20
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2
# hwnd = win32gui.FindWindow(0, "铁血战士胖虎")
hwnd = CommonUtils.getSmallHwnd()
成功 = '../image/活动通用/success.png'
蛇皮 = '../image/活动通用/蛇皮.png'
自动1 = '../image/活动通用/自动1.png'
自动2 = '../image/活动通用/自动2.png'
failImg = '../image/活动通用/fail.png'
挑战 = '../image/活动通用/挑战.png'


def 开始挑战活动() :
    # 设置挑战次数
    start = datetime.datetime.now()
    print("现在是：" +  str(start))
    print("预计挑战活动 " + str(maxcount) + "局")

    # 读取文件里的结算坐标
    overAddress = []
    overFile = open('../address/组队魂土/结算坐标.txt')

    for line in overFile.readlines():
        line = line.strip('\n')
        overAddress.append(line)
    # 赋值完毕
    overFile.close()

    # 用于计算已经攻击过的点
    totalAddress = []

    for i in range(maxcount):
        print("------------------------")
        print("开始打第 " + str(i + 1) + " 次")
        i += 1
        time.sleep(random.uniform(1, 2));

        overXSmall, overYSmall = overAddress[random.randint(0, 22)].split(',')

        while CommonUtils.openimages(挑战, hwnd) == 0:
            CommonUtils.click_point_random(overXSmall, overYSmall, hwnd)
            time.sleep(random.uniform(2.5, 3));


        # 首先找到挑战坐标 点击
        while CommonUtils.openimages(挑战, hwnd) != 0 :
            CommonUtils.click_img(挑战, hwnd)
            break;
        wait = consumeTime + random.uniform(0.5, 0.9)
        # print("战斗中间间隔：" + str(wait) + " 秒")
        time.sleep(wait)
        # 打完后点击结算
        while CommonUtils.openimages(自动1, hwnd) != 0 or CommonUtils.openimages(自动2, hwnd) != 0:
            time.sleep(2)
            print("等待2秒")
        time.sleep(random.uniform(1.5, 2));

        while CommonUtils.openimages(蛇皮, hwnd) != 0 :
            print("小号点击结算")
            CommonUtils.click_point_random(overXSmall, overYSmall, hwnd)
            time.sleep(random.uniform(0.5, 1));

        time.sleep(random.uniform(3.0, 4));






    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")

开始挑战活动()

