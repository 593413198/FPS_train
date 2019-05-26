#!/usr/bin/python3
# @brief: 一个练fps手速的小游戏，类似于aim
# @author: luhao
# @date: 2019,5,26

from tkinter import *
import tkinter.messagebox as messagebox
from time import *
from random import *
import threading

window = Tk()
window.title('fps training')
window.geometry('1000x900') # 窗口坐标范围是x<=1000,y<=900,from 0

start_time = int(time()) # 游戏开始时间，以秒为单位，后7位小数

canvas = Canvas(window, bg='black')  # 主画布

R = 50 # 生成圈的半径

def run():
    x = randint(0+R,1000-R)
    y = randint(0+R,900-R)
    canvas.create_oval(x,y,x+R/(2**0.5),y+R/(2**0.5),fill='white',outline='white')
    window.after(600,run)

more = 1

def change():
    global more
    # 把所有圈逐渐放大
    more += 0.06
    for i in canvas.find_all():
        x, y = canvas.coords(i)[0], canvas.coords(i)[1]
        canvas.delete(i)
        canvas.create_oval(x,y,x+more*R/(2**0.5),y+more*R/(2**0.5),fill='white',outline='white')
    window.after(400,change)

run()
change()

def near(x0, y0, x, y, r): # 判断鼠标点击是否在圈的一定范围内
    if (x-x0)**2 + (y-y0)**2 <= r**2:
        return True
    return False

def onLeftDown(event): # 单击鼠标左键
    x = event.x
    y = event.y
    for i in canvas.find_all():
        x0, y0 = canvas.coords(i)[0], canvas.coords(i)[1]
        x1, y1 = canvas.coords(i)[2], canvas.coords(i)[3]
        r = (x0-x1)**2 + (y0-y1)**2
        if near(x0, y0, x, y, r):
            canvas.delete(i)

canvas.bind('<Button-1>',onLeftDown) # 单击鼠标左键
canvas.pack(fill=BOTH, expand=YES)
window.mainloop()
