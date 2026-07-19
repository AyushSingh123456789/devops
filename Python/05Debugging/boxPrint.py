def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2')
    if height <= 2:
        raise Exception('Height must be greater than 2')
    
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width-2)) + symbol)
    print(symbol * width)
    
try:
    box_print('*', 4, 4)
    box_print('0', 20, 5)
    box_print('x', 1, 3)
    box_print('ZZ', 3, 3)
except Exception as err:
    print('An exception happend: ' + str(err))
try:
    box_print('ZZ', 3, 3)
except Exception as err:
    print('An exception happened: ' + str(err))



# Here, we’ve defined a box_print() function that takes a character, a width, and a height, and uses the character to make a little picture of a box with that width and height. This box shape is printed to the screen.

# Say we want the function to accept a single character only, and we expect the width and height to be greater than 2. We add if statements to raise exceptions if these requirements aren’t satisfied. Later, when we call box _print() with various arguments, our try-except will handle invalid arguments.

# This program uses the except Exception as err form of the except statement ❹. If an Exception object is returned from box_print() ❶ ❷ ❸, this except statement will store it in a variable named err. We can then convert the Exception object to a string by passing it to str() to produce a user-friendly error message ❺.

# Using the try and except statements, you can handle errors gracefully, rather than letting the entire program crash.