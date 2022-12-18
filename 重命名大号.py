import win32gui, win32con, win32api,win32ui

import CommonUtils
import async_all

hwnd = win32gui.FindWindow(0, "阴阳师 - MuMu模拟器")



def rename():

    win32gui.SetWindowText(hwnd,'铁血战士胖虎')


rename()