import win32gui, win32con, win32api,win32ui

import CommonUtils
import async_all

hwnd = win32gui.FindWindow(0, "阴阳师 - MuMu模拟器")



def rename():
    hwnd = win32gui.FindWindow(0, "阴阳师 - MuMu模拟器")
    win32gui.SetWindowText(hwnd,'川源')


