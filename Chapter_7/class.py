#!/usr/bin/env python
# -*- coding: utf-8 -*-

__metaclass__ = type # Make sure we get new style classes
title = 'Class Definition'
print title
print len(title) * '-'
class Person:
	def setName(self, name):
				self.name = name
	def getName(self):
		return self.name
	def greet(self):
		print "Hello, world! I'm %s." % self.name

foo = Person()
bar = Person()
foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')
foo.greet()
bar.greet()
print

foo.name
bar.name = 'Yoda'
bar.greet()
Person.greet(foo)

class Class:
	def method(self):
		print 'I have a self!'
def function():
	print "I don't..."
def function1(self):
	print "I have a self", self

isinstance = Class()
isinstance.method()
isinstance.method = function
isinstance.method()
isinstance.method = function1
# isinstance.method()
isinstance.method(isinstance)

# The self parameter is not dependent on calling
# the method the way, as instance.method.
class Bird:
	song = 'Squaawk!'
	def sing(self):
		print self.song

bird = Bird()
bird.sing()
birdsong = bird.sing
birdsong()
print

print 'Privacy'
class Secretive:
	print 'Class Secretive being defined...'
	def __inaccessible(self):	# accessible through '_Secretive__inaccessible()'
		print "Bet you can't see me..."
	def accessible(self):
		print "The secret message is:"
		self.__inaccessible()
	def _inaccessible1(self):	# Names with an initial underscore aren’t imported withstarredimports
		print "accessible"

s = Secretive()
s.accessible()
# s.__inaccessible()
s._Secretive__inaccessible()
s._inaccessible1()
print

title = 'Class Namespace'
print title
print len(title) * '-'

print 'Class Alternate Definition:'
def foo(x): return x*x
foo1 = lambda x: x*x

print foo(2)
print foo1(3)
print

class C:
	print 'Class C being defined...'
print

class MemberCounter:
	members = 0		# class member
	def init(self):
		MemberCounter.members += 1
	def init1(self):
		MemberCounter.members = 2

m1 = MemberCounter()
m1.init()
print MemberCounter.members

m2 = MemberCounter()
m2.init()
# m2.init1()
print MemberCounter.members

print 'm1', m1.members
print 'm2', m2.members
print

m1.members = 3
print MemberCounter.members
print 'm1', m1.members
print 'm2', m2.members
print

m1.members = 'Two'
print MemberCounter.members
print 'm1', m1.members
print 'm2', m2.members