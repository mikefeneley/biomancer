
class CesdQuestionnaire:
    def __init__(self, filename="results.txt"):
        self.filename = filename
        self.user_score = 0 
        self.sadness = 0
        self.appetite = 0
        self.sleep = 0
        self.thinking = 0
        self.guilt = 0
        self.tired = 0
        self.movement = 0
        self.suicide = 0

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
	u = range(1,21)
	i = 0
	while i < 20:
		inpt = input("Please select an option for Question {0}: ".format(u[i]))
		if not(inpt=="1") and not(inpt=="2") and not(inpt=="3") and not(inpt=="4") and not(inpt=="5"):
		 	print("Error. Please select an option between 1 and 5")
		else:
			i = i + 1
			if inpt == "1":
				
			elif inpt == "2":
				print(1)
			elif inpt == "3":
				print(2)
			elif inpt == "4":
				print(3)
			elif inpt == "5":
				print(4)
	self.update_value = update_value
        pass 
    

   
 #   Update the sadness value by the amount update_value

  #  Return:
    
   #     If value is update correctly: return 1
                       
    #    update_value must be [0, 4]. If not: return 0
 
     #   For other error: return 0

   
    def update_sadness(self, update_value):
        pass


    """ 
    Update the appetite value by the amount update_value

    Return:
    
        If value is update correctly: return 1
                       
        update_value must be [0, 4]. If not: return 0
 
        For other error: return 0

    """ 
    def update_appetite(self, update_value):
        pass

    """ 
    Update the sleep value by the amount update_value

    Return:
    
        If value is update correctly: return 1
                       
        update_value must be [0, 4]. If not: return 0
 
        For other error: return 0

    """     
    def update_sleep(self, update_value):
        pass
    
    """ 
    Update the concentation value by the amount update_value

    Return:
    
        If value is update correctly: return 1
                       
        update_value must be [0, 4]. If not: return 0
 
        For other error: return 0

    """     
    def update_thinking(self, update_value):
        pass

    """ 
    Update the guilt value by the amount update_value

    Return:
    
        If value is update correctly: return 1
                       
        update_value must be [0, 4]. If not: return 0
 
        For other error: return 0

    """     
    def update_guilt(self, update_value):
        pass


    """ 
    Update the tired value by the amount update_value

    Return:
    
        If value is update correctly: return 1
                       
        update_value must be [0, 4]. If not: return 0
 
        For other error: return 0

    """ 
    def update_tired(self, update_value):
        pass 

    """ 
    Update the movement value by the amount update_value
    
    Return:
    
        If value is update correctly: return 1
                       
        update_value must be [0, 4]. If not: return 0
 
        For other error: return 0

    """ 
    def update_movement(self, update_value):
        pass


    """ 
    Update the suicide value by the amount update_value

    Return:
    
        If value is update correctly: return 1
                       
        update_value must be [0, 4]. If not: return 0
 
        For other error: return 0

    """ 
    def update_suicide(self, update_value):
        pass


    """
    NOT TO BE
    Calculates the total score the user got from the questioniare.

    The score is the sum of all the users responses.

    Return:

        The users total score

    """ 
    def calculate_score(self, update_value):
        pass 


    """ 
    Check if the user meets the threshold criteria for depression

    Return:

        If score >= 16: return True

        If score < 16: return False

    """ 

    def meets_depression_subthreshhold(self):

        pass


    """
    Entry point into the test.

    """
    def start_test(self):
        pass


    """ 
    Display greeting message to the user when they start the program.
    
    Return:
        return 1
    """
    def display_greeting(self):
        pass


    """
    Ask the users all the questions of the CESD-R test

    Return:
        return 1

    """
    def ask_questions(self):
        pass
    

    """
    Ask user the first question of the CESD-R test. 

    Read the users response and increment the user_score and

    appetite values by this amount.

    Return:
        return 1

    """
    def ask_question1(self):        
        pass    


    """
    Ask user the second question of the CESD-R test. 

    Read the users response and increment the user_score and

    sadness values by this amount.

    Return:
        return 1

    """
    def ask_question2(self):
        pass



    """
    Ask user the third question of the CESD-R test. 

    Read the users response and increment the user_score and

    thinking values by this amount.

    Return:
        return 1

    """       
    def ask_question3(self):
        pass

    """
    Ask user the fourth question of the CESD-R test. 

    Read the users response and increment the user_score and

    sadness values by this amount.

    Return:
        return 1

    """   
    def ask_question4(self):
        pass

    """
    Ask user the fifth question of the CESD-R test. 

    Read the users response and increment the user_score and

    sleep values by this amount.

    Return:
        return 1

    """   
    def ask_question5(self):
        pass


    """
    Ask user the sixth question of the CESD-R test. 

    Read the users response and increment the user_score and

    sadness values by this amount.

    Return:
        return 1

    """   
    def ask_question6(self):
        pass
    
    """
    Ask user the seventh question of the CESD-R test. 

    Read the users response and increment the user_score and

    tired values by this amount.

    Return:
        return 1

    """   
    def ask_question7(self):
        pass



    """
    Ask user the eigth question of the CESD-R test. 

    Read the users response and increment the user_score and

    interest values by this amount.

    Return:
        return 1

    """         
    def ask_question8(self):
        pass


    """
    Ask user the ninth question of the CESD-R test. 

    Read the users response and increment the user_score and

    guilt values by this amount.

    Return:
        return 1

    """       
    def ask_question9(self):
        pass


    """
    Ask user the tenth question of the CESD-R test. 

    Read the users response and increment the user_score and

    interest values by this amount.

    Return:
        return 1

    """              
    def ask_question10(self):
        pass



    """
    Ask user the eleventh question of the CESD-R test. 

    Read the users response and increment the user_score and

    sleep values by this amount.

    Return:
        return 1

    """       
    def ask_question11(self):
        pass


    """
    Ask user the thirteenth question of the CESD-R test. 

    Read the users response and increment the user_score and

    movement values by this amount.

    Return:
        return 1

    """       
    def ask_question13(self):
        pass


    """
    Ask user the fourteenth question of the CESD-R test. 

    Read the users response and increment the user_score and

    suicide values by this amount.

    Return:
        return 1

    """               
    def ask_question14(self):
        pass

    """
    Ask user the fifteenth question of the CESD-R test. 

    Read the users response and increment the user_score and

    suicide values by this amount.

    Return:
        return 1

    """       
    def ask_question15(self):
        pass

    """
    Ask user the sixteenth question of the CESD-R test. 

    Read the users response and increment the user_score and

    tired values by this amount.

    Return:
        return 1

    """       
    def ask_question16(self):
        pass
        
    """
    Ask user the seventeenth question of the CESD-R test. 

    Read the users response and increment the user_score and

    guilt values by this amount.

    Return:
        return 1

    """   
    def ask_question17(self):
        pass
        
    """
    Ask user the eighteenth question of the CESD-R test. 

    Read the users response and increment the user_score and

    appetite values by this amount.

    Return:
        return 1

    """   
    def ask_question18(self):
        pass


    """
    Ask user the ninteenth question of the CESD-R test. 

    Read the users response and increment the user_score and

    sleep values by this amount.

    Return:
        return 1

    """          
    def ask_question19(self):
        pass



    """
    Ask user the twentieth question of the CESD-R test. 

    Read the users response and increment the user_score and

    thinking values by this amount.

    Return:
        return 1

    """   
    def ask_question20(self):
        pass


    """
    Writes the results of the test out to file.

    Format:

    Firstname Lastname
    Age
    mm/dd/xxxx

    Total: xx
    Sadness: xx
    Interest: xx
    Appetite: xx
    Sleep: xx
    Thinking: xx
    Guilt: xx
    Tired: xx
    Movement: xx
    Suicide: xx


    Return:
        For success: 1
        For failure: 0

    """         
    def log_results(self):
        pass



if __name__=="__main__":
    question = CesdQuestionnaire()
    question.start_test()
    
