from tkinter import *

class Demo:
    
    # All widgets creation goes inside the constructor method:
    def __init__(self,root1):
        frame = Frame(root1)
        frame.pack()
        
        self.printbutton = Button(frame,text="Click Here",command=self.printmessage)
        self.printbutton.pack()
        
        self.quitbutton = Button(frame,text="Exit",command=frame.quit)
        self.quitbutton.pack()
        
    # All methods creation goes inside the same class: 
    def printmessage(self):
        print("Button Clicked")
    
 # object creation and processes related to objects always outside the class:   
root = Tk()
b = Demo(root) # root obj get passed in the place of root1 in the constructor.

root.geometry("300x300")
root.mainloop()