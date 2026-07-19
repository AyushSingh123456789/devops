def spam():
    global eggs
    eggs = 'spam'
    
eggs = 'global'
spam()
print(eggs) # prints 'spam'

# Because eggs is declared global at the top of spam() ❶, setting eggs to 'spam'❷ changes the value of the globally scoped eggs. No local eggs variable is ever created.

# Use these four rules to tell whether a variable belongs to a local scope or the global scope:

 # 1.  A variable in the global scope (that is, outside all functions) is always a global variable.

  #2.  A variable in a function with a global statement is always a global variable in that function.

 # 3.  Otherwise, if a function uses a variable in an assignment statement, it is a local variable.

  #4.  However, if the function uses a variable but never in an assignment statement, it is a global variable.