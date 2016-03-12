#!/usr/local/bin/python
n1 = int(input("Introduce numero1: "))
n2 = int(input("Introduce numero2: "))
n3 = int(input("Introduce numero3: "))
t1 = 2
total = 0
total = n1/n2
if total> 30:
	print ("Total si > 30: ") + str (n1/n3 * n2**3)
total1 = 0
suma = 0
if total<=30:
	while t1 <= 30:
		total1 = t1**2
		suma = suma + total1
		print ("Total de ")+ str(t1) + str(" elevado a 2 es = ") + str (total1)
		total1= 0
		t1 = t1 + 2
	print suma
