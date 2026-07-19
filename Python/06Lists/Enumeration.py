supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)
    
#  Instead of using the range(len(some_list)) technique with a for loop to obtain the integer index of the items in the list, you can call the enumerate() function. On each iteration of the loop, enumerate() will return two values: the index of the item in the list, and the item in the list itself.

# The enumerate() function is useful if you need both the item and the item’s index in the loop’s block.