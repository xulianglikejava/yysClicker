import datetime
import time
import win32clipboard
from 不怎么用的 import CommonUtils
import random
import pyautogui

hwnd = CommonUtils.getBigHwndMuMu()
评论 = '../image/抖音/评论.png'
更多 = '../image/抖音/更多.png'
maxcount = 30


# 读取文件里的结算坐标
revierArr = []
revierFile = open('../review/评论内容.txt', encoding='utf-8')
for line in revierFile.readlines():
    line = line.strip('\n')
    revierArr.append(line)
# 赋值完毕
revierFile.close()

def startReview(hwnd):
    print('开始评论')
    selectedReview = random.choice(revierArr)
    # 1.点击评论按钮
    CommonUtils.click_point_random(1,1,hwnd);
    review_delay();
    # 2.输入评论  点击输入栏按钮
    CommonUtils.click_point_random(1,1,hwnd);
    # 把数据放到剪切板
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(selectedReview, win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    time.sleep(3)
    # 把数据放到输入框
    pyautogui.hotkey('ctrl', 'v')
    review_delay(7,8);

    # 3.关闭评论
    CommonUtils.click_point_random(1,1,hwnd);




def 开始刷视频(hwnd):

    for i in range(maxcount):
        print('开始第{}次循环'.format(i))
        reviewFlag = random.randint(0, 9);
        print('本次随机数为{}'.format(reviewFlag))
        if reviewFlag >= 8 :
            # 大于7 进行评论  相当于20%概率评论吧
            startReview(hwnd);

        if reviewFlag >= 2 and reviewFlag < 6 :
            # 大于2小于6 进行滑动下个视频   相当于40%概率评论吧
            mouseScrol(random.randint(-90, -50))
        sleepTime = random.randint(3, 80);
        print('本次睡眠{}秒'.format(sleepTime))
        watch_delay();
        # 睡眠结束 滑动滚轮

        # 结束循环
        break;

def mouseScrol(shortest=-100):
    print('鼠标滚轮滑动{}圈'.format(shortest))
    pyautogui.scroll(shortest)
    review_delay()

def review_delay(shortest=1.5, longest=3.5):
    sleepTime = random.uniform(shortest, longest);
    print('本次评论睡眠{}秒'.format(sleepTime))
    time.sleep(sleepTime)

def watch_delay(shortest=20, longest=46):
    """生成一个介于最短和最长时间之间的随机延迟"""
    sleepTime = random.uniform(shortest, longest);
    print('本次观看睡眠{}秒'.format(sleepTime))
    time.sleep(sleepTime)


mouseScrol(random.randint(-90, -50))
