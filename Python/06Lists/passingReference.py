def eggs(some_parameter):
    some_parameter.append('Hello')
    
spam = [1,2,3]
eggs(spam)
print(spam) # Prints [1,2,3,'Hello']

# Notice that when you call eggs(), a return value doesn’t assign a new value to spam. Instead, it directly modifies the list in place. When run, this program outputs [1, 2, 3, 'Hello'].

# Even though spam and some_parameter contain separate references, they both refer to the same list. This is why the append('Hello') method call inside the function affects the list even after the function call has returned.

# Keep this behavior in mind. Forgetting that Python handles list and dictionary variables in this way can lead to unexpected behavior and confusing bugs.