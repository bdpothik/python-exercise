#!/usr/bin/env python
# -*- coding: utf-8 -*-

print
print 'Dictionary'
print len('Dictionary') * '-'

# Using key-value pair
phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print phonebook
print

# Using dic funtion from sequences of (key, value)
items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
print d
print d['name']
print 'name' in d
print 'phone' in d
d['address'] = 'Dhaka'
print d
print

# Using keyword arguments
d = dict(name='Gumby', age=42)
print d
print

title = 'String Formatting with Dictionaries'
print title
print len(title) * '-'
phonebook = {'Beth': '9102', 'Alice': '2341', 'Cecil': '3258'}
print "Cecil's phone number is %(Cecil)s." % phonebook
print

template = '''
<html>
	<head>
		<title>%(title)s</title>
	</head>
	<body>
		<h1>%(title)s</h1>
		<p>%(text)s</p>
	</body>
</html>'''
data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
print template % data
print

title = 'copy vs deepcopy'
print title
print len(title) * '-'

from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print 'Using "copy": ' + str(c)
print 'Using "deepcopy": ' + str(dc)
print