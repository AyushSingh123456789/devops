# static methods do not have any access to either the instance methods and its variables, nor class methods and its variables.

class Student:
    
    @staticmethod
    def add(a,b):
        print(a+b)
        
Student.add(10,5)

class Circle:
    @staticmethod
    def area(r):
        return 3.14 * (r * r)
    
    @staticmethod
    def circumference(r):
        return 2* 3.14 * r
    
a = Circle.area(10)
print(a)
c = Circle.circumference(10)
print(c)