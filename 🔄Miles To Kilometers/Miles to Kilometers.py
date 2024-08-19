import tkinter
from tkinter import *

import ttkbootstrap
from ttkbootstrap import *


def convert_miles():
    value = input_int.get()
    output_str.set(value*1.60934)

# Window
window = ttkbootstrap.Window(themename = 'darkly')
window.title('App')
window.geometry('300x150')

# Title
title_label = tkinter.Label(master = window, text = 'Miles -> Kilometers', font = 'Calibri 24 bold')
title_label.pack()

# Input
input_frame = tkinter.Frame(master = window)
input_int = tkinter.IntVar()
input = tkinter.Entry(master = input_frame, textvariable = input_int)

# Button
button = tkinter.Button(master = input_frame, text = 'Convert', command = convert_miles)

# Input/Button Pack
input.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

# Output
output_str = tkinter.StringVar()
output_label = tkinter.Label(master = window, textvariable = output_str)
output_label.pack()

window.mainloop()