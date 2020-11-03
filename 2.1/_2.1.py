def arithmetic (a, b, z):
	if z=="+":
		return (a+b)
	elif z=="-":
		return (a-b)
	elif z=="*":
		return (a*b)
	elif z=="/":
		return (a/b)
	else :
		return ("Неизвестная операция")
a = int(input("Введите первое число: "))
b = int(input("Введите второе чиcло: "))
z = input("Введите знак арифметической операции: ")
print ("Результат: ", arithmetic(a, b, z))