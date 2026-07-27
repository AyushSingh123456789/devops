while True:
    with open('name.txt', "a") as file:
        name = input("Enter name to be added: ")
        file.write(name + '\n')
        choice = input("Do you want to add more names: (Y/n)")
        if choice == 'n':
            break
        

with open("name.txt", "r") as file:
    lines = file.readlines()
    
for line in lines:
    print(line.strip().capitalize())