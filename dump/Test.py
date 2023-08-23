from tkinter import *
from PIL import Image, ImageTk
import win32gui
import win32con
import pyautogui
from win32api import GetSystemMetrics
from pynput.mouse import Listener
import win32api
import time


class Gui:

    bg = Canvas
    root = Tk()

    def main(self):
        self.setClickthrough()
        self.window()

    def print_hi(name):
        print(f'Hi, {name}')

    def setClickthrough(self):
        print("setting window properties")
        try:
            styles = win32gui.GetWindowLong(self, win32con.GWL_EXSTYLE)
            styles = win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
            win32gui.SetWindowLong(self, win32con.GWL_EXSTYLE, styles)
            win32gui.SetLayeredWindowAttributes(self, 0, 255, win32con.LWA_ALPHA)
        except Exception as e:
            print(e)

    def window(self):
        width = GetSystemMetrics(0) #self.winfo_screenwidth()
        height = GetSystemMetrics(1) #self.winfo_screenheight()

        self.root.geometry('%dx%d' % (width, height))
        self.root.title("Applepie")
        self.root.attributes('-transparentcolor', 'white', '-topmost', 1)
        self.root.config(bg='white')
        self.root.bind('<Button-1>', self.on_click)
        #root.attributes("-alpha", 0.25)
        self.root.wm_attributes("-topmost", 1)
        bg = Canvas(self.root, width=width, height=height, bg='white')

        self.root.lift
        self.root.attributes("-fullscreen", 1)
        self.root.attributes("-topmost", 1)
        self.setClickthrough()
        #self.stay_on_top()

        #frame = ImageTk.PhotoImage(file="shot.png")
     #bg.create_image(1920 / 2, 1080 / 2, image=frame)
        bg.create_rectangle(200, 200, 600, 600, fill="#476042")
        bg.pack()
        self.root.mainloop()

    def on_click(self, event):
        position = pyautogui.position()
        self.bg.create_rectangle(position.x, position.y, position.x+200, position.y+200, fill="#476042")
        return

    #def stay_on_top(self):
    #    self.root.lift
    #    self.root.after(2000, self.stay_on_top())

