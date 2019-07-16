import os
clear = lambda: os.system('cls')

def find_factors(n):
	On = True
	while On:
		for x in range(2,n):
			if prime(n):
				print(f'Factor: {n}')
				On = False
				break
			if n%x==0:
				print(f'Factor: {x}')
				n = int(n/x)
				break

def prime(n):
	for x in range(2,n):
		if n%x==0:
			return False
	return True

clear()
value = int(input('Enter the number: '))
find_factors(value)