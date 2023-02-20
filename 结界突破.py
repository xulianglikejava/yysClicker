import win32gui, win32con, win32api,win32ui
import time
import CommonUtils
import random
import datetime

import async_all

# 体力
power = 200
# 每局消耗体力
consume = 8
# 计划打的局数
maxcount = 30
# 每局消耗时间
consumeTime = 23
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 1.5

成功 = './image/结界突破/成功.png'
失败一 = './image/结界突破/失败一.png'
失败二 = './image/结界突破/失败二.png'
进攻 = './image/结界突破/进攻.png'
返回按钮 = './image/结界突破/返回按钮.png'
退出确认按钮 = './image/结界突破/退出确认按钮.png'
再次挑战按钮= './image/结界突破/再次挑战按钮.png'
再次挑战确认按钮 = './image/结界突破/再次挑战确认按钮.png'
刷新按钮 = './image/结界突破/刷新按钮.png'
刷新确认按钮 = './image/结界突破/刷新确认按钮.png'
勋章 = './image/结界突破/勋章.png'
灰刷新 = './image/结界突破/灰刷新.png'
结界突破 = './image/结界突破/结界突破.png'
结算勋章 = './image/结界突破/结算勋章.png'

# 读取文件里的挑战坐标
startAddress = []
startFile = open('./address/结界突破/挑战坐标.txt')
for line in startFile.readlines():
    line = line.strip('\n')
    startAddress.append(line)
startFile.close()

# 读取文件里的结算坐标
overAddress = []
overFile = open('./address/结界突破/结算坐标.txt')
for line in overFile.readlines():
    line = line.strip('\n')
    overAddress.append(line)
# 赋值完毕
overFile.close()

# 窗口句柄
hwnd = CommonUtils.getSmallHwnd()
def 开始结界突破() :
    # 设置突破卷数量
    start = datetime.datetime.now()
    print("现在是：" +  str(start))
    print("预计挑战结界 " + str(maxcount) + "局")
    # 用于计算已经攻击过的点
    totalAddress = []
    successTotal = 0
    # 开始执行任务
    for i in range(maxcount):
        print("------------------------")
        print("开始打第 " + str(i + 1) + " 次")
        i += 1
        overX, overY = overAddress[random.randint(0, 9)].split(',')
        # 首先找到挑战坐标 点击  每次挑战坐标全部随机 最后打完刷新
        tempAddr = random.randint(0, 8)
        if i % 10 == 0  or i % 19 == 0 or i % 28 == 0 :

            if successTotal == 9 :
                totalAddress = []
                successTotal = 0

            else:
                totalAddress = []
                successTotal = 0

                while CommonUtils.openimages(刷新按钮, hwnd) != 0:
                    print("点击刷新")
                    CommonUtils.click_img_no_retry(刷新按钮,hwnd)
                    time.sleep(random.uniform(1.0, 2.0))

                while CommonUtils.openimages(刷新确认按钮, hwnd) != 0:
                    print("点击刷新确认按钮")
                    CommonUtils.click_img_no_retry(刷新确认按钮, hwnd)
                    time.sleep(random.uniform(1.0, 2.0))
        # 正常流程

        while tempAddr in totalAddress:
            tempAddr = random.randint(0, 8)
        totalAddress.append(tempAddr)
        print("开始打第 " + str(tempAddr + 1) + " 个点")
        startX, startY, againX, againY = startAddress[tempAddr].split(',')
        # 这个防止没有退出结算
        while CommonUtils.openimages(刷新按钮, hwnd) == 0 and CommonUtils.openimages(灰刷新, hwnd) == 0:
            CommonUtils.click_point_random(overX, overY, hwnd)
            time.sleep(random.uniform(0.8, 1.2))
        #     开始
        CommonUtils.click_point_random(startX,startY,hwnd)
        time.sleep(random.uniform(0.8,1.2))
        # 防止没有成功进去
        playCount = 0
        while CommonUtils.openimages(进攻, hwnd) == 0:
            print("点击挑战点")
            CommonUtils.click_point_random(startX, startY, hwnd)
            time.sleep(random.uniform(0.8, 1.2))
            # 点三次进攻都没出来 这个点打过了
            playCount += 1
            if playCount > 2:
                successTotal = successTotal + 1
                break
        if playCount > 2:
            print("打其他点")
            continue
        attackCount = 0
        while CommonUtils.openimages(进攻, hwnd) != 0:
            print("进攻")
            CommonUtils.click_img(进攻, hwnd)
            attackCount += 1
            if attackCount > 2:
                return
            time.sleep(random.uniform(0.8, 1.2))

        # 如果最后一次 那么就要退出2次
        if i == 9 or i == 18 or  i == 27 :
            time.sleep(random.uniform(3, 3.5))
            print('9退2')
            for j in range(2):
                j += 1
                print("退出第" + str(j) + "次" )
                while CommonUtils.openimages(返回按钮, hwnd) != 0:
                    CommonUtils.click_img_no_retry(返回按钮, hwnd)
                    break
                time.sleep(random.uniform(1.0, 2.0))
                while CommonUtils.openimages(退出确认按钮, hwnd) != 0:
                    CommonUtils.click_img(退出确认按钮, hwnd)
                    break
                time.sleep(random.uniform(4.0, 4.5))

                while CommonUtils.openimages(再次挑战按钮, hwnd) != 0:
                    CommonUtils.click_img(再次挑战按钮, hwnd)
                    break
                time.sleep(random.uniform(1.0, 2.5))

                while CommonUtils.openimages(再次挑战确认按钮, hwnd) != 0:
                    CommonUtils.click_img(再次挑战确认按钮, hwnd)
                    break
                time.sleep(random.uniform(2.0, 3.5))

        # 一把打完至少要三十秒
        time.sleep(15)
        # 循环找图用的
        flag = 0
        # 由于计算等待次数
        countTime = 0

        # 循环截图 判断是否打完
        while flag == 0 :

            if CommonUtils.openimages(成功, hwnd) == 0 and CommonUtils.openimages(失败一, hwnd) == 0:
                print("等待第 " + str(countTime + 1 ) + " 次...")
                countTime = countTime + 1
                time.sleep(3)

            if CommonUtils.openimages(失败一, hwnd) != 0 and CommonUtils.openimages(失败二, hwnd) != 0 and CommonUtils.openimages(成功, hwnd) == 0:
                print("失败了")
                while CommonUtils.openimages(失败二, hwnd) != 0 :
                    print("点击结算")
                    CommonUtils.click_point_random(overX, overY, hwnd)
                    time.sleep(random.uniform(2.4, 3.5))

                flag = 1
                break

            if CommonUtils.openimages(失败一, hwnd) == 0 and CommonUtils.openimages(结算勋章, hwnd) != 0 :
                # 如果成功 那么成功次数加一  加一后再计算是否是第三次 如果是得多点次
                print("点击结算")
                print("已经成功打完了第" + str(successTotal + 1 ) + " 次...")
                successTotal = successTotal + 1
                CommonUtils.click_point_random(overX, overY,hwnd)
                time.sleep(random.uniform(1.0, 2.0))

                while CommonUtils.openimages(勋章, hwnd) != 0 :
                    print("点击弹窗胜利")
                    CommonUtils.click_point_random(overX, overY, hwnd)
                    time.sleep(random.uniform(1.0, 1.5))
                break;


        time.sleep(smallWaitTime +  random.uniform(0.1,0.7))

    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")


开始结界突破()
