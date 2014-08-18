#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Filter:
	def init(self):
		self.blocked = []
	def filter(self, sequence):
		return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter): # SPAMFilter is a subclass of Filter
	def init(self): # Overrides init method from Filter superclass
		self.blocked = ['SPAM']

f = Filter()
f.init()
print f.filter([1, 2, 3, 'SPAM', 'S'])

s = SPAMFilter()
s.init()
print s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM'])

print 'SPAMFilter is subclass of Filter:', issubclass(SPAMFilter, Filter)
print 'Filter is subclass of SPAMFilter:', issubclass(Filter, SPAMFilter)
print 'Base class of SPAMFilter:', SPAMFilter.__bases__

class TestFilter(SPAMFilter):
	"""docstring for TestFilter"""
	def __init__(self, arg):
		super(TestFilter, self).__init__()
		self.arg = arg

print 'Base class of TestFilter:', TestFilter.__bases__
print

s = SPAMFilter()
print isinstance(s, SPAMFilter)
print isinstance(s, Filter)
s = Filter()
print isinstance(s, SPAMFilter)
print

print s.__class__

class TestClass(object):
	pass

s = TestClass()
print type(s)

class TestClass1:
	__metaclass__ = type
	pass

s = TestClass1()
print type(s)
print

class Calculator:
	def calculate(self, expression):
		self.value = eval(expression)
	def function(self):
		print 'from Calculator'
class Talker:
	def talk(self):
		print 'Hi, my value is', self.value
	def function(self):
		print 'from Talker'
class TalkingCalculator(Calculator, Talker):
	pass

tc = TalkingCalculator()
tc.calculate('1+2*3')
tc.talk()
tc.function()

class TalkingCalculator(Talker, Calculator):
	pass
tc = TalkingCalculator()
tc.function()
