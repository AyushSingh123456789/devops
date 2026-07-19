def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'
    
def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'

# After the creation of the above fns, the program begins from below:
eggs = 'global'
bacon()
print(eggs) # prints 'global'