
import time
import CommonUtils
import random
import datetime


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
战斗 = '../image/斗鸡/战斗.png'
返回 = '../image/斗鸡/返回.png'
确认 = '../image/斗鸡/确认.png'
取消 = '../image/斗鸡/取消.png'
准备 = '../image/斗鸡/准备.png'
胜利 = '../image/斗鸡/胜利.png'
失败 = '../image/斗鸡/失败.png'
战斗数据 = '../image/斗鸡/战斗数据.png'
分享 = '../image/斗鸡/分享.png'

hwnd = CommonUtils.getBigHwnd()


def 开始斗鸡() :
    start = datetime.datetime.now()
    print("现在是：" +  str(start))
    print("预计组队挑战斗鸡 " + str(maxcount) + "局")
    # 读取文件里的结算坐标
    overAddress = []
    overFile = open('../address/斗鸡/结算坐标.txt')
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
                print("找对手中，第 " + str(countTime + 1) + " 次...")
                countTime = countTime + 1
                time.sleep(3)

            elif CommonUtils.openimages(返回, hwnd) != 0 and CommonUtils.openimages(取消, hwnd) == 0:
                print("找到对手了")
                time.sleep(random.uniform(5.2, 5.8))
                print("点击准备")
                CommonUtils.click_img(准备,hwnd)
                print("等待打完")

                tempFlag = 0
                tempCountTime = 0
                while tempFlag == 0:
                    if CommonUtils.openimages(取消, hwnd) != 0:
                        print("打架中，第 " + str(countTime + 1) + " 次...")
                        countTime = countTime + 1
                        time.sleep(3)

                    elif CommonUtils.openimages(胜利, hwnd) != 0 or CommonUtils.openimages(失败, hwnd) != 0:
                        while CommonUtils.openimages(胜利, hwnd) != 0 or CommonUtils.openimages(失败, hwnd) != 0:
                            overX, overY = overAddress[random.randint(0, 9)].split(',')
                            print("点击结算")
                            CommonUtils.click_point_random(overX, overY, hwnd)
                            time.sleep(random.uniform(3.2, 4.8))
                            tempFlag = 1
                            flag = 1
                    elif CommonUtils.openimages(战斗数据, hwnd) != 0 and CommonUtils.openimages(分享, hwnd) != 0:
                            overX, overY = overAddress[random.randint(0, 9)].split(',')
                            print("点击结算")
                            CommonUtils.click_point_random(overX, overY, hwnd)
                            time.sleep(random.uniform(3.2, 4.8))
                            print("再点击结算")
                            CommonUtils.click_point_random(overX, overY, hwnd)
                            time.sleep(random.uniform(3.2, 4.8))
                            tempFlag = 1
                            flag = 1




    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")
    # os.system('shutdown -s -t 1')  # 1代表一秒内关机，可自行设置


开始斗鸡()