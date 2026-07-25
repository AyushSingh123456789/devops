# number = 5

# def factorial(num):
#     f = 1
#     while num > 0:
#         f = f * num
#         num -= 1
#     return f

# result = factorial(number)
# print(result)


# We can also calculate the factorial of a number using recursion:

number = 5

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

result = factorial(number)
print(result)


# factorial(5) => 5 * factorial(4)
# factorial(4) => 4 * factorial(3)
# factorial(3) => 3 * factorial(2)
# factorial(2) => 2 * factorial(1)
# factorial(1) => 1
# => 1*2*3*4*5 = 120