#!/usr/bin/env python
# -*- coding: utf-8 -*-

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)

print 'Factorial:', factorial(8)

def power(x, n):
	if n == 0:
		return 1
	else:
		return x * power(x, n-1)

print 'Power:', power(2, 8)

print 'Binary Search'

def search(sequence, number, lower=0, upper=None):
	if upper is None:
		upper = len(sequence) - 1

	if lower == upper:
		if number == sequence[upper]:
			return upper
		return None
	else:
		middle = (lower + upper) // 2

		if number > sequence[middle]:
			return search(sequence, number, middle+1, upper)
		else:
			return search(sequence, number, lower, middle)

seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print seq
print 'Fount at', search(seq, 95)
