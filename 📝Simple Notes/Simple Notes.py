import customtkinter
from customtkinter import *

window = CTk()
window.geometry('380x520')
window.minsize(380, 520)
window.title('Notes')

Notes = 0

set_default_color_theme('blue')

def theme_change():

    if get_appearance_mode() == 'Dark':
        set_appearance_mode('light')

    else:
        set_appearance_mode('dark')

def create_note():
    global Notes

    if Notes < 10:
        Notes += 1
        tabview.add(str(Notes))
        CTkTextbox(master = tabview.tab(str(Notes)), font = ('Dubai', 12), width = 320, height = 420).pack()

    return Notes

def close_note():
    global Notes
    Notes -= 1

    if tabview.get() == '🏠':
        pass
    else:
        tabview.delete(tabview.get())

    return Notes

tabview = CTkTabview(master = window)
tabview.add('🏠')
tabview.pack()

CTkLabel(master = tabview.tab('🏠'), text = 'Simple Notes', font = ('Dubai', 24, 'bold'), text_color = '#1F6AA9').pack(side = TOP)
CTkLabel(master = tabview.tab('🏠'), text = 'Welcome To Simple Notes!', font = ('Dubai', 12)).pack(side = TOP)
CTkLabel(master = tabview.tab('🏠'), text = 'Press 🎨 to change between light and dark mode.', font = ('Dubai', 12)).pack(side = TOP)
CTkLabel(master = tabview.tab('🏠'), text = 'Press ➕ to create a new note.', font = ('Dubai', 12)).pack(side = TOP)
CTkLabel(master = tabview.tab('🏠'), text = 'Press ❌ to delete a note.', font = ('Dubai', 12)).pack(side = TOP)

Button_Frame = CTkFrame(master = window)

CTkButton(master = Button_Frame, text = '🎨', font = ('Dubai', 10), width = 20, height = 20, command = theme_change).pack(side = 'left', padx = 3, pady = 3)
CTkButton(master = Button_Frame, text = '➕', font = ('Dubai', 8), width = 22, height = 22, command = create_note).pack(side = 'left')
CTkButton(master = Button_Frame, text = '❌', font = ('Dubai', 8), width = 22, height = 22, command = close_note).pack(side = 'left', padx = 3, pady = 3)

Button_Frame.pack(pady = 5)

window.mainloop()
