import unittest
from password_generator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
            
    def test_generate_words(self):
        pwd = PasswordGenerator()
        second_pwd = PasswordGenerator()
        
        self.assertIs(type(pwd.word_list), list)

        common_words = [word for word in pwd.word_list if word in second_pwd.word_list]
        
        #both passwords should draw from same
        #source of word list
        self.assertEqual(len(pwd.word_list), len(second_pwd.word_list), len(common_words))
    
    def test_contains_punctuation(self):
        pwd = PasswordGenerator()
        
        result_true = pwd.contains_punctuation("a.new_program")
        result_false= pwd.contains_punctuation("notApunctuationString")
       
        self.assertTrue(result_true)
        self.assertFalse(result_false)
        
    def test_generate_pwd(self):
        """ generate_pwd should combine two words, an integer, and at least
        one special character into a single string, in no particular order """
        pwd = PasswordGenerator()
        
        #contains at least 2 words, len >= 4 chars
        #for a total of at least 10 chars
        self.assertTrue(len(pwd.word_list) >=0)
        self.assertTrue(any(c.isalpha() for c in pwd.password))
        self.assertTrue(len(pwd.password) >= 10)
        
        #has at least 1 digit and 1 special char
        self.assertTrue(any(c.isdigit() for c in pwd.password))
        self.assertFalse(pwd.password.isalnum())
        
    def test_repr(self):
        pwd = PasswordGenerator()
        self.assertEqual(pwd.password, str(pwd) )
        
    def test_rand_number(self):
        pwd_nums_list = []
        
        for _ in range(5):
            pwd = PasswordGenerator()
            pwd_nums_list.append(pwd.number)
            
        pwd_nums_set = set(pwd_nums_list)
      
        #set should have same length as list,
        #but allowing for 1 duplicate due to random
        #selection
        self.assertTrue(len(pwd_nums_list) - len(pwd_nums_set) <= 1)
        

if __name__ == '__main__':
    unittest.main()
    

