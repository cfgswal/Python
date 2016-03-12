#!/usr/local/bin/python
n1 = int(input("Introduce numero: "))
n = 1
contador = 0
total = 0
while n <= n1 :
	if (n % 3 and n % 2) == 0:	
		print n
		total = total + n	
		contador = contador + 1
	n = n + 1
print "Contador: " + str (contador)
print "Total: " + str (total)