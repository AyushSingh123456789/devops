# file = open('test.txt', 'r')
# content = file.read()
# content = file.readline()
# content = file.read(10)
# print(content)
# file.close()


# file = open('test.txt', 'w')
# file.write('New content to be added to file')
# file.close()


# file = open('test.txt', 'a')
# content = '\nThis is a fourth line'
# file.write(content)
# file.close()



# with open('test.txt', 'r') as file:
#     content = file.read()
#     print(content)


with open('test.txt', 'r') as file:
    # line1 = file.readline()
    # line2 = file.readline()
    
    lines = file.readlines()

# print(line1)
# print(line2)
print(lines.strip('\n'))
for line in lines:
    print(line.strip())