# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 14:07:30 2023

@author: Marcus
"""

import tkinter as tk
window = tk.Tk()
window.title("Menu")
window.geometry("500x500")
menuBar = tk.Menu(window)
fileMenu = tk.Menu(menuBar,tearoff=False)
fileMenu.add_command(label="new game")
fileMenu.add_command(label="Admin code")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")
menuBar.add_cascade(label="file",menu=fileMenu)
ayyyyooo = tk.Menu(menuBar,tearoff=False)
ayyyyooo.add_command(label="H")
ayyyyooo.add_command(label="i")
menuBar.add_cascade(label="ayyyyooo",menu=ayyyyooo)
Admincode = tk.Menu(menuBar,tearoff=False)
Admincode.add_command(label="kill arua")
Admincode.add_command(label="fly hack")
Admincode.add_command(label="atuo toxit")
Admincode.add_command(label="anti void")
fileMenu.add_cascade(label="Admincode",menu=Admincode)

window.config(menu=menuBar)
window.mainloop()