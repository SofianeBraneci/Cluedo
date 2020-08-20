# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 21:15:04 2020

@author: hp
"""

from tkinter import * 
import threading 



class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        Label(text='Text', master=self).grid(row=0, column=0)

class Worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        App().mainloop()
    