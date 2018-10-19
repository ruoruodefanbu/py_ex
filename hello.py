#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import tkinter as tk

 

def btnHelloClicked():

                labelHello.config(text = "Hello,我的小宝宝!")

 

top = tk.Tk()

top.title("我开始写桌面程序啦啦啦")

 

labelHello = tk.Label(top, text = "Press the button...", height = 20, width = 80, fg = "blue")

labelHello.pack()

 

btn = tk.Button(top, text = "Hello", command = btnHelloClicked)

btn.pack()

 

top.mainloop()