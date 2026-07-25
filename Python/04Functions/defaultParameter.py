def area(radius, pi=3.14):
    print(pi*radius*radius)

area(100)


# Whenever passing a default parameter along side a positional parameter, make sure to pass the default parameter after the positional one.

# Passing a diff value to the default parameter through the argument is allowed.

#area(100, 3.15)