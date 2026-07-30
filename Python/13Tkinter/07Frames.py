# 2 Frames inserted inside a single window in order to view/calculate two different things side by side in a gui window.

from tkinter import *

root = Tk()
frame = Frame(root,highlightthickness=1,highlightbackground="white",padx="20",pady="20")
frame.pack()
frame2 = Frame(root)
frame2.pack(side=BOTTOM)

root.geometry("600x460")

button = Button(frame,text="Button1")
button2 = Button(frame2,text="Button2")
button.pack()
button2.pack()

root.mainloop()

