#!/usr/local/bin/python
n = 100
total = 0
while n >= 0 :
	if n % 2 != 0:	
		print n
		total = total + n	
	n = n - 1
print total