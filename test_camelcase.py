import camelcase
import unittest
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('helloWorld', camelcase.camel_case('Hello World')) 
        self.assertEqual('\U0001f600', camelcase.camel_case('\U0001f600')) #emoji
        
    
    def test_camelcase_with_symbols(self):
        self.assertEqual('#*Cat9Lives?!', camelcase.camel_case('#*cat 9 lives?!')) 
        self.assertEqual('👽🌎🌺', camelcase.camel_case( '👽🌎🌺')) 

    def test_camelcase_with_new_line(self):
        self.assertEqual('newLineTest', camelcase.camel_case('new line \n test'))      

    def test_camelcase_sentence_extra_spaces(self):
        self.assertEqual('spacingTest', camelcase.camel_case('  spacing   test    ')) 
        self.assertEqual('anotherSpacingTest', camelcase.camel_case('  another  spacing    Test'))

    def test_camelcase_empty_string(self):
        self.assertEqual('', camelcase.camel_case(''))
        self.assertEqual('', camelcase.camel_case('     '))

    def test_camelcase_sentence_with_numbers(self):
        self.assertEqual('cat9Lives', camelcase.camel_case('cat 9 lives')) 
        self.assertEqual('99BottlesOfWaterOnTheWall', camelcase.camel_case('99 bottles of water on the wall'))   

    def test_camelcase_lots_of_words(self):
        self.assertEqual('onceUponATimeThereLivedThreeLittlePigs', camelcase.camel_case('once upon a time there lived three little pigs'))

    def test_camelcase_all_caps_input(self):
        self.assertEqual('testing', camelcase.camel_case('TESTING')) 
        self.assertEqual('whenYouWishUponAStar', camelcase.camel_case('WHEN YOU WISH UPON A STAR'))

    def test_camelcase_with_tab(self): 
        self.assertEqual('thisIsATabTest', camelcase.camel_case('This is a \t tab test'))

if __name__ == '__main__': #can run test this way, or from command prompt using pyton3 -m unittest fileName.py
    unittest.main()
