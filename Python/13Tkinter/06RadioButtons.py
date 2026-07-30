from tkinter import *

def selected():
    label.config(text="Choice of fuel is: " + fuel.get())

root = Tk()
root.geometry("300x300")

fuel = StringVar(value="Petrol")
# default value could be anything b/w the three options.

radio1 = Radiobutton(root,text="Petrol",variable=fuel,value="Petrol",command=selected)
radio2 = Radiobutton(root,text="Diesel",variable=fuel,value="Diesel",command=selected)
radio3 = Radiobutton(root,text="Electric",variable=fuel,value="Electric",command=selected)
# 'value' criteria takes care of the selected box to be the one which is being clicked, and then pushes its value inside the 'fuel' variable. 

label = Label(root)

radio1.pack()
radio2.pack()
radio3.pack()
label.pack()
root.mainloop()