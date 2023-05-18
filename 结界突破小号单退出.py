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
开始无勋章 = './image/结界突破/无勋章.png'
进攻 = './image/寮突/进攻.png'
成功 = './image/寮突/成功.png'
失败 = './image/寮突/失败.png'
勋章 = './image/寮突/勋章.png'
突破记录 = './image/寮突/突破记录.png'

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
hwndBig = CommonUtils.getSmallHwnd()
def 开始结界突破() :
    while CommonUtils.openimages(开始无勋章, hwndBig) != 0 and CommonUtils.openimages(进攻, hwndBig) == 0:
        while CommonUtils.openimages(进攻, hwndBig) == 0:
            print("点击开始")
            CommonUtils.click_img_no_retry(开始无勋章, hwndBig)
            time.sleep(random.uniform(1.0, 1.5))
    while CommonUtils.openimages(进攻, hwndBig) != 0:
        print("点击进攻")
        CommonUtils.click_img(进攻, hwndBig)
        time.sleep(random.uniform(1.0, 1.5))
    time.sleep(random.uniform(2, 2.5))
    print('9退3')
    for j in range(4):
        j += 1
        print("退出第" + str(j) + "次")
        while CommonUtils.openimages(返回按钮, hwndBig) != 0:
            CommonUtils.click_img_no_retry(返回按钮, hwndBig)
            break
        time.sleep(random.uniform(1.0, 1.5))
        while CommonUtils.openimages(退出确认按钮, hwndBig) != 0:
            CommonUtils.click_img(退出确认按钮, hwndBig)
            break
        time.sleep(random.uniform(3.0, 3.5))

        while CommonUtils.openimages(再次挑战按钮, hwndBig) != 0:
            CommonUtils.click_img(再次挑战按钮, hwndBig)
            break
        time.sleep(random.uniform(1.0, 2.5))

        while CommonUtils.openimages(再次挑战确认按钮, hwndBig) != 0:
            CommonUtils.click_img(再次挑战确认按钮, hwndBig)
            break
        time.sleep(random.uniform(3.0, 3.5))


开始结界突破()
