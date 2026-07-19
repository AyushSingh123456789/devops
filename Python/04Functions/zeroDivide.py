def spam(divide_by):
    try: 
        # Any code in this block that causes ZeroDivisionError won't crash
        return 42/divide_by
    except ZeroDivisionError:
        # If ZeroDivisionError happened, the code in this block runs:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

# When code in a try clause causes an error, the program execution immediately moves to the code in the except clause. After running that code, the execution continues as normal. If the program doesn’t raise an exception in the try clause, the program skips the code in the except clause. #