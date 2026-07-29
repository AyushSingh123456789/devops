import re
txt = "The rain in Spain"
x = re.search("Spain", txt)
print(x.span())


y = re.match('^T', txt)
print(y)

z = re.search('$n', txt)
# 'search' only checks only for the first iteration in the whole string, Here, 'n' is found before the last letter.
print(z) # returns None

p = re.search(r"i\w+", txt)
# first iteration for 'i' as word character with 1 or more occurences in the whole string.
print(p.span())

q = re.finditer(r"i\w*", txt)
# for all the occurences with span positions of the char 'i' in the whole string.
print(list(q)) # printed as list instead of obj
