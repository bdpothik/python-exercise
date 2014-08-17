#!/usr/bin/env python
# -*- coding: utf-8 -*-

print
title = 'Conditionals, Loops, and Some Other Statements'
print title
print len(title) * '-'

print 'Printing with Commas'
print 'Age:', 42
print 1, 2, 3
print (1, 2, 3)
print 'print 1', 'print 2',
print 'start next print from same line as previous one'
print

# if statement
print "'if' statements"
num = input('Enter a number: ')
if num > 0:
	print 'The number is positive'
elif num < 0:
	print 'The number is negative'
else:
	print 'The number is zero'
print

# nested if statement
name = raw_input('What is your name? ')
if name.endswith('Gumby'):
	if name.startswith('Mr.'):
		print 'Hello, Mr. Gumby'
	elif name.startswith('Mrs.'):
		print 'Hello, Mrs. Gumby'
	else:
		print 'Hello, Gumby'
else:
	print 'Hello, stranger'

