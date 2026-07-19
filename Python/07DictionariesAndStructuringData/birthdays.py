birthdays = {'Alice': 'Apr1', 'Bob': 'Dec12', 'Carol': 'Mar4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday # assigned the new bday value to the new Name in the existing dict 'birthdays'.
        print('Birthday database updated.')
        
        
# Three dictionary methods will return list-like values of the dictionary’s keys, values, or both keys and values: keys(), values(), and items().

# When you use the keys(), values(), and items() methods, a for loop can iterate over the keys, values, or key-value pairs in a dictionary, respectively, and you can use the in and not in operators to determine if a value exists as a key or value in the dictionary. Notice that the values in the dict_items value returned by the items() method are tuples of the key and value.


# The list(spam.keys()) line takes the dict_keys value returned from keys() and passes it to list(), which then returns a list value of ['color', 'age'].