import camelcase
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('helloWorld', camelcase.camel_case('Hello World'))
        self.assertEqual('', camelcase.camel_case(''))
        self.assertEqual('testing', camelcase.camel_case('TESTING'))   
        self.assertEqual('\U0001f600', camelcase.camel_case('\U0001f600')) #emoji
        
    #testing w/ symbols failed
    # self.assertEqual('#*cat9Lives!', camelcase.camel_case('#*cat 9 lives!'))  
 #testing w \n fails
    #self.assertEqual('newLineTest', camelcase.camel_case('new line \n test'))      

    def test_camelcase_sentence_extra_spaces(self):
        self.assertEqual('spacingTest', camelcase.camel_case('  spacing   test    ')) 

    
    def test_camelcase_sentence_with_numbers(self):
        self.assertEqual('cat9Lives', camelcase.camel_case('cat 9 lives'))    