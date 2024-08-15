from customtkinter import *

window = CTk()
window.geometry('400x550')
window.title('Notes')

colourVar = 0

set_default_color_theme('blue')

def theme_change():
    if get_appearance_mode() == 'Dark':
        set_appearance_mode('light')
    else:
        set_appearance_mode('dark')

CTkLabel(master = window, text = 'Simple Notes', font = ('Dubai', 24, 'bold'), text_color = '#1F6AA9').pack()

tabview = CTkTabview(master = window)
tabview.add('Note 1')
tabview.add('Note 2')
tabview.pack()

CTkTextbox(master = tabview.tab('Note 1'), font = ('Dubai', 12), width = 320, height = 420).pack()
CTkTextbox(master = tabview.tab('Note 2'), font = ('Dubai', 12), width = 320, height = 420).pack()

CTkButton(master = window, text = 'Theme', font = ('Dubai', 12, 'bold'), width = 20, height = 20, command = theme_change).pack(side = 'top', padx = 3, pady = 6)

window.mainloop()