#!/usr/local/bin/python
n1 = int(input("Introduce numero1: "))
n2 = int(input("Introduce numero2: "))
t1 = 10
total1 = 0
total2 = 0
if n1 >= n2:
	while t1 <=50:
		print t1
		t1 = t1 + 4
		total1 = total1 + t1
	print total1
total2 = n1/n2
if total2 <= 30:
	print ("Total: ") + str (n1**2+n2**2)
