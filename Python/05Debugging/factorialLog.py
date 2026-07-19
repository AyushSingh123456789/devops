import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(' + str(n) + ')')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(' + str(n) + ')')
    return total

print(factorial(5))
logging.debug('End of program')

# While logging messages are helpful, they can clutter your screen and make it hard to read the program’s output. Writing the logging messages to a file will keep your screen clear and enable you to read the messages after running the program. You can open this text file in any text editor, such as Notepad or TextEdit.


# Entering import logging and logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s') is somewhat unwieldy. You may want to use print() calls instead, but don’t give in to this temptation! Once you’re done debugging, you’ll end up spending a lot of time removing print() calls from your code for each log message. You might even accidentally remove some print() calls that were used for non-log messages. The nice thing about log messages is that you’re free to fill your program with as many as you like, and can always disable them later by adding a single logging.disable(logging.CRITICAL) call. Unlike print(), the logging module makes it easy to switch between showing and hiding log messages.

# Log messages are intended for the programmer, not the user. The user won’t care about the contents of some dictionary value you need to see to help with debugging; use a log message for something like that. For error messages that the user should see, like File not found or Invalid input, please enter a number, use a print() call. You don’t want to deprive the user of helpful information they can use to solve their problem.