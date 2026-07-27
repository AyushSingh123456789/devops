import json
import os

def save_user_data():
    user_list = []
    
    while True:
        name = input("Enter name (or 'quit' to exit the program): ")
        if name == "quit":
            break
        email = input('Enter email: ')
        contact = input("Enter contact: ")
        
        # creating a dictionary
        user_data = {
            "name": name,
            "email": email,
            "contact": contact
        }
        
        user_list.append(user_data)

    if os.path.exists("user_data.json"):
        with open("user_data.json", "r") as file:
            existing_data = json.load(file)
        user_list.extend(existing_data)
        
        
    with open('user_data.json', 'w') as file:
        json.dump(user_list, file)
        
    print("User data saved successfully")
    
def read_user_data():
    if not os.path.exists("user_data.json"):
        print("No user data found")
        return
    
    with open("user_data.json", "r") as file:
        user_list = json.load(file)
        for user_data in user_list:
            print("Name: ", user_data["name"])
            print("Email: ", user_data["email"])
            print("Contact: ", user_data["contact"])
            print("\n")
        
#save_user_data()
#read_user_data()

# Editing/Updating a saved functionality of data present in a json file:

def edit_user_data(name):
    if not os.path.exists("user_data.json"):
            print("No user data found")
            return
    
    with open('user_data.json', 'r') as file:
        user_list = json.load(file)
    
    user_found = False
    for user_data in user_list:
        if user_data['name'].lower() == name.lower():
            email = input("Enter updated email: ")
            contact = input("Enter updated contact: ")
            
            user_data['email'] = email
            user_data['contact'] = contact
            user_found = True
            break
    if not user_found:
        print('user not found')
        
    with open("user_data.json", "w") as file:
        json.dump(user_list, file)
    print("user data updated successfully")        
        
 
# Deleting User data from a json file:


def delete_user_data(name):
    if not os.path.exists("user_data.json"):
            print("No user data found")
            return
    
    with open('user_data.json', 'r') as file:
        user_list = json.load(file)
    
    user_found = False
    for user_data in user_list:
        if user_data['name'].lower() == name.lower():
            user_list.remove(user_data)
            user_found = True
            break
    if not user_found:
        print('user not found')
        
    with open("user_data.json", "w") as file:
        json.dump(user_list, file)
    print("user data deleted successfully")



       
delete_name = input("Enter name which you want to delete: ")
delete_user_data(delete_name)
read_user_data()