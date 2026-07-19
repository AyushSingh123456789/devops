name1 = ('hello', )
print(type(name1))  # class Tuple
name2 = ('hello')
print(type(name2))  # class string

print(list('hello'))
#  If you have only one value in your tuple, you can indicate this by placing a trailing comma after the value inside the parentheses. Otherwise, Python will think you’ve entered a value inside regular parentheses. (Unlike some other programming languages, it’s fine to have a trailing comma after the last item in a list or tuple in Python.

spam = [0,1,2,3]
eggs = spam # The reference, not the list, is being copied.
eggs[1] = 'Hello!' # This changes the list value.
print(spam)
print(eggs) # The eggs var refers to the same list.


# When you create the list ❶, you assign a reference to it in the spam variable. But the next line copies only the list reference in spam to eggs ❷, not the list value itself. There is still only one list, and spam and eggs now both refer to it. The reason there is only one underlying list is that the list itself was never actually copied. So, when you modify the first element of eggs ❸, you’re modifying the same list that spam refers to. 


# It becomes a bit more complicated, as lists also don’t contain a sequence of values directly, but rather a sequence of references to values.

# i) In Python, variables never contain values. They contain only references to values.

# ii) In Python, the = assignment operator copies only references. It never copies values.