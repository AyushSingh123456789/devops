def collatz(number):
    if(number % 2 == 0):
        result =  number // 2
    elif(number % 2 == 1):
        result = 3 * number + 1
    print(result, end = ' ')
    return result

print("Enter an Integer: ")
try:
    user_num = int(input('>'))
    while(user_num != 1):
        user_num = collatz(user_num)
except ValueError:
    print("Please enter a valid number.")
    
# Didn't get the Question at all from the question statement, had to take the help of AI at the end.
    
