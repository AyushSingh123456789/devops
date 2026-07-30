from tkinter import *

def selected():
    sugar = sugar_var.get() #bool value
    ice = ice_var.get() # bool value
    cream = cream_var.get() # bool value
    
    if sugar:
        sugar="sugar"
    else:
        sugar="No sugar"
    if ice:
        ice="ice"
    else:
        ice="No ice"
    if cream:
        cream="cream"
    else:
        cream="No cream"
        
    label.config(text="Options selected are: " + sugar + " \n " + ice + " \n " + cream)

root = Tk()
root.geometry("300x300")

sugar_var = BooleanVar()
ice_var = BooleanVar()
cream_var = BooleanVar()

sugar_checkbox = Checkbutton(root,text="Sugar",variable=sugar_var,command=selected)
ice_checkbox = Checkbutton(root,text="Ice",variable=ice_var,command=selected)
cream_checkbox = Checkbutton(root,text="Cream",variable=cream_var,command=selected)

label = Label(root)

sugar_checkbox.pack()
ice_checkbox.pack()
cream_checkbox.pack()
label.pack()

root.mainloop()


# Imp note: Check Buttons inside tkinter allow to check all the boxes present, all at the same time, but if we want the user to be able to check only one box at a time, we'd use Radio Buttons. 
