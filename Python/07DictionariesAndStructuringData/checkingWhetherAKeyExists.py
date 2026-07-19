picnic_items = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnic_items.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnic_items.get('eggs', 0)) + ' eggs.')


# Because there is no 'eggs' key in the picnic_items dictionary, the get() method returns the default value 0. Without using get(), the code would have caused an error message.