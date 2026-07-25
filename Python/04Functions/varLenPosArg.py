def add(*args):
    sum = 0
    for n in args:
        sum = sum + n
    return sum
    
result = add(5,10,15,20,25,30)
print(result)