import re
string = "bc"
# string = "abbbbbbbbbaac"
pattern = "ab*c"
# b must be present 0 or more times, and placed b/w 'a' and 'c' characters.

if(re.match(pattern, string)):
    print('Match found')
else:
    print('Match not found')