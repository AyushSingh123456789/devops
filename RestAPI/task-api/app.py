
from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import psycopg
from psycopg.rows import dict_row

load_dotenv()
app = FastAPI()

# Database connection settings
def get_db_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        row_factory=dict_row
    )

# Defines the shape of data expected in a POST request
class UserCreate(BaseModel):
    name: str
    email: str
    age: int
    is_verified: bool = False
    
# Get all users(GET request)
@app.get("/users") # app decorator for our root dir'/users'
def get_users():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            users = cur.fetchall()
            return users

# Create a new user (POST request)
@app.post("/users")
def create_user(user: UserCreate):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name,email,age,is_verified) VALUES (%s,%s,%s,%s)", (user.name,user.email,user.age,user.is_verified,))
        conn.commit()
    return {"message": "User created successfully"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
        conn.commit()
    return {"message": f"User {user_id} deleted successfully"}

# get a user by id:
@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE id=%s", (user_id,))
            user = cur.fetchone() # returns a single dictionary instead of list
        if not user:
            return {"error": "user not found"}
        return user