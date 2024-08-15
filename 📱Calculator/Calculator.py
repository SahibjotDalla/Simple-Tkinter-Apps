from customtkinter import *

#| Operation Variables
addVar = False
subVar = False
divideVar = False
multiVar = False

#| Calculate Functions
def calculate():
    if addVar == True:
        answer = int(Value1.get()) + int(Value2.get())
        output.configure(text = answer)

    if subVar == True:
        answer = int(Value1.get()) - int(Value2.get())
        output.configure(text = answer)

    if multiVar == True:
        answer = int(Value1.get()) * int(Value2.get())
        output.configure(text = answer)

    if divideVar == True:
        answer = int(Value1.get()) / int(Value2.get())
        output.configure(text = answer)

#| Operation Functions
def add():
    global addVar
    global subVar
    global divideVar
    global multiVar

    addVar = True
    subVar = False
    divideVar = False
    multiVar = False

def sub():
    global addVar
    global subVar
    global divideVar
    global multiVar

    addVar = False
    subVar = True
    divideVar = False
    multiVar = False

def multi():
    global addVar
    global subVar
    global divideVar
    global multiVar

    addVar = False
    subVar = False
    divideVar = False
    multiVar = True

def divide():
    global addVar
    global subVar
    global divideVar
    global multiVar

    addVar = False
    subVar = False
    divideVar = True
    multiVar = False

#| Window
window = CTk()
window.geometry('500x300')
window.title('Calculator')

set_appearance_mode('dark')
set_default_color_theme('green')

#| Operation Button Frame
button_frame = CTkFrame(master = window)
button_frame.pack(side = 'top')

#| Operation Buttons
CTkButton(master = button_frame, text = '+', width = 1, corner_radius = 16, font = ('Dubai', 14, 'bold'), command = add).pack(side = 'left', padx = 1, pady = 10)
CTkButton(master = button_frame, text = '-', width = 1, corner_radius = 16, font = ('Dubai', 14, 'bold'), command = sub).pack(side = 'left', padx = 1, pady = 10)
CTkButton(master = button_frame, text = 'x', width = 1, corner_radius = 16, font = ('Dubai', 14, 'bold'), command = multi).pack(side = 'left', padx = 1, pady = 10)
CTkButton(master = button_frame, text = '÷', width = 1, corner_radius = 16, font = ('Dubai', 14, 'bold'), command = divide).pack(side = 'left', padx = 1, pady = 10)

#| Value Label
CTkLabel(master = window, font = ('Dubai', 24, 'bold'), text = 'Values').pack(side = 'top')

#| Values Frame
value_frame = CTkFrame(master = window)
value_frame.pack(side = 'top')

#| Value 1 Input
Value1 = CTkEntry(master = value_frame, border_color = '#FFFFFF', border_width = 2)
Value1.pack(side = 'left', pady = 5, padx = 5)

#| Value 2 Input
Value2 = CTkEntry(master = value_frame, border_color = '#FFFFFF', border_width = 2)
Value2.pack(side = 'right', pady = 5, padx = 5)

#| Output
output = CTkLabel(master = window, font = ('Dubai', 14, 'bold'), text = '')
output.pack(side = 'top')

#| Calculate Button
button = CTkButton(master = window, font = ('Dubai', 14, 'bold'), width = 1, corner_radius = 16, text = 'Calculate', command = calculate)
button.pack()

window.mainloop()