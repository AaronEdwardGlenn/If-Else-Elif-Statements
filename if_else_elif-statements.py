if True:
    print('Conditional was true')

language = 'java'

if language == 'python':
    print('Conditional was true')

# object identity uses 'is' instead of ==

# else statement
if language == 'java':
    print('langage is python')
else:
    print('no match')

# elif statement
if language == 'python':
    print('langage is python')
elif language == 'java':
    print('lang is java')
else:
    print('no match')

# you can use and, or, not in if statements
user = 'User'
logged_in = True

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Credentials')

# if the boolean for this if statement is false, which in this example it is not
if not logged_in:
    print('you not logged in')
else:
    print('welcome')

# now we will go over the 'is' statement:
# object identity tests if two objects have the same id in memory. Two objects can be equal and not be the same in memory.
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # this is true because they are equal

print(a is b)   # this is false. becaue they are not the same object in memory

# we can see the difference in the object's id this way:
print(id(a))
print(id(b))    # this shows the different ids.

c = [1, 2, 3]
d = c
print(id(d))
print(id(c))    # now the ids are the same

print(d is c)   # this is now true
# the 'is' opperator is doing the same as this now:
print(id(d) == id(c))

# Pythons 'Falsey' values are:
# False
# None
# Zero 0
# empty sequence like '', []
# an empty mapping like {}
# NOTE everything else evaluates to True

condition = 5

if condition:
    print('this is True')
else:
    print('evaluates to False')
