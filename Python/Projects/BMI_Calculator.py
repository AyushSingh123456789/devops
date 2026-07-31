from tkinter import *

def BMI():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight/(height*height)
    
    if bmi <= 18.5:
        Result_label.config(text=f"BMI: {bmi:.2f}, Hella Underweight")
    elif bmi > 18.5 and bmi <= 24.9:
        Result_label.config(text=f"BMI: {bmi:.2f}, Normal Weight")
    else:
        Result_label.config(text=f"BMI: {bmi:.2f}, Hella Overweight")


root = Tk()

weight_label = Label(root,text="Enter Weight(in kg): ",padx=5,pady=5)
height_label = Label(root,text="Enter Height(in m): ",padx=5,pady=5)

weight_entry = Entry(root)
height_entry = Entry(root)

Calculate_BMI = Button(root,text="Calculate",command=BMI,padx=5,pady=5,bg="Purple")


Result_label = Label() # A label defined just for displaying the final BMI at the end of it all.

weight_label.grid(row=0,column=0)
weight_entry.grid(row=0,column=1)
height_label.grid(row=1,column=0)
height_entry.grid(row=1,column=1)
Calculate_BMI.grid(row=3,column=1)
Result_label.grid(row=4,column=0,padx=2,pady=5)

root.geometry("300x300")
root.mainloop()