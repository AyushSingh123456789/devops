# Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# Print the string passed into the function:

print(x.string)

# Print the part of the string where there was a match.
# The regular expression looks for any words that starts with an upper case "S":

print(x.group())