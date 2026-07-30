# VVI

from tkinter import *

root = Tk()

for x in range(3):
    for y in range(3):
        frame = Frame(root)
        frame.grid(row=x,column=y)
        button = Button(frame,text=f"Row: {x}\n Column: {y}")
        button.pack(padx=5,pady=5)
        
# frame is added to the gui window using 'grid' method for a 3X3 layout(complex layout), while button is added to the gui window using 'pack' method, as it's a simple approach.

root.geometry("300x300")
root.mainloop()