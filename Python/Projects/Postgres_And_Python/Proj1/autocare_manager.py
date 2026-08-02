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
    
def create_tables():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("create table vehicles(id serial primary key, owner_name text, license_plate varchar(10), model text, mileage integer, service_status text)")
            
            owner_name = input("Enter the name of vehicle's owner: ")
            license_plate = input("Enter the license number of the vehicle: ")
            model = input("Enter the model of the vehicle: ")
            mileage = input("Enter the mileage of the vehicle: ")
            service_status = input("Enter the service status of the vehicle(Pending/InProgress/Completed): ")
            
            cur.execute("insert into vehicles(owner_name, license_plate, model, mileage, service_status) values (%s,%s,%s,%s,%s)", (owner_name,license_plate,model,mileage,service_status,))
            
            cur.execute("select * from vehicles")
            vehicle_data = cur.fetchall()
            print(vehicle_data)
            
create_tables()