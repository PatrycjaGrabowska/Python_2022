"""
first exercise from udemy python course
Tracking changes on id numbers on variables
"""

a = b = c = 10
print('a = ', a, 'b = ', b, 'c = ', c)
print('id a = ', id(a), 'id b = ', id(b), 'id c = ', id(c))
a = 20
print('id a = ', id(a), 'id b = ', id(b), 'id c = ', id(c))

a = b = c = [1, 2, 3]
print('a = ', a, 'b = ', b, 'c = ', c)
print('id a = ', id(a), 'id b = ', id(b), 'id c = ', id(c))
a.append(4)
print('new a', a)
print('id a = ', id(a), 'id b = ', id(b), 'id c = ', id(c))

x = 10
y = 10
print('id x = ', id(x), 'id y = ', id(y)) #same id for two separated variables

y = y + 1 - 1
print('id x = ', id(x), 'id y = ', id(y)) #id didn't change even after working on y variable

y = y + 1234567890 - 1234567890
print('id x = ', id(x), 'id y = ', id(y)) #apparently in some of the python varsions the id change in this example, not here tho :D