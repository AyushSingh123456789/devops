class Car:
    def __init__(self, brand):
        self.brand = brand
        self.steering_object = self.Steering()
    
    @staticmethod
    def drive():
        print("Drive")
        
    class Steering:
        @staticmethod
        def rotate():
            print("Rotate")
            
car = Car("ABC")
car.drive()

# For accessing and using an inner class's method:
# i) Create an inner class self object inside the outer class's __init__() method.
#ii) define: innerobject = outerclassobject.innerclassselfobject
#iii) use: innerobject.innermethod()

steering = car.steering_object
steering.rotate()