import time
from 不怎么用的 import CommonUtils
import random
import datetime

# 体力
power = 392
# 每局消耗体力
consume = 8
# 计划打的局数
maxcount = 3
# 每局消耗时间
consumeTime = 80
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2

# 图片素材
探索Img = '../image/通用图片/探索.png'
地域鬼王Img = '../image/地域鬼王/地域鬼王.png'
筛选Img = '../image/地域鬼王/筛选.png'
挑战Img = '../image/地域鬼王/挑战.png'
准备Img = '../image/地域鬼王/准备.png'
收藏按钮Img = '../image/地域鬼王/收藏按钮.png'
收藏挑战1Img = '../image/地域鬼王/收藏挑战1.png'
收藏挑战2Img = '../image/地域鬼王/收藏挑战2.png'
第一 = '../image/地域鬼王/第一.png'
第二 = '../image/地域鬼王/第二.png'
第三 = '../image/地域鬼王/第三.png'
叉叉Img = '../image/地域鬼王/叉叉.png'
胜利 = '../image/地域鬼王/胜利.png'
成功 = '../image/地域鬼王/成功.png'
失败一 = '../image/地域鬼王/失败一.png'


hwnd = CommonUtils.getBigHwnd()
# 读取文件里的挑战坐标
startAddress = []
startFile = open('../address/地域鬼王/鬼王坐标.txt')
for line in startFile.readlines():
    line = line.strip('\n')
    startAddress.append(line)
startFile.close()
# 读取文件里的结算坐标
overAddress = []
overFile = open('../address/地域鬼王/结算坐标.txt')
for line in overFile.readlines():
    line = line.strip('\n')
    overAddress.append(line)
# 赋值完毕
overFile.close()

# 读取文件里的红蛋坐标
redAddress = []
redFile = open('../address/地域鬼王/红蛋坐标.txt')
for line in redFile.readlines():
    line = line.strip('\n')
    redAddress.append(line)
# 赋值完毕
redFile.close()

# 读取文件里的关闭坐标
closeAddress = []
closeFile = open('../address/地域鬼王/关闭坐标.txt')
for line in closeFile.readlines():
    line = line.strip('\n')
    closeAddress.append(line)
# 赋值完毕
closeFile.close()

def 开始打地域鬼王() :
    start = datetime.datetime.now()
    print("现在是：" +  str(start))
    print("开始打地域鬼王")
    print('点击探索')

    # CommonUtils.click_point_random(833,200, hwnd)

    if CommonUtils.openimages(探索Img, hwnd) != 0 :
        CommonUtils.click_img(探索Img, hwnd)
    time.sleep(random.uniform(1.1, 2.5))

    print('点击地域鬼王图标')
    if CommonUtils.openimages(地域鬼王Img, hwnd) != 0:
        CommonUtils.click_img(地域鬼王Img, hwnd)
    time.sleep(random.uniform(1.1, 2.5))

    # 开始执行任务
    for i in range(maxcount):
        print("------------------------")
        print("开始打第 " + str(i + 1) + " 次")
        print('点击筛选')
        while CommonUtils.openimages(筛选Img, hwnd) != 0:
            CommonUtils.click_img_no_retry(筛选Img, hwnd)
            break
        time.sleep(random.uniform(2.0, 2.5))


        if i == 0 :
            print('第一')
            while CommonUtils.openimages(第一, hwnd) != 0:
                CommonUtils.click_img(第一, hwnd)
                break
        elif i == 1 :
            print('第二')
            while CommonUtils.openimages(第二, hwnd) != 0:
                CommonUtils.click_img(第二, hwnd)
                break
        elif i == 2 :
            print('第三')
            while CommonUtils.openimages(第三, hwnd) != 0:
                CommonUtils.click_img(第三, hwnd)
                break
        print('挑战')
        time.sleep(random.uniform(1.0, 2.0))
        while CommonUtils.openimages(挑战Img, hwnd) != 0:
            CommonUtils.click_img(挑战Img, hwnd)
            break
        time.sleep(random.uniform(2.0, 3.0))
        print('准备')
        while CommonUtils.openimages(准备Img, hwnd) != 0:
            CommonUtils.click_img(准备Img, hwnd)
            break
        time.sleep(consumeTime + random.uniform(2.0, 2.5))
        # 循环找图用的
        flag = 0
        # 由于计算等待次数
        countTime = 0

        # 循环截图 判断是否打完
        while flag == 0:
            if CommonUtils.openimages(成功, hwnd) == 0 and CommonUtils.openimages(失败一, hwnd) == 0:
                countTime = countTime + 1
                print("等待第 " + str(countTime) + " 次...")
                time.sleep(3)

            if CommonUtils.openimages(胜利, hwnd) != 0 :
                flag = 1
                print('战斗结束')
                overX, overY = overAddress[random.randint(0, 9)].split(',')
                print("点击结算")
                CommonUtils.click_point_random(overX, overY, hwnd)
                time.sleep(random.uniform(3.1, 3.5))
                print("再点击结算")
                CommonUtils.click_point_random(overX, overY, hwnd)
                time.sleep(random.uniform(3.1, 3.5))
                break

        print('点击叉叉')
        while CommonUtils.openimages(叉叉Img, hwnd) != 0:
            CommonUtils.click_img_no_retry(叉叉Img, hwnd)
            time.sleep(random.uniform(2.1, 2.5))

            break

        i += 1


    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")



开始打地域鬼王()
