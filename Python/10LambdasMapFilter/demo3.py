# filter() in Python:

numbers = [1,2,3,4,5,6,7,8,9,10]
odd_num_test = list(map(lambda x: x % 2 != 0, numbers))
odd_num_values = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_num_test)
print(odd_num_values)

# lambda x: x % 2 != 0 is a small anonymous function that takes one element x and returns True if it's odd.
# map(function, iterable) would transform every element (e.g., turning each into True/False), not filter them out — that's the key difference between the two.
# filter(function, iterable) applies that function to each element and keeps only the ones where it returns True.