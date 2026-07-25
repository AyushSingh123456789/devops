def circle(r):
    area = 3.14 * r * r
    circumference = 2 * 3.14 * r
    return area, circumference

a,c = circle(5)
# print('The area of the circle is: ' + str(a))
# print('The circumference of the circle is: ' + str(c))

print(f" Area of the circle is {a} and the circumference is {c}")