class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    
class Teacher:
    def __init__(self, teacher_name, salary, grade):
        self.teacher_name = teacher_name
        self.salary = salary
        self.grade = grade
    
    def display_salary(self):
        print(f"The salary of {self.teacher_name} is {self.salary} rupees.")
        
        
class Course:
    def __init__(self, grade, name, teacher_name):
        self.grade = grade
        self.name = name
        self.teacher_name = teacher_name
    
    def display_course_details(self):
        print(f"The student {self.name} with grade {self.grade} has been appointed {self.teacher_name} as their teacher for the next semester.")
        
    
    
while True:
    choice = input("Choose from the following options: \n1) Assign myself a teacher \n2)Check salary of Teachers(cond applied) \n3) Exit the program \n")
    if choice == "1":
        print("To assign yourself a Teacher and a Course to study, Follow the necessary steps provide below")
        name = input("Enter your name: ")
        grade = input("Choose your grade of prev sem(A,B,C,D,E,F): ")
        if grade == "E" or grade == "F":
            print("Sorry, you have failed the exam, and hence won't be allowed to study the next semester")
            break
        teacher_name = input("Choose your teacher b/w 'AA Sir' or 'AB Sir': ")
        course = Course(grade, name, teacher_name)
        course.display_course_details()
    
    elif choice == "2":
        teacher_name = input("Choose the teacher of whom you wanna check the salary of \n1) AA Sir \n2) AB Sir: \n")
        if teacher_name == "1":
            teacher_name = "AA Sir"
            salary = "45000"
        elif teacher_name == "2":
            teacher_name = "AB Sir"
            salary = "50000"
        else:
            print("Invalid Value, exiting the program")
            break
        
        grade = input("Enter your grade(A,B,C,D,E,F): ")
        if grade == "B" or grade == "C" or grade == "D" or grade == "E" or grade == "F":
            print("Sorry, you are not eligible to check the salary of " + teacher_name)
            break
        
        teacher = Teacher(teacher_name, salary, grade)
        teacher.display_salary()
        
    elif choice == "3":
        print("Bye")
        break
