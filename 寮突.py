import time
from 不怎么用的 import CommonUtils
import random
import datetime

# 体力
power = 390
# 每局消耗体力
consume = 8
# 计划打的局数
maxcount = 6
# 每局消耗时间
consumeTime = 10
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2

开始 = './image/寮突/开始.png'
进攻 = './image/寮突/进攻.png'
成功 = './image/寮突/成功.png'
失败 = './image/寮突/失败.png'
勋章 = './image/寮突/勋章.png'
突破记录 = './image/寮突/突破记录.png'
hwndBig = CommonUtils.getBigHwnd()


def 开始寮突() :
    start = datetime.datetime.now()
    print("现在是：" +  str(start))
    print("预计寮突 " + str(maxcount) + "局")
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


        while CommonUtils.openimages(开始, hwndBig) != 0 and CommonUtils.openimages(进攻, hwndBig) == 0:
            while CommonUtils.openimages(进攻, hwndBig) == 0:
                print("点击开始")
                CommonUtils.click_img_no_retry(开始, hwndBig)
                time.sleep(random.uniform(1.0,1.5))
        while CommonUtils.openimages(进攻, hwndBig) != 0:
            print("点击进攻")
            CommonUtils.click_img(进攻, hwndBig)
            time.sleep(random.uniform(1.0,1.5))
        print("战斗中间间隔：" + str(consumeTime) + " 秒")
        time.sleep(consumeTime)
        # 打完后点击结算
        flag = 0
        countTime = 0
        while flag == 0:
            if CommonUtils.openimages(成功, hwndBig) == 0 or CommonUtils.openimages(失败, hwndBig) == 0:
                print("等待第 " + str(countTime + 1) + " 次...")
                countTime = countTime + 1
                time.sleep(2)
            if CommonUtils.openimages(成功, hwndBig) != 0 or CommonUtils.openimages(失败, hwndBig) != 0:
                print("打完了")
                time.sleep(random.uniform(1.2, 2.3))
                print("点击结算")
                overX, overY = overAddress[random.randint(0, 9)].split(',')
                CommonUtils.click_point_random(overX, overY, hwndBig)
                time.sleep(random.uniform(2.2, 2.5))
                # while CommonUtils.openimages(勋章, hwndBig) != 0 and CommonUtils.openimages(突破记录, hwndBig) == 0 :
                #
                flag = 1
                break;

    startFile.close()
    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")
    # os.system('shutdown -s -t 1')  # 1代表一秒内关机，可自行设置


开始寮突()