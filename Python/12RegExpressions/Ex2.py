import re
txt = 'The rain in Spain'
x = re.findall('[a-c]', txt) 
# returns a list of the matched characters.
print(x)#returns a list of matched chars b/w a-c inside a list.

o = re.match('[a-c]', txt)
# searches for only in the start of the string
print(o) # no match in the start, so returns None

y = re.search('[a-c]', txt) #searches for only the first iteration through out the string.
print(y) # returns span posn tuple and match letter, whole as an object for the first iter only.
print(y.span()) #returns a tuple with start& end pos
print(y.group()) # returns matching part of the str

z = re.finditer('[a-c]', txt) 
# returns span posn. of 'a,b,c' throughout the string, i.e. span(5,6), match = 'a', span(14,15), match = 'a'.
print(list(z)) # transformed to list and returned

q = re.split('[a-c]', txt)
#deletes 'a,b,c' in the string
print(q) # returns the transformed string

p = re.sub('[a-c]','*', txt)
# replaces 'a,b,c' in the string with '*""
print(p) #returns the transformed string