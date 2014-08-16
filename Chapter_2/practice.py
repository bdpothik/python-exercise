#!/usr/bin/env python

# Practice Length, Minimum, and Maximum

numbers = [100, 34, 678]
print len(numbers)
print max(numbers)
print min(numbers)
print max(2, 3)
print min(9, 3, 2, 5, 2)

a = 'Hello'
b = list('Hello')
print a
print b
print ''.join(b)
print '/'.join(b)

# Basic List Operations

x = [1, 2, 1, 4]
x[2] = 3
print x

del x[1]
print x

name = list('Perl')
print name
name[2:] = list('ar')
print name
name[1:] = list('ython')
print name
name[1:1] = list('JJ')
print name
name[:2] = []	#or list('')
print name

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print numbers
numbers[::2] = [-1, -3, -5, -7, -9]
print numbers
numbers[-2::-2] = [-2, -4, -6, -8]	# Assigned from last to first
print numbers
numbers[-2:-10:-2] = [-8, -6, -4, -2]
print numbers

# List Methods

lst = [1, 2, 3]
lst.append(4)
print 'lst: ' + str(lst)

# If I use the name 'list' for a list,
# I won't be able to call the function
# 'list(object)' anymore. E.g., follow
# the next four lines.

# list = [1, 2, 3]
# list.append(4)
# print 'list: ' + str(list)

# print list('Hello')

# The count method counts the occurrences of an element in a list:

print ['to', 'be', 'or', 'not', 'to', 'be'].count('to')

x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print x.count(1)
print x.count([1, 2])

# Extend Method
a = [1, 2, 3]
b = [4, 5, 6]
print a.extend(b)	# return nothing
print 'Extend:(a) ' + str(a)	# The extended sequence (in this case, a) is modified.

a = [1, 2, 3]
b = [4, 5, 6]

print 'Ordinary Concatenation:(a + b) ' + str(a + b)	# Ordinary concatenation returns a completely new sequence.
print 'a ' + str(a)

# Index Method
knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni', 'who']
print knights.index('who')
# print knights.index('herring')	# give "ValueError: 'herring' is not in list"

numbers = [1, 2, 5, 6, 7]
numbers[2:2] = ['three']
numbers.insert(3, 'four')
print numbers

# Pop methods

x = [1, 2, 3, 4, 5]
print x.pop()
print x
print x.pop(1)
print x

# Remove method

x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('be')
print x
# x.remove('bee')	# give ValueError: list.remove(x): x not in list

# reverse method
x = [1, 2, 3]
x.reverse()
print x

# reversed
# If you want to iterate over a sequence in reverse, you can use the reversed function. This function doesn't return a list, though; it returns an iterator.

x = [1, 2, 3]
print list(reversed(x))

# sort

x = [4, 6, 2, 1, 7, 9]
x.sort()
print 'sorted: ' + str(x)
y = x 	# both refer to same
y.sort()
print 'x: ' + str(x)
print 'y: ' + str(y)

x = [4, 6, 2, 1, 7, 9]
y = x[:]	# new copy
y.sort()	# or y = sorted(x)
print 'x: ' + str(x)
print 'y: ' + str(y)

numbers = [5, 2, 9, 7]
numbers.sort(cmp)
print numbers

x = ['aardvark', 'abrate', 'ahrate', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len)
print x
x = ['aardvark', 'abrate', 'ahrate', 'abalone', 'acme', 'add', 'aerate']
x.sort(cmp, key=len)
print x
x = ['aardvark', 'abrate', 'ahrate', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len, reverse=True)
print x
x = ['aardvark', 'abrate', 'ahrate', 'abalone', 'acme', 'add', 'aerate']
x.sort(cmp)
print x
x = ['aardvark', 'abrate', 'ahrate', 'abalone', 'acme', 'add', 'aerate']
x.sort(reverse=True)
print x
x = ['aardvark', 'abrate', 'ahrate', 'abalone', 'acme', 'add', 'aerate']
x.sort()	# x.sort(cmp)
x.sort(key=len)
print x