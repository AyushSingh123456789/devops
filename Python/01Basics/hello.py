print("Hello, World!")
print("What is your name?")
my_name = input('>') # waits for user's response with '>' sign
print("It is good to meet you, " + my_name)
print("The length of your name is: ")
print(len(my_name))
print("What is your age?")
my_age = input('>')
print("You will be " + str(int(my_age)+1) + " in 1 year.")
# my_age returned as string from input -> converted to integer -> got 1 added -> converted back to string to concatenate
spam = input('>')
print(type(spam)) # any value stored in a variable by taking input from the user, is always stored in "String" form.
#print(int(spam) + 69) => first type cast the input value of spam into int from string, and then mathematical operations.
print(int(7.7))
print(round(7.75672, 2)) # round off to 1 decimal digit only
print(round(-2.67)) # round off to the nearest integer
# Half-way numbers(ending with ".5", e.g: 1.5,2.5,3.5, ...etc) are rounded-upto the nearest Even Integer(Also Called Banker's Rounding)
print(round(3.5))
print(round(2.5))
print(abs(-2.2)) # returns the Absolute value/ Positive value of the number
print(abs(0))
print(42 == '42') # false
print(42 == 42.0) # true

# Operators for mathematical operations: +,-,*,**,/,//,%
# Operators for String operations: +,*