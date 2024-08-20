import customtkinter
from customtkinter import *

window = CTk()
window.geometry('380x520')
window.minsize(380, 520)
window.title('Notes')

set_default_color_theme('blue')

def theme_change():
    current_theme = get_appearance_mode()

    if current_theme == "Dark":
        set_appearance_mode("light")
    else:
        set_appearance_mode("dark")

def create_note():
    tab_names = tabview._tab_dict.keys()

    numeric_tab_names = [int(name) for name in tab_names if name.isdigit()]

    if len(numeric_tab_names) >= 10:
        return

    if numeric_tab_names:
        next_note = max(numeric_tab_names) + 1
    else:
        next_note = 1

    tabview.add(str(next_note))
    CTkTextbox(master = tabview.tab(str(next_note)), font = ('Dubai', 12), width = 320, height = 420, wrap = WORD).pack()

def close_note():
    if tabview.get() == '🏠':
        pass
    else:
        tabview.delete(tabview.get())

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
