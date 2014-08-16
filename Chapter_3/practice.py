#!/usr/bin/env python
# -*- coding: utf-8 -*-

# string format with tuples

format = "Hello, %s. %s enougn for ya?"
values = ('world', 'Hot')
print format % values

format = "Pi with three decimals: %10.3f test"
from math import pi
print format % pi
format = "Pi with three decimals: %-10.3f test"
print format % pi

# If you use a list or some other sequence
# instead of a tuple, the sequence will be
# interpreted as a single value. Only 
# tuples and dictionaries will allow you
# to format more than one value.

# format = "Hello, %s. %s enougn for ya?"
format = "Hello, %s. enougn for ya?"
values = ['world', 'Hot']
print format % values

# Template string with 'Keyword Arguments'
from string import Template
s = Template('$x, glorious $x!')
print 'With Keyword Argument: ' + s.substitute(x='slurm')

s = Template("It's ${x}tastic!")
print 'With Keyword Argument: ' + s.substitute(x='slurm')

# Template string with 'Dictionary'
s = Template('A $thing must never $action.')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
print 'With Dictionary: ' + s.substitute(d)

# Simple Conversion
print 'Price of eggs: $%d' % 42
print 'Hexadecimal price of eggs: %x' % 42

from math import pi
print 'Pi: %f...' % pi
print 'Very inexact estimate of pi: %i' % pi
print 'Using str: %s' % 42L
print 'Using repr: %r' % 42L

# Width and Precision

print '"%10f"' % pi      # Field width 10
print '"%10.2f"' % pi    # Field width 10, precision 2
print '"%.2f"' % pi      # Precision 2
print '"%.5s"' % 'Guido van Rossum'
print '"%.*s", "%.*s"' % (2 * (5, 'Guido van Rossum'))
print '"%.*s", "%.*s"' % (5, 'Guido van Rossum', 9, 'Hasan Ibna Akbar')

print '"%010.2f"' % pi
print '"%+10.2f"' % pi
print '"%+10.2f"' % -3.789
print '"%-10.2f"' % pi
print '"% 10.2f"' % pi
print '"% 010.2f"' % pi

# String Methods
print '\n\n'
print 'find(..):'
print len('find(..):') * '-'
print 'With a moo-moo here, and a moo-moo there'.find('moo')

subject = '$$$ Get rich now!!! $$$'
print subject.find('$$$')
print subject.find('$$$', 1) # Only supplying the start
print subject.find('!!!')
print subject.find('!!!', 0, 16) # Supplying start and end

print '\n\n'
print 'join(..):'
print len('join(..):') * '-'

# gives 'TypeError: sequence item 0: expected string, int found'
# seq = [1, 2, 3, 4, 5]
# sep = '+'
# print sep.join(seq) # Trying to join a list of numbers

seq = ['1', '2', '3', '4', '5']
sep = '+'
print sep.join(seq) # Joining a list of strings

dirs = '', 'usr', 'bin', 'env'
print '/'.join(dirs)
print 'C:' + '\\'.join(dirs)

print '\n\n'
print 'split(..):'
print len('split(..):') * '-'

string = '1+2+3+4+5'
print string.split(sep)
print string.split(sep, 3)

print '\n\n'
print 'lower(..) and others:'
print len('lower(..) and others:') * '-'

name = 'Trondheim Hammer Dance'
print name.lower()
print name.swapcase()
print name.capitalize()
print name.islower()
print name.isupper()
print name.upper()
print name.title()
print name.istitle()

print "that's all folks".title()

import string
print string.capwords("that's all folks".title())

print '\n\n'
print 'replace(..) and others:'
print len('replace(..) and others:') * '-'

print 'This is a test'.replace('is', 'eez')
print '      internal whitespace is kept      '.strip()
print '*** SPAM * for * everyone!!! ***'.strip(' *!')

from string import maketrans
table = maketrans('cs', 'kz')
print len(table)
print table[97:123]
print maketrans('', '')[97:123]
print 'this is an incredible test'.translate(table)
print 'this is an incredible test'.translate(table, ' ')

print 'BØLLEFRØ'.lower()	# It does not work for non-english alphabets

# To work 'lower' properly we may use translate like this
table = maketrans('ÆØÅ', 'æøå')
word = 'KÅPESØM'
print word.lower()
print word.translate(table)
print word.translate(table).lower()

# But simply using Unicode might solve this
print u'ærnæringslære'.upper()