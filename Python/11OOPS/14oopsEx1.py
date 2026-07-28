# Creating a class
class Vehicle:
    # Class Attributes:
    class_attribute = "This is a vehicle class"
    
    # Instance Attributes:
    # Creating an Instance Constructor
    def __init__(self, name, color):
        # Instance Variables
        self.name = name
        self.color = color
    #pass
    # instance method
    def display_info(self):
        print(f"Name: {self.name}, Color: {self.color}")
    
    # Class method
    @classmethod
    def class_method(cls):
        print("This is a class method")
        print(f"I can access the class attribute: {cls.class_attribute}")
    
    # Static method
    @staticmethod
    def static_method():
        print("I am static method, I cannot access anything")

# inheriting class       
class Car(Vehicle):
    #pass
    # Overriding Super class Constructor in sub class
    def __init__(self, name, color, fuel_type):
        super().__init__(name,color) #overriding the values of "name" and "color" from the Super class's __init__ const
        self.fuel_type = fuel_type
    # Overriding superclass method in the subclass
    def display_info(self):
        print(f"{self.name}, {self.color}, {self.fuel_type}")

# Creating an Object for instance methods and instance var
vehicle = Vehicle("CoolCar", "Red")
#print(f"{vehicle.name} {vehicle.color}")
vehicle.display_info() # calling an instance method

# Creating an Object for class method and class var
car = Car("Luxury", "Black", "Petrol")
car.display_info()

#print(Vehicle.class_attribute)
Vehicle.class_method() # calling a class method

Vehicle.static_method() # calling a static method