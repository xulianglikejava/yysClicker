import time
import random
import datetime

from 不怎么用的 import async_all, CommonUtils

# 体力
power = 230
# 每局消耗体力
consume = 3
# 计划打的局数
maxcount = 10
# 每局消耗时间
consumeTime = 13
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2

# hwnd = win32gui.FindWindow(0, "捉鼠大师小叮当")
hwnd = CommonUtils.getBigHwnd()


# 图片素材
endImg = './image/百鬼夜行/end.png'

@async_all.async_call
def 开始百鬼夜行() :
    start = datetime.datetime.now()
    print("现在是：" +  str(start))
    print("预计百鬼夜行 " + str(maxcount) + "局")

    # 读取文件里的鬼王坐标
    mainAddress = []
    mainFile = open('../address/百鬼夜行/鬼王坐标.txt')
    for line in mainFile.readlines():
        line = line.strip('\n')
        mainAddress.append(line)
    # 赋值完毕
    mainFile.close()

    # 读取文件里的结算坐标
    overAddress = []
    overFile = open('../address/百鬼夜行/结算坐标.txt')
    for line in overFile.readlines():
        line = line.strip('\n')
        overAddress.append(line)
    # 赋值完毕
    overFile.close()

    # 读取文件里的进入坐标
    startAddress = []
    startFile = open('../address/百鬼夜行/进入坐标.txt')
    for line in startFile.readlines():
        line = line.strip('\n')
        startAddress.append(line)
    # 赋值完毕
    startFile.close()

    # 读取文件里的进入坐标
    fightAddress = []
    fightFile = open('../address/百鬼夜行/撒豆坐标.txt')
    for line in fightFile.readlines():
        line = line.strip('\n')
        fightAddress.append(line)
    # 赋值完毕
    fightFile.close()


    startX,startY = startAddress[0].split(',')


    # 开始执行任务
    for i in range(maxcount):
        print("------------------------")
        print("开始打第 " + str(i + 1) + " 次")
        time.sleep(random.uniform(0.5, 1.2))

        #     邀请好友
        print('邀请好友')
        CommonUtils.click_point_random(125, 453, hwnd)
        time.sleep(smallWaitTime + random.uniform(0.5, 0.9))

        #     选择第一个好友
        print('选择第一个好友')
        CommonUtils.click_point_random(377, 197, hwnd)
        time.sleep(smallWaitTime + random.uniform(0.5, 0.9))



        print('首先先进去')
        CommonUtils.click_point_random(startX, startY, hwnd)
        time.sleep(smallWaitTime + random.uniform(0.5, 0.9))

        mainX, mainY = mainAddress[random.randint(0, 2)].split(',')

        #  选择鬼王
        print('选择鬼王')
        CommonUtils.click_point_random(mainX, mainY, hwnd)
        time.sleep(smallWaitTime + random.uniform(0.1, 0.3))

        #  开始
        print('开始')
        CommonUtils.click_point_random(startX, startY, hwnd)
        time.sleep(bigWaitTime + random.uniform(2.0, 3.1))

        print("撒豆开始")
        for j in range(50):
            fightX, fightY = fightAddress[random.randint(0, 9)].split(',')
            CommonUtils.click_point_random(fightX, fightY, hwnd)
            print(250 - j*10)
            time.sleep(random.uniform(1, 1.5))
        print("撒豆结束")
        time.sleep(bigWaitTime + random.uniform(3.5,4.9))

        print("点击结束")
        overX, overY = overAddress[random.randint(0, 9)].split(',')
        CommonUtils.click_point_random(overX, overY, hwnd)

        time.sleep(bigWaitTime + random.uniform(0.5, 0.9))

    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")


开始百鬼夜行()
