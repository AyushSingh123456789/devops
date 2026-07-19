while True:
    print('Who are you?')
    name = input('>')
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input('>')
    if password == 'swordfish':
        break
print('Access granted.')

#If the user enters any name besides Joe ❶, the continue statement ❷ causes the program execution to jump back to the start of the loop. When the program reevaluates the condition, the execution will always enter the loop, because the condition is simply the value True. Once the user makes it past that if statement, they are asked for a password ❸. If the password entered is swordfish, the break statement ❹ is run, and the execution jumps out of the while loop to print Access granted. ❺ Otherwise, the execution continues to the end of the while loop, where it then jumps back to the start of the loop#

# Truthy and Falsy values:
print(bool(0))
print(bool(42))
print(bool('Hello'))
print(bool(''))