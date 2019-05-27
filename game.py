#!/usr/bin/python3
# @brief: 一个练fps手速的小游戏，类似于aim
# @author: luhao
# @date: 2019,5,26

from tkinter import *
import tkinter.messagebox as messagebox
from random import *

window = Tk()
window.title('fps training')
window.geometry('800x600') # 窗口坐标范围是x<=1000,y<=900,from 0

canvas = Canvas(window, bg='black')  # 主画布

D = 30 # 生成圈的直径

def run():
    x = randint(0,800-D)
    y = randint(0,600-D)
    canvas.create_oval(x,y,x+D,y+D,fill='white',outline='white')
    window.after(600,run)

more = 1

def change():
    global more
    # 把所有圈逐渐放大
    for i in canvas.find_all():
        x, y = canvas.coords(i)[0], canvas.coords(i)[1]
        x0, y0 = canvas.coords(i)[2], canvas.coords(i)[3]
        d = abs(x-x0)
        d += 0.1
        canvas.delete(i)
        canvas.create_oval(x,y,x+d,y+d,fill='white',outline='white')
    window.after(20,change) # 每隔20毫秒刷新一次


run()
change()

def onLeftDown(event): # 单击鼠标左键
    x = event.x
    y = event.y
    for i in canvas.find_all():
        x1, y1 = canvas.coords(i)[0], canvas.coords(i)[1]
        x2, y2 = canvas.coords(i)[2], canvas.coords(i)[3]
        if x1 <= x <= x2 and y1 <= y <= y2:
            # 判断鼠标点击区域在某个圈内
            canvas.delete(i) # 删除这个圈

canvas.bind('<Button-1>',onLeftDown) # 单击鼠标左键
canvas.pack(fill=BOTH, expand=YES)
window.mainloop()

