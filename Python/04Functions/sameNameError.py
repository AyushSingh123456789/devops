def spam():
    print(eggs) # ERROR!
    eggs = 'spam local'

eggs = 'global'
spam()

# This error happens because Python sees that there is an assignment statement for eggs in the spam() function ❶ and, therefore, considers any mention of an eggs variable in spam() to be a local variable. But because print(eggs) is executed before eggs is assigned anything, the local variable eggs doesn’t exist. Python won’t fall back to using the global eggs variable ❷ #