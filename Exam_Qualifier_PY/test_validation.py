import unittest
import io
import sys
import valid_input as valid_input

class TestValidation(unittest.TestCase):
    def test_Validation_y(self):
        self.assertTrue(valid_input.validate_input("y"))
    
    def test_Validation_Y(self):
        self.assertTrue(valid_input.validate_input("Y"))
    
    def test_Validation_n(self):
        self.assertTrue(valid_input.validate_input("n"))
    
    def test_Validation_N(self):
        self.assertTrue(valid_input.validate_input("N"))

    def test_Validation_False(self):
        text = io.StringIO()
        sys.stdout = text
        self.assertFalse(valid_input.validate_input("r"))
        sys.stdout = sys.__stdout__

    
if __name__=="__main__":
    unittest.main()