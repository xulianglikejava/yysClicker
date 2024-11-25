import math
import time
from 不怎么用的 import CommonUtils
import random
import datetime

# 体力
power = 392
# 每局消耗体力
consume = 8
# 计划打的局数
maxcount = 29
# 每局消耗时间
consumeTime = 34
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2
挑战按钮 = './image/魂水/挑战按钮.png'
不可挑战按钮 = './image/魂水/不可挑战按钮.png'
成功 = './image/魂水/成功.png'
成功1 = './image/魂水/成功1.png'
金币 = './image/魂土/金币.png'
hwndBig = CommonUtils.getBigHwnd()
hwndSmall = CommonUtils.getSmallHwnd()


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
        while CommonUtils.openimages(挑战按钮, hwndSmall) != 0 :
            startX, startY, = CommonUtils.openimages(挑战按钮, hwndSmall)
            CommonUtils.click_point_random(startX, startY, hwndSmall)
            time.sleep(random.uniform(0.8, 1.2))
            break;
        playCount = 0
        while CommonUtils.openimages(挑战按钮, hwndSmall) != 0:
            # print("---没有成功进去挑战!!!---")
            # if CommonUtils.openimages(不可挑战按钮, hwndSmall) != 0:
            #     print('---队友没有进来---')
            #     return
            playCount = playCount + 1
            if playCount > 3:
                return
            startX, startY, = CommonUtils.openimages(挑战按钮, hwndSmall)
            CommonUtils.click_point_random(startX, startY, hwndSmall)
            time.sleep(random.uniform(1.2, 1.8))
        wait = consumeTime + random.uniform(0.5,0.9)
        # print("战斗中间间隔：" + str(wait) + " 秒")
        time.sleep(wait)
        # 打完后点击结算
        flag = 0
        countTime = 0
        overXSmall, overYSmall = overAddress[random.randint(0, 9)].split(',')
        overXBig, overYBig = overAddress[random.randint(0, 9)].split(',')

        while flag == 0:
            if CommonUtils.openimages(成功, hwndSmall) == 0 and CommonUtils.openimages(成功1, hwndSmall) == 0:
                # print("等待第 " + str(countTime + 1) + " 次...")
                countTime = countTime + 1
                time.sleep(1)

            elif CommonUtils.openimages(成功, hwndSmall) != 0 and CommonUtils.openimages(成功, hwndBig) != 0:
                # print("小号找到完成图了")
                time.sleep(random.uniform(1.2, 1.8))
                print("小号点击结算")
                CommonUtils.click_point_random(overXSmall, overYSmall, hwndSmall)
                print("大号点击结算")
                CommonUtils.click_point_random(overXBig, overYBig, hwndBig)
                wait = smallWaitTime + random.uniform(0.3, 1)
                time.sleep(wait);
                # 等待跳转
                break;

        while CommonUtils.openimages(金币, hwndSmall) != 0 and CommonUtils.openimages(金币, hwndBig) != 0:
            print("小号点击金币")
            CommonUtils.click_point_random(overXSmall, overYSmall, hwndSmall)
            print("大号点击金币")
            CommonUtils.click_point_random(overXBig, overYBig, hwndBig)
            wait = bigWaitTime + random.uniform(0.3, 1)
            time.sleep(wait);
            break

    startFile.close()
    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")
    # os.system('shutdown -s -t 1')  # 1代表一秒内关机，可自行设置


开始组队魂土()