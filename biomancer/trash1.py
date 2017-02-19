class Questionnaire:
    def __init__(self, user_score):
        self.user_score = 0 
	user_score = user_score + user_value
	print("1: Not at all or less than one day")
	print("2: 1-2 days")
	print("3: 3-4 days")
	print("4: 5-7 days")
	print("5: Nearly every day for 2 weeks")
    
    # Update the user_score by the amount update_value

    # Return:
#        If value is update correctly: return 1
 #                      
  #      update_value must be [0, 4]. If not: do nothing and return 0
 
 #       For other error: return 0
    
    def update_score(self, update_value):
	self.update_value = 0
	u = range(1,21)
	i = 0
	while i < 20:
		inpt = input("Please select an option for Question {0}: ".format(u[i]))
		if not(inpt=="1") and not(inpt=="2") and not(inpt=="3") and not(inpt=="4") and not(inpt=="5"):
		 	print("Error. Please select an option between 1 and 5")
		else:
			i = i + 1
			if inpt == "1":
				update_value = update_value + 1
			elif inpt == "2":
				update_value = update_value + 2
			elif inpt == "3":
				update_value = update_value + 3
			elif inpt == "4":
				update_value = update_value + 4
			elif inpt == "5":
				update_value = update_value + 5




