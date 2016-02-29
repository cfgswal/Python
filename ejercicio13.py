#!/usr/local/bin/python
n = 1
contador = 0

while n <= 100 :
	if n % 3 == 0:	
		print n
			
		contador = contador + 1
	n = n + 1
print "Contador: " + str (contador)
