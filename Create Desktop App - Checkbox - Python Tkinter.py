from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Turtle Code")

window.geometry('350x200')

combo = Combobox(window)

combo['values'] = (1, 2, 3, 4, 5, "Text")

combo.current(2)

combo.grid(column = 0, row = 0)

lbl = Label(window, text = " Hello ")
lbl.grid(column = 1 , row = 4)

def clicked():
    if combo.get() == "1":
        lbl.configure(text = "You picked 1")
    elif combo.get() == "2":
        lbl.configure(text = "You picked 2")
    elif combo.get() == "3":
        lbl.configure(text = "You picked 3")
    elif combo.get() == "4":
        lbl.configure(text = "You picked 4")
    else:
        lbl.configure(text = "None")

btn = Button(window, text = "Click me", command = clicked)
btn.grid(column=2 , row = 0)

window.mainloop()