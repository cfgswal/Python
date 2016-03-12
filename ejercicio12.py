  
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