class Student:
    #class variable
    category = "student"
    
    @classmethod
    def info(cls):
        print(f"This is a method of class {cls.category}")
        
Student.info()