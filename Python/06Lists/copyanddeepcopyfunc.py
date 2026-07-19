import copy
spam = ['A', 'B', 'C']
cheese = copy.copy(spam) # creats a duplicate copy of the list
cheese[1] = 42 # changes cheese
print(spam) # unchanged variable
print(cheese) # changed variable

# Now the spam and cheese variables refer to separate lists, which is why only the list in cheese is modified when you assign 42 at index 1.

# Just as variables refer to values rather than contain values, lists contain references to values rather than values themselves.

# If the list you need to copy contains lists, use the copy.deepcopy() function instead of copy.copy(). The copy.deepcopy() function will copy these inner lists as well.