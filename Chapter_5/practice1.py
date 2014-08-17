#!/usr/bin/env python
# -*- coding: utf-8 -*-

print
title = 'Conditionals, Loops, and Some Other Statements'
print title
print len(title) * '-'
print

# Assertion
age = 10
assert 0 < age < 100
# age = -1
# assert 0 < age < 100

print 3 * '*' + ' while loops ' + 3 * '*'
x =1
while x <= 10:
	print x
	x += 1
print

print 3 * '*' + ' for loops ' + 3 * '*'
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
	print word
print

for number in range(1,11):
	print number
print

for number in xrange(1,10):
	print number
print

d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
	print key, 'corresponds to', d[key]
print

for value in d.values():
	print 'Value', value
print

for key, value in d.items():
	print key, 'corresponds to', value
print

print 3 * '*', 'Iteration Utilities', 3 * '*'
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
for name, age in zip(names, ages):
	print name, 'is', age, 'years old'
print

print zip(xrange(100000000), range(5))
print

print 3 * '*', 'Numbered Iteration', 3 * '*'
strings = ['anne', 'beth', 'george', 'damon', 'xxx']
print strings
for index, string in enumerate(strings):
	if 'xxx' in string:
		strings[index] = '[censored]'
print strings
print

from math import sqrt
for n in range(99, 0, -1):
	root = sqrt(n)
	if root == int(root):
		print n, sqrt(n)
		break
print

print 3 * '*', 'while true/break Idiom', 3 * '*'
while True:
	word = raw_input('Please enter a word: ')
	if not word: break
	# do something with the word:
	print 'The word was ' + word
print

print 3 * '*', 'else Clauses in Loops', 3 * '*'
from math import sqrt
for n in range(99, 81, -1):
	root = sqrt(n)
	if root == int(root):
		print n
		break
else:
	print "Didn't find it!"
print

print 3 * '*', 'List Comprehension—Slightly Loopy', 3 * '*'
print [x*x for x in xrange(10)]
print [x*x for x in xrange(10) if x % 3 == 0]
print [(x, y) for x in xrange(3) for y in xrange(3)]

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
print [(b, g) for b in boys for g in girls if b[0] == g[0]]

# A better solution
girls = ['alice', 'bernice', 'clarice'] 
boys = ['chris', 'arnold', 'bob'] 
letterGirls = {}
for girl in girls:
	letterGirls.setdefault(girl[0], []).append(girl)
print [b+'+'+g for b in boys for g in letterGirls[b[0]]]
print

exec "print 'Hello, world!'"
from math import sqrt
scope = {}
print 'scope length (before):', len(scope)
exec 'sqrt = 1' in scope
print sqrt(4)
print scope['sqrt']
print 'scope length (after):', len(scope)
print

print eval(raw_input("Enter an arithmetic expression: "))

scope = {}
scope['x'] = 2
scope['y'] = 3
print eval('x * y', scope)

scope = {}
exec 'x = 2' in scope
print eval('x*x', scope)
print

char = 'c'
print 'Ordinal value of', char, ord(char)
print