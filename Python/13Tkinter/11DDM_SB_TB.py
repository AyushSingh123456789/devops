from tkinter import *

def function1():
    print("Menu item clicked")

root = Tk()

my_menu = Menu(root)
root.config(menu=my_menu) # No grid() or pack() allowed here.

sub_menu = Menu(my_menu)

my_menu.add_cascade(label="File",menu=sub_menu)

sub_menu.add_command(label="Project",command=function1)
sub_menu.add_command(label="Save",command=function1)


# Status Bar-:

status = Label(root,text="This is the current status",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)


# Tool Bar-:

toolbar = Frame(root,bg="green")
insert_button = Button(toolbar,text="Insert files",command=function1)
delete_button = Button(toolbar,text="Delete files",command=function1)

insert_button.pack(side=LEFT,padx=2,pady=3)
delete_button.pack(side=LEFT,padx=2,pady=2)
toolbar.pack()

root.geometry("300x300")
root.mainloop()