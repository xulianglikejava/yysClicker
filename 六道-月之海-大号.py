import time
from 不怎么用的 import CommonUtils
import random
import datetime

# 体力
power = 350
# 每局消耗体力
consume = 60
# 计划打的局数
maxcount = 100
# 每局消耗时间
consumeTime = 500
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2

六道入口 = './image/六道-月之海/六道入口.png'
月之海入口 = './image/六道-月之海/月之海入口.png'
准备按钮 = './image/六道-月之海/准备按钮.png'
开启按钮 = './image/六道-月之海/开启按钮.png'
继续按钮 = './image/六道-月之海/继续按钮.png'
确定开始 = './image/六道-月之海/确定开始.png'
开启2按钮 = './image/六道-月之海/开启2按钮.png'
技能怪 = './image/六道-月之海/技能怪.png'
挑战按钮 = './image/六道-月之海/挑战按钮.png'
挑战BOSS = './image/六道-月之海/挑战BOSS.png'
挑战技能怪 = './image/六道-月之海/挑战技能怪.png'
万相铃 = './image/六道-月之海/万相铃.png'
结束 = './image/六道-月之海/结束.png'
使用 = './image/六道-月之海/使用.png'
获得奖励 = './image/六道-月之海/获得奖励.png'

柔风抱暖 = './image/六道-月之海/柔风抱暖.png'
细雨化屏 = './image/六道-月之海/细雨化屏.png'
六道暴虐 = './image/六道-月之海/六道暴虐.png'
妖力化身 = './image/六道-月之海/妖力化身.png'

柔风抱暖文字 = './image/六道-月之海/柔风抱暖文字.png'
细雨化屏文字 = './image/六道-月之海/细雨化屏文字.png'
六道暴虐文字 = './image/六道-月之海/六道暴虐文字.png'
妖力化身文字 = './image/六道-月之海/妖力化身文字.png'

小柔风抱暖 = './image/六道-月之海/小柔风抱暖.png'
小细雨化屏 = './image/六道-月之海/小细雨化屏.png'
小六道暴虐 = './image/六道-月之海/小六道暴虐.png'
小妖力化身 = './image/六道-月之海/小妖力化身.png'
万相之赐 = './image/六道-月之海/万相之赐.png'
没钱按钮 = './image/六道-月之海/没钱按钮.png'
刷新按钮 = './image/六道-月之海/刷新按钮.png'

检查柔风抱暖 = './image/六道-月之海/检查柔风抱暖.png'
检查细雨化屏 = './image/六道-月之海/检查细雨化屏.png'
检查六道暴虐 = './image/六道-月之海/检查六道暴虐.png'
检查妖力化身 = './image/六道-月之海/检查妖力化身.png'
万相之赐文字 = './image/六道-月之海/万相之赐文字.png'

确定按钮 = './image/六道-月之海/确定按钮.png'
确认按钮 = './image/六道-月之海/确认按钮.png'
跳过按钮 = './image/六道-月之海/跳过按钮.png'
选择按钮 = './image/六道-月之海/选择按钮.png'

麓战1 = './image/六道-月之海/麓战1.png'
混沌1 = './image/六道-月之海/混沌1.png'
神秘1 = './image/六道-月之海/神秘1.png'
星之屿1 = './image/六道-月之海/星之屿1.png'
安息1 = './image/六道-月之海/安息1.png'

火之卷 = './image/六道-月之海/火之卷.png'
冰之卷 = './image/六道-月之海/冰之卷.png'
变呱符咒 = './image/六道-月之海/变呱符咒.png'
攻击御守 = './image/六道-月之海/攻击御守.png'
抵抗御守 = './image/六道-月之海/抵抗御守.png'
风之卷 = './image/六道-月之海/风之卷.png'
石之卷 = './image/六道-月之海/石之卷.png'
雷之卷 = './image/六道-月之海/雷之卷.png'
生命御守 = './image/六道-月之海/生命御守.png'
庇护头盔 = './image/六道-月之海/庇护头盔.png'
乾坤袋 = './image/六道-月之海/乾坤袋.png'
妒火人偶 = './image/六道-月之海/妒火人偶.png'
黑蛇莲 = './image/六道-月之海/黑蛇莲.png'
# 混沌
幸运宝箱 = './image/六道-月之海/幸运宝箱.png'
精英 = './image/六道-月之海/精英.png'
离开宝箱 = './image/六道-月之海/离开宝箱.png'

# 神秘
仿造按钮 = './image/六道-月之海/仿造按钮.png'
虚仿造按钮 = './image/六道-月之海/虚仿造按钮.png'
转换1 = './image/六道-月之海/转换1.png'
退出神秘之屿 = './image/六道-月之海/退出神秘之屿.png'

# 安息
离开商店 = './image/六道-月之海/离开商店.png'
商品柔风抱暖 = './image/六道-月之海/商品柔风抱暖.png'
商品细雨化屏 = './image/六道-月之海/商品细雨化屏.png'
商品六道暴虐 = './image/六道-月之海/商品六道暴虐.png'
商品妖力化身 = './image/六道-月之海/商品妖力化身.png'
刷新商店 = './image/六道-月之海/刷新商店.png'

月读按钮 = './image/六道-月之海/月读按钮.png'
胜利 = './image/六道-月之海/胜利.png'

# 备战
备战 = './image/六道-月之海/备战.png'
重置技能 = './image/六道-月之海/重置技能.png'
装备 = './image/六道-月之海/装备.png'
技能刷新 = './image/六道-月之海/技能刷新.png'
退出技能重置 = './image/六道-月之海/退出技能重置.png'

# 技能怪坐标
技能怪X = 637
技能怪Y = 252

# 精英怪坐标
精英怪X = 637
精英怪Y = 252

# 符咒坐标
符咒X = 788
符咒Y = 92

# 读取文件里的结算坐标
overAddress = []
overFile = open('./address/六道-月之海/结算坐标.txt')
for line in overFile.readlines():
    line = line.strip('\n')
    overAddress.append(line)
# 赋值完毕
overFile.close()
# 窗口句柄
hwnd = CommonUtils.getBigHwnd()


def 关卡内战斗(fightCount):
    startTmp = datetime.datetime.now()

    while CommonUtils.openimages(胜利, hwnd) == 0 and CommonUtils.openimages(使用, hwnd) == 0:
        time.sleep(random.uniform(1.2, 2.0))

        # 判断是否打到月读了
        while CommonUtils.openimages(挑战BOSS, hwnd) != 0:
            # 调整技能
            # 备战BOSS()
            CommonUtils.click_img(挑战BOSS, hwnd)
            time.sleep(random.uniform(1.2, 2.0))

            print("释放符咒一次")
            CommonUtils.click_point_random(符咒X, 符咒Y, hwnd)
            time.sleep(random.uniform(45, 50))
            print("再释放符咒一次")
            CommonUtils.click_point_random(符咒X, 符咒Y, hwnd)
            continue

        # 判断是否有麓战
        if CommonUtils.openimages(麓战1, hwnd) != 0:
            fightCount += 1
            麓战(fightCount)
            continue

        # 判断是否有神秘
        if CommonUtils.openimages(神秘1, hwnd) != 0:
            神秘()
            continue

        # 判断是否有混沌
        if CommonUtils.openimages(混沌1, hwnd) != 0:
            fightCount += 2
            混沌(fightCount)
            continue

        # 判断是否有星之子
        if CommonUtils.openimages(星之屿1, hwnd) != 0:
            fightCount += 1
            星之子(fightCount)
            continue
        # 判断是否有安息
        if CommonUtils.openimages(安息1, hwnd) != 0:
            安息(fightCount)
            continue

    # 判断是否胜利
    while CommonUtils.openimages(胜利, hwnd) != 0 or CommonUtils.openimages(使用, hwnd) != 0:
        if CommonUtils.openimages(使用, hwnd) != 0:
            print("使用双倍")
            CommonUtils.click_img(使用, hwnd)
        print("点击结算")
        time.sleep(random.uniform(1.2, 2.0))

        # CommonUtils.生成截图(hwnd)
        overX, overY = overAddress[random.randint(0, 9)].split(',')
        CommonUtils.click_point_random(overX, overY, hwnd)
        time.sleep(random.uniform(1.2, 2.0))

        while CommonUtils.openimages(获得奖励, hwnd) != 0:
            print("再点击获得奖励")
            CommonUtils.click_img(获得奖励, hwnd)
            time.sleep(random.uniform(1.2, 2.0))

        while CommonUtils.openimages(结束, hwnd) == 0:
            print("没有找到结束")
            time.sleep(random.uniform(1.2, 2.0))

            CommonUtils.click_point_random(overX, overY, hwnd)
            time.sleep(random.uniform(1.2, 2.0))

        print("再点击结束")
        CommonUtils.click_img(结束, hwnd)
        time.sleep(random.uniform(1.2, 2.0))

        break
    endTmp = datetime.datetime.now()
    print(">>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<")
    print(">>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<")
    print(">>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<")
    print("一次战斗耗时为：" + str(endTmp - startTmp).split(".")[0] + " 秒")
    print(">>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<")
    print(">>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<")
    print(">>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<")
    time.sleep(random.uniform(1.5, 2.5))


def 星之子(fightCount):
    # 判断是否有麓战 优先打麓战
    while CommonUtils.openimages(星之屿1, hwnd) != 0:
        print("打星之子喽")
        CommonUtils.click_img(星之屿1, hwnd)
        time.sleep(random.uniform(1.2, 2.0))

        while CommonUtils.openimages(挑战技能怪, hwnd) == 0:
            CommonUtils.click_point_random(技能怪X, 技能怪Y, hwnd)
            time.sleep(random.uniform(1.2, 2.0))

        CommonUtils.click_img(挑战技能怪, hwnd)
        time.sleep(5)
        # 打完后点击结算
        flag = 0
        countTime = 0
        while flag == 0:
            if CommonUtils.openimages(万相之赐, hwnd) == 0:
                print("等待第 " + str(countTime + 1) + " 次...")
                countTime = countTime + 1
                time.sleep(2)
            elif CommonUtils.openimages(万相之赐, hwnd) != 0:
                flag = 1
                选择符咒()
                if fightCount > 2:
                    选择技能(1)
                else:
                    选择万相之赐()
                break;
        break


def 神秘():
    print("选择神秘")
    while CommonUtils.openimages(神秘1, hwnd) != 0:
        CommonUtils.click_img(神秘1, hwnd)
        # 如果是转换
        while CommonUtils.openimages(转换1, hwnd) != 0:
            CommonUtils.click_img_no_retry(退出神秘之屿, hwnd)
            time.sleep(random.uniform(1.2, 2.0))

        # 如果是仿造
        while CommonUtils.openimages(虚仿造按钮, hwnd) != 0:
            if CommonUtils.openimages(小柔风抱暖, hwnd) != 0:
                CommonUtils.click_img_no_retry(小柔风抱暖, hwnd)
                CommonUtils.click_img_no_retry(仿造按钮, hwnd)
                if CommonUtils.openimages(确定按钮, hwnd) != 0:
                    CommonUtils.click_img(确定按钮, hwnd)
                    overX, overY = overAddress[random.randint(0, 9)].split(',')
                    CommonUtils.click_point_random(overX, overY, hwnd)
                    break
            if CommonUtils.openimages(小六道暴虐, hwnd) != 0:
                CommonUtils.click_img_no_retry(小六道暴虐, hwnd)
                CommonUtils.click_img_no_retry(仿造按钮, hwnd)
                if CommonUtils.openimages(确定按钮, hwnd) != 0:
                    CommonUtils.click_img(确定按钮, hwnd)
                    overX, overY = overAddress[random.randint(0, 9)].split(',')
                    CommonUtils.click_point_random(overX, overY, hwnd)
                    break
            if CommonUtils.openimages(小细雨化屏, hwnd) != 0:
                CommonUtils.click_img_no_retry(小细雨化屏, hwnd)
                CommonUtils.click_img_no_retry(仿造按钮, hwnd)
                if CommonUtils.openimages(确定按钮, hwnd) != 0:
                    CommonUtils.click_img(确定按钮, hwnd)
                    overX, overY = overAddress[random.randint(0, 9)].split(',')
                    CommonUtils.click_point_random(overX, overY, hwnd)
                    break
            if CommonUtils.openimages(小妖力化身, hwnd) != 0:
                CommonUtils.click_img_no_retry(小妖力化身, hwnd)
                CommonUtils.click_img_no_retry(仿造按钮, hwnd)
                if CommonUtils.openimages(确定按钮, hwnd) != 0:
                    CommonUtils.click_img(确定按钮, hwnd)
                    overX, overY = overAddress[random.randint(0, 9)].split(',')
                    CommonUtils.click_point_random(overX, overY, hwnd)
                    break


def 混沌(fightCount):
    print("选择混沌")
    # 判断是否有麓战 优先打麓战
    while CommonUtils.openimages(混沌1, hwnd) != 0:
        CommonUtils.click_img(混沌1, hwnd)
        time.sleep(random.uniform(1.2, 2.0))

        if CommonUtils.openimages(幸运宝箱, hwnd) != 0:
            print("离开幸运宝箱")
            CommonUtils.click_img(离开宝箱, hwnd)
            break
        else:
            print("挑战精英")
            while CommonUtils.openimages(挑战技能怪, hwnd) == 0:
                print("点击精英")
                CommonUtils.click_point_random(精英怪X, 精英怪Y, hwnd)
                time.sleep(random.uniform(1.2, 2.0))

            CommonUtils.click_img(挑战技能怪, hwnd)
            time.sleep(15)
            # 打完后点击结算
            flag = 0
            countTime = 0
            while flag == 0:
                if CommonUtils.openimages(万相之赐, hwnd) == 0:
                    print("等待第 " + str(countTime + 1) + " 次...")
                    countTime = countTime + 1
                    time.sleep(1)
                elif CommonUtils.openimages(万相之赐, hwnd) != 0:
                    flag = 1
                    if fightCount > 2:
                        选择技能(0)
                        选择技能(1)
                    else:
                        选择万相之赐()
                        选择万相之赐()

                    break;
            break


def 安息(fightCount):
    print("选择安息")
    while CommonUtils.openimages(安息1, hwnd) != 0:
        CommonUtils.click_img(安息1, hwnd)
        time.sleep(random.uniform(1.2, 2.0))

        购买(fightCount)


def 购买(fightCount):
    print("购买商品")
    time.sleep(random.uniform(1.5, 2.5))
    flush = 0
    if fightCount < 3:
        print("没得钱,不刷新商店,有啥买啥")
        if CommonUtils.openimages(商品柔风抱暖, hwnd) != 0:
            print("有柔风抱暖")
            CommonUtils.click_img_buy(商品柔风抱暖, hwnd)
            if CommonUtils.openimages(确定按钮, hwnd) != 0:
                CommonUtils.click_img(确定按钮, hwnd)

        if CommonUtils.openimages(商品六道暴虐, hwnd) != 0:
            print("有六道暴虐")
            CommonUtils.click_img_buy(商品六道暴虐, hwnd)
            if CommonUtils.openimages(确定按钮, hwnd) != 0:
                CommonUtils.click_img(确定按钮, hwnd)
        if CommonUtils.openimages(商品妖力化身, hwnd) != 0:
            print("有妖力化身")
            CommonUtils.click_img_buy(商品妖力化身, hwnd)
            if CommonUtils.openimages(确定按钮, hwnd) != 0:
                CommonUtils.click_img(确定按钮, hwnd)

        if CommonUtils.openimages(商品细雨化屏, hwnd) != 0:
            print("有细雨化屏")
            CommonUtils.click_img_buy(商品细雨化屏, hwnd)
            if CommonUtils.openimages(确定按钮, hwnd) != 0:
                CommonUtils.click_img(确定按钮, hwnd)

    else:
        while flush < 2:

            if CommonUtils.openimages(商品柔风抱暖, hwnd) != 0:
                print("有柔风抱暖")
                CommonUtils.click_img_buy(商品柔风抱暖, hwnd)
                if CommonUtils.openimages(确定按钮, hwnd) != 0:
                    CommonUtils.click_img(确定按钮, hwnd)

            if CommonUtils.openimages(商品六道暴虐, hwnd) != 0:
                print("有六道暴虐")
                CommonUtils.click_img_buy(商品六道暴虐, hwnd)
                if CommonUtils.openimages(确定按钮, hwnd) != 0:
                    CommonUtils.click_img(确定按钮, hwnd)
            if CommonUtils.openimages(商品妖力化身, hwnd) != 0:
                print("有妖力化身")
                CommonUtils.click_img_buy(商品妖力化身, hwnd)
                if CommonUtils.openimages(确定按钮, hwnd) != 0:
                    CommonUtils.click_img(确定按钮, hwnd)

            if CommonUtils.openimages(商品细雨化屏, hwnd) != 0:
                print("有细雨化屏")
                CommonUtils.click_img_buy(商品细雨化屏, hwnd)
                if CommonUtils.openimages(确定按钮, hwnd) != 0:
                    CommonUtils.click_img(确定按钮, hwnd)
            # 打了8次才有点钱刷新吧
            if fightCount < 8:
                print("打的太少了，不刷新了")
                flush = flush + 1
            # 打了8次才有点钱刷新吧
            if CommonUtils.openimages(刷新商店, hwnd) != 0 and flush < 1 and fightCount > 8:
                print("刷新商店")
                CommonUtils.click_img_no_retry(刷新商店, hwnd)
            flush = flush + 1

    print("离开商店")
    CommonUtils.click_img(离开商店, hwnd)


def 麓战(fightCount):
    # 判断是否有麓战 优先打麓战
    print("打麓战")
    while CommonUtils.openimages(麓战1, hwnd) != 0:
        print("打技能怪喽")
        CommonUtils.click_img(麓战1, hwnd)
        time.sleep(random.uniform(1.2, 2.0))

        while CommonUtils.openimages(挑战技能怪, hwnd) == 0:
            CommonUtils.click_point_random(技能怪X, 技能怪Y, hwnd)
            time.sleep(random.uniform(1.2, 2.0))

        CommonUtils.click_img(挑战技能怪, hwnd)
        time.sleep(5)
        # 打完后点击结算
        flag = 0
        countTime = 0
        while flag == 0:
            if CommonUtils.openimages(万相之赐, hwnd) == 0:
                print("等待第 " + str(countTime + 1) + " 次...")
                countTime = countTime + 1
                time.sleep(2)
            elif CommonUtils.openimages(万相之赐, hwnd) != 0:
                flag = 1
                if fightCount > 2:
                    选择技能(1)
                else:
                    选择万相之赐()
                break;

        break


def 选择技能(flag):
    # 刷新次数
    flush = 0
    print("选技能咯")
    print("是否有奖励页面 如果有直接停止")
    time.sleep(random.uniform(1.5, 2.5))
    if CommonUtils.openimages(万相铃, hwnd) != 0:
        flush = 5
        print("点击结算")
        overX, overY = overAddress[random.randint(0, 9)].split(',')
        CommonUtils.click_point_random(overX, overY, hwnd)
        time.sleep(random.uniform(1.2, 2.0))

        playCount = 0
        while CommonUtils.openimages(万相铃, hwnd) != 0:
            print("---没有成功点击!!!---")
            time.sleep(random.uniform(1.2, 2.0))

            playCount = playCount + 1
            if playCount > 3:
                return
            CommonUtils.click_point_random(overX, overY, hwnd)
    while flush < 4:
        time.sleep(random.uniform(1.0, 1.5))
        if CommonUtils.openimages(柔风抱暖文字, hwnd) != 0:
            print("选柔风咯")
            CommonUtils.click_img_select_fz(柔风抱暖文字, hwnd)

            break;
        if CommonUtils.openimages(妖力化身文字, hwnd) != 0:
            print("选分身咯")
            CommonUtils.click_img_select_fz(妖力化身文字, hwnd)
            break;

        if CommonUtils.openimages(六道暴虐, hwnd) != 0:
            print("选暴虐咯")
            CommonUtils.click_img_select(六道暴虐, hwnd)
            break;
        if CommonUtils.openimages(细雨化屏文字, hwnd) != 0:
            print("选化雨咯")
            CommonUtils.click_img_select_fz(细雨化屏文字, hwnd)
            break;
        if flush < 3:
            print("刷新！刷新技能!")
            x, y = CommonUtils.openimages(刷新按钮, hwnd)
            CommonUtils.click_point_random(x, y, hwnd)
            flush += 1
            continue

        if flush == 3:
            print("没刷新次数喽，选万相之赐咯")
            CommonUtils.click_img_select_fz(万相之赐文字, hwnd)
            break;

    if flag == 1:
        print("点击结算")
        overX, overY = overAddress[random.randint(0, 9)].split(',')
        CommonUtils.click_point_random(overX, overY, hwnd)
        time.sleep(random.uniform(1.0, 2.0))
        while CommonUtils.openimages(万相铃, hwnd) != 0:
            print("---没有成功点击结算!!!---")
            time.sleep(random.uniform(1.2, 2.0))

            CommonUtils.click_point_random(overX, overY, hwnd)


def 选择万相之赐():
    # 刷新次数
    time.sleep(random.uniform(1.5, 2.5))

    print("打次数少直接不选")
    print("是否有奖励页面 如果有直接停止")
    if CommonUtils.openimages(万相铃, hwnd) != 0:
        flush = 5
        print("点击结算")
        overX, overY = overAddress[random.randint(0, 9)].split(',')
        CommonUtils.click_point_random(overX, overY, hwnd)
        time.sleep(random.uniform(1.2, 2.0))

        playCount = 0
        while CommonUtils.openimages(万相铃, hwnd) != 0:
            print("---没有成功点击!!!---")
            time.sleep(random.uniform(1.2, 2.0))

            playCount = playCount + 1
            if playCount > 3:
                return
            CommonUtils.click_point_random(overX, overY, hwnd)
    if CommonUtils.openimages(柔风抱暖文字, hwnd) != 0:
        print("选柔风咯")
        CommonUtils.click_img_select_fz(柔风抱暖文字, hwnd)

    if CommonUtils.openimages(六道暴虐, hwnd) != 0:
        print("选暴虐咯")
        CommonUtils.click_img_select(六道暴虐, hwnd)

    if CommonUtils.openimages(妖力化身文字, hwnd) != 0:
        print("选分身咯")
        CommonUtils.click_img_select_fz(妖力化身文字, hwnd)

    if CommonUtils.openimages(细雨化屏文字, hwnd) != 0:
        print("选化雨咯")
        CommonUtils.click_img_select_fz(细雨化屏文字, hwnd)

    if CommonUtils.openimages(万相之赐文字, hwnd) != 0:
        print("没钱喽，选万相之赐咯")
        CommonUtils.click_img_select_fz(万相之赐文字, hwnd)

    print("点击结算")
    overX, overY = overAddress[random.randint(0, 9)].split(',')
    CommonUtils.click_point_random(overX, overY, hwnd)
    time.sleep(random.uniform(1.5, 2.5))
    while CommonUtils.openimages(万相铃, hwnd) != 0:
        print("---没有成功点击结算!!!---")
        time.sleep(random.uniform(1.2, 2.0))

        CommonUtils.click_point_random(overX, overY, hwnd)


def 选择初始技能():
    if CommonUtils.openimages(柔风抱暖文字, hwnd) != 0:
        print("选柔风咯")
        CommonUtils.click_img_select_fz(柔风抱暖文字, hwnd)


def 备战BOSS():
    print("点击备战")
    CommonUtils.click_img(备战, hwnd)
    time.sleep(random.uniform(1.5, 2.5))
    检查技能()
    CommonUtils.click_img_no_retry(退出技能重置, hwnd)


def 检查技能():
    print("检查技能是否全")
    print("技能不全")
    CommonUtils.click_img(技能刷新, hwnd)
    time.sleep(random.uniform(1.5, 2.5))
    CommonUtils.click_img(重置技能, hwnd)
    time.sleep(random.uniform(1.5, 2.5))
    CommonUtils.click_img(确认按钮, hwnd)
    time.sleep(random.uniform(1.5, 2.5))
    print("填充技能")
    CommonUtils.click_img_no_retry(小柔风抱暖, hwnd)
    CommonUtils.click_img(装备, hwnd)

    CommonUtils.click_img_no_retry(小六道暴虐, hwnd)
    CommonUtils.click_img(装备, hwnd)

    CommonUtils.click_img_no_retry(小细雨化屏, hwnd)
    CommonUtils.click_img(装备, hwnd)

    CommonUtils.click_img_no_retry(小妖力化身, hwnd)
    CommonUtils.click_img(装备, hwnd)

    CommonUtils.click_img_no_retry(退出技能重置, hwnd)
    # if CommonUtils.openimages(检查柔风抱暖,hwnd) == 0 and  CommonUtils.openimages(检查六道暴虐,hwnd) == 0 and CommonUtils.openimages(检查细雨化屏, hwnd) == 0 and  CommonUtils.openimages(检查妖力化身,hwnd) == 0 :


def 选择符咒():
    # 刷新次数
    flag = 0
    print("选符咒咯")
    time.sleep(random.uniform(1.0, 2.0))
    while flag == 0:
        if CommonUtils.openimages(攻击御守, hwnd) != 0:
            print("选攻击御守咯")
            CommonUtils.click_img_select_fz(攻击御守, hwnd)
            flag = 1
            break
        if CommonUtils.openimages(火之卷, hwnd) != 0:
            print("选火之卷咯")
            CommonUtils.click_img_select_fz(火之卷, hwnd)
            flag = 1
            break
        if CommonUtils.openimages(变呱符咒, hwnd) != 0:
            print("选变呱符咒咯")
            CommonUtils.click_img_select_fz(变呱符咒, hwnd)
            flag = 1
            break
        if CommonUtils.openimages(雷之卷, hwnd) != 0:
            print("选雷之卷咯")
            CommonUtils.click_img_select_fz(雷之卷, hwnd)
            flag = 1
            break

        if CommonUtils.openimages(冰之卷, hwnd) != 0:
            print("选冰之卷咯")
            CommonUtils.click_img_select_fz(冰之卷, hwnd)
            flag = 1
            break
        if CommonUtils.openimages(抵抗御守, hwnd) != 0:
            print("选抵抗御守咯")
            CommonUtils.click_img_select_fz(抵抗御守, hwnd)
            flag = 1
            break
        if CommonUtils.openimages(风之卷, hwnd) != 0:
            print("选风之卷咯")
            CommonUtils.click_img_select_fz(风之卷, hwnd)
            flag = 1
            break
        if CommonUtils.openimages(石之卷, hwnd) != 0:
            print("选石之卷咯")
            CommonUtils.click_img_select_fz(石之卷, hwnd)
            flag = 1
            break
        if CommonUtils.openimages(生命御守, hwnd) != 0:
            print("选生命御守咯")
            CommonUtils.click_img_select_fz(生命御守, hwnd)
            flag = 1
            break
        if CommonUtils.openimages(庇护头盔, hwnd) != 0:
            print("选庇护头盔咯")
            CommonUtils.click_img_select_fz(庇护头盔, hwnd)
            flag = 1
            break
        if CommonUtils.openimages(抵抗御守, hwnd) != 0:
            print("选抵抗御守咯")
            CommonUtils.click_img_select_fz(抵抗御守, hwnd)
            flag = 1
            break
        if CommonUtils.openimages(妒火人偶, hwnd) != 0:
            print("选妒火人偶咯")
            CommonUtils.click_img_select_fz(妒火人偶, hwnd)
            flag = 1
            break
        if CommonUtils.openimages(黑蛇莲, hwnd) != 0:
            print("选黑蛇莲咯")
            CommonUtils.click_img_select_fz(黑蛇莲, hwnd)
            flag = 1
            break
        if CommonUtils.openimages(乾坤袋, hwnd) != 0:
            print("选乾坤袋咯")
            CommonUtils.click_img_select_fz(乾坤袋, hwnd)
            flag = 1
            break


def 开始六道月之海():
    start = datetime.datetime.now()
    print("现在是：" + str(start))
    print("预计挑战六道月之海 " + str(maxcount) + "局")
    # 战斗次数
    playCount = 0
    while playCount < maxcount:
        print("------------------------")
        print("开始打第 " + str(playCount + 1) + " 次")
        playCount += 1
        fightCount = 2

        if CommonUtils.openimages(六道入口, hwnd) != 0:
            print("六道入口")
            CommonUtils.click_img(六道入口, hwnd)
            time.sleep(random.uniform(2.0, 2.5))
        if CommonUtils.openimages(月之海入口, hwnd) != 0:
            print("月之海入口")
            CommonUtils.click_img(月之海入口, hwnd)
            time.sleep(random.uniform(2.0, 2.5))
        if CommonUtils.openimages(开启按钮, hwnd) != 0:
            fightCount = 0
            # 首先找到开启坐标 点击
            CommonUtils.click_img(开启按钮, hwnd)
            time.sleep(random.uniform(2.0, 2.5))

            # 找到确定坐标 点击
            CommonUtils.click_img(确定开始, hwnd)
            time.sleep(random.uniform(1.2, 2.0))

            # 找到开启2坐标 点击
            CommonUtils.click_img(开启2按钮, hwnd)
            time.sleep(random.uniform(1.2, 2.0))

            # 找到柔风保暖坐标 点击
            选择初始技能()
        if CommonUtils.openimages(继续按钮, hwnd) != 0:
            # 首先找到开启坐标 点击
            CommonUtils.click_img(继续按钮, hwnd)
            time.sleep(random.uniform(1.2, 2.0))

        print("开始战斗")
        关卡内战斗(fightCount)

    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")
    # os.system('shutdown -s -t 1')  # 1代表一秒内关机，可自行设置


# 选择技能(0)
开始六道月之海()
