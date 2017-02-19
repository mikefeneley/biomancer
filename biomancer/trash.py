print("1: Not at all or less than one day")
print("2: 1-2 days")
print("3: 3-4 days")
print("4: 5-7 days")
print("5: Nearly every day for 2 weeks")
u = range(1,21)
i = 0
while i < 20:
		inpt = input("Please select an option for Question {0}: ".format(u[i]))
		if not(inpt=="1") and not(inpt=="2") and not(inpt=="3") and not(inpt=="4") and not(inpt=="5"):
		 	print("Error. Please select an option between 1 and 5")
		else:
			i = i + 1
			if inpt == "1":
				print(0)
			elif inpt == "2":
				print(1)
			elif inpt == "3":
				print(2)
			elif inpt == "4":
				print(3)
			elif inpt == "5":
				print(4)
