from random import randint
import os
clear = lambda: os.system('cls')

def addReport():
	clear()
	file=open('data.txt','r')
	list = file.readlines()
	file.close()

	plist = randint(0,40000)
	num = str(plist)
	list.append(num + "\n")
	plist = input("Type av Åtgärd: ")
	list.append(plist + "\n")
	plist = input("Sektion: ")
	list.append(plist + "\n")
	plist = input("Utförd av: ")
	list.append(plist + "\n")
	plist = input("Datum: ")
	list.append(plist + "\n")
	plist = input("Längre beskriving: ")
	list.append(plist + "\n \n")

	# This opens the file, writes each item in the list to a line and then closes it    
	file=open('data.txt','w')
	for item in list:
	    file.write(str(item))
	file.close()
	print("Rapport Nummer: " + num)

def search():
	clear()
	reportNum = input("Skriv in Rapport Nummer: ")
	file=open("data.txt", "r")
	read=file.readlines()
	reportNum += "\n"
	for n in range(0,len(read)):
		if read[n]==reportNum:
			print(read[n+5])
	file.close()


# def delete():
# 	clear()
# 	tabort = input("Skriv in Rapport Nummret på den rapport som ska raderas: ")
# 	file=open("data.txt", "r")
# 	read=file.readlines()
# 	tabort += "\n"
# 	file.close()

# 	file=open('data.txt','w')
# 	for n in range(0,len(read)):
# 		if read[n]==tabort:
# 			file.write(read[n])
# 			file.write(read[n])
# 			file.write(read[n])
# 			file.write(read[n])
# 			file.write(read[n])
# 			file.write(read[n])
# 	file.close()

def run():
	num="0"
	while True:
		print("Databas för rapporter")
		print("1. Lägg till rapport")
		print("2. Sök efter rapport")
		# print("3. Radera en rapport")
		print("3. Rensa Terminalen")
		print("4. Avsluta")
		num = input("Ditt val: ")
		if num=="1":
			addReport()
		if num=="2":
			search()
		# if num=="3":
		# 	delete()
		if num=="3":
			clear()
		if num=="4":
			break

	print("Avslutas")



run()