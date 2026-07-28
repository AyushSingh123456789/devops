class Student:
    def __init__(self, name):
        self.name = name
        # instance variable
        
    # instance method: a method which accesses an instance variable defined inside a constructor.
    def hello(self): 
        # passing self is necessary to accept the variable as an instance.
        print(f"Hello, my name is {self.name}")
    
    # instance method    
    def name_length(self):
        return (len(self.name))
        

student1 = Student("Ayush")
student1.hello() # instance method acts on an Object
length = student1.name_length()
print(length)