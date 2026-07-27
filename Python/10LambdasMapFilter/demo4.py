# Generators in python or generator() in python:
# "yield" instead of "return" is used.
# "return" stops the func. and the code stops with that return value, while "yield" suspends the func, and returns that yielded value to the collar, i.e. the function. And then again the code resumes.

# def func():
#     counter = 0
#     while counter<= 10:
#         yield counter
#         counter += 1
        
# print(list(func()))


def even_generator(x):
    for i in range(x):
        if i %2 == 0:
            yield i

print(list(even_generator(10)))