class Parent:
    def __init__(self):
        self.parent_balance = 50000
       
    def display_balance(self):
        print(f"Parent's balance is: {self.parent_balance}") 
        
class Child(Parent):
    #pass
    def __init__(self):
        super().__init__()
        self.child_balance = 20000
    
    def display_balance(self):
        print(f"Child's balance is: {self.child_balance + self.parent_balance}")

mike = Child()
mike.display_balance()

#using super() method, we get access to the Parent Class, then calling __init__ method, allows us to access all the instance attributes along with all the methods declared inside that Parent Class.
# So, this lets us access the self.parent_balance.