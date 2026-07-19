spam = {'color': 'red', 'age': 32}
for k, v in spam.items():
    print('Key: ' + str(k) + ' Value: ' + str(v))



# This code creates a dictionary with keys 'color' and 'age' whose values are 'red' and 42, respectively. The for loop iterates over the tuples returned by the items() method: ('color', 'red') and ('age', 42). The two variables, k and v, are assigned the first (the key) and second (the value) values from these tuples. The body of the loop prints out the k and v variables for each key-value pair.


# While you can use many values for keys, you cannot use a list or dictionary as the key in a dictionary. These data types are unhashable, which is a concept beyond the scope of this book. If you need a list for a dictionary key, use a tuple instead.