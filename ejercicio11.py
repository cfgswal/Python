#!/usr/local/bin/python
n = 1
total1 = 0
total2 = 0
while n <= 100 :
	print n
	if n % 2 != 0:			
		total1 = total1 + n	
		n = n + 1
	else:
		total2 = total2 + n	
		n = n + 1

print total1
print total2