import math
import time
from 不怎么用的 import CommonUtils
import random
import datetime

# 体力
power = 200
# 每局消耗体力
consume = 4
# 计划打的局数
maxcount = 0
# 每局消耗时间
consumeTime = 18
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2
挑战按钮 = './image/魂土/挑战按钮.png'
不可挑战按钮 = './image/魂土/不可挑战按钮.png'
成功 = './image/魂土/成功.png'
成功1 = './image/魂土/成功1.png'
金币 = './image/通用图片/金币.png'
队友 = './image/魂土/队友.png'
组队 = './image/通用图片/组队.png'
御魂 = './image/通用图片/御魂.png'
魂十 = './image/通用图片/魂十.png'
魂土 = './image/通用图片/魂土.png'
魂王 = './image/通用图片/魂王.png'
创建队伍 = './image/通用图片/创建队伍.png'
创建 = './image/通用图片/创建.png'
邀请 = './image/通用图片/邀请.png'
邀请好友 = './image/通用图片/邀请好友.png'
队友 = './image/通用图片/队友.png'
接受邀请 = './image/通用图片/接受邀请.png'
组队界面 = './image/通用图片/组队界面.png'
默认邀请队友 = './image/通用图片/默认邀请队友.png'
确定 = './image/通用图片/确定.png'
自动接受邀请 = './image/通用图片/自动接受邀请.png'
战斗中 = './image/通用图片/战斗中.png'
hwndBig = CommonUtils.getBigHwnd()
hwndSmall = CommonUtils.getSmallHwnd()


def 开始组队魂土() :
    maxcount = math.floor(power/consume)
    start = datetime.datetime.now()
    print("现在是：" +  str(start))
    print("预计组队挑战魂十 " + str(maxcount) + "局")
    # 读取文件里的结算坐标
    overAddress = []
    overFile = open('./address/组队魂土/结算坐标.txt')
    for line in overFile.readlines():
        line = line.strip('\n')
        overAddress.append(line)
    if CommonUtils.openimages(组队界面, hwndSmall) == 0:
        CommonUtils.click_img(组队,hwndSmall)
        time.sleep(random.uniform(0.6, 1));
        CommonUtils.click_img_no_retry(御魂,hwndSmall)
        time.sleep(random.uniform(0.6, 1));
        CommonUtils.click_img_no_retry(魂王, hwndSmall)
        time.sleep(random.uniform(0.6, 1));
        CommonUtils.click_img_no_retry(创建队伍, hwndSmall)
        time.sleep(random.uniform(0.6, 1));
        CommonUtils.click_img(创建, hwndSmall)
        time.sleep(random.uniform(0.6, 1));
    while CommonUtils.openimages(组队界面, hwndBig) == 0:
        CommonUtils.邀请队友(hwndSmall,hwndBig)
    # 赋值完毕

    CommonUtils.打开御魂经验(hwndSmall,hwndBig)

    for i in range(maxcount):
        print("------------------------")
        print("开始打第 " + str(i + 1) + " 次")
        i += 1
        time.sleep(random.uniform(1, 2));

        overXSmall, overYSmall = overAddress[random.randint(0, 22)].split(',')
        overXBig, overYBig = overAddress[random.randint(0, 22)].split(',')
        while CommonUtils.openimages(组队界面, hwndSmall) == 0 :
            CommonUtils.click_point_random(overXSmall, overYSmall, hwndSmall)
            time.sleep(random.uniform(2.5, 3));

        while CommonUtils.openimages(组队界面, hwndBig) == 0 :
            CommonUtils.click_point_random(overXBig, overYBig, hwndBig)
            time.sleep(random.uniform(2.5, 3));

        # 首先找到挑战坐标 点击
        while CommonUtils.openimages(组队界面, hwndSmall) != 0 and CommonUtils.openimages(组队界面, hwndBig) != 0:
            CommonUtils.click_img(挑战按钮, hwndSmall)
            break;
        wait = consumeTime + random.uniform(0.5,0.9)
        # print("战斗中间间隔：" + str(wait) + " 秒")
        time.sleep(wait)
        # 打完后点击结算
        while CommonUtils.openimages(战斗中, hwndSmall) != 0 :
            time.sleep(2)
            print("等待2秒")
        time.sleep(random.uniform(1.5, 2));

        while CommonUtils.openimages(成功, hwndSmall) != 0 or CommonUtils.openimages(成功1, hwndSmall) != 0:
            print("小号点击结算")
            CommonUtils.click_point_random(overXSmall, overYSmall, hwndSmall)
            time.sleep(random.uniform(0.5, 1));

        while CommonUtils.openimages(成功, hwndBig) != 0 or CommonUtils.openimages(成功1, hwndBig) != 0:
            print("大号点击结算")
            CommonUtils.click_point_random(overXBig, overYBig, hwndBig)
            time.sleep(random.uniform(0.5, 1));

        while CommonUtils.openimages(金币, hwndSmall) != 0 and CommonUtils.openimages(确定, hwndSmall) == 0:
            print("小号再点击结算")
            CommonUtils.click_point_random(overXSmall, overYSmall, hwndSmall)
            time.sleep(random.uniform(0.5, 1));

        while CommonUtils.openimages(金币, hwndBig) != 0 :
            print("大号再点击结算")
            CommonUtils.click_point_random(overXBig, overYBig, hwndBig)
            time.sleep(random.uniform(1.5, 2));

        if i == 1 and CommonUtils.openimages(默认邀请队友, hwndSmall) != 0 and CommonUtils.openimages(确定, hwndSmall) != 0:
            print("自动邀请队友")
            CommonUtils.click_img(默认邀请队友, hwndSmall)
            time.sleep(random.uniform(0.2, 0.5));
            CommonUtils.click_img(确定, hwndSmall)
            time.sleep(random.uniform(0.6, 1));
            CommonUtils.click_img(自动接受邀请, hwndBig)
            time.sleep(random.uniform(0.6, 1));
    print('打完了')
    CommonUtils.关闭加成(hwndSmall, hwndBig)
    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")
    # os.system('shutdown -s -t 1')  # 1代表一秒内关机，可自行设置


开始组队魂土()