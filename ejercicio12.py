#!/usr/local/bin/python
n1 = int(input("Introduce numero1: "))
n2 = int(input("Introduce numero2: "))
t1 = 0
t2 = 0
total=0
contador1=0
contador2=0
if n1 < n2:
	t1 = n1
	t2 = n2
else:
	t1 = n2
	t2 = n1
while t1 <= t2:

	print t1
	if t1 % 2 == 0:
		contador2 = contador2 + 1
		total=total + t1
	t1 = t1 + 1
	contador1 = contador1 + 1
print "Contador: " + str (contador1)	
print "Contador pares: " + str (contador2)
print "Suma pares: " + str (total)