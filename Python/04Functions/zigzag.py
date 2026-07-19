import time, sys
indent = 0 # How many spaces to indent
indent_increasing = True # whether the indention is increasing or not

try:
    while True: # The main program loop
        print(' ' * indent, end = '')
        print('********')
        time.sleep(0.1) # Pause for 1/10th of a second.
        
        if indent_increasing:
            # Increases the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indent_increasing = False
        else:
            #Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()
    
    
# First, we’ll import the time and sys modules. Our program uses two variables. The indent variable keeps track of how many spaces of indentation occur before the band of eight asterisks, and the indent_increasing variable contains a Boolean value to determine whether the amount of indentation is increasing or decreasing:

# Next, we place the rest of the program inside a try statement. When the user presses CTRL-C while a Python program is running, Python raises the KeyboardInterrupt exception. If there is no try-except statement to catch this exception, the program crashes with an ugly error message. However, we want our program to cleanly handle the KeyboardInterrupt exception by calling sys.exit(). (You can find the code that accomplishes this in the except statement at the end of the program.)

# The while True: infinite loop will repeat the instructions in the program forever. This involves using ' ' * indent to print the correct number of spaces for the indentation. We don’t want to automatically print a newline after these spaces, so we also pass end='' to the first print() call. A second print() call prints the band of asterisks. We haven’t discussed the time.sleep() function yet; suffice it to say that it introduces a one-tenth-of-a-second pause in our program:

# Next, we want to adjust the amount of indentation used the next time we print asterisks. If indent_increasing is True, we’ll add 1 to indent, but once indent reaches 20, we’ll decrease the indentation:

# If indent_increasing is False, we’ll want to subtract one from indent. Once indent reaches 0, we’ll want the indentation to increase once again. Either way, the program execution will jump back to the start of the main program loop to print the asterisks again.

# If the user presses CTRL-C at any point that the program execution is in the try block, this except statement raises and handles the KeyboardInterrupt exception: