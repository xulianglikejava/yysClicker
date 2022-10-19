import win32gui, win32con, win32api,win32ui
from win32clipboard import *
from PIL import Image
import cv2
import numpy as np
import aircv as ac
import random
import time

hwndBig = win32gui.FindWindow(0, "阴阳师 - MuMu模拟器")



def test():

    win32gui.SetWindowText(hwndBig,'铁血战士胖虎')

test()
