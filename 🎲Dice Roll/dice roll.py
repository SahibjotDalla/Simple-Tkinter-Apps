import tkinter, ttkbootstrap, random

from tkinter import *
from ttkbootstrap import *

def button_press():
    output_var.set(random.randrange(1, 6))

#| Window
window = ttkbootstrap.Window(themename = 'darkly')
window.title('App')

window.geometry('500x300')

#| Label
text = tkinter.Label(master = window, text = 'Roll A Dice', font = ('Calibri, 24'))
text.pack()

#| Button
button_frame = tkinter.Frame(master = window)
button = tkinter.Button(master = button_frame, text = 'Roll', command = button_press)

button_frame.pack()
button.pack(side = 'left', pady = 10)

#| Output
output_var = tkinter.StringVar()
output_label = tkinter.Label(master = window, font = ('Calibri, 10'), textvariable = output_var)

output_label.pack(pady = 10)

window.mainloop()