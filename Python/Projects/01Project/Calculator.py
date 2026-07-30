from tkinter import *

def add():
    num1 = float(add_entry1.get())
    num2 = float(add_entry2.get())
    result = num1+num2
    
    result_label1.config(text=f"Result: {result}")
    
def subtract():
    num1 = float(subtract_entry1.get())
    num2 = float(subtract_entry2.get())
    result = num1-num2
    
    result_label2.config(text=f"Result: {result}")
    
def multiply():
    num1 = float(multiply_entry1.get())
    num2 = float(multiply_entry2.get())
    result = num1*num2
    
    result_label3.config(text=f"Result: {result}")
    
def divide():
    num1 = float(divide_entry1.get())
    num2 = float(divide_entry2.get())
    result = num1/num2
    
    result_label4.config(text=f"Result: {result}")

root = Tk()
root.geometry("300x300")

add_frame = Frame(root)
subtract_frame = Frame(root)
multiply_frame = Frame(root)
divide_frame = Frame(root)

add_button = Button(add_frame,text="Addition",bg="lightblue",command=add)
subtract_button = Button(subtract_frame,text="Subtraction",bg="red",command=subtract)
multiply_button = Button(multiply_frame,text="Multiplication",bg="yellow",command=multiply)
divide_button = Button(divide_frame,text="Division",bg="pink",command=divide)

add_entry1 = Entry(add_frame)
add_entry2 = Entry(add_frame)

subtract_entry1 = Entry(subtract_frame)
subtract_entry2 = Entry(subtract_frame)

multiply_entry1 = Entry(multiply_frame)
multiply_entry2 = Entry(multiply_frame)

divide_entry1 = Entry(divide_frame)
divide_entry2 = Entry(divide_frame)

add_frame.grid(row=0,column=0)
add_button.pack(padx=5,pady=5)
add_entry1.pack(padx=2,pady=2)
add_entry2.pack(padx=2,pady=2)
subtract_frame.grid(row=0,column=1)
subtract_button.pack(padx=5,pady=5)
subtract_entry1.pack(padx=2,pady=2)
subtract_entry2.pack(padx=2,pady=2)
multiply_frame.grid(row=1,column=0)
multiply_button.pack(padx=5,pady=5)
multiply_entry1.pack(padx=2,pady=2)
multiply_entry2.pack(padx=2,pady=2)
divide_frame.grid(row=1,column=1)
divide_button.pack(padx=5,pady=5)
divide_entry1.pack(padx=2,pady=2)
divide_entry2.pack(padx=2,pady=2)

result_label1 = Label(add_frame,text="Result: ")
result_label1.pack()
result_label2 = Label(subtract_frame,text="Result: ")
result_label2.pack()
result_label3 = Label(multiply_frame,text="Result: ")
result_label3.pack()
result_label4 = Label(divide_frame,text="Result: ")
result_label4.pack()

root.mainloop()


# Pehle frame lelo saare operations ke liye, aur saare frames ko grid mein row no aur column no deke saja do, phir wapas aake un saare frames ko button bana do,color dedo, fns. as command dedo, fir saare buttons ko pack krdo kuch padding ke saath, fir entry 2 numbers ki lelo saare operations ke liye, saare entries ko apne buttons pack ke niche hi pack karte jao kuch paddings ke saath. Ab result_label bana lo saare operations ke alag alag, unme respective operation_frame pass kardo, text mein: "result: " jaisa kardo, jo button ke just niche gui window mein dikhta rahega. result_labels ko pack bhi saath-saath hi karte jaana. Functions bana lo saare operations ke(jo command mein naam diya hai button declare karte waqt usi naam se), do numbers entry1 aur entry2 se lelo respective operations ke liye, usko string se integer/float transform kar lena, fir resultant operation(inside a var, e.g: result = num1+num2) ko pass karna inside a f-string inside respective result_label jo banaye hue the per operation, in the format: result_label1.config(text="result: " {result}). Fir ye result gui window mein just button ke niche hi dikhega(e.g: Result: 10.0)