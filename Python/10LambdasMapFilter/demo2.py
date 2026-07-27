# Map in Python: Mapping a func on an iterable to perform the requd. logic, without using any loop.
# The map() function takes the user's func, maps it over the iterable's data/values, and then returns us an object.
# The map() func in python is written in C prog lang, so it's more memory efficient(one data/value at a time) than any loop in python.
# Parentheses are omitted when passing a function to map() because parentheses execute the function immediately, whereas map() requires a reference to the function object itself to apply it later to each item in the iterable.

# numbers = [1,2,3,4,5]

def square(x):
    return x*x

new_list = list(map(square, numbers)) # converting obj to list.
print(new_list)


# numbers = ["1", "2", "3", "4", "5"]
# print(numbers)
# new_list = list(map(int,numbers))
# print(new_list)


# 5% discount to the original prices:
# prices = [100,200,300,400,500]

# new_prices = list(map(lambda x: x - (x*5)/100, prices))
# print(new_prices)



names = ['john', 'rob', 'mike']
cap_names = list(map(str.capitalize, names))
up_names = list(map(str.upper, names))
print(cap_names)
print(up_names)