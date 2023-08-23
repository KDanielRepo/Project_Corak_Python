from tkinter import *

import pywintypes
from PIL import Image, ImageTk
import win32gui
import win32con
import pyautogui
from win32api import GetSystemMetrics
from pynput.mouse import Listener
import win32api
import time


class Gui(Frame):
    def __init__(self, master, width, height):
        Frame.__init__(self, master=None)
        print(width)
        print(height)
        self.canvas = Canvas(self, width=width, height=height, bg='white')
        self.canvas.bind('<Button-1>', self.on_click)
        self.canvas.grid(row=0, column=0, sticky=N + S + E + W)
        print('created')
        #self.canvas.create_rectangle(0, 0, 600, 600, fill="#476042")

    def on_click(self, event):
        print('click')
        position = pyautogui.position()
        self.canvas.create_rectangle(position.x, position.y, (position.x+200), (position.y+200), fill="#476042")
        return

