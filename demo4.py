import win32gui

MAIN_HWND = 0

def is_win_ok(hwnd, starttext):
    s = win32gui.GetWindowText(hwnd)
    if s.startswith(starttext):

            global MAIN_HWND
            MAIN_HWND = hwnd
            return None
    return 1


def find_main_window(starttxt):
    global MAIN_HWND
    win32gui.EnumChildWindows(0, is_win_ok, starttxt)
    return MAIN_HWND


def winfun(hwnd, lparam):
    s = win32gui.GetWindowText(hwnd)
    if len(s) > 3:
        print("winfun, child_hwnd: %d   txt: %s" % (hwnd, s))
        print("bighwnd--->" + str(hwnd))

    return 1

def main():
    main_app = '铁血战士胖虎'
    hwnd = win32gui.FindWindow(None, main_app)
    if hwnd < 1:
        hwnd = find_main_window(main_app)

    if hwnd:
        win32gui.EnumChildWindows(hwnd, winfun, None)
    print("hwnd--->" + str(hwnd))
main()