from tkinter import *

def selected():
    label.config(text=check_value.get())

root = Tk()
root.geometry("300x300")

check_value = BooleanVar() # accepting a boolean value using the checkbutton inside the gui window

checkbutton = Checkbutton(root,text="Accept terms",variable=check_value,command=selected)
# passed a variable to take value from checking and unchecking the defined checkbutton
checkbutton.pack()
label = Label(root)
label.pack()
root.mainloop()