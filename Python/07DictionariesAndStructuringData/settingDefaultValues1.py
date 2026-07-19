spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
print(spam)


# The setdefault() method offers a way to do this in one line of code. The first argument passed to the method is the key to check for, and the second argument is the value to set at that key if the key doesn’t exist. If the key does exist, the setdefault() method returns the key’s value.


pam = {'name': 'Pookie', 'age': 12}
pam.setdefault('color', 'red') # sets 'color' key to 'black'
print(pam)