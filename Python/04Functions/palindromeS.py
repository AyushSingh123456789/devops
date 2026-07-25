#name = "Python"
name = "racecar"

def is_Palindrome(word):
    i = 0
    j = len(name)-1
    flag = False
    while(i < j):
        if word[i] == word[j]:
            flag = True
            i += 1
            j -= 1
        else:
            return str(word) + " is not a palindrome string."
            break
    if flag:
        return word + " is a palindrome string."
    
result = is_Palindrome(name)
print(result)
        