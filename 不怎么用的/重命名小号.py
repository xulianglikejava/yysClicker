import win32gui

hwnd = win32gui.FindWindow(0, "阴阳师 - MuMu模拟器")



def rename():
    win32gui.SetWindowText(hwnd,'捉鼠大师小叮当')

