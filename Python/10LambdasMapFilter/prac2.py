# words = ["Python", "Java", "JavaScript", "C++"]
# reversed_words = list(map(lambda word: word[::-1], words))
# print(reversed_words)

# def fibonacci(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0,1]
#     else:
#         fib_seq = [0,1]
#         fib_seq.extend(map(lambda i: fib_seq[i-1] + fib_seq[i-2], range(2,n)))
#         return fib_seq
    
# fibonacci_sequence = fibonacci(10)
# print(fibonacci_sequence)


# Better fibonacci seq:














numbers = [2,3,4,5,6,7,8,9,10]
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
# n = int(input("Enter the num to check: "))
# print(is_prime(n))
            
prime_num = list(filter(is_prime, numbers))
print(prime_num)