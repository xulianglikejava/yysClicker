import win32gui

hwnd = win32gui.FindWindow(0, "雷电模拟器")



def rename():
    win32gui.SetWindowText(hwnd,'铁血战士胖虎')


rename()