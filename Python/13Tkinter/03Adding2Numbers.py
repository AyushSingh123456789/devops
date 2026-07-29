from tkinter import *

def add():
    # by default these values are accepted as strings, manually converted to int for addition
    n1 = int(number1.get())
    n2 = int(number2.get())
    result = str(n1+n2)
    # converted back to string to be able to be displayed inside the gui window instead of the terminal.
    answer.config(text="Answer is: "+ result)
    # used the label 'answer' inside the gui window to display the result using string concat.


root = Tk()
root.geometry("300x300")

number1 = Entry(root)
number2 = Entry(root)
number1.pack()
number2.pack()

button = Button(root,text='Add',command=add)
button.pack()

answer = Label(root)
answer.pack()


root.mainloop()