#!/usr/bin/env python
# -*- coding: utf-8 -*-

print
title = 'Abstraction'
print title
print len(title) * '-'
print

print 'Fibonacci numbers'
fibs = [0, 1]
for i in range(8):
	fibs.append(fibs[-2] + fibs[-1])
print fibs

def fibs(num):
	result = [0, 1]
	for i in range(num-2):
		result.append(result[-2] + result[-1])
	return result
print fibs(10);
print

print 'Check whether callable'
import math
x = 1
y = math.sqrt
print callable(x)
print callable(y)
print

print 'Documenting Functions'
def square(x):
	'Calculates the square of the number x.'
	return x*x

print square.__doc__
# print help(square)
print

def testReturnOfDiffType(x):
	if x < 10:
		return x
	elif x < 15:
		return (x, x**2)
	else:
		pass

print testReturnOfDiffType(2)
print testReturnOfDiffType(13)
print testReturnOfDiffType(19)
print

def testPrintSequence(x):
	x[0] += 2

x = [1]
print x[0], testPrintSequence(x), x[0], testPrintSequence(x), x[0]
print

print 'Test Functions'
def init(data):
	data['first'] = {}
	data['middle'] = {}
	data['last'] = {}

def lookup(data, label, name):
	return data[label].get(name)

# def store(data, full_name):
# 	names = full_name.split()
	
# 	if len(names) == 1: names[len(names):] = ['', '']
# 	if len(names) == 2: names.insert(1, '')
	
# 	labels = 'first', 'middle', 'last'

# 	for label, name in zip(labels, names):
# 		people = lookup(data, label, name)
# 		if people:
# 			people.append(full_name)
# 		else:
# 			data[label][name] = [full_name]

def store(data, *full_names):
	for full_name in full_names:
		names = full_name.split()
		if len(names) == 1: names[len(names):] = ['', '']
		if len(names) == 2: names.insert(1, '')
		
		labels = 'first', 'middle', 'last'
		for label, name in zip(labels, names):
			people = lookup(data, label, name)
			if people:
				people.append(full_name)
			else:
				data[label][name] = [full_name]

MyNames = {}
init(MyNames)
store(MyNames, 'Magnus Lie Hetland')
print lookup(MyNames, 'middle', 'Lie')

store(MyNames, 'Robin Hood')
store(MyNames, 'Robin Locksley')
print lookup(MyNames, 'first', 'Robin')

store(MyNames, 'Mr. Gumby')
print lookup(MyNames, 'middle', '')

store(MyNames, 'Luke Skywalker', 'Anakin Skywalker')
print lookup(MyNames, 'last', 'Skywalker')
print

def hello_4(name, greeting='Hello', punctuation='!'):
	print '%s, %s%s' % (greeting, name, punctuation)

def  hello_5(name, greeting, punctuation='!'):
	print '%s, %s%s' % (greeting, name, punctuation)

hello_4('Mars')
hello_4('Mars', 'Howdy')
hello_4('Mars', 'Howdy', '...')
hello_4('Mars', punctuation='.')
hello_4('Mars', greeting='Top of the morning to ya')

# print hello_5('hasan', greeting='Salut', '$')
# hello_5('hasan', '$', greeting='Salut')
hello_5('hasan', 'Salut', punctuation='$')
print

def print_params(*params):
	print params

print_params('Testing')
print_params(1, 2, 3)
print_params('ab', 'cd', 'ef')
print

def print_params_2(title, *params):
	print title,
	print params

print_params_2('Params:', 1, 2, 3)
print_params_2('Nothing:')
print

def print_params_3(**params):
	print params

print_params_3(x=1, y=2, z=3)
print_params_3()
print

def print_params_4(x, y, z=3, *pospar, **keypar):
	print x, y, z,
	print pospar,
	print keypar

print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2)
print_params_4(1, 2)
#print_params_4(1, 2, 3, 5, 6, 7, foo=1, x=2)
print

def add(x, y): return x + y
params = (1, 2)
print add(*params)
print add(*(4, 5))
print

params = {'name': 'Sir Robin', 'greeting': 'Well met'}
hello_4(**params)
print

def with_stars(**kwds):
	print kwds['name'], 'is', kwds['age'], 'years old'

def without_stars(kwds):
	print kwds['name'], 'is', kwds['age'], 'years old'

args = {'name': 'Mr. Gumby', 'age': 42}
with_stars(**args)
without_stars(args)
print

print 'Scoping'
x = 1
scope = vars()
print scope['x']
scope['x'] += 1
print x
print

def combine(parameter):
	print parameter, globals()['parameter']
	print locals()['parameter']
parameter = 'berry'
combine('Shrub')

x = 1
def change_global():
	global x
	x = x+ 1

change_global()
print x

def foo():
	def bar():
		print "Hello, world!"
	bar()
foo()

def multiplier(factor):
	def multiplyByFactor(number):
		return number*factor
	return multiplyByFactor
print multiplier(4)(5)
print
