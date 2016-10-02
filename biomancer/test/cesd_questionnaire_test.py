import sys
sys.path.append("../")

import unittest
from cesd_questionnaire import CesdQuestionnaire 

class TestCesdQuestionnaire(unittest.TestCase):

    def setUp(self):
       self.questionnaire = CesdQuestionnaire("results_test.txt") 

    def test_setup(self):
        self.assertEqual(self.questionnaire.user_score, 0)
        self.assertEqual(self.questionnaire.sadness, 0)
        self.assertEqual(self.questionnaire.appetite, 0)

        self.assertEqual(self.questionnaire.sleep, 0)
        self.assertEqual(self.questionnaire.thinking, 0)
        self.assertEqual(self.questionnaire.guilt, 0)

        self.assertEqual(self.questionnaire.tired, 0)
        self.assertEqual(self.questionnaire.movement, 0)
        self.assertEqual(self.questionnaire.suicide, 0)


    def test_update_score(self):
        """ Check values outside acceptable range """
        self.assertEqual(self.questionnaire.user_score, 0)
        result = self.questionnaire.update_score(-1)
        self.assertEqual(result, 0)
        self.assertEqual(self.questionnaire.user_score, 0)
        result = self.questionnaire.update_score(5)
        self.assertEqual(result, 0)
        self.assertEqual(self.questionnaire.user_score, 0)

        """ Check values in the acceptable range """
        result = self.questionnaire.update_score(0)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.user_score, 0)

        result = self.questionnaire.update_score(1)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.user_score, 1)

        result = self.questionnaire.update_score(2)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.user_score, 3)
        
        result = self.questionnaire.update_score(3)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.user_score, 6)

        result = self.questionnaire.update_score(4)
        self.assertEqual(result, 1)

        """ Check final values """
        self.assertEqual(self.questionnaire.user_score, 10)
        self.assertEqual(self.questionnaire.sadness, 0)
        self.assertEqual(self.questionnaire.appetite, 0)

        self.assertEqual(self.questionnaire.sleep, 0)
        self.assertEqual(self.questionnaire.thinking, 0)
        self.assertEqual(self.questionnaire.guilt, 0)

        self.assertEqual(self.questionnaire.tired, 0)
        self.assertEqual(self.questionnaire.movement, 0)
        self.assertEqual(self.questionnaire.suicide, 0)


    def test_update_sadness(self):
        """ Check values outside acceptable range """
        self.assertEqual(self.questionnaire.sadness, 0)
        result = self.questionnaire.update_sadness(-1)
        self.assertEqual(result, 0)
        self.assertEqual(self.questionnaire.sadness, 0)
        result = self.questionnaire.update_sadness(5)
        self.assertEqual(result, 0)
        self.assertEqual(self.questionnaire.sadness, 0)

        """ Check values in the acceptable range """
        result = self.questionnaire.update_sadness(0)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.sadness, 0)

        result = self.questionnaire.update_sadness(1)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.sadness, 1)

        result = self.questionnaire.update_sadness(2)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.sadness, 3)
        
        result = self.questionnaire.update_sadness(3)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.sadness, 6)

        result = self.questionnaire.update_sadness(4)
        self.assertEqual(result, 1)

        """ Check final values """
        self.assertEqual(self.questionnaire.user_score, 0)
        self.assertEqual(self.questionnaire.sadness, 10)
        self.assertEqual(self.questionnaire.appetite, 0)

        self.assertEqual(self.questionnaire.sleep, 0)
        self.assertEqual(self.questionnaire.thinking, 0)
        self.assertEqual(self.questionnaire.guilt, 0)

        self.assertEqual(self.questionnaire.tired, 0)
        self.assertEqual(self.questionnaire.movement, 0)
        self.assertEqual(self.questionnaire.suicide, 0)

    def test_update_appetite(self):
        """ Check values outside acceptable range """
        self.assertEqual(self.questionnaire.appetite, 0)
        result = self.questionnaire.update_appetite(-1)
        self.assertEqual(result, 0)
        self.assertEqual(self.questionnaire.appetite, 0)
        result = self.questionnaire.update_appetite(5)
        self.assertEqual(result, 0)
        self.assertEqual(self.questionnaire.appetite, 0)

        """ Check values in the acceptable range """
        result = self.questionnaire.update_appetite(0)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.appetite, 0)

        result = self.questionnaire.update_appetite(1)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.appetite, 1)

        result = self.questionnaire.update_appetite(2)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.appetite, 3)
        
        result = self.questionnaire.update_appetite(3)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.appetite, 6)

        result = self.questionnaire.update_appetite(4)
        self.assertEqual(result, 1)
        
        """ Check final values """
        self.assertEqual(self.questionnaire.user_score, 0)
        self.assertEqual(self.questionnaire.sadness, 0)
        self.assertEqual(self.questionnaire.appetite, 10)

        self.assertEqual(self.questionnaire.sleep, 0)
        self.assertEqual(self.questionnaire.thinking, 0)
        self.assertEqual(self.questionnaire.guilt, 0)

        self.assertEqual(self.questionnaire.tired, 0)
        self.assertEqual(self.questionnaire.movement, 0)
        self.assertEqual(self.questionnaire.suicide, 0)


    def test_update_sleep(self):
        """ Check values outside acceptable range """
        self.assertEqual(self.questionnaire.sleep, 0)
        result = self.questionnaire.update_sleep(-1)
        self.assertEqual(result, 0)
        self.assertEqual(self.questionnaire.sleep, 0)
        result = self.questionnaire.update_sleep(5)
        self.assertEqual(result, 0)
        self.assertEqual(self.questionnaire.sleep, 0)

        """ Check values in the acceptable range """
        result = self.questionnaire.update_sleep(0)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.sleep, 0)

        result = self.questionnaire.update_sleep(1)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.sleep, 1)

        result = self.questionnaire.update_sleep(2)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.sleep, 3)
        
        result = self.questionnaire.update_sleep(3)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.sleep, 6)

        result = self.questionnaire.update_sleep(4)
        self.assertEqual(result, 1)

        """ Check final values """
        self.assertEqual(self.questionnaire.user_score, 0)
        self.assertEqual(self.questionnaire.sadness, 0)
        self.assertEqual(self.questionnaire.appetite, 0)

        self.assertEqual(self.questionnaire.sleep, 10)
        self.assertEqual(self.questionnaire.thinking, 0)
        self.assertEqual(self.questionnaire.guilt, 0)

        self.assertEqual(self.questionnaire.tired, 0)
        self.assertEqual(self.questionnaire.movement, 0)
        self.assertEqual(self.questionnaire.suicide, 0)


    def test_update_thinking(self):
        """ Check values outside acceptable range """
        self.assertEqual(self.questionnaire.thinking, 0)
        result = self.questionnaire.update_thinking(-1)
        self.assertEqual(result, 0)
        self.assertEqual(self.questionnaire.thinking, 0)
        result = self.questionnaire.update_thinking(5)
        self.assertEqual(result, 0)
        self.assertEqual(self.questionnaire.thinking, 0)

        """ Check values in the acceptable range """
        result = self.questionnaire.update_thinking(0)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.thinking, 0)

        result = self.questionnaire.update_thinking(1)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.thinking, 1)

        result = self.questionnaire.update_thinking(2)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.thinking, 3)
        
        result = self.questionnaire.update_thinking(3)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.thinking, 6)

        result = self.questionnaire.update_thinking(4)
        self.assertEqual(result, 1)

        """ Check final values """
        self.assertEqual(self.questionnaire.user_score, 0)
        self.assertEqual(self.questionnaire.sadness, 0)
        self.assertEqual(self.questionnaire.appetite, 0)

        self.assertEqual(self.questionnaire.sleep, 0)
        self.assertEqual(self.questionnaire.thinking, 10)
        self.assertEqual(self.questionnaire.guilt, 0)

        self.assertEqual(self.questionnaire.tired, 0)
        self.assertEqual(self.questionnaire.movement, 0)
        self.assertEqual(self.questionnaire.suicide, 0)



    def test_update_guilt(self):
        """ Check values outside acceptable range """
        self.assertEqual(self.questionnaire.guilt, 0)
        result = self.questionnaire.update_guilt(-1)
        self.assertEqual(result, 0)
        self.assertEqual(self.questionnaire.guilt, 0)
        result = self.questionnaire.update_guilt(5)
        self.assertEqual(result, 0)
        self.assertEqual(self.questionnaire.guilt, 0)

        """ Check values in the acceptable range """
        result = self.questionnaire.update_guilt(0)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.guilt, 0)

        result = self.questionnaire.update_guilt(1)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.guilt, 1)

        result = self.questionnaire.update_guilt(2)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.guilt, 3)
        
        result = self.questionnaire.update_guilt(3)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.guilt, 6)

        result = self.questionnaire.update_guilt(4)
        self.assertEqual(result, 1)


        """ Check final values """
        self.assertEqual(self.questionnaire.user_score, 0)
        self.assertEqual(self.questionnaire.sadness, 0)
        self.assertEqual(self.questionnaire.appetite, 0)

        self.assertEqual(self.questionnaire.sleep, 0)
        self.assertEqual(self.questionnaire.thinking, 0)
        self.assertEqual(self.questionnaire.guilt, 10)

        self.assertEqual(self.questionnaire.tired, 0)
        self.assertEqual(self.questionnaire.movement, 0)
        self.assertEqual(self.questionnaire.suicide, 0)


    def test_update_tired(self):
        """ Check values outside acceptable range """
        self.assertEqual(self.questionnaire.tired, 0)
        result = self.questionnaire.update_tired(-1)
        self.assertEqual(result, 0)
        self.assertEqual(self.questionnaire.tired, 0)
        result = self.questionnaire.update_tired(5)
        self.assertEqual(result, 0)
        self.assertEqual(self.questionnaire.tired, 0)

        """ Check values in the acceptable range """
        result = self.questionnaire.update_tired(0)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.tired, 0)

        result = self.questionnaire.update_tired(1)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.tired, 1)

        result = self.questionnaire.update_tired(2)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.tired, 3)
        
        result = self.questionnaire.update_tired(3)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.tired, 6)

        result = self.questionnaire.update_tired(4)
        self.assertEqual(result, 1)

        """ Check final values """
        self.assertEqual(self.questionnaire.user_score, 0)
        self.assertEqual(self.questionnaire.sadness, 0)
        self.assertEqual(self.questionnaire.appetite, 0)

        self.assertEqual(self.questionnaire.sleep, 0)
        self.assertEqual(self.questionnaire.thinking, 0)
        self.assertEqual(self.questionnaire.guilt, 0)

        self.assertEqual(self.questionnaire.tired, 10)
        self.assertEqual(self.questionnaire.movement, 0)
        self.assertEqual(self.questionnaire.suicide, 0)


    def test_update_movement(self):
        """ Check values outside acceptable range """
        self.assertEqual(self.questionnaire.movement, 0)
        result = self.questionnaire.update_movement(-1)
        self.assertEqual(result, 0)
        self.assertEqual(self.questionnaire.movement, 0)
        result = self.questionnaire.update_movement(5)
        self.assertEqual(result, 0)
        self.assertEqual(self.questionnaire.sadness, 0)

        """ Check values in the acceptable range """
        result = self.questionnaire.update_movement(0)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.movement, 0)

        result = self.questionnaire.update_movement(1)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.movement, 1)

        result = self.questionnaire.update_movement(2)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.movement, 3)
        
        result = self.questionnaire.update_movement(3)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.movement, 6)

        result = self.questionnaire.update_movement(4)
        self.assertEqual(result, 1)

        """ Check final values """
        self.assertEqual(self.questionnaire.user_score, 0)
        self.assertEqual(self.questionnaire.sadness, 0)
        self.assertEqual(self.questionnaire.appetite, 0)

        self.assertEqual(self.questionnaire.sleep, 0)
        self.assertEqual(self.questionnaire.thinking, 0)
        self.assertEqual(self.questionnaire.guilt, 0)

        self.assertEqual(self.questionnaire.tired, 0)
        self.assertEqual(self.questionnaire.movement, 10)
        self.assertEqual(self.questionnaire.suicide, 0)


    def test_update_suicide(self):
        """ Check values outside acceptable range """
        self.assertEqual(self.questionnaire.suicide, 0)
        result = self.questionnaire.update_suicide(-1)
        self.assertEqual(result, 0)
        self.assertEqual(self.questionnaire.suicide, 0)
        result = self.questionnaire.update_suicide(5)
        self.assertEqual(result, 0)
        self.assertEqual(self.questionnaire.suicide, 0)

        """ Check values in the acceptable range """
        result = self.questionnaire.update_suicide(0)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.suicide, 0)

        result = self.questionnaire.update_suicide(1)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.suicide, 1)

        result = self.questionnaire.update_suicide(2)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.suicide, 3)
        
        result = self.questionnaire.update_suicide(3)
        self.assertEqual(result, 1)
        self.assertEqual(self.questionnaire.suicide, 6)

        result = self.questionnaire.update_suicide(4)
        self.assertEqual(result, 1)
        
        """ Check final values """
        self.assertEqual(self.questionnaire.user_score, 0)
        self.assertEqual(self.questionnaire.sadness, 0)
        self.assertEqual(self.questionnaire.appetite, 0)

        self.assertEqual(self.questionnaire.sleep, 0)
        self.assertEqual(self.questionnaire.thinking, 0)
        self.assertEqual(self.questionnaire.guilt, 0)

        self.assertEqual(self.questionnaire.tired, 0)
        self.assertEqual(self.questionnaire.movement, 0)
        self.assertEqual(self.questionnaire.suicide, 10)


    def test_meets_depression_subthreshhold(self):
        self.assertEqual(self.questionnaire.user_score, 0)
        result = self.questionnaire.meets_depression_subthreshhold()
        self.assertFalse(result)

        self.questionnaire.user_score = 16
        self.assertEqual(self.questionnaire.user_score, 16)
        result = self.questionnaire.meets_depression_subthreshhold()
        self.assertTrue(result)
        
        self.questionnaire.user_score = 60
        self.assertEqual(self.questionnaire.user_score, 60)
        result = self.questionnaire.meets_depression_subthreshhold()
        self.assertTrue(result)


    def test_start_test(self):
        pass
    def test_display_greeting(self):
        pass
    def test_ask_questions(self):
        pass
    def test_ask_question1(self):
        pass
    def test_ask_question2(self):
        pass
    def test_ask_question3(self):
        pass
    def test_ask_question4(self):
        pass
    def test_ask_question5(self):
        pass
    def test_ask_question6(self):
        pass
    def test_ask_question7(self):
        pass
    def test_ask_question8(self):
        pass
    def test_ask_question9(self):
        pass
    def test_ask_question10(self):
        pass
    def test_ask_question11(self):
        pass
    def test_ask_question13(self):
        pass
    def test_ask_question14(self):
        pass
    def test_ask_question15(self):
        pass
    def test_ask_question16(self):
        pass
    def test_ask_question17(self):
        pass
    def test_ask_question18(self):
        pass
    def test_ask_question19(self):
        pass
    def test_ask_question20(self):
        pass

if __name__== "__main__":
    unittest.main()
