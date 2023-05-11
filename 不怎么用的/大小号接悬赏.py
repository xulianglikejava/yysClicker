import time
from 不怎么用的 import CommonUtils
import random

# 体力
power = 350
# 每局消耗体力
consume = 8
# 计划打的局数
maxcount = 0
# 每局消耗时间
consumeTime = 26
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2
接受邀请 = '../image/通用图片/接受邀请.png'
hwndBig = CommonUtils.getBigHwnd()
hwndSmall = CommonUtils.getSmallHwnd()


def 开始组队魂土() :
    count = 0
    print("开始监控是否有悬赏")
    while 1 == 1 :
        time.sleep(random.uniform(6.0, 7.0))
        # 检查大号
        while CommonUtils.openimages(接受邀请, hwndBig) != 0:
            startX, startY, = CommonUtils.openimages(接受邀请, hwndBig)
            CommonUtils.click_point_random(startX, startY, hwndBig)
            print("---大号获取了一个悬赏---")
            break
        # 检查小号
        while CommonUtils.openimages(接受邀请, hwndSmall) != 0:
            startX, startY, = CommonUtils.openimages(接受邀请, hwndSmall)
            CommonUtils.click_point_random(startX, startY, hwndSmall)
            print("---小号获取了一个悬赏---")
            break

        count = count + 1



开始组队魂土()