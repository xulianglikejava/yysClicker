import math
import win32gui, win32con, win32api,win32ui
from PIL import Image
import cv2
import numpy as np
import aircv as ac
import time
import CommonUtils
import random
import datetime
import os
import logging

import async_all

# 体力
power = 350
# 每局消耗体力
consume = 60
# 计划打的局数
maxcount = 2
# 每局消耗时间
consumeTime = 500
# 大等待时间
bigWaitTime = 3
# 小等待时间
smallWaitTime = 2

仿造按钮 = './image/六道-月之海/仿造按钮.png'
准备按钮 = './image/六道-月之海/准备按钮.png'
开启按钮 = './image/六道-月之海/开启按钮.png'
开启2按钮 = './image/六道-月之海/开启2按钮.png'
技能怪 = './image/六道-月之海/技能怪.png'
挑战按钮 = './image/六道-月之海/挑战按钮.png'
星之子按钮 = './image/六道-月之海/星之子按钮.png'
柔风抱暖 = './image/六道-月之海/柔风抱暖.png'
细雨化屏 = './image/六道-月之海/细雨化屏.png'
暴虐按钮 = './image/六道-月之海/暴虐按钮.png'
妖力分身 = './image/六道-月之海/妖力分身.png'
混沌按钮 = './image/六道-月之海/混沌按钮.png'
确定按钮 = './image/六道-月之海/确定按钮.png'
确认按钮 = './image/六道-月之海/确认按钮.png'
神秘按钮 = './image/六道-月之海/神秘按钮.png'
跳过按钮 = './image/六道-月之海/跳过按钮.png'
选择按钮 = './image/六道-月之海/选择按钮.png'
麓战按钮 = './image/六道-月之海/麓战按钮.png'
麓战1 = './image/六道-月之海/麓战1.png'
麓战2 = './image/六道-月之海/麓战2.png'
麓战3 = './image/六道-月之海/麓战3.png'
麓战4 = './image/六道-月之海/麓战4.png'
麓战5 = './image/六道-月之海/麓战5.png'
月读按钮 = './image/六道-月之海/月读按钮.png'
万相之赐 = './image/六道-月之海/万相之赐.png'
没钱按钮 = './image/六道-月之海/没钱按钮.png'
刷新按钮 = './image/六道-月之海/刷新按钮.png'


# 技能怪坐标
powerX = 637
powerY = 252

# 读取文件里的结算坐标
overAddress = []
overFile = open('./address/结界突破/结算坐标.txt')
for line in overFile.readlines():
    line = line.strip('\n')
    overAddress.append(line)
# 赋值完毕
overFile.close()




hwnd = CommonUtils.getBigHwnd()

def 关卡内战斗():
    # 判断是否打到月读了
    while CommonUtils.openimages(月读按钮, hwnd) != 0:
         # 调整技能
         break

    麓战()




def 麓战():
    # 判断是否有麓战 优先打麓战
    while CommonUtils.openimages(麓战1, hwnd) != 0:
        print("打技能怪喽")
        CommonUtils.click_img(麓战1, hwnd)

        CommonUtils.click_point_random(powerX, powerY, hwnd)

        CommonUtils.click_img(挑战按钮, hwnd)

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
                break;
        break
    while CommonUtils.openimages(麓战2, hwnd) != 0:
        print("打技能怪喽")
        CommonUtils.click_img(麓战2, hwnd)

        CommonUtils.click_point_random(powerX, powerY, hwnd)

        CommonUtils.click_img(挑战按钮, hwnd)

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
                break;
        break

        # 判断是否有麓战 优先打麓战
    while CommonUtils.openimages(麓战3, hwnd) != 0:
        print("打技能怪喽")
        CommonUtils.click_img(麓战3, hwnd)

        CommonUtils.click_point_random(powerX, powerY, hwnd)

        CommonUtils.click_img(挑战按钮, hwnd)

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
                break;
        break
    while CommonUtils.openimages(麓战4, hwnd) != 0:
        print("打技能怪喽")
        CommonUtils.click_img(麓战4, hwnd)

        CommonUtils.click_point_random(powerX, powerY, hwnd)

        CommonUtils.click_img(挑战按钮, hwnd)

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
                break;
        break
    while CommonUtils.openimages(麓战5, hwnd) != 0:
        print("打技能怪喽")
        CommonUtils.click_img(麓战5, hwnd)

        CommonUtils.click_point_random(powerX, powerY, hwnd)

        CommonUtils.click_img(挑战按钮, hwnd)

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
                break;
        break

def 选择技能():
    # 刷新次数
    flush = 0
    flag = 0
    print("选技能咯")
    while flag == 0:
        if flush < 3 :
            if CommonUtils.openimages(柔风抱暖, hwnd) != 0:
                print("选柔风咯")
                CommonUtils.click_img_select(柔风抱暖,hwnd)
                break;

            if CommonUtils.openimages(细雨化屏, hwnd) != 0:
                print("选化雨咯")
                CommonUtils.click_img_select(细雨化屏,hwnd)
                break;

            if CommonUtils.openimages(暴虐按钮, hwnd) != 0:
                print("选暴虐咯")
                CommonUtils.click_img_select(暴虐按钮,hwnd)
                break;

            if CommonUtils.openimages(妖力分身, hwnd) != 0:
                print("选分身咯")
                CommonUtils.click_img_select(妖力分身,hwnd)
                break;

            if CommonUtils.openimages(没钱按钮, hwnd) == 0:
                print("没钱喽，选万相之赐咯")
                CommonUtils.click_img(万相之赐,hwnd)
                break;

            if CommonUtils.openimages(没钱按钮, hwnd) != 0:
                print("刷新！刷新技能!")
                CommonUtils.click_img(刷新按钮,hwnd)
                flush += 1

    overX, overY = overAddress[random.randint(0, 9)].split(',')
    CommonUtils.click_point_random(overX, overY,hwnd)



def 开始六道月之海() :
    start = datetime.datetime.now()
    print("现在是：" +  str(start))
    print("预计挑战六道月之海 " + str(maxcount) + "局")

    # 战斗次数
    playCount = 0
    while playCount < maxcount :
        print("------------------------")
        print("开始打第 " + str(playCount + 1) + " 次")

        # 首先找到开启坐标 点击
        CommonUtils.click_img(开启按钮,hwnd)
        time.sleep(random.uniform(0.8, 1.2))

        # 找到确定坐标 点击
        CommonUtils.click_img(确定按钮, hwnd)
        time.sleep(random.uniform(0.8, 1.2))

        # 找到开启2坐标 点击
        CommonUtils.click_img(开启2按钮, hwnd)
        time.sleep(random.uniform(0.8, 1.2))

        # 找到柔风保暖坐标 点击
        CommonUtils.click_img_select(柔风按钮, hwnd)
        time.sleep(random.uniform(0.8, 1.2))



    end = datetime.datetime.now()
    print("总共耗时为：" + str(end - start) + " 秒")
    # os.system('shutdown -s -t 1')  # 1代表一秒内关机，可自行设置


关卡内战斗()