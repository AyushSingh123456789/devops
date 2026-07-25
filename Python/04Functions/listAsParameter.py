scores = [1,2,3,4,5]

def add(numbers):
    for num in numbers:
        print(num, end=" ")
    print()
    print(numbers, sep=",")
    
add(scores)