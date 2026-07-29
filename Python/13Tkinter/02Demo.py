from tkinter import *

def display():
    data = entry.get() # gets the entered data from the gui window
    print(data)

root = Tk()
root.geometry("300x300")

entry = Entry(root)# taking entry/input from the user inside the gui window
entry.pack()

button = Button(root, text="Click here",command=display)
# commanding the button click inside the gui to execute our defined function "display" inside the terminal.
button.pack()
root.mainloop()