import pyautogui
import numpy as np
import cv2 as cv
from screencaptureutils import ScreenCaptureUtils
from time import time
import pynput
import keyboard
import datetime

#capture = ScreenCaptureUtils('Heroes of Might and Magic III: Horn of the Abyss')
capture = ScreenCaptureUtils('RetroArch FCEUmm (SVN) ad2c71d')
loop_time = time()
fps_counter = False
show_capture = True

def on_click(x, y, c, d):
    print(x, y, c, d)


def on_press(a):
    print(a)


if __name__ == '__main__':
    while True:
        key = cv.waitKey(1)
        if show_capture:
            sc = capture.capture_v2()
            cv.imshow('Test', sc)
            if key == ord('q'):
                cv.destroyAllWindows()
                break
        if keyboard.is_pressed('y'):
            sc = capture.capture_v2()
            time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            save_path = f"C:\\Users\\Daniel\\Desktop\\HOMM3_SCREENS\\image{time}.jpg"
            cv.imwrite(save_path, sc)
        if fps_counter:
            print('FPS {}'.format(1 / (time() - loop_time)))
            loop_time = time()
