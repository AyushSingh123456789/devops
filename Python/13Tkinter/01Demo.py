#(Imp note: elements/texts added to a window are called widgets.)

from tkinter import *

root = Tk()
# creating a window object(instance) of class Tk
root.geometry("300x300")

hello = Label(root,text="Hello World",fg="red",bg="white",font=("Arial",16))
# Label belongs to the root window, and its value: "Hello World", with foreground color = "red", background color= "white", font type(only the ones on the machine) = Arial, size = 16.

hello.pack()



root.mainloop() 
# created window obj gets in a loop