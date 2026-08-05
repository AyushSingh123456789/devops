import requests

BASE_URL = "http://127.0.0.1:8000"

#1.GET all users
response = requests.get(f"{BASE_URL}/users")
print("All Users: ", response.json())

#2. POST a new user
new_user = {
    "name": "Alice Doe",
    "email": "alice@example.com",
    "age": 28,
    "is_verified": True
}
post_response = requests.post(f"{BASE_URL}/users", json=new_user)
print("Created User Response:",post_response.json())

#3. GET user by ID(eg. ID 1)
user_response = requests.get(f"{BASE_URL}/users/1")
print("User 1:", user_response.json())
