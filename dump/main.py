from tkinter import *
import win32gui
import gui
from win32api import GetSystemMetrics
import pynput

def on_click(x, y, c, d):
    print(x, y, c, d)


def on_press(a):
    print(a)


def callback(hwnd, extra):
    if win32gui.IsWindowVisible(hwnd):
        print(f"window text: '{win32gui.GetWindowText(hwnd)}'")


if __name__ == '__main__':
    root = Tk()
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)

    root.geometry('%dx%d' % (width, height))
    root.title("Project_Corak")
    root.attributes('-transparentcolor', 'white', '-topmost', 1)
    root.config(bg='white')
    #root.attributes("-alpha", 0.25)
    root.wm_attributes("-topmost", 1)

    root.lift
    root.attributes("-fullscreen", 1)
    root.attributes("-topmost", 1)
    gui = gui.Gui(root, width, height)
    gui.pack()

    with pynput.mouse.Listener(on_click=on_click) as mouseListener:
        with pynput.keyboard.Listener(on_press=on_press) as keyboardListener:
            root.mainloop()
            mouseListener.join()
            keyboardListener.join()






