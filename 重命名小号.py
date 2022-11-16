import win32gui, win32con, win32api,win32ui


import async_all

hwnd = win32gui.FindWindow(0, "阴阳师 - MuMu模拟器")


@async_all.async_call
def rename():
    win32gui.SetWindowText(hwnd,'捉鼠大师小叮当')

rename()