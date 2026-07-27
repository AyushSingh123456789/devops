# F=(c*9/5) +32

celsius_temp = [25,30,15,10,35]

fahrenheit_temp = list(map(lambda c: (c*9/5)+32, celsius_temp))
print(fahrenheit_temp)

# Use map to get diff values from an iterable by performing operations on them, Use filter to filter out the already present values out of  iterable, by applying some functions/conditions on them.


names = ["John Doe", "Alice Smith", "Bob Ford"]

# for name in names:
#     print(name.split()[0][0]+ name.split()[1][0])

initials = list(map(lambda name: "".join([n[0] for n in name.split()]), names))
print(initials)

# The split() method breaks a string into a list of substrings based on a specified delimiter, while the join() method combines a list of strings into a single string using a specified separator.
# Using split() By default, split() divides a string by any whitespace. You can specify a delimiter to split by a specific character or sequence.