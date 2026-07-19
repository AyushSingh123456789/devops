all_guests = {'Alice': {'apples': 5, 'pretzels': 12}, 'Bob': {'ham sandwiches': 3, 'apples': 2}, 'Carol': {'cups': 3, 'apple pies': 1}}

def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(item,0)
    return num_brought

print('Number of things being brought: ')
print(' - Apples     ' + str(total_brought(all_guests, 'apples')))
print(' - Cups   ' + str(total_brought(all_guests, 'cups')))
print(' - Cakes   ' + str(total_brought(all_guests, 'cakes')))
print(' - Ham Sandwiches  ' + str(total_brought(all_guests, 'ham sandwiches')))
print(' - Apple Pies   ' + str(total_brought(all_guests, 'apple pies')))


# Inside the total_brought() function, the for loop iterates over the key-value pairs in guests ❶. Inside the loop, the string of the guest’s name is assigned to k, and the dictionary of picnic items they’re bringing is assigned to v. If the item parameter exists as a key in this dictionary, its value (the quantity) is added to num_brought ❷. If it doesn’t exist as a key, the get() method returns 0 to be added to num_brought.


# The number of items brought to a picnic may seem like such a simple thing to model that you wouldn’t need to bother with writing a program to do it. But realize that this same total_brought() function could easily handle a dictionary that contains thousands of guests, each bringing thousands of different picnic items. In that case, having this information in a data structure, along with the total_brought() function, would save you a lot of time!

# You can model things with data structures in whatever way you like, as long as the rest of the code in your program can work with the data model correctly. When you first begin programming, don’t worry so much about the “right” way to model data. As you gain more experience, you may come up with more efficient models; the important thing is that the data model works for your program’s needs.
