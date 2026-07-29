import re
string = "bc"
# string = "abbbbbbbbbaac"
pattern = r"ab*c"
# b must be present 0 or more times, and placed b/w 'a' and 'c' characters.

if(re.match(pattern, string)):
    print('Match found')
else:
    print('Match not found')
    
string2 = "abc"
pattern2 = r"ab+c"

if(re.match(pattern2, string2)):
    print('Match found')
else:
    print('Match not found')
    
string3 = "abbbb"
pattern3 = r"ab{3}"

if(re.match(pattern3, string3)):
    print('Match found')
else:
    print('Match not found')
    
string4 = "ab"
pattern4 = r"ab{1,}c" 
# b min 1 times or repeat finitely before c

if(re.match(pattern4, string4)):
    print('Match found')
else:
    print('Match not found')
    
string5 = "acb"
pattern5 = r"a.b" # any one char b/w a and b

if(re.match(pattern5, string5)):
    print('Match found')
else:
    print('Match not found')

string6 = "a-b"
pattern6 = r"a-?b" # optional '-' b/w a and b

if(re.match(pattern6, string6)):
    print('Match found')
else:
    print('Match not found')
    
string7 = "921234567892"
pattern7 = r"^91"

if(re.match(pattern7, string7)):
    print('Match found')
else:
    print('Match not found')
    
string8 = "python"
pattern8 = r"[pP]ython"

if(re.match(pattern8, string8)):
    print('Match found')
else:
    print('Match not found')
    
string9 = "5ython"
pattern9 = r"[0-9a-zA-Z]ython"

if(re.match(pattern9, string9)):
    print('Match found')
else:
    print('Match not found')
    
string10 = "The cat find the dog sat on the mat"
pattern10 = r"[abc]"
pattern11 = r"[aeiou]" # Vowels
matches = re.findall(pattern10, string10)
matches2 = re.findall(pattern11, string10)
print(matches)
print(matches2)

# ShortHand Character Search methods:

text = "The meeting is scheduled at 9 AM"
#pattern12 = r"[0-9]"
pattern12 = r"\d" # only num char
pattern13 = r"\D" # every char except num
matches3 = re.findall(pattern12, text)
matches4 = re.findall(pattern13, text)
print(matches3)
print(matches4)

text2 = "The variable! name is my_var123 \n"
pattern14 = r"\w" #every alpha-numeric char, no ''
pattern15 = r"\W" # every non-alphnumeric char
matches5 = re.findall(pattern14, text2)
matches6 = re.findall(pattern15, text2)
print(matches5)
print(matches6)

text3 = "The sentence \t includes punctuations! \n"
pattern16 = r"\s" # every whitespace characters
pattern17 = r"\S" # all non-whitespace chars.
pattern18 = r"\S+" 
# combined all non-whitespace char.present 1 or more
matches7 = re.findall(pattern16, text3)
matches8 = re.findall(pattern17, text3)
matches9 = re.findall(pattern18, text3)
print(matches7)
print(matches8)
print(matches9)

text4 = "Hellooooo, Python is awesomeeeeee!"
pattern19 = r"\w*o+\w*"

#\w*: matches zero or more alphanumeric chars.
#o+: matches one or more occurences of the letter 'o'
#\w*: matches zero or more alphanumeric chars.

matches10 = re.findall(pattern19, text4)
print(matches10)

text5 = "Please contact me at +1 (123) 456-7890 or via email at john@example.com"

pattern20 = r"\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,3}[-.\s]?\d{1,4}" # detecting phone num

pattern21 = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

matches11 = re.findall(pattern20, text5)
print(matches11)
#matches12 = re.findall(pattern21, text5)
#print(matches12)

email = input("Enter email address: ")
matches12 = re.match(pattern21, email)
if re.match(pattern21, email):
    print('Valid email')
else:
    print("invalid email")

# VVI

# \b earns its place in the email pattern because \w-based classes need boundary protection, while the phone pattern's punctuation-based structure already does that job implicitly.

text6 = "Date: 2026-07-29 29-07-2026"

pattern22 = r"\d{4}-\d{2}-\d{2}"

matches13 = re.findall(pattern22, text6)
print(matches13)