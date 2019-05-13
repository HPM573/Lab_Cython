#!/anaconda3/bin/python
from __future__ import print_function

def fib(n):
	a = 0
	b = 1
	while b < n:
		print(b, end= ' ')
		a,b = b, a + b

	print()
