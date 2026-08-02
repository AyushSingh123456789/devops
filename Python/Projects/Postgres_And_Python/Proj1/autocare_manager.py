import os
from dotenv import load_dotenv
import psycopg

load_dotenv()

def get_db_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        dbname=os.getenv("DB_NAME"),
        password=os.getenv("DB_PASSWORD")
    )
    
print("========================================================")
print("AUTOCARE SERVICE CENTER")
print("========================================================")

print("1. Check-in New Vehicles (Create) \n2. View Active Vehicles (Read All) \n3. Search Vehicle by License Plate (Read One) \n4. Update Service Status or Mileage (Update) \n5. Check-out Vehicle/ Remove Entry (Delete) \n6. Read the whole available vehicle entry \n7. Exit")
print("========================================================")

while True:
    
    first_choice = input("Select an option(1-6): ")

    if first_choice == "1":
        def create_tables():
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    try:
                        cur.execute("create table if not exists vehicles(id serial primary key, owner_name text, license_plate varchar(10), model text, mileage integer, service_status text)")
                                    
                        owner_name = input("Enter the name of vehicle's owner: ")
                        license_plate = input("Enter the license number of the vehicle: ")
                        model = input("Enter the model of the vehicle: ")
                        mileage = int(input("Enter the mileage of the vehicle: "))
                        try:
                            service_status = input("Enter the service status of the vehicle(Pending/InProgress/Completed): ")
                        except Exception as error:
                            print(str(error) + "service_status has been assigned the default value, Pending")
                            service_status = "Pending"
                        
                        if mileage <0:
                            print("Negative mileage is invalid, try again")
                            mileage = input("Enter the mileage of the vehicle: ")
                        
                        cur.execute("insert into vehicles(owner_name, license_plate, model, mileage, service_status) values (%s,%s,%s,%s,%s)", (owner_name,license_plate,model,mileage,service_status,))
                        
                        cur.execute("select * from vehicles")
                        vehicle_data = cur.fetchall()
                        print(vehicle_data)    
                    except Exception as error:
                        print(f"Database error: {error}")
        create_tables()
        
    elif first_choice == "2":
        def read_active_vehicles():
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    try:
                        cur.execute("select * from vehicles where service_status = 'Completed'")
                        active_details = cur.fetchall()
                        print(active_details)
                    except Exception as error:
                        print(f"Error: {error}")
        read_active_vehicles()
        
    elif first_choice == "3":
        def search_by_license_plate():
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    try: 
                        license = input("Enter the licence_plate number: ")
                        try:  
                            cur.execute("select * from vehicles where license_plate = %s", (license,))
                            details = cur.fetchall()
                            print(details)
                        except Exception as error:
                            print(f"License number {license} not found, exited with error: {error}")        
                    except Exception as error:
                        print(f"Database Error: {error}")
                        
        search_by_license_plate()
        
    elif first_choice == "4":
        def update_tables():
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    try:
                        vehicle_id = input("Enter the vehicle_id of the vehicle you wanna update: ")
                        try:
                            cur.execute("select * from vehicles where id = %s", (vehicle_id,))
                            if cur.fetchone(): # if the vehicle exists
                                choice = input("Choose from the two options: 1) Service Status Updation, 2) Mileage Updation: ")
                                if choice == "1":
                                    new_service_status = input("Enter the new service status of the vehicle(1.Pending,2.InProgress,3.Completed): ")
                                    try:
                                        if new_service_status == "1":
                                            cur.execute("update vehicles set service_status = 'Pending' where id = %s", (vehicle_id,))
                                            print("The service status has been updated successfully:")
                                            cur.execute("select * from vehicles where id = %s", (vehicle_id,))
                                            updated_detail1 = cur.fetchall()
                                            print(updated_detail1)
                                        elif new_service_status == "2":
                                            cur.execute("update vehicles set service_status = 'InProgress' where id = %s", (vehicle_id,))
                                            cur.execute("select * from vehicles where id = %s", (vehicle_id,))
                                            updated_detail2 = cur.fetchall()
                                            print(updated_detail2)
                                        elif new_service_status == "3":
                                            cur.execute("update vehicles set service_status = 'Completed' where id = %s", (vehicle_id,))
                                            cur.execute("select * from vehicles where id = %s", (vehicle_id,))
                                            updated_detail3 = cur.fetchall()
                                            print(updated_detail3)
                                        else:
                                            print("Invalid service status")
                                    except Exception as error:
                                        print(f"Error: {error}")
                                elif choice == "2":
                                    new_mileage = int(input("Enter the new mileage: "))
                                    try:   
                                        cur.execute("update vehicles set mileage = %s where id = %s", (new_mileage,vehicle_id,))
                                        print("The new mileage updated successfully:")
                                        cur.execute("select * from vehicles where id = %s", (vehicle_id,))
                                        updated_detail4 = cur.fetchall()
                                        print(updated_detail4)
                                    except Exception as error:
                                        print(f"Error: {error}")
                                else:
                                    print("Invalid choice")
                            else:
                                print("This vehicle_id does not exist.")
                        except Exception as error:
                            print(f"Error: {error}")                       
                    except Exception as error:
                        print(f"Occured Error: {error}")
        
        update_tables()
        
    elif first_choice == "5":
        def delete_tables():
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    try:
                        vehicle_id = input("Enter the id of the vehicle's entry you wanna delete: ")
                        try:
                            cur.execute("select * from vehicles where id = %s", (vehicle_id,))
                            if cur.fetchone(): 
                                confirmation = input("Are you sure you wanna delete this vehicle's entry(y/n): ")
                                if confirmation.lower() == "y":
                                    cur.execute("delete from vehicles where id = %s", (vehicle_id,))
                                    print("The vehicle's entry has been successfully deleted:")
                                    cur.execute("select * from vehicles")
                                    updated_data = cur.fetchall()
                                    print(updated_data)
                                elif confirmation.lower() == "n":
                                    print("No entry has been harmed in the vehicles table.")
                            else:
                                print("No such id exists.")       
                        except Exception as error:
                            print(f"Error: {error}")  
                    except Exception as error:
                        print(f"Error: {error}")
                        
        delete_tables()
        
    elif first_choice == "6":
        def full_detail():
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    try:
                        cur.execute("select * from vehicles")
                        full_detail = cur.fetchall()
                        print(full_detail)
                    except Exception as error:
                        print(f"Error: {error}")
        full_detail()
        
    elif first_choice == "7":
        print("Bye")
        cur.close()
        break
        
    else:
        print("Invalid option, Try again")
        cur.close()
        break


# Imp Note: In SQL, the VALUES (%s) syntax is used for INSERT statements, not SELECT queries.