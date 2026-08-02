import os
from dotenv import load_dotenv
import psycopg

load_dotenv()


def get_db_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def create_table():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("create table students(student_id serial primary key, name text, address text, age int, number text);")
            print("students table created")
            
def insert_data():
    # code to accept data from user
    name = input("Enter name: ")
    address = input("Enter address: ")
    age = input("Enter age: ")
    number = input("Enter number: ")
    
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("insert into students(name,address,age,number) values (%s,%s,%s,%s)",(name,address,age,number))
            print("data added in students table")
            
def read_data():
    student_id = input("Enter the id of the student you wanna view the table of: ")
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("select * from students where student_id=%s", (student_id,)) #print(cur.fetchall())
            student = cur.fetchone()
            print(student)

def delete_data():
    student_id = input("Enter the id of the student you want to delete: ")
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            # Search Query to check the existence of the student first, before deleting it
            
            cur.execute("select * from students where student_id=%s",(student_id,))
            student = cur.fetchone() # returns the whole row of the student with mentioned id
            
            if student: # if student exits
                print(f"Student to be deleted: ID: {student[0]}, Name: {student[1]}, Address: {student[2]}, Age: {student[3]}")
                choice = input("Are you sure you want to delete the student: (yes/no)")
                if choice.lower() == "yes":
                    cur.execute("delete from students where student_id = %s", (student_id,))
                    print("Student record deleted")
                else:
                    print("Deletion Cancelled")
            else:
                print("Student not found")

   
def update_data():
    student_id = input("Enter id of the student to be updated: ")
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            fields = {
                "1": ("name","Enter the new name: "),
                "2": ("address","Enter the new address: "),
                "3": ("age", "Enter the new age: "),
                "4": ("number", "Enter the number: ")
            }
            print("Which field would you like to update")
            for key,val in fields.items():
                print(f"{key}: {val[0]}")
            field_choice = input("Enter the number of the field you want to update: ")
            
            if field_choice in fields:
                field_name, prompt = fields[field_choice]
                new_value = input(prompt)
                if field_choice == "age":
                    new_value = int(new_value)
                
                sql = f"update students set {field_name} = %s where student_id=%s"
                cur.execute(sql,(new_value,student_id))
                print(f"{field_name} updated successfully")
                
            else:
                print("Invalid Choice")

# create_table()               
#insert_data()
#update_data() 
#delete_data()
read_data()


# Imp Note: Many of the () used inside this program are actually tuples.      
# Even if inside a tuple exists only one value, we still need to close it with a comma(,) so python understands it as tuple.