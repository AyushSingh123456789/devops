import random
for i in range(100): # Perform 100 coin flips.
    if random.randint(0,1) == 0:
        print('H', end = ' ')
    else:
        print('T', end = ' ')
print() # print one new line at the end.

# Just some random print statement characteristics
print('cats', 'dogs', 'mice')
print('cats', 'dogs', 'mice', sep = ',')