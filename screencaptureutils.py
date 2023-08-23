import pyautogui
import numpy as np
import cv2 as cv
import win32gui, win32con, win32ui
import time
import datetime


class ScreenCaptureUtils:
    hwnd = None
    width = 0
    height = 0
    #width_offset = 8
    #height_offset = 50
    x_position = 0
    y_position = 0

    def __init__(self, window_name):
        #self.list_window_names()
        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception('Window not found: {}'.format(window_name))
        win32gui.SetForegroundWindow(self.hwnd)
        time.sleep(1.0)
        self.update_window_position()
        print(self.width, self.height)

    def capture_v2(self):
        self.update_window_position()
        desktop = win32gui.GetDesktopWindow()
        hwndDC = win32gui.GetWindowDC(desktop)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()

        saveBitMap = win32ui.CreateBitmap()
        #saveBitMap.CreateCompatibleBitmap(mfcDC, self.width-self.width_offset, self.height-self.height_offset)
        saveBitMap.CreateCompatibleBitmap(mfcDC, self.width, self.height)

        saveDC.SelectObject(saveBitMap)

        #saveDC.BitBlt((0, 0), (self.width-self.width_offset, self.height-self.height_offset), mfcDC, (window[0]+self.width_offset, window[1]+self.height_offset), win32con.SRCCOPY)
        saveDC.BitBlt((0, 0), (self.width, self.height), mfcDC, (self.x_position, self.y_position), win32con.SRCCOPY)

        bmpstr = saveBitMap.GetBitmapBits(True)

        img = np.fromstring(bmpstr, dtype='uint8')
        #img.shape = (self.height-self.height_offset, self.width-self.width_offset, 4)
        img.shape = (self.height, self.width, 4)

        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(desktop, hwndDC)

        return img

    @staticmethod
    def list_window_names():
        def callback(hwnd, extra):
            if win32gui.IsWindowVisible(hwnd):
                print(f"window text: '{win32gui.GetWindowText(hwnd)}'")
        win32gui.EnumWindows(callback, None)

    def take_screenshot(self):
        img = self.capture_v2()
        time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        save_path = f"C:\\Users\\Daniel\\Desktop\\HOMM3_SCREENS\\image{time}.jpg"
        screenshot.save(save_path)

    def get_window_position(self, window):
        return

    def update_window_position(self):
        window = win32gui.GetWindowRect(self.hwnd)
        if self.x_position != window[0]:
            self.x_position = window[0]
        if self.y_position != window[1]:
            self.y_position = window[1]
        if self.width == 0:
            self.width = window[2] - window[0]
        if self.height == 0:
            self.height = window[3] - window[1]
