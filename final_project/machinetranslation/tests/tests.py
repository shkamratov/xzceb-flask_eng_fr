import unittest
from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase): 
    def test1(self): 
        with self.assertRaises(TypeError): 
            english_to_french() # pylint: disable=no-value-for-parameter
        self.assertEqual(english_to_french("Hello"), "Bonjour")  # test for the translation of the world 'Hello' and 'Bonjour'.


class TestF2E(unittest.TestCase): 
    def test1(self): 
        with self.assertRaises(TypeError): 
            french_to_english() # pylint: disable=no-value-for-parameter
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test for the translation of the world 'Hello' and 'Bonjour'.
        
unittest.main()